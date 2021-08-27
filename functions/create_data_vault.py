from sqlalchemy import schema
from functions.fcrb_data_vault import fcrb_data_vault
from control_files.fcrb_keys_and_sats import fcrb_keys, fcrb_sats
import pandas as pd
pd.options.mode.chained_assignment = None

def get_table_and_table_keys(data, source_table_name):
    table = data[source_table_name]
    table_keys = []
    for key in fcrb_keys:
        if key in table.columns:
            table_keys.append(key)
    return table, table_keys
    
def get_remaining_fields(table, table_keys):
    remaining_columns = [column for column in table.columns if column not in set(table_keys)]
    # print("REMAINING FIELDS")
    # print(table[remaining_columns])
    # print("\n")
    return table[remaining_columns]



def build_hubs(table, table_keys):
    hub_fields = table[table_keys]
    for key in fcrb_keys:
        if key not in hub_fields.columns:
            hub_fields.loc[:, key] = None
    # print("HUB_FIELDS")
    # print(hub_fields)
    # print("\n")
    return hub_fields

def get_satellite_fields(table, table_keys):
    columns = [column for column in table.columns if column in set(table_keys)]
    return table[columns]

def build_satellites(source_table_name, remaining_fields):
    satellite_definitions = fcrb_sats[source_table_name]
    satellites = []
    for satellite_name in satellite_definitions:
        columns = satellite_definitions[satellite_name]['columns']
        satellite = get_satellite_fields(remaining_fields, columns)
        if not satellite.empty:
            satellite_details = {
                'name': satellite_name,
                'hub': satellite_definitions[satellite_name]['hub'],
                'table': satellite
            }
            satellites.append(satellite_details)
    print(satellites)

def create_data_vault(source_data, body):
    """This is a single hospital's full data set"""
    for hospital in body['hospital_ids']:
        data = source_data[hospital]

        """This is a single table from the data set and picks the keys"""
        for source_table_name in data.keys():
            table, table_keys = get_table_and_table_keys(data, source_table_name)
            
            """Fill the hubs with the values for the primary keys"""
            remaining_fields = get_remaining_fields(table, table_keys)
            hubs = build_hubs(table, table_keys)
            print(hubs)
            satellites = build_satellites(source_table_name, remaining_fields)
            

