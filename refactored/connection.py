from sqlalchemy import create_engine

import string
import random

def random_schema_name():
    return '_' + ''.join(random.choice(string.ascii_lowercase) for c in range(8))

def data_vault_connection(password, port, database):
    engine = create_engine(f"postgresql://postgres:{password}@localhost:{port}/{database}")
    return engine