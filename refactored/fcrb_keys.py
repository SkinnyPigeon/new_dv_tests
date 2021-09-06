from sqlalchemy import Column, BigInteger, String
from id_column import id_column
def fcrb_keys():
    return [
        id_column(),
        Column("einri", String(4)),
        Column("patnr", BigInteger),
        Column("falnr", String(10)),
        Column("pernr", String(12)),
        Column("orgid", String(8)),
        Column("vppid", String(15))
    ]