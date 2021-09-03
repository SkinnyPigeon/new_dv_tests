# Imports

from sqlalchemy import create_engine, MetaData
from sqlalchemy.schema import CreateSchema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, BigInteger

from dotenv import load_dotenv
from pathlib import Path

import os
import subprocess

import string
import random

project_folder = subprocess.check_output(
    "pwd", shell=True).decode("utf-8").rstrip()
load_dotenv(os.path.join(project_folder, '.env'))
PORT = os.getenv('PGPORT')
PASSWORD = os.getenv('PGPASSWORD')
if PORT == None:
    PASSWORD = os.environ.get('PGPASSWORD')
    PORT = os.environ.get('PGPORT')

def create_random_schema():
    return '_' + ''.join(random.choice(string.ascii_lowercase) for c in range(8))

def fcrb_data_vault():
    schema = create_random_schema()
    print(f"SCHEMA: {schema}")
    Base = declarative_base()
    engine = create_engine('postgresql://postgres:{}@localhost:{}/data_vault'.format(PASSWORD, PORT))
    engine.execute(CreateSchema(schema))

    class HubTime(Base):
        __tablename__ = 'hub_time'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        einri = Column(String(4))
        patnr = Column(BigInteger)
        falnr = Column(String(10))
        pernr = Column(String(12))
        orgid = Column(String(8))
        vppid = Column(String(15))

    class HubPerson(Base):
        __tablename__ = 'hub_person'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        einri = Column(String(4))
        patnr = Column(BigInteger)
        falnr = Column(String(10))
        pernr = Column(String(12))
        orgid = Column(String(8))
        vppid = Column(String(15))

    class HubObject(Base):
        __tablename__ = 'hub_object'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        einri = Column(String(4))
        patnr = Column(BigInteger)
        falnr = Column(String(10))
        pernr = Column(String(12))
        orgid = Column(String(8))
        vppid = Column(String(15))

    class HubLocation(Base):
        __tablename__ = 'hub_location'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        einri = Column(String(4))
        patnr = Column(BigInteger)
        falnr = Column(String(10))
        pernr = Column(String(12))
        orgid = Column(String(8))
        vppid = Column(String(15))

    class HubEvent(Base):
        __tablename__ = 'hub_event'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        einri = Column(String(4))
        patnr = Column(BigInteger)
        falnr = Column(String(10))
        pernr = Column(String(12))
        orgid = Column(String(8))
        vppid = Column(String(15))

    class TimePersonLink(Base):
        __tablename__ = 'time_person_link'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        time_id = Column(Integer, ForeignKey(HubTime.id))
        person_id = Column(Integer, ForeignKey(HubPerson.id))

    class TimeObjectLink(Base):
        __tablename__ = 'time_object_link'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        time_id = Column(Integer, ForeignKey(HubTime.id))
        object_id = Column(Integer, ForeignKey(HubObject.id))

    class TimeLocationLink(Base):
        __tablename__ = 'time_location_link'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        time_id = Column(Integer, ForeignKey(HubTime.id))
        location_id = Column(Integer, ForeignKey(HubLocation.id))

    class TimeEventLink(Base):
        __tablename__ = 'time_event_link'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        time_id = Column(Integer, ForeignKey(HubTime.id))
        event_id = Column(Integer, ForeignKey(HubEvent.id))

    class PersonObjectLink(Base):
        __tablename__ = 'person_object_link'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        person_id = Column(Integer, ForeignKey(HubPerson.id))
        object_id = Column(Integer, ForeignKey(HubObject.id))

    class PersonLocationLink(Base):
        __tablename__ = 'person_location_link'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        person_id = Column(Integer, ForeignKey(HubPerson.id))
        location_id = Column(Integer, ForeignKey(HubLocation.id))

    class PersonEventLink(Base):
        __tablename__ = 'person_event_link'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        person_id = Column(Integer, ForeignKey(HubPerson.id))
        event_id = Column(Integer, ForeignKey(HubEvent.id))

    class ObjectLocationLink(Base):
        __tablename__ = 'object_location_link'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        object_id = Column(Integer, ForeignKey(HubObject.id))
        location_id = Column(Integer, ForeignKey(HubLocation.id))

    class ObjectEventLink(Base):
        __tablename__ = 'object_event_link'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        object_id = Column(Integer, ForeignKey(HubObject.id))
        event_id = Column(Integer, ForeignKey(HubEvent.id))

    class LocationEventLink(Base):
        __tablename__ = 'location_event_link'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        location_id = Column(Integer, ForeignKey(HubLocation.id))
        event_id = Column(Integer, ForeignKey(HubEvent.id))

    # Satellites

    class SatEventDiagnosticDetails(Base):
        __tablename__ = 'sat_event_diagnostic_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        lfdnr = Column(String(3))
        dkey1 = Column(String(30))

    class SatTimeEpisodeDetails(Base):
        __tablename__ = 'sat_time_episode_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        erdat = Column(DateTime(timezone=False))
        begdt = Column(DateTime(timezone=False))
        enddt = Column(DateTime(timezone=False))

    class SatEventEpisodeDetails(Base):
        __tablename__ = 'sat_event_episode_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        falar = Column(String(1))
        bekat = Column(String(40))
        einzg = Column(String(9))
        statu = Column(String(1))
        krzan = Column(String(1))
        storn = Column(String(1))
        casetx = Column(String(20))
        fatxt = Column(String(40))
        enddtx = Column(String(20))

    class SatPersonMedicalSpecialty(Base):
        __tablename__ = 'sat_person_medical_specialty'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        orgna = Column(String(40))

    class SatTimeMedicationDetails(Base):
        __tablename__ = 'sat_time_medication_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        erdat = Column(DateTime(timezone=False))
        stdat = Column(DateTime(timezone=False))


    class SatEventMedicationDetails(Base):
        __tablename__ = 'sat_event_medication_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        motx = Column(String(60))
        mostx = Column(String(80))
        mpresnr = Column(String(10))
        motypid = Column(String(2))
        storn = Column(String(1))
        stusr = Column(String(10))
        stoid = Column(String(15))

    class SatTimeMonitoringParams(Base):
        __tablename__ = 'sat_time_monitoring_params'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        datyp = Column(DateTime(timezone=False))

    class SatEventMonitoringParams(Base):
        __tablename__ = 'sat_event_monitoring_params'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        vbem = Column(String(150))
        wertogr = Column(String(20))
        wertugr = Column(String(20))
        wertmax = Column(String(20))
        wertmin = Column(String(20))

    class SatTimeOrderEntry(Base):
        __tablename__ = 'sat_time_order_entry'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        erdat = Column(DateTime(timezone=False))

    class SatEventOrderEntry(Base):
        __tablename__ = 'sat_event_order_entry'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        idodr = Column(String(10))

    class SatLocationPatientAddress(Base):
        __tablename__ = 'sat_location_patient_address'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        pstlz = Column(String(10))
        stras = Column(String(50))
        land = Column(String(15))
        ort = Column(String(20))
        deck = Column(String(15))
        adrnr = Column(String(5))

    class SatPersonPatientDetails(Base):
        __tablename__ = 'sat_person_patient_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        gschl = Column(String(1))
        nname = Column(String(30))
        vname = Column(String(30))
        gbdat = Column(DateTime(timezone=False))
        gbnam = Column(String(30))
        namzu = Column(String(5))
        glrand = Column(String(20))
        famst = Column(String(10))
        telf1 = Column(String(15))
        rvnum = Column(String(20))

    class SatTimeProfessionalDetails(Base):
        __tablename__ = 'sat_time_professional_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        begdt = Column(DateTime(timezone=False))
        enddt = Column(DateTime(timezone=False))
        erdat = Column(DateTime(timezone=False))

    class SatPersonProfessionalDetails(Base):
        __tablename__ = 'sat_person_professional_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        erusr = Column(String(12))
        gbdat = Column(DateTime(timezone=False))
        rank = Column(String(3))

    class SatTimeVitalSigns(Base):
        __tablename__ = 'sat_time_vital_signs'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        erdat = Column(DateTime(timezone=False))

    class SatEventVitalSigns(Base):
        __tablename__ = 'sat_event_vital_signs'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        idvs = Column(String(10))
        dttyp = Column(String(10))
        typevs = Column(String(9))
        vwert = Column(String(7))
        vbem = Column(String(150))

    Base.metadata.create_all(engine)
    engine.dispose()
    return schema