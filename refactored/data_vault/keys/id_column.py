from sqlalchemy import Column, BigInteger
def id_column(column_name):
    return Column(column_name, BigInteger, primary_key=True)