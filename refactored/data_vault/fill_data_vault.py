from sqlalchemy import MetaData, insert, Table

from refactored.data_vault.keys.id_column import id_column
from refactored.tables.fcrb_table_definitions import fcrb_table_definitions
from refactored.tables.ustan_table_definitions import ustan_table_definitions
from refactored.tables.zmc_table_definitions import zmc_table_definitions
from control_files.fcrb_keys_and_sats import fcrb_keys, fcrb_sats
from control_files.ustan_keys_and_sats import ustan_keys, ustan_sats
from control_files.zmc_keys_and_sats import zmc_keys, zmc_sats
from refactored.connection.password_and_port import get_password_and_port
from refactored.connection.connection import data_vault_connection


def hospital_picker(hospital):
    if hospital == 'FCRB':
        return fcrb_keys, fcrb_sats, fcrb_table_definitions
    elif hospital == 'USTAN':
        return ustan_keys, ustan_sats, ustan_table_definitions
    elif hospital == 'ZMC':
        return zmc_keys, zmc_sats, zmc_table_definitions

def fill_data_vault(data, hospital, database, schema, tags):
    password, port = get_password_and_port()
    engine = data_vault_connection(password, port, database)
    metadata = MetaData(bind=engine, schema=schema, reflect=True)
    keys, sats, table_definitions = hospital_picker(hospital)
    # This will loop through the tables in the data
    table_name = 'ustan.smr01'
    table_data = data[table_name]
    # stmt = (insert(table).values())
    # print(stmt)
    print(sats[table_name])
    # link_names = sats[table_name].pop('links')
    # print(link_names)
    for row in table_data:
        hub_keys = {key: row[key] for key in row if key in keys}
        print(hub_keys)
        link_values = {}
        for sat_name in sats[table_name]:
            hub_obj = Table(sats[table_name][sat_name]['hub'], metadata, autoload_with=engine)
            hub_stmt = (insert(hub_obj).values(**hub_keys))
            link_ref = sats[table_name][sat_name]['hub'].split('_')[1] + '_id'
            hub_id = engine.execute(hub_stmt).inserted_primary_key[0]
            link_values[link_ref] = hub_id

            sat_obj = Table(f"{sat_name}", metadata, autoload_with=engine)
            column_names = sats[table_name][sat_name]['columns']
            row_values = {key: row[key] for key in row if key in column_names}
            row_values['hub_id'] = hub_id
            sat_stmt = (insert(sat_obj).values(**row_values))
            engine.execute(sat_stmt)
        print(link_values)
        # for link_name in link_names:

            