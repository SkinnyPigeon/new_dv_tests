from sqlalchemy import Table
from sqlalchemy.sql.schema import MetaData
from refactored.data_vault.keys.id_column import id_column
from refactored.tables.zmc_table_definitions import zmc_table_definitions
from control_files.zmc_keys_and_sats import zmc_sats

def zmc_satellites(schema, engine, tags):
    metadata = MetaData()
    for tag in tags:
        source = tag['source']
        satellites = zmc_sats[source]
        satellites.pop('links')

        column_definitions = zmc_table_definitions[source]

        for satellite in satellites:
            columns = satellites[satellite]['columns']
            fields_set = set(tag['fields'])
            common_fields = list(fields_set.intersection(columns))
            sat_columns = [column_definitions[field] for field in common_fields]
            sat_columns.insert(0, id_column())
            print(sat_columns)
            table = Table(satellite, metadata, schema=schema, *sat_columns)
            table.create(engine)