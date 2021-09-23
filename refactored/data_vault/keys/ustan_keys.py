from sqlalchemy import Column, BigInteger, String
from refactored.data_vault.keys.id_column import id_column
def ustan_keys(start_value, table_name, metadata=None):
    return [
        id_column("id", table_name, metadata=metadata, primary=True, start_value=start_value),
        Column("chi", BigInteger)
    ]