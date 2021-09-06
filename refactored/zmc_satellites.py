from sqlalchemy import Table
from sqlalchemy.sql.schema import MetaData
from refactored.id_column import id_column
from refactored.zmc_satellite_definitions import zmc_satellite_definitions
import json
def zmc_satellites(schema, engine, tags):
    metadata = MetaData()
    for tag in tags:
        source = tag['source'].split('.')[1]

    metadata.create_all(engine)