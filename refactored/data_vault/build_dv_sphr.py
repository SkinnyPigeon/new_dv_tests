import copy
import pandas as pd
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

def table_picker(tag_name, tags):
    return [tag['source'] for tag in tags if tag['tag'] == tag_name]

def sat_picker(tables, sat_definitions):
    sat_names = []
    for table in tables:
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
    sats = {}
    for table in sat_definitions:
        sat_definitions[table].pop('links')
        for sat in sat_names:
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
    # print(dv_sphr)
    return dv_sphr


def convert_single_hub(hub_name, hubs):
    hub = [hub[hub_name] for hub in hubs]
    hub_dfs = [pd.DataFrame.from_dict(hub_table) for hub_table in hub]
    hub_result = pd.concat(hub_dfs, ignore_index=True, sort=False)
    return hub_result

def convert_hubs(hubs):
    hub_names = ['hub_time', 'hub_person', 'hub_object', 'hub_location', 'hub_event']
    df_hubs = [convert_single_hub(hub_name, hubs) for hub_name in hub_names]
    # hubs = [[hub[hub_name] for hub in hubs] for hub_name in hub_names]
    # hub_dfs = [pd.DataFrame.from_dict(hub) for hub in hubs]
    # hub_times = [hub['hub_time'] for hub in hubs]
    # hub_persons = [hub['hub_person'] for hub in hubs]
    # hub_objects = [hub['hub_object'] for hub in hubs]
    # hub_locations = [hub['hub_location'] for hub in hubs]
    # hub_events = [hub['hub_event'] for hub in hubs]
    # time_dfs = [pd.DataFrame.from_dict(hub_time) for hub_time in hub_times]
    # time_results = pd.concat(time_dfs, ignore_index=True, sort=False)
    # df_time = DataFrame.from_dict(hub_times, orient='columns')
    # print(time_results)
    for df in df_hubs:
        print(tabulate(df, headers='keys', tablefmt='psql'))
        
def convert_to_single_dict(dv_sphr, hospitals):
    hubs = []
    hubs.extend([dv_sphr[hospital]['hubs'] for hospital in hospitals])
    convert_hubs(hubs)
    # hubs = convert_hubs(dv_sphr[])
    # single_dv = {}
    # single_dv['hubs'] = []
    # single_dv['links'] = []
    # single_dv['satellites'] = []
    # for hospital in hospitals:
    #     single_dv['hubs'].append(dv_sphr[hospital]['hubs'])
    #     single_dv['links'].append(dv_sphr[hospital]['links'])
    #     single_dv['satellites'].append(dv_sphr[hospital]['satellites'])
    # print(single_dv)
    # return single_dv
