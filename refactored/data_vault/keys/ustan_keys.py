from sqlalchemy import Column, BigInteger, String
from refactored.data_vault.keys.id_column import id_column
def ustan_keys():
    return [
        id_column("id"),
        Column("chi", BigInteger)
    ]