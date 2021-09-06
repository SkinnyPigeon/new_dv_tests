from sqlalchemy import Column, BigInteger, String

def fcrb_keys():
    return [
        Column("id", BigInteger, primary_key=True),
        Column("einri", String(4)),
        Column("patnr", BigInteger),
        Column("falnr", String(10)),
        Column("pernr", String(12)),
        Column("orgid", String(8)),
        Column("vppid", String(15))
    ]