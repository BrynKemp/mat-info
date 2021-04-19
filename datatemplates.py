##########################################       Triage answers   ######################################################

d_yesno = {
    '1': 'No',
    '2': 'Yes'
    }

d_vacc_doses = {
    '1': 'No',
    '2': '1 dose',
    '3': '2 doses'
    }

d_vaccine = {
    '1': 'Vaccinated:  No',
    '2': 'Vaccinated: Yes, 1 dose',
    '3': 'Vaccinated: Yes, 2 doses'
    }

d_vacc_typ = {
    '0': 'None',
    '1': 'Pfizer',
    '2': 'Oxford - AZ',
    '3': 'Moderna',
    '4': 'Other'
    }

d_cov_status = {
    '1': 'Negative',
    '2': 'Pending',
    '3': 'Positive'
}

d_symptoms = {
    '0': 'None',
    '1': 'Fever or temp \u226537.8C',
    '2': 'Shortness of breath',
    '3': 'Dry cough',
    '4': 'Chest pain',
    '5': 'Loss of taste/smell',
    '6': 'GI symptoms',
    '7': 'Skin changes'
}

d_risk_woman = {
    '0': 'None',
    '1': 'Ethnicity: Black or Asian origin',
    '2': 'BMI \u226530',
    '3': 'Hypertension [PIH/PET or Essential]',
    '4': 'Diabetes [Type 1 or 2] \U0001f6a9',
    '5': 'Kidney or inflammatory bowel disease',
    '6': 'Uses oral steroids or Biologics \U0001f6a9',
    '7': 'Transplant recipient',
    '8': 'HIV or other immunosuppressed',
    '9': 'Anaemia [Hb <105g/L] \U0001f6a9',
    '10': 'On UK shielding list \U0001f6a9'

}

d_risk_baby = {
    '0': 'None',
    '1': 'Reduced fetal movements',
    '2': 'Known SGA',
    '3': 'Ruptured membranes',
    '4': 'Other'
}

d_treatment_list = {
    '0': 'None',
    '1': 'Prednisolone',
    '2': 'Tocilizumab',
    '3': 'Remdesivir',
    '4': 'Aspirin',
    '5': 'LMWH - Tinzaparin',
    '6': 'Vitamin D',
    '7': 'Iron',
    '8': 'Dexamethasone - baby',
    '9': 'Magnesium sulphate - baby'
}

d_assess_1 = {
    '0': 'None',
    '1': 'Chest Xray',
    '2': 'CTPA or VQ',
    '3': 'Growth scan in last 28 days'
}


d_assess_2 = {
    '0': 'None',
    '1': 'Chest Xray - normal',
    '2': 'Chest Xray - abnormal',
    '3': 'CTPA/ VQ - normal',
    '4': 'CTPA/ VQ - abnormal',
    '5': 'ECHO - normal',
    '6': 'ECHO - abnormal',
    '7': 'Growth - normal',
    '8': 'Growth - SGA + abnormal Doppler',
    '9': 'Growth - SGA + normal Doppler',
}

#############################################    data set   ############################################################

covid_data = {
    'datetime_d': '',
    'triageloc_d': '',
    'surname_d': 'Surname',
    'nhs_d': 'Last 4 digits',
    'dob_d': 'Year only',
    'parity_d': 'Maximum 10',
    'edd_d': 'Click to enter',
    'del_d': '1',
    'deldate_d': 'Click to enter',
    'tel_d': '07000 123456',
    'vaccine_d': '1',
    'dose1date_d': 'Click to enter',
    'dose2date_d': 'Click to enter',
    'vactype1_d': '',
    'vactype2_d': '',
    'covidtest_d': '',
    'covidstatus_d': '',
    'covidswabdate_d': 'Click to enter',
    'covidadmit_d': '',
    'admitdate_d': 'Click to enter',
    'dischdate_d': 'Click to enter',
    'sentences_d': '1',
    'spo2_1': 'Pre SpO2',
    'spo2_2': 'Post SpO2',
    'tsym1_d': '',
    'tsym2_d': '',
    'tsym3_d': '',
    'tsym4_d': '',
    'risksw1_d': '',
    'risksw2_d': '',
    'risksw3_d': '',
    'risksw4_d': '',
    'risksb1_d': '',
    'risksb2_d': '',
    'risksb3_d': '',
    'risksb4_d': '',
    'clin1assess1_d': '',
    'clin1assess2_d': '',
    'clin1assess3_d': '',
    'clin1assess4_d': '',
    'clin2assess1_d': '',
    'clin2assess2_d': '',
    'clin2assess3_d': '',
    'clin2assess4_d': '',
    'covrxw1_d': '',
    'covrxw2_d': '',
    'covrxw3_d': '',
    'covrxw4_d': '',
    'labour_d':'',
    'fetconcern_d':'',
    'fhr_d':''
}