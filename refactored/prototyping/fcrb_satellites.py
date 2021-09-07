from sqlalchemy import Table
from sqlalchemy.sql.schema import MetaData
from refactored.data_vault.keys.id_column import id_column
from refactored.tables.fcrb_table_definitions import fcrb_table_definitions

def fcrb_satellites(schema, engine, tags):
    metadata = MetaData()
    for tag in tags:
        pass

    # diagnostic = fcrb_satellite_definitions['diagnostic']
    # Table('sat_event_diagnostic_details', metadata, schema=schema, *[
    #                                             id_column(), 
    #                                             diagnostic['lfdnr'], 
    #                                             diagnostic['dkey1']])
    # Table('sat_time_diagnostic_details', metadata, schema=schema, *[
    #                                             id_column(), 
    #                                             diagnostic['erdat'], 
    #                                             diagnostic['begdt'], 
    #                                             diagnostic['enddt']])
    
    # episode = fcrb_satellite_definitions['episode']
    # Table('sat_time_episode_details', metadata, schema=schema, *[
    #                                             id_column(),
    #                                             episode['erdat'],
    #                                             episode['begdt'],
    #                                             episode['enddt']])
    # Table('sat_event_episode_details', metadata, schema=schema, *[
    #                                             id_column(),
    #                                             episode['falar'],
    #                                             episode['bekat'],
    #                                             episode['einzg'],
    #                                             episode['statu'],
    #                                             episode['krzan'],
    #                                             episode['storn'],
    #                                             episode['casetx'],
    #                                             episode['fatxt'],
    #                                             episode['enddtx']])

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

    metadata.create_all(engine)

        # Base.metadata.create_all(engine)
        # engine.dispose()
    #     return schema

    # except Exception as e:
    #     engine.dispose()
    #     return {"Error": str(e)}