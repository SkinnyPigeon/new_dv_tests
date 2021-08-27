fcrb_keys = ['einri', 'patnr', 'falnr', 'pernr', 'orgid', 'vppid']

fcrb_satellites = {
    'sat_event_diagnostic_details': {
        'columns': ['lfdnr', 'dkey1'], 
        'hub': 'hub_event'
    },
    'sat_time_episode_details': {
        'columns': ['erdat', 'begdt', 'enddt'],
        'hub': 'hub_time'
    },
    'sat_event_episode_details': {
        'columns': ['falar', 'bekat', 'einzg', 'statu', 'krzan', 'storn', 'casetx', 'fatxt', 'enddtx'],
        'hub': 'hub_event'
    }, 
    'sat_person_medical_specialty': {
        'columns': ['orgna'],
        'hub': 'hub_person'
    },
    'sat_time_medication_details': {
        'columns': ['erdat', 'stdat'],
        'hub': 'hub_time'
    },
    'sat_event_medication_details': {
        'columns': ['mpresnr', 'motx', 'mostx', 'motypid', 'storn', 'stusr', 'stoid'],
        'hub': 'hub_event'
    },
    'sat_time_monitoring_params': {
        'columns': ['datyp'],
        'hub': 'hub_time'
    },
    'sat_event_monitoring_params': {
        'columns': ['vbem', 'wertogr', 'wertugr', 'wertmax', 'wertmin'],
        'hub': 'hub_event'
    },
    'sat_time_order_entry': {
        'columns': ['erdat'],
        'hub': 'hub_time'
    },
    'sat_event_order_entry': {
        'columns': ['idodr'],
        'hub': 'hub_event'
    },
    'sat_location_patient_address': {
        'columns': ['pstlz', 'stras', 'land', 'ort', 'deck', 'adrnr'],
        'hub': 'hub_location'
    },
    'sat_person_patient_details': {
        'columns': ['gschl', 'nname', 'vname', 'gbdat', 'gbnam', 'namzu', 'glrand', 'famst', 'telf1', 'rvnum'],
        'hub': 'hub_person'
    },
    'sat_time_professional_details': {
        'columns': ['begdt', 'enddt', 'erdat'],
        'hub': 'hub_time'
    },
    'sat_person_professional_details': {
        'columns': ['erusr', 'gbdat',  'rank'],
        'hub': 'hub_person'
    },
    'sat_time_vital_signs': {
        'columns': ['erdat'],
        'hub': 'hub_time'
    },
    'sat_event_vital_signs': {
        'columns': ['idvs', 'dttyp', 'typevs', 'vwert', 'vbem'],
        'hub': 'hub_event'
    }
}