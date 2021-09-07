from sqlalchemy.schema import CreateSchema

from refactored.connection.password_and_port import get_password_and_port
from refactored.connection.connection import random_schema_name, data_vault_connection
from refactored.data_vault.data_vault_boilerplate import boilerplate

from refactored.data_vault.keys.fcrb_keys import fcrb_keys
# from refactored.data_vault.tables.fcrb_satellites import fcrb_satellites

from refactored.data_vault.keys.zmc_keys import zmc_keys
# from refactored.zmc_satellites import zmc_satellites

from refactored.data_vault.satellites import satellites

def pick_hospital(hospital):
    if hospital == 'FCRB':
        return fcrb_keys
    elif hospital == 'ZMC':
        return zmc_keys

def data_vault(hospital, database, tags):
    password, port = get_password_and_port()
    schema = random_schema_name()
    print(f"SCHEMA: {schema}")
    engine = data_vault_connection(password, port, database)
    engine.execute(CreateSchema(schema))
    keys = pick_hospital(hospital)
    boilerplate(schema, engine, keys)
    satellites(hospital, schema, engine, tags)