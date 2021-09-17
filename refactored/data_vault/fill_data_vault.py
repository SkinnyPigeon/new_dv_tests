from refactored.data_vault.keys.id_column import id_column
from refactored.tables.fcrb_table_definitions import fcrb_table_definitions
from refactored.tables.ustan_table_definitions import ustan_table_definitions
from refactored.tables.zmc_table_definitions import zmc_table_definitions
from control_files.fcrb_keys_and_sats import fcrb_sats
from control_files.ustan_keys_and_sats import ustan_sats
from control_files.zmc_keys_and_sats import zmc_sats

def hospital_picker(hospital):
    if hospital == 'FCRB':
        return fcrb_sats, fcrb_table_definitions
    elif hospital == 'USTAN':
        return ustan_sats, ustan_table_definitions
    elif hospital == 'ZMC':
        return zmc_sats, zmc_table_definitions

def fill_data_vault(data, database, schema, tags):
    print(tags)
    pass