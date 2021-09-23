from refactored.data_vault.keys.id_column import id_column
from refactored.tables.fcrb_table_definitions import fcrb_table_definitions
from refactored.tables.ustan_table_definitions import ustan_table_definitions
from refactored.tables.zmc_table_definitions import zmc_table_definitions
from control_files.fcrb_keys_and_sats import fcrb_keys, fcrb_sats
from control_files.ustan_keys_and_sats import ustan_keys, ustan_sats
from control_files.zmc_keys_and_sats import zmc_keys, zmc_sats
from refactored.connection import connection

def hospital_picker(hospital):
    if hospital == 'FCRB':
        return fcrb_keys, fcrb_sats, fcrb_table_definitions
    elif hospital == 'USTAN':
        return ustan_keys, ustan_sats, ustan_table_definitions
    elif hospital == 'ZMC':
        return zmc_keys, zmc_sats, zmc_table_definitions

def fill_data_vault(data, hospital, database, schema, tags):
    keys, sats, table_definitions = hospital_picker(hospital)
    # This will loop through the tables in the data
    table_name = 'ustan.smr01'
    test = data[table_name]
    sats[table_name].pop('links')
    for row in test:
        row_keys = {key: row[key] for key in row if key in keys}
        for sat_name in sats[table_name]:
            hub_name = sats[table_name][sat_name]['hub']
            column_names = sats[table_name][sat_name]['columns']
            print(sat_name)
            print(hub_name)
            print(column_names)