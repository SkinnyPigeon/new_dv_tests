from sqlalchemy.schema import CreateSchema

from refactored.password_and_port import get_password_and_port
from refactored.connection import random_schema_name, data_vault_connection
from refactored.data_vault_boilerplate import boilerplate

from refactored.fcrb_keys import fcrb_keys
from refactored.fcrb_satellites import fcrb_satellites

from refactored.zmc_keys import zmc_keys
from refactored.zmc_satellites import zmc_satellites

def pick_hospital(hospital):
    if hospital == 'FCRB':
        return fcrb_keys, fcrb_satellites
    elif hospital == 'ZMC':
        return zmc_keys, zmc_satellites

def data_vault(database, tags):
    password, port = get_password_and_port()
    schema = random_schema_name()
    print(f"SCHEMA: {schema}")
    engine = data_vault_connection(password, port, database)
    engine.execute(CreateSchema(schema))
    keys, satellites = pick_hospital('ZMC')
    boilerplate(schema, engine, keys)
    satellites(schema, engine, tags)