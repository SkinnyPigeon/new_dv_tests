import copy
from functions.get_source_data import PASSWORD

from sqlalchemy import Table, MetaData, select

from refactored.connection.password_and_port import get_password_and_port
from refactored.connection.connection import data_vault_connection
from control_files.fcrb_keys_and_sats import fcrb_keys, fcrb_sats
from control_files.ustan_keys_and_sats import ustan_keys, ustan_sats
from control_files.zmc_keys_and_sats import zmc_keys, zmc_sats

def hospital_picker(hospital):
    if hospital == 'FCRB':
        return fcrb_keys, copy.deepcopy(fcrb_sats)
    elif hospital == 'USTAN':
        return ustan_keys, copy.deepcopy(ustan_sats)
    elif hospital == 'ZMC':
        return zmc_keys, copy.deepcopy(zmc_sats)

def select_all_from_table(table_name, schema, database):
    password, port = get_password_and_port()
    engine = data_vault_connection(password, port, database)
    metadata = MetaData(bind=engine, schema=schema, reflect=True)
    table_obj = Table(table_name, metadata, autoload_with=engine)
    stmt = (select([table_obj]))
    result = engine.execute(stmt).fetchall()
    return [row for row in result]

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


def build_dv_sphr(hospitals, schemas, database):
    dv_sphr = {}
    for hospital in hospitals:
        schema = schemas[hospital]
        sat_definitions = hospital_picker(hospital)[1]
        for table in sat_definitions:
            pass