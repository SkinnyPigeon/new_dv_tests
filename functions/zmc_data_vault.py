# Imports

from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, BigInteger, Numeric, Time

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

def zmc_data_vault():
    schema = create_random_schema()
    print(f"SCHEMA: {schema}")
    Base = declarative_base()
    engine = create_engine(f"postgresql://postgres:{PASSWORD}@localhost:{PORT}/zmc")
    # try:
    engine.execute(CreateSchema(schema))

    class HubTime(Base):
        __tablename__ = 'hub_time'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        patnr = Column(BigInteger)

    class HubPerson(Base):
        __tablename__ = 'hub_person'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        patnr = Column(BigInteger)

    class HubObject(Base):
        __tablename__ = 'hub_object'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        patnr = Column(BigInteger)

    class HubLocation(Base):
        __tablename__ = 'hub_location'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        patnr = Column(BigInteger)

    class HubEvent(Base):
        __tablename__ = 'hub_event'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        patnr = Column(BigInteger)

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

    # sat_time_wearable_details
    # sat_event_wearable_details
        
    class ZMCTimeWearable(Base):
        __tablename__ = 'sat_time_wearable_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        date = Column(DateTime(timezone=False))
        
    class ZMCEventWearable(Base):
        __tablename__ = 'sat_event_wearable_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        w_time = Column(Time)
        w_steps = Column(Integer)
        w_cad = Column(Integer)
        sst = Column(Integer)
        sst_time = Column(Numeric(3, 1))
        cyc_time = Column(Time)
        cyc_steps = Column(Integer)
        cyc_cad = Column(Integer)

    # sat_time_complaints_and_diagnosis
    # sat_event_complaints_and_diagnosis

    class ZMCTimeComplaints(Base):
        __tablename__ = 'sat_time_complaints_and_diagnosis'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        begin_date = Column(DateTime(timezone=False))
        end_date = Column(DateTime(timezone=False))

    class ZMCEventComplaints(Base):
        __tablename__ = 'sat_event_complaints_and_diagnosis'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        complaints_and_diagnosis = Column(String(50))
        status = Column(String(20))
        specialism = Column(String(20))
        type = Column(String(20))
        name_of_diagnosis_or_complaint = Column(String(30))
        anatomical_location = Column(String(20))
        laterality = Column(String(10))

    # sat_person_medication_agreements
    # sat_object_medication_agreements

    class ZMCPersonMedicationAgreements(Base):
        __tablename__ = 'sat_person_medication_agreements'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        prescribed_by = Column(String(40))

    class ZMCObjectMedicationAgreements(Base):
        __tablename__ = 'sat_object_medication_agreements'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        medicines = Column(String(30))
        description = Column(String(50))

    # sat_object_medication_use

    class ZMCObjectMedicationUse(Base):
        __tablename__ = 'sat_object_medication_use'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        product = Column(String(30))
        use = Column(String(40))
        reason = Column(String(50))


    # sat_object_medical_aids_and_tools

    class ZMCObjectMedicalAids(Base):
        __tablename__ = 'sat_object_medical_aids_and_tools'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        product_description = Column(String(50))
        anatomical_location = Column(String(40))
        description = Column(String(50))

    # sat_time_bloodpressure_details
    # sat_location_bloodpressure_details
    # sat_event_bloodpressure_details

    class ZMCTimeBloodpressure(Base):
        __tablename__ = 'sat_time_bloodpressure_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        date = Column(DateTime(timezone=False))

    class ZMCLocationBloodpressure(Base):
        __tablename__ = 'sat_location_bloodpressure_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        position = Column(String(40))

    class ZMCEventBloodpressure(Base):
        __tablename__ = 'sat_event_bloodpressure_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        value  = Column(String(20))
        systolic_bloodpressure = Column(Integer)
        diastolic_bloodpressure = Column(Integer)
        measurement_method = Column(String(40))
        manchette_type = Column(String(40))
        measurement_location = Column(String(40))
        description = Column(String(40))

    # sat_time_weight_details
    # sat_event_weight_details

    class ZMCTimeWeight(Base):
        __tablename__ = 'sat_time_weight_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        date = Column(DateTime(timezone=False))

    class ZMCEventWeight(Base):
        __tablename__ = 'sat_event_weight_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        measurement = Column(String(10))
        clothes = Column(String(20))
        description = Column(String(40))

    # sat_time_length_details
    # sat_event_length_details

    class ZMCTimeLength(Base):
        __tablename__ = 'sat_time_length_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        date = Column(DateTime(timezone=False))

    class ZMCEventLength(Base):
        __tablename__ = 'sat_event_length_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        measurement = Column(String(10))
        description = Column(String(40))

    # sat_time_registered_events
    # sat_location_registered_events
    # sat_event_registered_events

    class ZMCTimeRegister(Base):
        __tablename__ = 'sat_time_registered_events'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        start_date = Column(DateTime(timezone=False))
        end_date = Column(DateTime(timezone=False))
        date = Column(DateTime(timezone=False))

    class ZMCLocationRegister(Base):
        __tablename__ = 'sat_location_registered_events'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        location = Column(String(100))

    class ZMCEventRegister(Base):
        __tablename__ = 'sat_event_registered_events'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        type = Column(String(40))
        method = Column(String(40))
        anatomical_location = Column(String(40))
        description = Column(String(255))
        laterality = Column(String(40))
        indication = Column(String(40))
        executor = Column(String(40))
        requested_by = Column(String(40))

    # sat_time_warning_details
    # sat_event_warning_details

    class ZMCTimeWarning(Base):
        __tablename__ = 'sat_time_warning_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        begindate = Column(DateTime(timezone=False))

    class ZMCEventWarning(Base):
        __tablename__ = 'sat_event_warning_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        alerts = Column(String(40))
        type = Column(String(40))

    # sat_time_functional_or_mental_state
    # sat_event_functional_or_mental_state

    class ZMCTimeFunctional(Base):
        __tablename__ = 'sat_time_functional_or_mental_state'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        date = Column(DateTime(timezone=False))

    class ZMCEventFunctional(Base):
        __tablename__ = 'sat_event_functional_or_mental_state'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        name = Column(String(40))
        value = Column(String(40))

    # sat_person_living_situation
    class ZMCPersonLiving(Base):
        __tablename__ = 'sat_person_living_situation'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        house_type = Column(String(40))
        description = Column(String(40))

    # sat_person_drug_use
    class ZMCPersonDrugs(Base):
        __tablename__ = 'sat_person_drug_use'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        substance = Column(String(40))
        quantity = Column(String(40))
        description = Column(String(40))

    # sat_person_alcohol_use
    class ZMCPersonAlcohol(Base):
        __tablename__ = 'sat_person_alcohol_use'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        usage_status = Column(String(40))
        quantity = Column(String(40))
        description = Column(String(40))

    # sat_person_tobacco_use
    class ZMCPersonTobacco(Base):
        __tablename__ = 'sat_person_tobacco_use'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        substance = Column(String(40))
        quantity = Column(Integer)
        description = Column(String(40))

    # sat_person_allergies_details
    class ZMCPersonAllergies(Base):
        __tablename__ = 'sat_person_allergies_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        caustive_substance = Column(String(40))
        critical = Column(String(20))
        description = Column(String(40))

    # sat_time_documents_details
    # sat_object_documents_details
    class ZMCTimeDocuments(Base):
        __tablename__ = 'sat_time_documents_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        date = Column(DateTime(timezone=False))

    class ZMCObjectDocuments(Base):
        __tablename__ = 'sat_object_documents_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        document_title = Column(String(50))
        type = Column(String(50))
        document = Column(String)

    # sat_time_images_details
    # sat_object_images_details
    class ZMCTimeImages(Base):
        __tablename__ = 'sat_time_images_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        date = Column(DateTime(timezone=False))

    class ZMCObjectImages(Base):
        __tablename__ = 'sat_object_images_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        image_title = Column(String(50))
        type = Column(String(50))
        image = Column(String)

    # sat_person_patient_details

    class ZMCPersonPatientDetails(Base):
        __tablename__ = 'sat_person_patient_details'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        nname = Column(String(40))
        nnams = Column(String(40))
        vname = Column(String(6))
        titel = Column(String(6))
        gschl = Column(String(10))
        gbdat = Column(DateTime(timezone=False))
        natio = Column(String(3))

    Base.metadata.create_all(engine)
    engine.dispose()
    return schema

    # except Exception as e:
    #     engine.dispose()
    #     return {"Error": str(e)}