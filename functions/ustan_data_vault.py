# Imports

from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, BigInteger, Numeric

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


        # sat_time_cycle_details
        # sat_event_cycle_details
       
        class USTANTimeCycleDetails(Base):
            __tablename__ = 'sat_time_cycle_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            init_appointment_date = Column(DateTime(timezone=False))
            elapsed_days = Column(Integer)
            interval_days = Column(Integer)
            appointment_date = Column(DateTime(timezone=False))
                
        class USTANEventCycleDetails(Base):
            __tablename__ = 'sat_event_cycle_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            regime_id = Column(Integer)
            intention_id = Column(Integer)
            cycle_id = Column(BigInteger)
            drug_names = Column(String(length=30))
            diagnosis = Column(String(length=30))
            intention = Column(String(length=30))
            regime = Column(String(length=30))
            cycle = Column(Integer)
            p_ps = Column(Integer)
            ps = Column(Integer)
            nausea = Column(Integer)
            vomiting = Column(Integer)
            diarrhoea = Column(Integer)
            constipation = Column(Integer)
            oralMucositis = Column(Integer)
            oesophagitis = Column(Integer)
            cycle = Column(Integer)
            neurotoxicity = Column(Integer)
            handFoot = Column(Integer)
            skin = Column(Integer)
            hypersensitivity = Column(Integer)
            fatigue = Column(Integer)
            required_doses = Column(Numeric(10, 6))

        # sat_time_general_details
        # sat_person_general_patient
        # sat_person_general_gp
        # sat_location_general_details
        # sat_event_general_details
        

        class USTANTimeGeneralDetails(Base):
            __tablename__ = 'sat_time_general_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            incidence_date = Column(DateTime(timezone=False))
            first_seen_date = Column(DateTime(timezone=False))
            survival_days = Column(Integer)
            dat_death = Column(DateTime(timezone=False))

        class USTANPersonGeneralPatient(Base):
            __tablename__ = 'sat_person_general_patient'
            __table_args__ = {'schema': 'ustan'}
            id = Column(BigInteger, primary_key=True)
            name = Column(String(30))
            date_of_birth = Column(DateTime(timezone=False))
            dob = Column(DateTime(timezone=False))
            age = Column(Integer)
            gender = Column(Integer)
            age_at_diagnosis = Column(Numeric(5, 2))
            weight = Column(Numeric(5, 2))
            bmi = Column(Numeric(5, 2))
            height = Column(Numeric(5, 2))
            religion = Column(Integer)
            civil_st = Column(Integer)
            postcode_pre = Column(String(2))
            postcode_suf = Column(String(5))

        class USTANPersonGeneralGP(Base):
            __tablename__ = 'sat_person_general_gp'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            gp_name = Column(String(30))
            gp_id = Column(Integer)

        class USTANLocationGeneralDetails(Base):
            __tablename__ = 'sat_location_general_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            ref_hospital = Column(Integer)

        class USTANEventGeneralDetails(Base):
            __tablename__ = 'sat_event_general_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            site_icd_10 = Column(String(5))
            site = Column(String(5))
            histology = Column(Integer)
            primary = Column(Integer)
            metastasis1 = Column(String(5))
            metastasis2 = Column(String(5))
            metastasis3 = Column(String(5))
            smid = Column(Integer)
            smid1 = Column(Integer)
            cong_heart_fail_flag = Column(Integer)
            con_tiss_disease_rheum_flag = Column(Integer)
            dementia_flag = Column(Integer)
            pulmonary_flag = Column(Integer)
            con_tiss_flag = Column(Integer)
            diabetes_flag = Column(Integer)
            para_hemiplegia_flag = Column(Integer)
            renal_flag = Column(Integer)
            liver_flag = Column(Integer)
            aids_hiv_flag = Column(Integer)
            cancer_flag = Column(Integer)
            charlson_score = Column(Integer)
            simd = Column(Numeric(5, 2))
            simd1 = Column(Numeric(5, 2))
            side = Column(Integer)
            stage = Column(Integer)
            stage_detail = Column(String(2))
            tnm_t = Column(Integer)
            tnm_t_detail = Column(String(2))
            tnm_n = Column(Integer)
            tnm_n_detail = Column(String(2))
            tnm_m = Column(Integer)
            perf_stat = Column(Integer)
            smr01_flag = Column(Integer)
            death_flag = Column(Integer)

        # sat_time_intentions_details
        # sat_person_intentions_details
        # sat_event_intentions_details
       
        class USTANTimeIntentionsDetails(Base):
            __tablename__ = 'sat_time_intentions_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            init_appointment_date = Column(DateTime(timezone=False))
            elapsed_days = Column(Integer)
            appointment_date = Column(DateTime(timezone=False))

        class USTANPersonIntentionDetails(Base):
            __tablename__ = 'sat_person_intentions_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            patient_id = Column(Integer)
         
        class USTANEventIntentionsDetails(Base):
            __tablename__ = 'sat_event_intentions_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            intention_id = Column(Integer)
            intention_seq = Column(Integer)
            first_intention = Column(String(12))
            regime_ratio = Column(Integer)
            cycle_ratio = Column(Integer)
            intention = Column(String(12))
            first_regime = Column(String(16))

        # sat_time_patients_details
        # sat_person_patients_details
        # sat_event_patients_details

        class USTANTimePatientsDetails(Base):
            __tablename__ = 'sat_time_patients_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            appointment_date = Column(DateTime(timezone=False))

        class USTANPersonPatientsDetails(Base):
            __tablename__ = 'sat_person_patients_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            patient_id = Column(Integer)

        class USTANEventPatientsDetails(Base):
            __tablename__ = 'sat_event_patients_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            first_intention = Column(String(12))

        # sat_time_regimes_details
        # sat_event_regimes_details
        
        class USTANTimeRegimesDetails(Base):
            __tablename__ = 'sat_time_regimes_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            interval_days = Column(Integer)
            elapsed_days = Column(Integer)
            init_appointment_date = Column(DateTime(timezone=False))
            appointment_date = Column(DateTime(timezone=False))

        class USTANEventRegimesDetails(Base):
            __tablename__ = 'sat_event_regimes_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            chi = Column(BigInteger)
            intention_id = Column(Integer)
            regime_id = Column(Integer)
            regime_seq = Column(Integer)
            regime_ratio = Column(Integer)
            cycle_ratio = Column(Integer)
            intention = Column(String(12))
            prev_regime = Column(String(16))
            first_regime = Column(String(16))
            regime = Column(String(16))

        # sat_time_smr01_details
        # sat_person_smr01_details
        # sat_event_smr01_details
        
        class USTANTimeSMR01Details(Base):
            __tablename__ = 'sat_time_smr01_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            incidence_date = Column(DateTime(timezone=False))
            admission_date = Column(DateTime(timezone=False))
            length_of_stay = Column(Integer)
            discharge_date = Column(DateTime(timezone=False))

        class USTANPersonSMR01Details(Base):
            __tablename__ = 'sat_person_smr01_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            marital_status = Column(String(1))
            ethnic_group = Column(String(2))

        class USTANEventSMR01Details(Base):
            __tablename__ = 'sat_event_smr01_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            other_condition1 = Column(String(5))
            other_condition2 = Column(String(5))
            other_condition3 = Column(String(5))
            main_operation_b = Column(String(5))
            waiting_list_type = Column(Integer)
            main_condition = Column(String(4))
            main_operation_a = Column(String(4))

        # sat_time_smr06_details
        # sat_event_smr06_details
        class USTANTimeSMR06Details(Base):
            __tablename__ = 'sat_time_smr06_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            chi = Column(BigInteger)
            incidence_date = Column(DateTime(timezone=False))
            er_status = Column(Integer)
            her2_status = Column(Integer)
            stage_clinical_t = Column(String(2))
            stage_clinical_n = Column(String(2))
            stage_clinical_m = Column(String(2))
            num_positive = Column(Integer)
            pathological_tum_size = Column(Integer)

        class USTANEventSMR06Details(Base):
            __tablename__ = 'sat_event_smr06_details'
            __table_args__ = {'schema': schema}
            id = Column(BigInteger, primary_key=True)
            chi = Column(BigInteger)
            incidence_date = Column(DateTime(timezone=False))
            er_status = Column(Integer)
            her2_status = Column(Integer)
            stage_clinical_t = Column(String(2))
            stage_clinical_n = Column(String(2))
            stage_clinical_m = Column(String(2))
            num_positive = Column(Integer)
            pathological_tum_size = Column(Integer)

        Base.metadata.create_all(engine)
        engine.dispose()
        return schema

    except Exception as e:
        engine.dispose()
        return {"Error": str(e)}