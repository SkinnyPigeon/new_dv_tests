from sqlalchemy import Column, BigInteger, String
from refactored.data_vault.keys.id_column import id_column
def zmc_keys(start_value, table_name, metadata=None, schema=None):
    return [
        id_column("id", table_name=table_name, metadata=metadata, schema=schema, hub=True, primary=True, start_value=start_value),
        Column("patnr", BigInteger)
    ]