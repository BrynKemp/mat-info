import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from datetime import date as dt
from dash.dependencies import Input, Output, State
from qbank import *
from apps.communitytriage import *
from apps.rbhtriage import *
from apps.telephonetriage import *
from dateutil.parser import parse
import numpy as np
import pandas as pd


def processDates(datacovid2):
    today = dt.today()
    dob = parse(datacovid2['dob_d'], dayfirst=True)
    dob = dob.date()
    deldate = parse(datacovid2['deldate_d'], dayfirst=True)
    deldate = deldate.date()
    edd = parse(datacovid2['edd_d'], dayfirst=True)
    edd = edd.date()

    age_str = ''
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    age_str = 'Age = %d years' % age

    ga_str = ''
    if datacovid2['del_d'] == '1':
        ga = today - edd
        ga = ga.days
        gadd = ga + 280
        gaw = gadd // 7
        gad = gadd - gaw * 7
        if gad == 1:
            ga_str = 'Gestational age = %d weeks + %d day' % (gaw, gad)
        elif gad > 1:
            ga_str = 'Gestational age = %d weeks + %d days' % (gaw, gad)

    pnga_str = ''
    if datacovid2['del_d'] == '2':
        pnga = (today - deldate)
        pnga = pnga.days
        pnga_str = 'Postnatal = Day %d' % pnga

    return age_str, ga_str


def concat_str(input):
    str_length = len(input)
    mystr = ''
    if str_length == 1:
        mystr = input
    if str_length > 1:
        mystr = ' '.join(input)
    return mystr


def sbar_risk(datacovid2):
    today = dt.today()
    dob = parse(datacovid2['dob_d'], dayfirst=True)
    dob = dob.date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    ## COVID status
    covidtest = ''
    if datacovid2['covidstatus_d'] == '1':
        covidtest = 'COVID test: negative'
    elif datacovid2['covidstatus_d'] == '2':
        covidtest = 'COVID test: pending'
    elif datacovid2['covidstatus_d'] == '3':
        if datacovid2['covidswabdate_d'] != 'Click to enter':
            covidtest = 'COVID test: positive [Date:  %s]' % datacovid2['covidswabdate_d']
        if datacovid2['covidswabdate_d'] == 'Click to enter':
            covidtest = 'COVID test: positive'

    ##  Completing sentences ##
    sentences = ''
    if datacovid2['sentences_d'] == '1':
        sentences = 'fail'
    elif datacovid2['sentences_d'] == '2':
        sentences = 'pass'

    ##  Rapid Walking Test Process ##
    rwt = ''
    if datacovid2['spo2_1'] != 'Pre SpO2' and datacovid2['spo2_2'] != 'Post SpO2':
        rwt = 'pass'
        if int(datacovid2['spo2_1']) < 95:
            rwt = 'fail'
        elif int(datacovid2['spo2_1']) > 94 and (int(datacovid2['spo2_2']) - int(datacovid2['spo2_1']) < -4):
            rwt = 'fail'
        elif int(datacovid2['spo2_1']) > 94 and (int(datacovid2['spo2_2']) - int(datacovid2['spo2_1']) < 5):
            rwt = 'pass'

    ## Decompensation
    decomp_index = False
    if sentences == 'fail' or rwt == 'fail':
        decomp_index = True

    vaccine = []
    if datacovid2['vaccine_d'] != '':
        vaccine = datacovid2['vaccine_d']

    symptoms = []
    if datacovid2['tsym1_d'] != '':
        symptoms.extend(datacovid2['tsym1_d'])
    if datacovid2['tsym2_d'] != '':
        symptoms.extend(datacovid2['tsym2_d'])
    if datacovid2['tsym3_d'] != '':
        symptoms.extend(datacovid2['tsym3_d'])
    if datacovid2['tsym4_d'] != '':
        symptoms.extend(datacovid2['tsym4_d'])

    womanrisk = []
    if datacovid2['risksw1_d'] != '':
        womanrisk.extend(datacovid2['risksw1_d'])
    if datacovid2['risksw2_d'] != '':
        womanrisk.extend(datacovid2['risksw2_d'])
    if datacovid2['risksw3_d'] != '':
        womanrisk.extend(datacovid2['risksw3_d'])
    if datacovid2['risksw4_d'] != '':
        womanrisk.extend(datacovid2['risksw4_d'])

    babyrisk = []
    if datacovid2['risksb1_d'] != '':
        babyrisk.extend(datacovid2['risksb1_d'])
    if datacovid2['risksb2_d'] != '':
        babyrisk.extend(datacovid2['risksb2_d'])
    if datacovid2['risksb3_d'] != '':
        babyrisk.extend(datacovid2['risksb3_d'])
    if datacovid2['risksb4_d'] != '':
        babyrisk.extend(datacovid2['risksb4_d'])

    clin1assess = []
    if datacovid2['clin1assess1_d'] != '':
        clin1assess.extend(datacovid2['clin1assess1_d'])
    if datacovid2['clin1assess2_d'] != '':
        clin1assess.extend(datacovid2['clin1assess2_d'])
    if datacovid2['clin1assess3_d'] != '':
        clin1assess.extend(datacovid2['clin1assess3_d'])
    if datacovid2['clin1assess4_d'] != '':
        clin1assess.extend(datacovid2['clin1assess4_d'])

    clin2assess = []
    if datacovid2['clin2assess1_d'] != '':
        clin2assess.extend(datacovid2['clin2assess1_d'])
    if datacovid2['clin2assess2_d'] != '':
        clin2assess.extend(datacovid2['clin2assess2_d'])
    if datacovid2['clin2assess3_d'] != '':
        clin2assess.extend(datacovid2['clin2assess3_d'])
    if datacovid2['clin2assess4_d'] != '':
        clin2assess.extend(datacovid2['clin2assess4_d'])

    covidrx = []
    if datacovid2['covrxw1_d'] != '':
        covidrx.extend(datacovid2['covrxw1_d'])
    if datacovid2['covrxw2_d'] != '':
        covidrx.extend(datacovid2['covrxw2_d'])
    if datacovid2['covrxw3_d'] != '':
        covidrx.extend(datacovid2['covrxw3_d'])
    if datacovid2['covrxw4_d'] != '':
        covidrx.extend(datacovid2['covrxw4_d'])

    symptoms.sort()
    womanrisk.sort()
    babyrisk.sort()
    clin1assess.sort()
    clin2assess.sort()
    covidrx.sort()

    risk = 'low'
    highrisk = [1, 2, 4, 5, 6, 7, 8, 10]
    if age > 35 or (any(x in highrisk for x in womanrisk)):
        risk = 'high'

    return symptoms, womanrisk, babyrisk, clin1assess, clin2assess, covidrx, risk, sentences, rwt, covidtest, decomp_index, vaccine


def getsbardata(datacovid2, setting):
    dob_a = parse(datacovid2['dob_d'], dayfirst=True)
    parity_str = 'Parity =%s' % datacovid2['parity_d']
    dob_str = dob_a.strftime('%d %B, %Y')
    age_str, ga_str, pnga_str = processDates(datacovid2)

    symptoms, womanrisk, babyrisk, clin1assess, clin2assess, covidrx, risk, sentences, rwt, covidtest, \
    decomp_index, vaccine = sbar_risk(datacovid2)

    pstatus = ''
    if datacovid2['del_d'] == '1':
        pstatus = 'AN'
    elif datacovid2['del_d'] == '2':
        pstatus = 'PN'

    # Situations

    situation_preamble = 'COVID-19 assessment'
    # situations = []
    situations = {
        0: 'Postnatal woman from a high risk group with respiratory distress;',
        1: 'Advised to attend Emergency Department immediately [call 999].',
        2: 'Postnatal woman from a high risk group without distress.',
        3: '',
        4: 'Postnatal woman with respiratory distress;',
        5: 'Advised to attend Emergency Department immediately [call 999].',
        6: 'Postnatal woman without distress.',
        7: '',
        8: 'Pregnant woman from a high risk group with respiratory distress;',
        9: 'Advised to attend Emergency Department immediately [call 999].',
        10: 'Pregnant woman from a high risk group without respiratory distress.',
        11: '',
        12: 'Pregnant woman with respiratory distress;',
        13: 'Advised to attend Emergency Department immediately [call 999].',
        14: 'Pregnant woman without respiratory distress.',
        15: ''
    }

    # situations.extend([
    #     'Postnatal woman from a high risk group with respiratory distress.<br>Advised to attend the Emergency Department [call 999].'])
    # situations.extend(['Postnatal woman from a high risk group without distress.'])
    # situations.extend([
    #     'Postnatal woman with respiratory distress.<br>Advised to attend the Emergency Department [call 999].'])
    # situations.extend(['Postnatal woman without distress.'])
    # situations.extend([
    #     'Pregnant woman from a high risk group with respiratory distress.<br>Advised to attend the Emergency Department [call 999].'])
    # situations.extend(['Pregnant woman from a high risk group without respiratory distress.'])
    # situations.extend(
    #     ['Pregnant woman with respiratory distress.<br>Advised to attend the Emergency Department [call 999].'])
    # situations.extend(['Pregnant woman without respiratory distress.'])

    situation = ''
    if pstatus == 'PN' and risk == 'high' and decomp_index is True:
        situation = situations[0], situations[1]
    elif pstatus == 'PN' and risk == 'high' and decomp_index is False:
        situation = situations[2], situations[3]
    if pstatus == 'PN' and risk == 'low' and decomp_index is True:
        situation = situations[4], situations[5]
    elif pstatus == 'PN' and risk == 'low' and decomp_index is False:
        situation = situations[6], situations[7]
    elif pstatus == 'AN' and risk == 'high' and decomp_index is True:
        situation = situations[8], situations[9]
    elif pstatus == 'AN' and risk == 'low' and decomp_index is False:
        situation = situations[10], situations[11]
    if pstatus == 'AN' and risk == 'high' and decomp_index is True:
        situation = situations[12], situations[13]
    elif pstatus == 'AN' and risk == 'low' and decomp_index is False:
        situation = situations[14], situations[15]

    # Background
    background1 = ''
    background2 = ''
    background1 = 'Ms %s   [DOB %s] [NHS %s].' % (
        datacovid2['surname_d'], dob_str, datacovid2['nhs_d'])
    if datacovid2['del_d'] == '1':
        background2 = '%s,  %s,  %s' % (age_str, parity_str, ga_str)
    elif datacovid2['del_d'] == '2':
        background2 = '%s,  %s,  %s' % (age_str, parity_str, pnga_str)

    vaccine_str = ''
    if vaccine:
        temp_list = vaccine
        d_list = d_vaccine
        vaccine_str = d_list[temp_list]

    # Assessment
    def processLists(temp_list, d_list):

        if len(temp_list) == 1:
            tempstr = '%d. %s ' % (1, d_list[str(temp_list[0])])
            string = tempstr
        if len(temp_list) > 1:
            for a in range(len(temp_list)):
                if a == 0:
                    tempstr = '%d. %s ' % (a + 1, d_list[str(temp_list[a])])
                    string = tempstr
                if len(temp_list) - 1 > a > 0:
                    tempstr = '%d. %s ' % (a + 1, d_list[str(temp_list[a])])
                    string = string + tempstr
                if a == len(temp_list) - 1:
                    tempstr = 'and %d. %s.' % (a + 1, d_list[str(temp_list[a])])
                    string = string + tempstr
        return string

    if symptoms:
        ts1 = [x for x in symptoms if x != '']
        ts2 = [x for x in ts1 if x != '0']
        symptom_str = processLists(ts2, d_symptoms)
    else:
        symptom_str = ''

    if womanrisk:
        tw1 = [x for x in womanrisk if x != '']
        tw2 = [x for x in tw1 if x != '0']
        womanrisk_str = processLists(tw2, d_risk_woman)
    else:
        womanrisk_str = ''

    if babyrisk:
        tb1 = [x for x in babyrisk if x != '']
        tb2 = [x for x in tb1 if x != '0']
        babyrisk_str = processLists(tb2, d_risk_baby)
    else:
        babyrisk_str = ''

    if covidrx:
        tc1 = [x for x in covidrx if x != '']
        tc2 = [x for x in tc1 if x != '0']
        treatments_str = processLists(tc2, d_treatment_list)
    else:
        treatments_str = ''

    setting_str = ''
    if setting == 'community':
        setting_str = 'Clinical Assessment [Community]: COVID-19'
    elif setting == 'telephone':
        setting_str = 'Maternity Triage [Telephone]:  COVID-19'
    elif setting == 'rbh':
        setting_str = 'Clinical Assessment [RBH]: COVID-19'

    ## Response - Community
    outcome1 = ''
    outcome2 = ''
    if setting == "community":
        if (sentences == "fail" or int(datacovid2["spo2_1"]) < 95) and (
                int(datacovid2["fhr_d"]) < 100 or int(datacovid2["fhr_d"]) > 160 or datacovid2["fetconcern_d"] == "2" or
                datacovid2["labour_d"] == "2"):
            outcome1 = {0: "Advise: Transfer immediately to Emergency Department by "
                           "Ambulance [999]."}
            outcome2 = {0: "Contact maternity triage immediately to advise patient in labour and request their "
                           "attendance in ED."}
        elif (sentences == "fail" or int(datacovid2["spo2_1"]) < 95) and (
                100 < int(datacovid2["fhr_d"]) < 160 and datacovid2["fetconcern_d"] == "1" and
                datacovid2["labour_d"] == "1"):
            outcome1 = {0: "Advise:  Urgent review in Emergency Department."}
            outcome2 = {0: "ED to alert maternity on arrival."}
        elif (sentences == "pass" and rwt == "pass") and (
                100 < int(datacovid2["fhr_d"]) < 160 or datacovid2["fetconcern_d"] == "1" or
                datacovid2["labour_d"] == "1"):
            outcome1 = {0: "Advise:  Arrange community testing via www.nhs.uk/coronavirus19 or call 119 . Do not "
                           "refer to maternity."}
            outcome2 = {0: "Notify to @AMU and @Maternity COVID team."}
        elif (sentences == "pass" and rwt == "fail") and (
                100 < int(datacovid2["fhr_d"]) < 160 or datacovid2["fetconcern_d"] == "1" or
                datacovid2["labour_d"] == "1"):
            outcome1 = {0: "Advise:  Review in Emergency Department."}
            outcome2 = {0: ""}
        elif (sentences == "pass" and rwt == "fail") and (
                int(datacovid2["fhr_d"]) < 100 or int(datacovid2["fhr_d"]) > 160 or datacovid2["fetconcern_d"] == "2" or
                datacovid2["labour_d"] == "2"):
            outcome1 = {0: "Advise:  Contact maternity triage, who will advise where patient will be reviewed."}
            outcome2 = {0: ""}

    ## Response - Triage telephone
    if setting == "telephone":
        if sentences == "Fail" and (
                (1 in babyrisk) or datacovid2["fetconcern_d"] == "2" or datacovid2["labour_d"] == "2"):
            outcome1 = {0: "Advise:  Urgent review in Emergency Department AND inform maternity triage "
                           "who will assess fetal wellbeing in ED."}
            outcome2 = {0: ""}
        elif sentences == "Fail" and (
                (0 in babyrisk) and datacovid2["fetconcern_d"] == "1" and datacovid2["labour_d"] == "1"):
            outcome1 = {0: "Advise:  Urgent review in Emergency Department."}
            outcome2 = {0: ""}
        elif sentences == "Pass" and (
                (1 in babyrisk) or datacovid2["fetconcern_d"] == "2" or datacovid2["labour_d"] == "2"):
            outcome1 = {0: "Advise:  Contact maternity triage, who will advise on most appropriate place for review."}
            outcome2 = {0: ""}
        elif sentences == "Pass" and (
                (0 in babyrisk) and datacovid2["fetconcern_d"] == "1" and datacovid2["labour_d"] == "1"):
            outcome1 = {0: "Advise:  Arrange community testing via www.nhs.uk/coronavirus19 or call 119 . Do not "
                           "refer to maternity."}
            outcome2 = {0: "Notify to @AMU and @Maternity COVID team."}

    ## Response - RBH onsite
    if setting == "rbh":
        if int(datacovid2["spo2_1"]) < 95:
            outcome1 = {0: "Advise:  Admission and treat as respiratory failure.  Assess fetal well-being once "
                           "maternal resuscitation underway and condition stabilised."}
            outcome2 = {0: ""}

        if int(datacovid2["spo2_1"]) > 94 and rwt == "pass" and ((2 in symptoms) or (3 in symptoms) or (4 in symptoms)):
            outcome1 = {0: "Arrange chest XRay."}
            outcome2 = {0: "CXR normal [not indicated] and RWT = pass [Severity = Mild]:",
                        1: "Advise outpatient monitoring,",
                        2: "1. Take covid swab,",
                        3: "2. Perform VTE risk assessment [COVID = 1 point],",
                        4: "3. Provide SpO2 monitor, and",
                        5: "4. Notify to @AMU and @Maternity COVID team.",
                        6: "CXR abnormal and RWT = pass [Severity = Mild/Moderate]:",
                        7: "1. Take COVID swab,",
                        8: "2. Start oral antibiotics CAP,",
                        9: "3. Prescribe Tinzaparin prophylaxis,",
                        10: "4. Discuss with physician on-call, and",
                        11: "5. If admitted - prescribe Dexamethasone 12mg OD IM for fetus [if not already "
                            "administered during pregnancy]."}
        if int(datacovid2["spo2_1"]) > 94 and rwt == "fail" and ((2 in symptoms) or (3 in symptoms) or (4 in symptoms)):
            outcome1 = {0: "Arrange chest XRay."}
            outcome2 = {0: "CXR normal and RWT = fail [Severity = Moderate]:",
                        1: "1. Take COVID swab,",
                        2: "2. Admit to hospital [Physicians],",
                        3: "3. Consider Prednisolone 40mg OD after discussion with physician on-call,",
                        4: "4. Prescribe Tinzaparin women [Maternity VTE Prevention EPR PowerPlan],",
                        5: "5. Prescribe Dexamethasone 12 mg OD IM for fetus [if not already administered during "
                           "pregnancy].",
                        6: "CXR abnormal and RWT = fail [Severity = Moderate]: ",
                        7: "As for 'CXR normal and RWT = fail [Severity = Moderate]' with the addition of antibiotics "
                           "for CAP."}

        elif int(datacovid2["spo2_1"]) > 94 and rwt == "pass" and (
                (2 not in symptoms) or (3 not in symptoms) or (4 not in symptoms)):
            outcome1 = {0: "Chest X-Ray not likely to be indicated."}
            outcome2 = {0: "RWT = pass [COVID severity = Mild]:",
                        1: "Advise outpatient monitoring,",
                        2: "1. Take covid swab,",
                        3: "2. Perform VTE risk assessment [COVID = 1 point],",
                        4: "3. Provide SpO2 monitor, and",
                        5: "4. Refer to AMU."}

        elif int(datacovid2["spo2_1"]) > 94 and rwt == "fail" and (
                (2 not in symptoms) or (3 not in symptoms) or (4 not in symptoms)):
            outcome1 = "Chest X-Ray not likely to be indicated.",
            outcome2 = {0: "RWT = fail [COVID severity = Moderate]:",
                        1: "Advise hospital admission [Physicians],",
                        2: "1. Take COVID swab,",
                        3: "2. Consider Prednisolone 40mg OD after discussion with physician on-call,",
                        4: "3. Prescribe Tinzaparin women [Maternity VTE Prevention EPR PowerPlan], and",
                        5: "4. Prescribe Dexamethasone 12 mg OD IM for fetus [if not already administered during "
                           "pregnancy]."}

    outcome1_str = outcome1[0]
    #outcome2_str = outcome1[1]

    if len(outcome2) > 1:
        for a in range(len(outcome2)):
            if a == 0:
                outcome2_str = outcome2[a]
            if a > 0:
                outcome2_str = outcome2_str + outcome2[a]
    else:
        outcome2_str = outcome2[0]


    return setting_str, situation, background1, background2, symptom_str, womanrisk_str, babyrisk_str, treatments_str, \
           outcome1_str, outcome2_str, risk, vaccine_str, pstatus
