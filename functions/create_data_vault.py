from sqlalchemy import schema
from functions.fcrb_data_vault import fcrb_data_vault
from control_files.fcrb_keys_and_sats import fcrb_keys, fcrb_sats

def create_data_vault(source_data, body):
    schema = fcrb_data_vault()
    for hospital in body['hospital_ids']:
        data = source_data[hospital]
        for source_table in data.keys():
            sats = fcrb_sats[source_table]
            for sat in sats.keys():
                print(f"SOURCE TABLE: {source_table}")
                print(sats[sat])
