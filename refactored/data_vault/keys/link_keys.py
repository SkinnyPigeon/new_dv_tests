from sqlalchemy import  ForeignKey, Column, Integer

def link_keys(hubs, key_one, key_two):
    
    link_keys = {
        'id': Column('id', Integer, primary_key=True),
        "time": Column('time_id', Integer, ForeignKey(hubs['time'].c.id)),
        "person": Column('person_id', Integer, ForeignKey(hubs['person'].c.id)),
        "object": Column('object_id', Integer, ForeignKey(hubs['object'].c.id)),
        "location": Column('location_id', Integer, ForeignKey(hubs['location'].c.id)),
        "event": Column('event_id', Integer, ForeignKey(hubs['event'].c.id))
    }

    return [link_keys['id'], link_keys[key_one], link_keys[key_two]]