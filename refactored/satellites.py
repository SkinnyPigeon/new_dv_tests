from sqlalchemy import Table
from sqlalchemy.sql.schema import MetaData
from refactored.id_column import id_column
from refactored.zmc_table_definitions import zmc_table_definitions
from refactored.fcrb_table_definitions import fcrb_table_definitions
from control_files.zmc_keys_and_sats import zmc_sats
from control_files.fcrb_keys_and_sats import fcrb_sats

def hospital_picker(hospital):
    if hospital == 'FCRB':
        return fcrb_sats, fcrb_table_definitions
    elif hospital == 'ZMC':
        return zmc_sats, zmc_table_definitions

def satellites(hospital, schema, engine, tags):
    sats, table_definitions = hospital_picker(hospital)
    metadata = MetaData()
    for tag in tags:
        source = tag['source']
        satellites = sats[source]
        satellites.pop('links')

        column_definitions = table_definitions[source]

        for satellite in satellites:
            columns = satellites[satellite]['columns']
            fields_set = set(tag['fields'])
            common_fields = list(fields_set.intersection(columns))
            sat_columns = [column_definitions[field] for field in common_fields]
            sat_columns.insert(0, id_column())
            print(sat_columns)
            table = Table(satellite, metadata, schema=schema, *sat_columns)
            table.create(engine)