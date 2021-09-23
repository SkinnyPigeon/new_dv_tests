from sqlalchemy import Column, BigInteger, String
from refactored.data_vault.keys.id_column import id_column
def zmc_keys(start_value):
    return [
        id_column("id", primary=True, start_value=start_value),
        Column("patnr", BigInteger)
    ]