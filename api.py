import json

from functions.get_source_data import get_patient_data
# from functions.create_data_vault import build_hubs_and_satellites, fill_data_vault
# from functions.new_create_dv import fill_data_vault
from refactored.data_vault.fill_data_vault import fill_data_vault
from refactored.data_vault.data_vault import data_vault
# from example_data.ustan_data import data
# from example_data.ustan_tags import tags
from refactored.data_vault.build_dv_sphr import build_dv_sphr, convert_to_single_dict

body = {
  "serums_id": 364,
  "rule_id": "RULE_0df8eb8b-a469-46ae-8119-fbf98fa05b92",
  "tags": [
    "all"
  ],
  "hospital_ids": [
    "USTAN",
    "FCRB", 
    "ZMC"
  ],
  "public_key": "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCDM+DNCybR7LdizOcK1gH2P7dD\nsajGUEIoPFp7wjhgKykYkCGVQCvl55g/zdh6UI9Cd/i2IEf5wo+Ct9oihy9SnJSp\n3sOp1KESV+ElwdK3vkaIo1AUuj+E8LTe7llyJ61JJdZaozyT0PxM8jB2vIaNEdbO\nbURHcIsIDc64L0e1ZQIDAQAB\n-----END PUBLIC KEY-----"
}

data = get_patient_data(body)
# print(tags)
# print(json.dumps(data, indent=2))
# json.dumps(data, indent=2)
# json_tags = json.dumps(tags, indent=2)
# print(json_tags)
hub_values = {
  'hub_time': 1,
  'hub_person': 1,
  'hub_object': 1,
  'hub_location': 1,
  'hub_event': 1
}
schemas = {}
for hospital in body["hospital_ids"]:
  schema = data_vault(hospital, 'test', data[hospital]['tags'], hub_values)
  # Change test below to be the hospital's own datalake
  hub_values = fill_data_vault(data[hospital]['data'], hospital, 'test', schema)
  schemas[hospital] = schema
  print(schema)
  print("\n\n")

dv_sphr = build_dv_sphr(body['hospital_ids'], schemas, 'test')
single_dv = convert_to_single_dict(dv_sphr, body['hospital_ids'])

# select_all_from_table('sat_time_cycle_details', '_ldqlwzxg', 'test')


# schema = data_vault('USTAN', 'test', data['USTAN']['tags'], hub_values)
# hub_values = fill_data_vault(data['USTAN']['data'], 'USTAN', 'test', schema)

# print(hub_values)
# fill_data_vault(data, body['hospital_ids'])
# results = build_hubs_and_satellites(data, body)
# print(results)