from sqlalchemy import create_engine, MetaData, insert, select
from sqlalchemy import func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

from functions.fcrb_data_vault import fcrb_data_vault
from control_files.fcrb_keys_and_sats import fcrb_keys, fcrb_sats
import pandas as pd
pd.options.mode.chained_assignment = None


import os
from dotenv import load_dotenv
import subprocess
project_folder = subprocess.check_output("pwd", shell=True).decode("utf-8").rstrip()
load_dotenv(os.path.join(project_folder, '.env'))
PORT = os.getenv('PGPORT')
PASSWORD = os.getenv('PGPASSWORD')
if PORT == None:
    PASSWORD = os.environ.get('PGPASSWORD')
    PORT = os.environ.get('PGPORT')

def setup_connection(schema):
    engine = create_engine('postgresql://postgres:{}@localhost:{}/source'.format(PASSWORD, PORT))
    metadata = MetaData(schema=schema, bind=engine)
    metadata.reflect(engine)
    Base = automap_base(metadata=metadata)
    Base.prepare()
    Session = sessionmaker(bind=engine)
    session = Session()
    return {"metadata": metadata, "base": Base, "engine": engine, "session": session, 'schema': schema}


def loop_through_tables(data, body):
    for table in data['FCRB']:
        print(table)
        for row in data['FCRB'][table]:
            print(row)
            print("\n")

# def get

def fill_data_vault(data, body):
    for table in data['FCRB']:
        satellite_definitions = fcrb_sats[table]
        links = satellite_definitions.pop('links')
        for satellite_name in satellite_definitions:
            satellite_definition = satellite_definitions[satellite_name]
            for row in data['FCRB'][table]:
                dv_row = print([row[key] for key in row if key in satellite_definition['columns']])
        #     print(f"COLUMNS: {columns}")
        # print(f"LINKS: {links}")
        # print("\n")