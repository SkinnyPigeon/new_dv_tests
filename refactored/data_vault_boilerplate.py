from sqlalchemy import  ForeignKey, Table, Column, Integer
from sqlalchemy.sql.schema import MetaData

def boilerplate(Base, schema, engine, columns):
    metadata = MetaData()
    hub_time = Table('hub_time', metadata, schema=schema, *columns)
    hub_person = Table('hub_person', metadata, schema=schema, *columns)
    hub_object = Table('hub_object', metadata, schema=schema, *columns)
    hub_location = Table('hub_location', metadata, schema=schema, *columns)
    hub_event = Table('hub_event', metadata, schema=schema, *columns)
    link_keys = {
        'id': Column('id', Integer, primary_key=True),
        "time": Column('time_id', Integer, ForeignKey(hub_time.c.id)),
        "person": Column('person_id', Integer, ForeignKey(hub_person.c.id)),
        "object": Column('object_id', Integer, ForeignKey(hub_object.c.id)),
        "location": Column('location_id', Integer, ForeignKey(hub_location.c.id)),
        "event": Column('event_id', Integer, ForeignKey(hub_event.c.id))
    }

    Table('time_person_link', metadata, schema=schema, *[link_keys['id'], link_keys['time'], link_keys['person']])
    Table('time_object_link', metadata, schema=schema, *[link_keys['id'], link_keys['time'], link_keys['object']])
    Table('time_location_link', metadata, schema=schema, *[link_keys['id'], link_keys['time'], link_keys['location']])
    Table('time_event_link', metadata, schema=schema, *[link_keys['id'], link_keys['time'], link_keys['event']])
    Table('person_object_link', metadata, schema=schema, *[link_keys['id'], link_keys['person'], link_keys['object']])
    Table('person_location_link', metadata, schema=schema, *[link_keys['id'], link_keys['person'], link_keys['location']])
    Table('person_event_link', metadata, schema=schema, *[link_keys['id'], link_keys['person'], link_keys['event']])
    Table('object_location_link', metadata, schema=schema, *[link_keys['id'], link_keys['object'], link_keys['location']])
    Table('object_event_link', metadata, schema=schema, *[link_keys['id'], link_keys['object'], link_keys['event']])
    Table('location_event_link', metadata, schema=schema, *[link_keys['id'], link_keys['location'], link_keys['event']])


    class TimePersonLink(Base):
        __tablename__ = 'time_person_link'
        __table_args__ = {'schema': schema}
        id = Column(Integer, primary_key=True)
        time_id = Column(Integer, ForeignKey(HubTime.id))
        person_id = Column(Integer, ForeignKey(HubPerson.id))

    metadata.create_all(engine)
    # hub_time.create(engine)
    # print(hub_time.c.id)
    # class HubTime(Base):
    #     __tablename__ = 'hub_time'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     [columns[key] for key in columns]


    # class HubPerson(Base):
    #     __tablename__ = 'hub_person'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     einri = Column(String(4))
    #     patnr = Column(BigInteger)
    #     falnr = Column(String(10))
    #     pernr = Column(String(12))
    #     orgid = Column(String(8))
    #     vppid = Column(String(15))

    # class HubObject(Base):
    #     __tablename__ = 'hub_object'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     einri = Column(String(4))
    #     patnr = Column(BigInteger)
    #     falnr = Column(String(10))
    #     pernr = Column(String(12))
    #     orgid = Column(String(8))
    #     vppid = Column(String(15))

    # class HubLocation(Base):
    #     __tablename__ = 'hub_location'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     einri = Column(String(4))
    #     patnr = Column(BigInteger)
    #     falnr = Column(String(10))
    #     pernr = Column(String(12))
    #     orgid = Column(String(8))
    #     vppid = Column(String(15))

    # class HubEvent(Base):
    #     __tablename__ = 'hub_event'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     einri = Column(String(4))
    #     patnr = Column(BigInteger)
    #     falnr = Column(String(10))
    #     pernr = Column(String(12))
    #     orgid = Column(String(8))
    #     vppid = Column(String(15))

    # class TimePersonLink(Base):
    #     __tablename__ = 'time_person_link'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     time_id = Column(Integer, ForeignKey(HubTime.id))
    #     person_id = Column(Integer, ForeignKey(HubPerson.id))

    # class TimeObjectLink(Base):
    #     __tablename__ = 'time_object_link'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     time_id = Column(Integer, ForeignKey(HubTime.id))
    #     object_id = Column(Integer, ForeignKey(HubObject.id))

    # class TimeLocationLink(Base):
    #     __tablename__ = 'time_location_link'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     time_id = Column(Integer, ForeignKey(HubTime.id))
    #     location_id = Column(Integer, ForeignKey(HubLocation.id))

    # class TimeEventLink(Base):
    #     __tablename__ = 'time_event_link'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     time_id = Column(Integer, ForeignKey(HubTime.id))
    #     event_id = Column(Integer, ForeignKey(HubEvent.id))

    # class PersonObjectLink(Base):
    #     __tablename__ = 'person_object_link'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     person_id = Column(Integer, ForeignKey(HubPerson.id))
    #     object_id = Column(Integer, ForeignKey(HubObject.id))

    # class PersonLocationLink(Base):
    #     __tablename__ = 'person_location_link'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     person_id = Column(Integer, ForeignKey(HubPerson.id))
    #     location_id = Column(Integer, ForeignKey(HubLocation.id))

    # class PersonEventLink(Base):
    #     __tablename__ = 'person_event_link'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     person_id = Column(Integer, ForeignKey(HubPerson.id))
    #     event_id = Column(Integer, ForeignKey(HubEvent.id))

    # class ObjectLocationLink(Base):
    #     __tablename__ = 'object_location_link'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     object_id = Column(Integer, ForeignKey(HubObject.id))
    #     location_id = Column(Integer, ForeignKey(HubLocation.id))

    # class ObjectEventLink(Base):
    #     __tablename__ = 'object_event_link'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     object_id = Column(Integer, ForeignKey(HubObject.id))
    #     event_id = Column(Integer, ForeignKey(HubEvent.id))

    # class LocationEventLink(Base):
    #     __tablename__ = 'location_event_link'
    #     __table_args__ = {'schema': schema}
    #     id = Column(Integer, primary_key=True)
    #     location_id = Column(Integer, ForeignKey(HubLocation.id))
    #     event_id = Column(Integer, ForeignKey(HubEvent.id))

    # Base.metadata.create_all(engine)