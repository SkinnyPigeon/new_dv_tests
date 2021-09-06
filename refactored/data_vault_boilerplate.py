from sqlalchemy import  ForeignKey, Table, Column, Integer
from sqlalchemy.sql.schema import MetaData

def boilerplate(schema, engine, columns):
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

    metadata.create_all(engine)