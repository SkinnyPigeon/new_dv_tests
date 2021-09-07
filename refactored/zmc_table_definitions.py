from sqlalchemy import Column, DateTime, Time, Integer, Numeric, String

zmc_table_definitions = {
    "zmc.wearable": {
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
    "zmc.medical_aids_and_tools": {
        "product_description": Column("product_description", String(50)),
        "anatomical_location": Column("anatomical_location", String(40)),
        "description":  Column("description", String(50))
    },
    "zmc.patient_details": {
        "nname": Column("nname", String(40)),
        "nnams": Column("nnams", String(40)),
        "vname": Column("vname", String(6)),
        "titel": Column("titel", String(6)),
        "gschl": Column("gschl", String(10)),
        "gbdat": Column("gbdat", DateTime(timezone=False)),
        "natio": Column("natio", String(3))
    }
}