from sqlalchemy import Column, String, Integer, DateTime, BigInteger
from sqlalchemy.dialects.postgresql import ARRAY, JSON

fcrb_table_definitions = {
    "fcrb.serums_ids": {
        "id": Column("id", BigInteger, primary_key=True),
        "serums_id": Column("serums_id", Integer),
        "patnr": Column("patnr", BigInteger)
    },
    "fcrb.hospital_doctors": {
        "id": Column("id", Integer, primary_key=True),
        "serums_id": Column("serums_id", Integer),
        "staff_id": Column("staff_id", Integer),
        "name": Column("name", String),
        "department_id": Column("department_id", Integer),
        "department_name": Column("department_name", String)
    },
    "fcrb.tags": {
        "id": Column("id", Integer, primary_key=True),
        "tags": Column("tags", ARRAY(String))
    },
    "fcrb.translated_tags": {
        "id": Column("id", Integer, primary_key=True),
        "tags": Column("tags", JSON)
    },
    "fcrb.diagnostic": {
        "id": Column("id", Integer, primary_key=True),
        "einri": Column("einri", String(4)),
        "patnr": Column("patnr", BigInteger),
        "falnr": Column("falnr", String(10)),
        "pernr": Column("pernr", String(12)),
        "lfdnr": Column("lfdnr", String(3)),
        "dkey1": Column("dkey1", String(30))
    },
    "fcrb.episode": {
        "id": Column("id", Integer, primary_key=True),
        "falnr": Column("falnr", String(10)),
        "pernr": Column("pernr", String(12)),
        "einri": Column("einri", String(4)),
        "falar": Column("falar", String(1)),
        "patnr": Column("patnr", BigInteger),
        "bekat": Column("bekat", String(40)),
        "einzg": Column("einzg", String(9)),
        "statu": Column("statu", String(1)),
        "krzan": Column("krzan", String(1)),
        "enddt": Column("enddt", DateTime(timezone=False)),
        "erdat": Column("erdat", DateTime(timezone=False)),
        "storn": Column("storn", String(1)),
        "begdt": Column("begdt", DateTime(timezone=False)),
        "casetx": Column("casetx", String(20)),
        "fatxt": Column("fatxt", String(40)),
        "enddtx": Column("enddtx", String(20))
    },
    "fcrb.medical_specialty": {
        "id": Column("id", Integer, primary_key=True),
        "orgid": Column("orgid", String(8)),
        "orgna": Column("orgna", String(40))
    },
    "fcrb.medication": {
        "id": Column("id", Integer, primary_key=True),
        "einri": Column("einri", String(4)),
        "patnr": Column("patnr", BigInteger),
        "falnr": Column("falnr", String(10)),
        "motx": Column("motx", String(60)),
        "mostx": Column("mostx", String(80)),
        "mpresnr": Column("mpresnr", String(10)),
        "motypid": Column("motypid", String(2)),
        "pernr": Column("pernr", String(10)),
        "erdat": Column("erdat", DateTime(timezone=False)),
        "storn": Column("storn", String(1)),
        "stusr": Column("stusr", String(10)),
        "stdat": Column("stdat", DateTime(timezone=False)),
        "stoid": Column("stoid", String(15))
    },
    "fcrb.monitoring_params": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "falnr": Column("falnr", String(10)),
        "vppid": Column("vppid", String(15)),
        "pernr": Column("pernr", String(10)),
        "vbem": Column("vbem", String(150)),
        "datyp": Column("datyp", DateTime(timezone=False)),
        "wertogr": Column("wertogr", String(20)),
        "wertugr": Column("wertugr", String(20)),
        "wertmax": Column("wertmax", String(20)),
        "wertmin": Column("wertmin", String(20))
    },
    "fcrb.order_entry": {
        "id": Column("id", Integer, primary_key=True),
        "idodr": Column("idodr", String(10)),
        "einri": Column("einri", String(10)),
        "falnr": Column("falnr", String(10)),
        "patnr": Column("patnr", BigInteger),
        "pernr": Column("pernr", String(12)),
        "erdat": Column("erdat", DateTime(timezone=False)),
        "orgid": Column("orgid", String(8))
    },
    "fcrb.patient_address": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "pstlz": Column("pstlz", String(10)),
        "stras": Column("stras", String(50)),
        "land": Column("land", String(15)),
        "ort": Column("ort", String(20)),
        "deck": Column("deck", String(15)),
        "adrnr": Column("adrnr", String(5))
    },
    "fcrb.patient": {
        "id": Column("id", Integer, primary_key=True),
        "patnr": Column("patnr", BigInteger),
        "gschl": Column("gschl", String(1)),
        "nname": Column("nname", String(30)),
        "vname": Column("vname", String(30)),
        "gbdat": Column("gbdat", DateTime(timezone=False)),
        "gbnam": Column("gbnam", String(30)),
        "namzu": Column("namzu", String(5)),
        "glrand": Column("glrand", String(20)),
        "famst": Column("famst", String(10)),
        "telf1": Column("telf1", String(15)),
        "rvnum": Column("rvnum", String(20))
    },
    "fcrb.professional": {
        "id": Column("id", Integer, primary_key=True),
        "pernr": Column("pernr", String(10)),
        "erusr": Column("erusr", String(12)),
        "orgid": Column("orgid", String(8)),
        "gbdat": Column("gbdat", DateTime(timezone=False)),
        "begdt": Column("begdt", DateTime(timezone=False)),
        "enddt": Column("enddt", DateTime(timezone=False)),
        "erdat": Column("erdat", DateTime(timezone=False)),
        "rank": Column("rank", String(3))
    },
    "fcrb.vital_signs": {
        "id": Column("id", Integer, primary_key=True),
        "idvs": Column("idvs", String(10)),
        "patnr": Column("patnr", BigInteger),
        "falnr": Column("falnr", String(10)),
        "vppid": Column("vppid", String(15)),
        "dttyp": Column("dttyp", String(10)),
        "erdat": Column("erdat", DateTime(timezone=False)),
        "typevs": Column("typevs", String(9)),
        "vwert": Column("vwert", String(7)),
        "vbem": Column("vbem", String(150))
    }
}