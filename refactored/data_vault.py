# Imports

from sqlalchemy.schema import CreateSchema

from password_and_port import get_password_and_port
from connection import random_schema_name, data_vault_connection
from data_vault_boilerplate import boilerplate

from fcrb_keys import fcrb_keys
from fcrb_satellites import fcrb_satellites

def pick_hospital(hospital):
    if hospital == 'FCRB':
        return fcrb_keys, fcrb_satellites

database = 'test'
def data_vault(database):
    password, port = get_password_and_port()
    schema = random_schema_name()
    print(f"SCHEMA: {schema}")
    engine = data_vault_connection(password, port, database)
    engine.execute(CreateSchema(schema))
    keys, satellites = pick_hospital('FCRB')
    boilerplate(schema, engine, keys)
    satellites(schema, engine)

       
    

data_vault('test')