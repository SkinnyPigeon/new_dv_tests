import json

from functions.get_source_data import get_patient_data
# from functions.create_data_vault import build_hubs_and_satellites, fill_data_vault
from functions.new_create_dv import fill_data_vault
from refactored.data_vault.data_vault import data_vault

body = {
  "serums_id": 364,
  "rule_id": "RULE_0df8eb8b-a469-46ae-8119-fbf98fa05b92",
  "tags": [
    "wearable"
  ],
  "hospital_ids": [
    "ZMC"
  ],
  "public_key": "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCDM+DNCybR7LdizOcK1gH2P7dD\nsajGUEIoPFp7wjhgKykYkCGVQCvl55g/zdh6UI9Cd/i2IEf5wo+Ct9oihy9SnJSp\n3sOp1KESV+ElwdK3vkaIo1AUuj+E8LTe7llyJ61JJdZaozyT0PxM8jB2vIaNEdbO\nbURHcIsIDc64L0e1ZQIDAQAB\n-----END PUBLIC KEY-----"
}

data, tags = get_patient_data(body)
json_tags = json.dumps(tags, indent=2)
print(json_tags)
data_vault('ZMC', 'test', tags)
# fill_data_vault(data, body['hospital_ids'])
# results = build_hubs_and_satellites(data, body)
# print(results)