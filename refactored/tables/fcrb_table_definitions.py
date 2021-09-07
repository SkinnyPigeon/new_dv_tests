from sqlalchemy import Column, String, Integer, DateTime 

fcrb_table_definitions = {
    "fcrb.diagnostic": {
        "lfdnr": Column("lfdnr", String(3)),
        "dkey1": Column("dkey1", String(30)),
        "erdat": Column("erdat", DateTime(timezone=False)),
        "begdt": Column("begdt", DateTime(timezone=False)),
        "enddt": Column("enddt",DateTime(timezone=False))
    },
    "fcrb.episode": {
        "erdat": Column("erdat", DateTime(timezone=False)),
        "begdt": Column("begdt",DateTime(timezone=False)),
        "enddt": Column("enddt",DateTime(timezone=False)),
        "falar": Column("falar",String(1)),
        "bekat": Column("bekat",String(40)),
        "einzg": Column("einzg",String(9)),
        "statu": Column("statu",String(1)),
        "krzan": Column("krzan",String(1)),
        "storn": Column("storn",String(1)),
        "casetx": Column("casetx",String(20)),
        "fatxt": Column("fatxt",String(40)),
        "enddtx": Column("enddtx",String(20))
    }

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

}