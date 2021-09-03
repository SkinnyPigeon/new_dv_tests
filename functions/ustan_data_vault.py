# Imports

from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, BigInteger

from dotenv import load_dotenv
# from pathlib import Path

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

def ustan_data_vault():
    schema = create_random_schema()
    print(f"SCHEMA: {schema}")
    Base = declarative_base()
    engine = create_engine(f"postgresql://postgres:{PASSWORD}@localhost:{PORT}/ustan")
    try:
        engine.execute(CreateSchema(schema))

        class HubTime(Base):
            __tablename__ = 'hub_time'
            __table_args__ = {'schema': schema}
            id = Column(Integer, primary_key=True)
            chi = Column(BigInteger)

        class HubPerson(Base):
            __tablename__ = 'hub_person'
            __table_args__ = {'schema': schema}
            id = Column(Integer, primary_key=True)
            chi = Column(BigInteger)

        class HubObject(Base):
            __tablename__ = 'hub_object'
            __table_args__ = {'schema': schema}
            id = Column(Integer, primary_key=True)
            chi = Column(BigInteger)

        class HubLocation(Base):
            __tablename__ = 'hub_location'
            __table_args__ = {'schema': schema}
            id = Column(Integer, primary_key=True)
            chi = Column(BigInteger)

        class HubEvent(Base):
            __tablename__ = 'hub_event'
            __table_args__ = {'schema': schema}
            id = Column(Integer, primary_key=True)
            chi = Column(BigInteger)

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

        # class SatEventDiagnosticDetails(Base):
        #     __tablename__ = 'sat_event_diagnostic_details'
        #     __table_args__ = {'schema': schema}
        #     id = Column(Integer, primary_key=True)
        #     lfdnr = Column(String(3))
        #     dkey1 = Column(String(30))


        Base.metadata.create_all(engine)
        engine.dispose()
        return schema

    except Exception as e:
        engine.dispose()
        return {"Error": str(e)}