from sqlalchemy import Column, BigInteger
def id_column():
    return Column("id", BigInteger, primary_key=True)