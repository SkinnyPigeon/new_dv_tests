from sqlalchemy import create_engine, MetaData, insert, select
from sqlalchemy import func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

from functions.fcrb_data_vault import fcrb_data_vault
from control_files.fcrb_keys_and_sats import fcrb_keys, fcrb_sats
import pandas as pd
pd.options.mode.chained_assignment = None


import os
from dotenv import load_dotenv
import subprocess
project_folder = subprocess.check_output("pwd", shell=True).decode("utf-8").rstrip()
load_dotenv(os.path.join(project_folder, '.env'))
PORT = os.getenv('PGPORT')
PASSWORD = os.getenv('PGPASSWORD')
if PORT == None:
    PASSWORD = os.environ.get('PGPASSWORD')
    PORT = os.environ.get('PGPORT')

def setup_connection(schema):
    engine = create_engine('postgresql://postgres:{}@localhost:{}/data_vault'.format(PASSWORD, PORT))
    metadata = MetaData(schema=schema, bind=engine)
    metadata.reflect(engine)
    Base = automap_base(metadata=metadata)
    Base.prepare()
    Session = sessionmaker(bind=engine)
    session = Session()
    return {"metadata": metadata, "base": Base, "engine": engine, "session": session, 'schema': schema}


def loop_through_tables(data, body):
    for table in data['FCRB']:
        print(table)
        for row in data['FCRB'][table]:
            print(row)
            print("\n")

def get_table_class(schema, base, table_name):
    for class_name in base._decl_class_registry.values():
        if hasattr(class_name, '__table__') and class_name.__table__.fullname == f"{schema}.{table_name}":
            return class_name

def get_link_keys(links):
    for link in links:
        split_text = link.split('_')
        link_keys = {link: {key + '_id': '' for key in split_text if key != 'link'}}
    print(link_keys)
    return link_keys



def fill_data_vault_v1(data, body):
    schema = fcrb_data_vault()
    connection = setup_connection(schema)
    for table in data['FCRB']:
        satellite_definitions = fcrb_sats[table]
        links = satellite_definitions.pop('links')
        for satellite_name in satellite_definitions:
            print(satellite_name)
            satellite_table = get_table_class(schema, connection['base'], satellite_name)
            print(satellite_table)
            satellite_definition = satellite_definitions[satellite_name]
            hub_name = satellite_definition['hub']
            hub_table = get_table_class(schema, connection['base'], hub_name)
            link_keys = {}
            for row in data['FCRB'][table]:
                dv_row = {key: row[key] for key in row if key in satellite_definition['columns']}
                hub_keys = {key: row[key] for key in row if key not in satellite_definition['columns']}
                print(hub_keys)
                sat_stmt = (insert(satellite_table).values(**dv_row))
                sat_id = connection['engine'].execute(sat_stmt)
                hub_stmt = (insert(hub_table).values(**hub_keys))
                hub_id = connection['engine'].execute(hub_stmt)
                print(hub_id.inserted_primary_key[0])

def fill_data_vault(data, body):
    schema = fcrb_data_vault()
    connection = setup_connection(schema)
    for table in data['FCRB']:
        satellite_definitions = fcrb_sats[table]
        links = satellite_definitions.pop('links')
        for row in data['FCRB'][table]:
            print(f"TABLE: {table}")
            if len(links) > 0:
                link_keys = get_link_keys(links)
            else:
                link_keys = None
            for satellite_name in satellite_definitions:
                satellite_table = get_table_class(schema, connection['base'], satellite_name)
                satellite_definition = satellite_definitions[satellite_name]
                hub_name = satellite_definition['hub']
                hub_id_name = hub_name.split('_')[1] + '_id'
                hub_table = get_table_class(schema, connection['base'], hub_name)
                dv_row = {key: row[key] for key in row if key in satellite_definition['columns']}
                hub_keys = {key: row[key] for key in row if key in fcrb_keys}
                sat_stmt = (insert(satellite_table).values(**dv_row))
                sat_id = connection['engine'].execute(sat_stmt)
                hub_stmt = (insert(hub_table).values(**hub_keys))
                hub_id = connection['engine'].execute(hub_stmt)
                if link_keys != None:
                    for link in link_keys:
                        if hub_id_name in link_keys[link].keys():
                            link_keys[link][hub_id_name] = hub_id.inserted_primary_key[0]
            print(link_keys)
            if link_keys != None:
                for link in links:
                    link_table = get_table_class(schema, connection['base'], link)
                    link_stmt = (insert(link_table).values(**link_keys[link]))
                    connection['engine'].execute(link_stmt)

            
