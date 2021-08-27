from functions.fcrb_data_vault import fcrb_data_vault
from functions.get_source_data import get_patient_data
from control_files.fcrb_keys_and_sats import fcrb_keys, fcrb_satellites
from sources.tags.fcrb import fcrb_tags

selected_tag = 'patient_address'

selected_tags = []
for tag in fcrb_tags:
    if tag['tag'] == selected_tag:
        selected_tags.append(tag)

body = {
  "serums_id": 364,
  "rule_id": "RULE_0df8eb8b-a469-46ae-8119-fbf98fa05b92",
  "tags": [
    "patient_address"
  ],
  "hospital_ids": [
    "FCRB"
  ],
  "public_key": "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCDM+DNCybR7LdizOcK1gH2P7dD\nsajGUEIoPFp7wjhgKykYkCGVQCvl55g/zdh6UI9Cd/i2IEf5wo+Ct9oihy9SnJSp\n3sOp1KESV+ElwdK3vkaIo1AUuj+E8LTe7llyJ61JJdZaozyT0PxM8jB2vIaNEdbO\nbURHcIsIDc64L0e1ZQIDAQAB\n-----END PUBLIC KEY-----"
}

data = get_patient_data(body)
print(data)