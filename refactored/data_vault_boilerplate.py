from sqlalchemy import Table
from sqlalchemy.sql.schema import MetaData
from link_keys import link_keys

def boilerplate(schema, engine, keys_function):
    metadata = MetaData()
    hub_time = Table('hub_time', metadata, schema=schema, *keys_function())
    hub_person = Table('hub_person', metadata, schema=schema, *keys_function())
    hub_object = Table('hub_object', metadata, schema=schema, *keys_function())
    hub_location = Table('hub_location', metadata, schema=schema, *keys_function())
    hub_event = Table('hub_event', metadata, schema=schema, *keys_function())
    hubs = {
        'time': hub_time,
        'person': hub_person,
        'object': hub_object,
        'location': hub_location,
        'event': hub_event
    }

    Table('time_person_link', metadata, schema=schema, *link_keys(hubs, 'time', 'person'))
    Table('time_object_link', metadata, schema=schema, *link_keys(hubs, 'time', 'object'))
    Table('time_location_link', metadata, schema=schema, *link_keys(hubs, 'time', 'location'))
    Table('time_event_link', metadata, schema=schema, *link_keys(hubs, 'time', 'event'))
    Table('person_object_link', metadata, schema=schema, *link_keys(hubs, 'person', 'object'))
    Table('person_location_link', metadata, schema=schema, *link_keys(hubs, 'person', 'location'))
    Table('person_event_link', metadata, schema=schema, *link_keys(hubs, 'person', 'event'))
    Table('object_location_link', metadata, schema=schema, *link_keys(hubs, 'object', 'location'))
    Table('object_event_link', metadata, schema=schema, *link_keys(hubs, 'object', 'event'))
    Table('location_event_link', metadata, schema=schema, *link_keys(hubs, 'location', 'event'))

    metadata.create_all(engine)