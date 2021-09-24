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


# schemas = {
#   'USTAN': '_zllupmqh',
#   'FCRB': '_httmmvon',
#   'ZMC': '_makbedon'
# }


# test_dv = {'USTAN': {'hubs': {'hub_time': [{'id': 1, 'chi': 1005549224}], 'hub_person': [{'id': 1, 'chi': 1005549224}, {'id': 2, 'chi': 1005549224}], 'hub_object': [], 'hub_location': [{'id': 1, 'chi': 1005549224}], 'hub_event': [{'id': 1, 'chi': 1005549224}]}, 'links': {'time_person_link': [{'id': 1, 'time_id': 1, 'person_id': 2}], 'time_object_link': [], 'time_location_link': [{'id': 1, 'time_id': 1, 'location_id': 1}], 'time_event_link': [{'id': 1, 'time_id': 1, 'event_id': 1}], 'person_object_link': [], 'person_location_link': [{'id': 1, 'person_id': 2, 'location_id': 1}], 'person_event_link': [{'id': 1, 'person_id': 2, 'event_id': 1}], 'object_location_link': [], 'object_event_link': [], 'location_event_link': [{'id': 1, 'location_id': 1, 'event_id': 1}]}, 'satellites': {}}, 'FCRB': {'hubs': {'hub_time': [{'id': 2, 'einri': None, 'patnr': 4641202, 'falnr': '988392719', 'pernr': None, 'orgid': None, 'vppid': None}, {'id': 3, 'einri': None, 'patnr': 4641202, 'falnr': '89439002', 'pernr': None, 'orgid': None, 'vppid': None}, {'id': 4, 'einri': None, 'patnr': 4641202, 'falnr': '96823483', 'pernr': None, 'orgid': None, 'vppid': None}], 'hub_person': [], 'hub_object': [], 'hub_location': [], 'hub_event': [{'id': 1, 'einri': 'HCPB', 'patnr': 4641202, 'falnr': '988392719', 'pernr': '2827346', 'orgid': None, 'vppid': None}, {'id': 2, 'einri': 'HCPB', 'patnr': 4641202, 'falnr': '98823483', 'pernr': '8405937', 'orgid': None, 'vppid': None}, {'id': 3, 'einri': None, 'patnr': 4641202, 'falnr': '988392719', 'pernr': None, 'orgid': None, 'vppid': None}, {'id': 4, 'einri': None, 'patnr': 4641202, 'falnr': '89439002', 'pernr': None, 'orgid': None, 'vppid': None}, {'id': 5, 'einri': None, 'patnr': 4641202, 'falnr': '96823483', 'pernr': None, 'orgid': None, 'vppid': None}]}, 'links': {'time_person_link': [], 'time_object_link': [], 'time_location_link': [], 'time_event_link': [{'id': 1, 'time_id': 1, 'event_id': 3}, {'id': 2, 'time_id': 2, 'event_id': 4}, {'id': 3, 'time_id': 3, 'event_id': 5}], 'person_object_link': [], 'person_location_link': [], 'person_event_link': [], 'object_location_link': [], 'object_event_link': [], 'location_event_link': []}, 'satellites': {}}, 'ZMC': {'hubs': {'hub_time': [{'id': 5, 'patnr': 1075835}, {'id': 6, 'patnr': 1075835}, {'id': 7, 'patnr': 1075835}, {'id': 8, 'patnr': 1075835}, {'id': 9, 'patnr': 1075835}, {'id': 10, 'patnr': 1075835}, {'id': 11, 'patnr': 1075835}, {'id': 12, 'patnr': 1075835}], 'hub_person': [{'id': 1, 'patnr': 1075835}], 'hub_object': [], 'hub_location': [{'id': 1, 'patnr': 1075835}, {'id': 2, 'patnr': 1075835}, {'id': 3, 'patnr': 1075835}, {'id': 4, 'patnr': 1075835}], 'hub_event': 
# [{'id': 5, 'patnr': 1075835}, {'id': 6, 'patnr': 1075835}, {'id': 7, 'patnr': 1075835}, {'id': 8, 'patnr': 1075835}, {'id': 9, 'patnr': 1075835}, {'id': 10, 'patnr': 1075835}, {'id': 11, 'patnr': 1075835}, {'id': 12, 'patnr': 1075835}]}, 'links': {'time_person_link': [], 'time_object_link': [], 'time_location_link': [{'id': 1, 'time_id': 4, 'location_id': 1}, {'id': 2, 'time_id': 7, 'location_id': 2}, {'id': 3, 'time_id': 8, 'location_id': 3}, {'id': 4, 'time_id': 9, 'location_id': 4}], 'time_event_link': [{'id': 1, 'time_id': 3, 'event_id': 5}, {'id': 2, 'time_id': 4, 'event_id': 6}, {'id': 3, 'time_id': 5, 'event_id': 7}, {'id': 4, 'time_id': 6, 'event_id': 8}, {'id': 5, 'time_id': 7, 'event_id': 9}, {'id': 6, 'time_id': 8, 'event_id': 10}, {'id': 
# 7, 'time_id': 9, 'event_id': 11}, {'id': 8, 'time_id': 10, 'event_id': 12}], 'person_object_link': [], 'person_location_link': [], 'person_event_link': [], 'object_location_link': [], 'object_event_link': [], 'location_event_link': [{'id': 1, 'location_id': 1, 'event_id': 6}, {'id': 2, 'location_id': 2, 'event_id': 9}, {'id': 3, 'location_id': 3, 'event_id': 10}, {'id': 4, 'location_id': 4, 'event_id': 11}]}, 'satellites': {}}}



dv_sphr = build_dv_sphr(body['hospital_ids'], schemas, 'test', body['tags'])
# print(dv_sphr)
single_dv = convert_to_single_dict(dv_sphr, body['hospital_ids'])

# select_all_from_table('sat_time_cycle_details', '_ldqlwzxg', 'test')


# schema = data_vault('USTAN', 'test', data['USTAN']['tags'], hub_values)
# hub_values = fill_data_vault(data['USTAN']['data'], 'USTAN', 'test', schema)

# print(hub_values)
# fill_data_vault(data, body['hospital_ids'])
# results = build_hubs_and_satellites(data, body)
# print(results)