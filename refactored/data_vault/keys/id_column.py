from sqlalchemy import Column, BigInteger
from sqlalchemy.schema import Sequence
def id_column(column_name, table_name=None, metadata=None, primary=False, start_value=0):
    if primary:
        return Column(column_name, BigInteger, Sequence(f"{table_name}_{column_name}_seq", metadata=metadata, start=start_value), primary_key=True)
        # return Column(column_name, BigInteger, Sequence(f"{table_name}_{column_name}_seq", start=start_value, increment=1), primary_key=True)
    else:
        return Column(column_name, BigInteger)