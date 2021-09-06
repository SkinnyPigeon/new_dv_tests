# Imports

from sqlalchemy.schema import CreateSchema
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, BigInteger
from sqlalchemy import MetaData

from password_and_port import get_password_and_port
from connection import random_schema_name, data_vault_connection
from data_vault_boilerplate import boilerplate

from fcrb_keys import fcrb_keys


database = 'test'
def data_vault(database):
    password, port = get_password_and_port()
    schema = random_schema_name()
    print(f"SCHEMA: {schema}")
    Base, engine = data_vault_connection(password, port, database)
    engine.execute(CreateSchema(schema))
    # IS THERE ANOTHER WAY INSTEAD OF FCRB_KEYS?
    boilerplate(Base, schema, engine, fcrb_keys)

       
        # # Satellites

        # class SatEventDiagnosticDetails(Base):
        #     __tablename__ = 'sat_event_diagnostic_details'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     lfdnr = Column(String(3))
        #     dkey1 = Column(String(30))

        # class SatTimeEpisodeDetails(Base):
        #     __tablename__ = 'sat_time_episode_details'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     erdat = Column(DateTime(timezone=False))
        #     begdt = Column(DateTime(timezone=False))
        #     enddt = Column(DateTime(timezone=False))

        # class SatEventEpisodeDetails(Base):
        #     __tablename__ = 'sat_event_episode_details'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     falar = Column(String(1))
        #     bekat = Column(String(40))
        #     einzg = Column(String(9))
        #     statu = Column(String(1))
        #     krzan = Column(String(1))
        #     storn = Column(String(1))
        #     casetx = Column(String(20))
        #     fatxt = Column(String(40))
        #     enddtx = Column(String(20))

        # class SatPersonMedicalSpecialty(Base):
        #     __tablename__ = 'sat_person_medical_specialty'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     orgna = Column(String(40))

        # class SatTimeMedicationDetails(Base):
        #     __tablename__ = 'sat_time_medication_details'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     erdat = Column(DateTime(timezone=False))
        #     stdat = Column(DateTime(timezone=False))


        # class SatEventMedicationDetails(Base):
        #     __tablename__ = 'sat_event_medication_details'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     motx = Column(String(60))
        #     mostx = Column(String(80))
        #     mpresnr = Column(String(10))
        #     motypid = Column(String(2))
        #     storn = Column(String(1))
        #     stusr = Column(String(10))
        #     stoid = Column(String(15))

        # class SatTimeMonitoringParams(Base):
        #     __tablename__ = 'sat_time_monitoring_params'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     datyp = Column(DateTime(timezone=False))

        # class SatEventMonitoringParams(Base):
        #     __tablename__ = 'sat_event_monitoring_params'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     vbem = Column(String(150))
        #     wertogr = Column(String(20))
        #     wertugr = Column(String(20))
        #     wertmax = Column(String(20))
        #     wertmin = Column(String(20))

        # class SatTimeOrderEntry(Base):
        #     __tablename__ = 'sat_time_order_entry'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     erdat = Column(DateTime(timezone=False))

        # class SatEventOrderEntry(Base):
        #     __tablename__ = 'sat_event_order_entry'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     idodr = Column(String(10))

        # class SatLocationPatientAddress(Base):
        #     __tablename__ = 'sat_location_patient_address'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     pstlz = Column(String(10))
        #     stras = Column(String(50))
        #     land = Column(String(15))
        #     ort = Column(String(20))
        #     deck = Column(String(15))
        #     adrnr = Column(String(5))

        # class SatPersonPatientDetails(Base):
        #     __tablename__ = 'sat_person_patient_details'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     gschl = Column(String(1))
        #     nname = Column(String(30))
        #     vname = Column(String(30))
        #     gbdat = Column(DateTime(timezone=False))
        #     gbnam = Column(String(30))
        #     namzu = Column(String(5))
        #     glrand = Column(String(20))
        #     famst = Column(String(10))
        #     telf1 = Column(String(15))
        #     rvnum = Column(String(20))

        # class SatTimeProfessionalDetails(Base):
        #     __tablename__ = 'sat_time_professional_details'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     begdt = Column(DateTime(timezone=False))
        #     enddt = Column(DateTime(timezone=False))
        #     erdat = Column(DateTime(timezone=False))

        # class SatPersonProfessionalDetails(Base):
        #     __tablename__ = 'sat_person_professional_details'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     erusr = Column(String(12))
        #     gbdat = Column(DateTime(timezone=False))
        #     rank = Column(String(3))

        # class SatTimeVitalSigns(Base):
        #     __tablename__ = 'sat_time_vital_signs'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     erdat = Column(DateTime(timezone=False))

        # class SatEventVitalSigns(Base):
        #     __tablename__ = 'sat_event_vital_signs'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     idvs = Column(String(10))
        #     dttyp = Column(String(10))
        #     typevs = Column(String(9))
        #     vwert = Column(String(7))
        #     vbem = Column(String(150))

        # Base.metadata.create_all(engine)
        # engine.dispose()
    #     return schema

    # except Exception as e:
    #     engine.dispose()
    #     return {"Error": str(e)}

data_vault('test')