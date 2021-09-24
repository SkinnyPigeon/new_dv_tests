import copy
from functions.get_source_data import PASSWORD

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

def select_all_from_table(table_name, schema, database):
    password, port = get_password_and_port()
    engine = data_vault_connection(password, port, database)
    metadata = MetaData(bind=engine, schema=schema, reflect=True)
    table_obj = Table(table_name, metadata, autoload_with=engine)
    stmt = (select([table_obj]))
    result = engine.execute(stmt).fetchall()
    engine.dispose()
    columns = table_obj.columns.keys()
    # print(table_obj.columns.keys())
    # results = []
    # for row in result:
    #     results.append({column: row[i] for i, column in enumerate(columns)})
    return [{column: row[i] for i, column in enumerate(columns)} for row in result]
        # for i, column in enumerate(columns):
        #     results.append({column: row[i]})
    
    # return [row for row in result]

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

def get_satellites(hospital, schema, database):
    sat_definitions, tags = hospital_picker(hospital)
    sats = {}
    for table in sat_definitions:
        sat_definitions[table].pop('links')
        for sat in sat_definitions[table]:
            try:
                sats[f"{hospital.lower()}_{sat}"] = select_all_from_table(sat, schema, database)
            except NoSuchTableError as e:
                print(f"Table does not exist: {e}")
    return sats

def build_dv_sphr(hospitals, schemas, database):
    dv_sphr = {}
    for hospital in hospitals:
        schema = schemas[hospital]
        dv_sphr[hospital] = {}
        hubs, links = get_hubs_and_links(schema, database)
        dv_sphr[hospital]['hubs'] = hubs
        dv_sphr[hospital]['links'] = links
        sats = get_satellites(hospital, schema, database)
        dv_sphr[hospital]['satellites'] = sats
    # print(dv_sphr)
    return dv_sphr

def convert_hubs(hubs):
    print(hubs)
        
def convert_to_single_dict(dv_sphr, hospitals):
    hubs = [[].append(dv_sphr[hospital]['hubs'] for hospital in hospitals)]
    print(hubs)
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
