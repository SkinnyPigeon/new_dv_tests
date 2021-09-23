from sqlalchemy import Column, BigInteger
from sqlalchemy.schema import Sequence
def id_column(column_name, table_name=None, metadata=None, schema=None, primary=False, start_value=0, hub=False):
    if hub and primary:
        seq = Sequence(f"{table_name}_{column_name}_seq", metadata=metadata, schema=schema, start=start_value)
        return Column(column_name, BigInteger, seq, server_default=seq.next_value(), primary_key=True, autoincrement=True)
    elif not hub and primary:
        return Column(column_name, BigInteger, primary_key=True)
    else:
        return Column(column_name, BigInteger)