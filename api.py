import json

from functions.get_source_data import get_patient_data
# from functions.create_data_vault import build_hubs_and_satellites, fill_data_vault
# from functions.new_create_dv import fill_data_vault
from refactored.data_vault.fill_data_vault import fill_data_vault
from refactored.data_vault.data_vault import data_vault
# from example_data.ustan_data import data
# from example_data.ustan_tags import tags

body = {
  "serums_id": 364,
  "rule_id": "RULE_0df8eb8b-a469-46ae-8119-fbf98fa05b92",
  "tags": [
    "all"
  ],
  "hospital_ids": [
    "USTAN"
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
  'hub_time': 10,
  'hub_person': 10,
  'hub_object': 10,
  'hub_location': 10,
  'hub_event': 10
}
# for hospital in body["hospital_ids"]:
#   schema = data_vault(hospital, 'test', data[hospital]['tags'])
#   fill_data_vault(data[hospital]['data'], hospital, 'test', schema, data[hospital]['tags'])
#   print(schema)
#   print("\n\n")
schema = data_vault('USTAN', 'test', data['USTAN']['tags'], hub_values)
fill_data_vault(data['USTAN']['data'], 'USTAN', 'test', schema)
# print(hub_values)
# fill_data_vault(data, body['hospital_ids'])
# results = build_hubs_and_satellites(data, body)
# print(results)