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


def get_table_and_table_keys(data, source_table_name):
    table = data[source_table_name]
    table_keys = []
    for key in fcrb_keys:
        if key in table.columns:
            table_keys.append(key)
    return table, table_keys
    
def get_remaining_fields(table, table_keys):
    remaining_columns = [column for column in table.columns if column not in set(table_keys)]
    return table[remaining_columns]

def build_hubs(table, table_keys):
    hub_fields = table[table_keys]
    for key in fcrb_keys:
        if key not in hub_fields.columns:
            hub_fields.loc[:, key] = None
    return hub_fields

def get_satellite_fields(table, table_keys):
    columns = [column for column in table.columns if column in set(table_keys)]
    return table[columns]

def build_satellites(source_table_name, remaining_fields):
    satellite_definitions = fcrb_sats[source_table_name]
    satellites = []
    links = fcrb_sats[source_table_name].pop('links')
    for satellite_name in satellite_definitions:
        columns = satellite_definitions[satellite_name]['columns']
        satellite = get_satellite_fields(remaining_fields, columns)
        if not satellite.empty:
            satellite_details = {
                'name': satellite_name,
                'hub': satellite_definitions[satellite_name]['hub'],
                'table': satellite
            }
            satellites.append(satellite_details)
            # print(satellite_details)
    return satellites, links

def build_hubs_and_satellites(source_data, body):
    """This is a single hospital's full data set"""
    results = {}
    for hospital in body['hospital_ids']:
        data = source_data[hospital]
        results[hospital] = {}
        """This is a single table from the data set and picks the keys"""
        for source_table_name in data.keys():
            table, table_keys = get_table_and_table_keys(data, source_table_name)
            results[hospital][source_table_name] = {}
            """Fill the hubs with the values for the primary keys"""
            remaining_fields = get_remaining_fields(table, table_keys)
            hubs = build_hubs(table, table_keys)
            results[hospital][source_table_name]['hub'] = hubs 
            satellites, links = build_satellites(source_table_name, remaining_fields)
            results[hospital][source_table_name]['satellites'] = satellites
            results[hospital][source_table_name]['links'] = links 
    return results


def build_link():
    """This needs to be done I think"""
            
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

def fill_data_vault(data, body):
    schema = fcrb_data_vault()
    connection = setup_connection(schema)
    hubs_and_satellites = build_hubs_and_satellites(data, body)
    for hospital in hubs_and_satellites:
        for table in hubs_and_satellites[hospital]:
            
            hub_definition = hubs_and_satellites[hospital][table]['hub'].reset_index(drop=True)
            links = hubs_and_satellites[hospital][table].pop('links')
            print(links)
            for satellite in hubs_and_satellites[hospital][table]['satellites']:
                satellite_name = satellite['name']
                satellite_hub = satellite['hub']
                satellite_table = satellite['table'].reset_index(drop=True)
                
                satellite_class = get_table_class(schema, connection['base'], satellite_name)
                key_range = {}
                
                hub_class = get_table_class(schema, connection['base'], satellite_hub)
                satellite_table.to_sql(satellite_name, connection['engine'], if_exists='append', schema=schema, index=False)
                if hub_class is not None:
                    result = connection['engine'].execute(func.max(hub_class.id)).fetchone()
                    if result[0] == None:
                        key_range['start'] = 1
                    else:
                        key_range['start'] = result[0]
                hub_definition.to_sql(satellite_hub, connection['engine'], if_exists='append', schema=schema, index=False)
                if hub_class is not None:
                    result = connection['engine'].execute(func.max(hub_class.id)).fetchone()
                    if result[0] == None:
                        key_range['end'] = 1
                    else:
                        key_range['end'] = result[0]
                key_range['link'] = links
                print(key_range)
    connection['engine'].dispose()

