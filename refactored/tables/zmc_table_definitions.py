from sqlalchemy import Column, DateTime, Time, Integer, Numeric, String, BigInteger
from sqlalchemy.dialects.postgresql import ARRAY, JSON

zmc_table_definitions = {
    "zmc.serums_ids": {
        "id": Column("id", BigInteger, primary_key=True),
        "serums_id": Column("serums_id", Integer),
        "patnr": Column("patnr", BigInteger)
    },
    "zmc.hospital_doctors": {
        "id": Column("id", Integer, primary_key=True),
        "serums_id": Column("serums_id", Integer),
        "staff_id": Column("staff_id", Integer),
        "name": Column("name", String),
        "department_id": Column("department_id", Integer),
        "department_name": Column("department_name", String)
    },
    "zmc.tags": {
        "id": Column("id", Integer, primary_key=True),
        "tags": Column("tags", ARRAY(String)) 
    },
    "zmc.translated_tags": {
        "id": Column("id", Integer, primary_key=True),
        "tags": Column("tags", JSON) 
    },
    "zmc.wearable": {
        "id": Column("id", BigInteger, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "date": Column("date", DateTime(timezone=False)),
        "w_time": Column("w_time", Time),
        "w_steps": Column("w_steps", Integer),
        "w_cad": Column("w_cad", Integer),
        "sst": Column("sst", Integer),
        "sst_time": Column("sst_time", Numeric(3, 1)),
        "cyc_time": Column("cyc_time", Time),
        "cyc_steps": Column("cyc_steps", Integer),
        "cyc_cad": Column("cyc_cad", Integer)
    },
    "zmc.images": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "image_title": Column("image_title", String(50)),
        "type": Column("type", String(50)),
        "date": Column("date", DateTime(timezone=False)),
        "image": Column("image", String)
    },
    "zmc.documents": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "document_title": Column("document_title", String(50)),
        "type": Column("type", String(50)),
        "date": Column("date", DateTime(timezone=False)),
        "document": Column("document", String)
    },
    "zmc.complaints_and_diagnosis": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "complaints_and_diagnosis": Column("complaints_and_diagnosis", String(50)),
        "status": Column("status", String(20)),
        "specialism": Column("specialism", String(20)),
        "type": Column("type", String(20)),
        "name_of_diagnosis_or_complaint": Column("name_of_diagnosis_or_complaint", String(30)),
        "anatomical_location": Column("anatomical_location", String(20)),
        "laterality": Column("laterality", String(10)),
        "begin_date": Column("begin_date", DateTime(timezone=False)),
        "end_date": Column("end_date", DateTime(timezone=False))
    },
    "zmc.medication_agreements": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "medicines": Column("medicines", String(30)),
        "prescribed_by": Column("prescribed_by", String(40)),
        "description": Column("description", String(50))
    },
    "zmc.medication_use": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "product": Column("product", String(30)),
        "use": Column("use", String(40)),
        "reason": Column("reason", String(50))
    },
    "zmc.medical_aids_and_tools": {
        "id": Column("id", BigInteger, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "product_description": Column("product_description", String(50)),
        "anatomical_location": Column("anatomical_location", String(40)),
        "description":  Column("description", String(50))
    },
    "zmc.bloodpressure": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "value": Column("value", String(20)),
        "date": Column("date", DateTime(timezone=False)),
        "systolic_bloodpressure": Column("systolic_bloodpressure", Integer),
        "diastolic_bloodpressure": Column("diastolic_bloodpressure", Integer),
        "position": Column("position", String(40)),
        "measurement_method": Column("measurement_method", String(40)),
        "manchette_type": Column("manchette_type", String(40)),
        "measurement_location": Column("measurement_location", String(40)),
        "description": Column("description", String(40))
    },
    "zmc.weight": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "measurement": Column("measurement", String(10)),
        "clothes": Column("clothes", String(20)),
        "description": Column("description", String(40)),
        "date": Column("date", DateTime(timezone=False))
    },
    "zmc.length": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "measurement": Column("measurement", String(10)),
        "description": Column("description", String(40)),
        "date": Column("date", DateTime(timezone=False))
    },
    "zmc.registered_events": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "type": Column("type", String(40)),
        "method": Column("method", String(40)),
        "anatomical_location": Column("anatomical_location", String(40)),
        "description": Column("description", String(255)),
        "laterality": Column("laterality", String(40)),
        "start_date": Column("start_date", DateTime(timezone=False)),
        "end_date": Column("end_date", DateTime(timezone=False)),
        "indication": Column("indication", String(40)),
        "executor": Column("executor", String(40)),
        "requested_by": Column("requested_by", String(40)),
        "location": Column("location", String(100)),
        "date": Column("date", DateTime(timezone=False))
    },
    "zmc.warning": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "alerts": Column("alerts", String(40)),
        "begindate": Column("begindate", DateTime(timezone=False)),
        "type": Column("type", String(40))
    },
    "zmc.functional_or_mental_state": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "name": Column("name", String(40)),
        "value": Column("value", String(40)),
        "date": Column("date", DateTime(timezone=False))
    },
    "zmc.living_situation": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "house_type": Column("house_type", String(40)),
        "description": Column("description", String(40))
    },
    "zmc.drug_use": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "substance": Column("substance", String(40)),
        "quantity": Column("quantity", String(40)),
        "description": Column("description", String(40))
    },
    "zmc.alcohol_use": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "usage_status": Column("usage_status", String(40)),
        "quantity": Column("quantity", String(40)),
        "description": Column("description", String(40))
    },
    "zmc.tobacco_use": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "substance": Column("substance", String(40)),
        "quantity": Column("quantity", Integer),
        "description": Column("description", String(40))
    },
    "zmc.allergies": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "caustive_substance": Column("caustive_substance", String(40)),
        "critical": Column("critical", String(20)),
        "description": Column("description", String(40))
    },
    "zmc.patient_details": {
        "id": Column("id", BigInteger, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "nname": Column("nname", String(40)),
        "nnams": Column("nnams", String(40)),
        "vname": Column("vname", String(6)),
        "titel": Column("titel", String(6)),
        "gschl": Column("gschl", String(10)),
        "gbdat": Column("gbdat", DateTime(timezone=False)),
        "natio": Column("natio", String(3))
    }
}