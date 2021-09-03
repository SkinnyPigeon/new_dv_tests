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

def get_table_class(schema, base, table_name):
    for class_name in base._decl_class_registry.values():
        if hasattr(class_name, '__table__') and class_name.__table__.fullname == f"{schema}.{table_name}":
            return class_name

def get_link_keys(links):
    for link in links:
        split_text = link.split('_')
        link_keys = {link: {key + '_id': '' for key in split_text if key != 'link'}}
    return link_keys

def empty_link_keys(links):
    if len(links) > 0:
        link_keys = get_link_keys(links)
    else:
        link_keys = None
    return link_keys

def hospital_picker(hospital):
    if hospital == 'FCRB':
        schema = fcrb_data_vault()
        return schema, fcrb_sats, fcrb_keys

def hub_elements(satellite_definition, schema, connection):
    hub_name = satellite_definition['hub']
    hub_id_name = hub_name.split('_')[1] + '_id'
    hub_table = get_table_class(schema, connection['base'], hub_name)
    return hub_id_name, hub_table

def hub_and_dv_row(row, satellite_definition):
    hub_row = {key: row[key] for key in row if key in fcrb_keys}
    dv_row = {key: row[key] for key in row if key in satellite_definition['columns']}
    return hub_row, dv_row

def create_row(row, columns):
    row = {key: row[key] for key in row if key in columns}
    return row

def insert_row(table, connection, row):
    stmt = (insert(table).values(**row))
    id = connection['engine'].execute(stmt)
    return id

def update_link_keys(link_keys, hub_id_name, hub_id):
    if link_keys != None:
        for link in link_keys:
            if hub_id_name in link_keys[link].keys():
                link_keys[link][hub_id_name] = hub_id.inserted_primary_key[0]
    return link_keys

def insert_links(link_keys, links, schema, connection):
    if link_keys != None:
        for link in links:
            link_table = get_table_class(schema, connection['base'], link)
            link_stmt = (insert(link_table).values(**link_keys[link]))
            connection['engine'].execute(link_stmt)

def fill_data_vault(data, hospitals):
    for hospital in hospitals:
        schema, satellites, keys = hospital_picker(hospital)
        connection = setup_connection(schema)

        for table in data[hospital]:
            satellite_definitions = satellites[table]
            links = satellite_definitions.pop('links')

            for row in data[hospital][table]:
                link_keys = empty_link_keys(links)

                for satellite_name in satellite_definitions:
                    satellite_table = get_table_class(schema, connection['base'], satellite_name)
                    satellite_definition = satellite_definitions[satellite_name]

                    hub_id_name, hub_table = hub_elements(satellite_definition, schema, connection)

                    hub_row = create_row(row, keys)
                    dv_row = create_row(row, satellite_definition['columns'])
                    
                    sat_id = insert_row(satellite_table, connection, dv_row)
                    hub_id = insert_row(hub_table, connection, hub_row)

                    link_keys = update_link_keys(link_keys, hub_id_name, hub_id)
                   
                insert_links(link_keys, links, schema, connection)
            connection['engine'].dispose()