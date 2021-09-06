from sqlalchemy import Column, BigInteger, String
from refactored.id_column import id_column
def zmc_keys():
    return [
        id_column(),
        Column("patnr", BigInteger)
    ]