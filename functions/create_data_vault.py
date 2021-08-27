from sqlalchemy import schema
from functions.fcrb_data_vault import fcrb_data_vault
from control_files.fcrb_keys_and_sats import fcrb_keys, fcrb_sats
import pandas as pd
pd.options.mode.chained_assignment = None

# def create_hubs(keys):
#     hub_time = pd.DataFrame(columns=keys)
#     hub_person = pd.DataFrame(columns=keys)
#     hub_object = pd.DataFrame(columns=keys)
#     hub_location = pd.DataFrame(columns=keys)
#     hub_event = pd.DataFrame(columns=keys)
#     return hub_time, hub_person, hub_object, hub_location, hub_event

# def create_key_dict(all_keys):
#     key_dict = {}
#     for key in all_keys:
#         key_dict[key] = ''
#     return key_dict

# def fill_hubs(fcrb_keys, row):
#     print(row)
#     key_dict = create_key_dict(fcrb_keys)


def get_table_and_table_keys(data, source_table_name):
    table = data[source_table_name]
    table_keys = []
    for key in fcrb_keys:
        if key in table.columns:
            table_keys.append(key)
    return table, table_keys
    
def get_remaining_fields(table, table_keys):
    remaining_columns = [column for column in table.columns if column not in set(table_keys)]
    return table[remaining_columns]

def build_hubs(table, table_keys):
    hub_fields = table[table_keys]
    for key in fcrb_keys:
        if key not in hub_fields.columns:
            hub_fields.loc[:, key] = None
    return hub_fields

def create_data_vault(source_data, body):
    """This is a single hospital's full data set"""
    for hospital in body['hospital_ids']:
        data = source_data[hospital]

        """This is a single table from the data set and picks the keys"""
        for source_table_name in data.keys():
            table, table_keys = get_table_and_table_keys(data, source_table_name)

            """Fill the hubs with the values for the primary keys"""
            remaining_fields = get_remaining_fields(table, table_keys)
            print("REMAINING FIELDS")
            print(remaining_fields)
            print("\n")

            hub_fields = build_hubs(table, table_keys)
            print("HUB_FIELDS")
            print(hub_fields)
            print("\n")

