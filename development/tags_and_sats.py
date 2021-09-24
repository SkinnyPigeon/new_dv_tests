from control_files.fcrb_keys_and_sats import fcrb_sats
from control_files.ustan_keys_and_sats import ustan_sats
from control_files.zmc_keys_and_sats import zmc_sats
import copy

ustan_diagnostic = {'tag': 'diagnostic', 'source': 'ustan.general', 'fields': ['chi', 'incidence_date', 'site_icd_10', 'name', 'first_seen_date', 'site', 'histology', 'primary', 'metastasis1', 'metastasis2', 'metastasis3', 'cong_heart_fail_flag', 'con_tiss_disease_rheum_flag', 'dementia_flag', 'pulmonary_flag', 'con_tiss_flag', 'diabetes_flag', 'para_hemiplegia_flag',
                                                                               'renal_flag', 'liver_flag', 'aids_hiv_flag', 'cancer_flag', 'charlson_score', 'age', 'side', 'gender', 'age_at_diagnosis', 'weight', 'bmi', 'height', 'ref_hospital', 'stage', 'stage_detail', 'tnm_t', 'tnm_t_detail', 'tnm_n', 'tnm_n_detail', 'tnm_m', 'perf_stat', 'smr01_flag', 'gp_name', 'survival_days', 'gp_id'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_diagnostic_1 = {'tag': 'diagnostic', 'source': 'fcrb.diagnostic', 'fields': [
    'einri', 'patnr', 'falnr', 'pernr', 'lfdnr', 'dkey1'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_diagnostic_2 = {'tag': 'diagnostic', 'source': 'fcrb.episode', 'fields': [
    'patnr', 'falnr'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
fcrb_treatments = {'tag': 'treatments', 'source': 'fcrb.episode', 'fields': ['patnr', 'bekat'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}


zmc_diagnostic_1 = {'tag': 'diagnostic', 'source': 'zmc.complaints_and_diagnosis', 'fields': ['patnr', 'complaints_and_diagnosis', 'status', 'specialism', 'type',
                                                                                              'name_of_diagnosis_or_complaint', 'anatomical_location', 'laterality', 'begin_date', 'end_date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_diagnostic_2 = {'tag': 'diagnostic', 'source': 'zmc.bloodpressure', 'fields': ['patnr', 'value', 'position', 'description', 'date', 'systolic_bloodpressure',
                                                                                   'diastolic_bloodpressure', 'measurement_method', 'manchette_type', 'measurement_location', 'description'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_diagnostic_3 = {'tag': 'diagnostic', 'source': 'zmc.weight', 'fields': [
    'patnr', 'measurement', 'clothes', 'description', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_diagnostic_4 = {'tag': 'diagnostic', 'source': 'zmc.length', 'fields': [
    'patnr', 'measurement', 'description', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_diagnostic_5 = {'tag': 'diagnostic', 'source': 'zmc.registered_events', 'fields': [
    'patnr', 'type', 'method', 'anatomical_location', 'laterality', 'start_date', 'end_date', 'indication', 'requested_by', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_diagnostic_6 = {'tag': 'diagnostic', 'source': 'zmc.functional_or_mental_state', 'fields': [
    'patnr', 'name', 'value', 'date'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}
zmc_diagnostic_7 = {'tag': 'diagnostic', 'source': 'zmc.patient_details', 'fields': [
    'patnr', 'nname', 'nnams', 'vname', 'titel', 'gschl', 'gbdat', 'natio'], 'key_lookup': {}, 'table': True, 'graph': False, 'image': False}

ustan_tags = [ustan_diagnostic]
fcrb_tags = [fcrb_diagnostic_1,
            fcrb_diagnostic_2,
            fcrb_treatments]
            
zmc_tags =  [zmc_diagnostic_1,
            zmc_diagnostic_2,
            zmc_diagnostic_3,
            zmc_diagnostic_4,
            zmc_diagnostic_5,
            zmc_diagnostic_6,
            zmc_diagnostic_7]

def hospital_picker(hospital):
    if hospital == 'FCRB':
        return copy.deepcopy(fcrb_sats), fcrb_tags
    elif hospital == 'USTAN':
        return copy.deepcopy(ustan_sats), ustan_tags
    elif hospital == 'ZMC':
        return copy.deepcopy(zmc_sats), zmc_tags

def table_picker(tag_names, tags):
    return [tag['source'] for tag in tags if tag['tag'] in [tag_name for tag_name in tag_names]]

def sat_picker(tables, sat_definitions):
    sat_names = []
    for table in tables:
        try:
            sat_definitions[table].pop('links')
        except:
            print(f"Already popped: {table}")
        sat_names.extend([sat_name for sat_name in sat_definitions[table]])
    return sat_names

# tables, tags = hospital_picker('FCRB')
# table_names = table_picker('diagnostic',tags )
# print(table_names)
# sats = []