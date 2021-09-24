import copy
import pandas as pd
from sqlalchemy.sql.expression import table
from tabulate import tabulate

from sqlalchemy import Table, MetaData, select
from sqlalchemy.exc import NoSuchTableError

from refactored.connection.password_and_port import get_password_and_port
from refactored.connection.connection import data_vault_connection
from control_files.fcrb_keys_and_sats import fcrb_keys, fcrb_sats
from control_files.ustan_keys_and_sats import ustan_keys, ustan_sats
from control_files.zmc_keys_and_sats import zmc_keys, zmc_sats
from sources.tags.fcrb import fcrb_tags
from sources.tags.ustan import ustan_tags
from sources.tags.zmc import zmc_tags

def hospital_picker(hospital):
    if hospital == 'FCRB':
        return copy.deepcopy(fcrb_sats), fcrb_tags
    elif hospital == 'USTAN':
        return copy.deepcopy(ustan_sats), ustan_tags
    elif hospital == 'ZMC':
        return copy.deepcopy(zmc_sats), zmc_tags

def table_picker(tag_names, tags):
    print(f"TAG NAMES: {tag_names}")
    for tag in tags:
        print(tag)
        print("\n")
        if tag['tag'] in tag_names:
            print(f"ASKDJSKJSD: {tag}")
    print([tag['source'] for tag in tags if tag['tag'] in tag_names])
    return [tag['source'] for tag in tags if tag['tag'] in tag_names]

def sat_picker(tables, sat_definitions):
    print(F"TABLES: {tables}")
    sat_names = []
    for table in tables:
        print(table)
        try:
            sat_definitions[table].pop('links')
        except:
            print(f"Already popped: {table}")
        sat_names.extend([sat_name for sat_name in sat_definitions[table]])
    return sat_names

def select_all_from_table(table_name, schema, database):
    password, port = get_password_and_port()
    engine = data_vault_connection(password, port, database)
    metadata = MetaData(bind=engine, schema=schema, reflect=True)
    table_obj = Table(table_name, metadata, autoload_with=engine)
    print(table_obj)
    stmt = (select([table_obj]))
    result = engine.execute(stmt).fetchall()
    engine.dispose()
    columns = table_obj.columns.keys()
    return [{column: row[i] for i, column in enumerate(columns)} for row in result]

def get_hubs_and_links(schema, database):
    hub_names = ['hub_time', 'hub_person', 'hub_object', 'hub_location', 'hub_event']
    link_names = [
        'time_person_link', 'time_object_link', 'time_location_link', 'time_event_link',
        'person_object_link', 'person_location_link', 'person_event_link',
        'object_location_link', 'object_event_link',
        'location_event_link'
    ]
    hubs = {hub: select_all_from_table(hub, schema, database) for hub in hub_names}
    links = {link: select_all_from_table(link, schema, database) for link in link_names}
    return hubs, links

def get_satellites(hospital, schema, database, request_tags):
    sat_definitions, tag_definitions = hospital_picker(hospital)
    table_names = table_picker(request_tags, tag_definitions)
    sat_names = sat_picker(table_names, sat_definitions)
    print(f"SAT NAMES: {sat_names}")
    sats = {}
    for table in sat_definitions:
        try:
            sat_definitions[table].pop('links')
        except:
            print("ALREADY POPPED")
        for sat in sat_names:
            print(f"SATELLITE {sat}")
            try:
                sats[f"{hospital.lower()}_{sat}"] = select_all_from_table(sat, schema, database)
            except NoSuchTableError as e:
                print(f"Table does not exist: {e}")
    return sats

def build_dv_sphr(hospitals, schemas, database, request_tags):
    dv_sphr = {}
    for hospital in hospitals:
        schema = schemas[hospital]
        dv_sphr[hospital] = {}
        hubs, links = get_hubs_and_links(schema, database)
        dv_sphr[hospital]['hubs'] = hubs
        dv_sphr[hospital]['links'] = links
        sats = get_satellites(hospital, schema, database, request_tags)
        dv_sphr[hospital]['satellites'] = sats
    return dv_sphr

def convert_single_table(table_name, table_group):
    table = [table[table_name] for table in table_group]
    table_dfs = [pd.DataFrame.from_dict(table_dict) for table_dict in table]
    table_result = pd.concat(table_dfs, ignore_index=True, sort=False)
    return table_result

def convert_tables(table_group, table_names):
    df_tables = [convert_single_table(table_name, table_group) for table_name in table_names]
    for df in df_tables:
        print(tabulate(df, headers='keys', tablefmt='psql'))
    return df_tables

def create_table_dfs(table_names, table_type, dv_sphr, hospitals):
    tables = []
    tables.extend([dv_sphr[hospital][table_type] for hospital in hospitals])
    table_dfs = convert_tables(tables, table_names)
    return table_dfs  

def get_satellite_names(dv_sphr):
    sat_names = []
    for hospital in dv_sphr:
        sat_names.extend([sat_name for sat_name in dv_sphr[hospital]['satellites']])
    print(sat_names)
    return sat_names

def convert_to_single_dict(dv_sphr, hospitals):
    hub_names = ['hub_time', 'hub_person', 'hub_object', 'hub_location', 'hub_event']
    hub_dfs = create_table_dfs(hub_names, 'hubs', dv_sphr, hospitals)

    link_names = [
        'time_person_link', 'time_object_link', 'time_location_link', 'time_event_link',
        'person_object_link', 'person_location_link', 'person_event_link',
        'object_location_link', 'object_event_link',
        'location_event_link'
    ]
    link_dfs = create_table_dfs(link_names, 'links', dv_sphr, hospitals)
    
    sat_names = get_satellite_names(dv_sphr)
    sat_dfs = create_table_dfs(sat_names, 'satellites', dv_sphr, hospitals)
    

