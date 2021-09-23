from sqlalchemy import Column, BigInteger
def id_column(column_name, primary=True):
    return Column(column_name, BigInteger, primary_key=primary)