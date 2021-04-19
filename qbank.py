import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from datetime import date as dt
from datatemplates import *

tooltip_covidtest_t = html.Div([
    dbc.Tooltip(
        "Tested in the last 90 days, including pending results",
        target="covidtest_qt",
    )])

tooltip_covidtest_c = html.Div([
    dbc.Tooltip(
        "Tested in the last 90 days, including pending results",
        target="covidtest_qc",
    )])

tooltip_covidtest_r = html.Div([
    dbc.Tooltip(
        "Tested in the last 90 days, including pending results",
        target="covidtest_qr",
    )])

tooltip_covidadmit_t = html.Div([
    dbc.Tooltip(
        "Admission to treat COVID related d_symptoms; not incidental finding on admission",
        target="covidadmit_qt",
    )])

tooltip_covidadmit_c = html.Div([
    dbc.Tooltip(
        "Admission to treat COVID related d_symptoms; not incidental finding on admission",
        target="covidadmit_qc",
    )])

tooltip_covidadmit_r = html.Div([
    dbc.Tooltip(
        "Admission to treat COVID related d_symptoms; not incidental finding on admission",
        target="covidadmit_qr",
    )])


tooltip_sentences_t = html.Div([
    dbc.Tooltip(
        "When speaking to woman, can complete two sentences without stopping to breathe.",
        target="sentences_qt",
    )])

tooltip_sentences_c = html.Div([
    dbc.Tooltip(
        "When speaking to woman, can complete two sentences without stopping to breathe.",
        target="sentences_qc",
    )])

tooltip_sentences_r = html.Div([
    dbc.Tooltip(
        "When speaking to woman, can complete two sentences without stopping to breathe.",
        target="sentences_qr",
    )])

tooltip_rwt_t = html.Div([
    dbc.Tooltip(
        "Rapid Walking Test:"
        "1.  Measure SpO2 at rest; 2. Ask Patient to walk 30 metres,"
        "OR 40 steps at a rapid pace, 3.  Measure SpO2 again.",
        target="rwt_qt",
    )])

tooltip_rwt_c = html.Div([
    dbc.Tooltip(
        "Rapid Walking Test:"
        "1.  Measure SpO2 at rest; 2. Ask Patient to walk 30 metres,"
        "OR 40 steps at a rapid pace, 3.  Measure SpO2 again.",
        target="rwt_qc",
    )])

tooltip_rwt_r = html.Div([
    dbc.Tooltip(
        "Rapid Walking Test:"
        "1.  Measure SpO2 at rest; 2. Ask Patient to walk 30 metres,"
        "OR 40 steps at a rapid pace, 3.  Measure SpO2 again.",
        target="rwt_qr",
    )])


tooltip_steroids_t = html.Div([
    dbc.Tooltip(
        "Steroids: Oral treatment >14 days duration,"
        "Immunosuppressant medication:  e.g. Azathioprine, Cyclosporin, Monoclonoal antibodies [Infliximab], "
        "Conditions relevant:  Inflammatory bowel disease, rheumatoid arthritis and transplant recipients.",
        target="risksw3_at",
    )])

tooltip_steroids_c = html.Div([
    dbc.Tooltip(
        "Steroids: Oral treatment >14 days duration,"
        "Immunosuppressant medication:  e.g. Azathioprine, Cyclosporin, Monoclonoal antibodies [Infliximab], "
        "Conditions relevant:  Inflammatory bowel disease, rheumatoid arthritis and transplant recipients.",
        target="risksw3_ac",
    )])
tooltip_steroids_r = html.Div([
    dbc.Tooltip(
        "Steroids: Oral treatment >14 days duration,"
        "Immunosuppressant medication:  e.g. Azathioprine, Cyclosporin, Monoclonoal antibodies [Infliximab], "
        "Conditions relevant:  Inflammatory bowel disease, rheumatoid arthritis and transplant recipients.",
        target="risksw3_ar",
    )])


tooltip_diabetes_t = html.Div([
    dbc.Tooltip(
        "Diabetes:  Types 1 and 2, "
        "Gestational diabetes is NOT a risk factor.",
        target="risksw2_at",
    )])

tooltip_diabetes_c = html.Div([
    dbc.Tooltip(
        "Diabetes:  Types 1 and 2, "
        "Gestational diabetes is NOT a risk factor.",
        target="risksw2_ac",
    )])

tooltip_diabetes_r = html.Div([
    dbc.Tooltip(
        "Diabetes:  Types 1 and 2, "
        "Gestational diabetes is NOT a risk factor.",
        target="risksw2_ar",
    )])

tooltip_anaemia_t = html.Div([
    dbc.Tooltip(
        "Anaemia:  Risk factor for sepsis related mortality.",
        target="risksw4_at",
    )])

tooltip_anaemia_c = html.Div([
    dbc.Tooltip(
        "Anaemia:  Risk factor for sepsis related mortality.",
        target="risksw4_ac",
    )])

tooltip_anaemia_r = html.Div([
    dbc.Tooltip(
        "Anaemia:  Risk factor for sepsis related mortality.",
        target="risksw4_ar",
    )])
#############################################        Surname       #####################################################

surname_qt = html.Div(html.P('Surname', className='formlabel'), style={'margin-top': '5%'})
surname_qc = html.Div(html.P('Surname', className='formlabel'), style={'margin-top': '5%'})
surname_qr = html.Div(html.P('Surname', className='formlabel'), style={'margin-top': '5%'})

surname_rt = html.Div(children=
                     [dbc.Input(className='form-control', id='surname_at', autoComplete='off', type='text', maxLength=15,
                                placeholder='Surname')])
surname_rc = html.Div(children=
                     [dbc.Input(className='form-control', id='surname_ac', autoComplete='off', type='text', maxLength=15,
                                placeholder='Surname')])
surname_rr = html.Div(children=
                     [dbc.Input(className='form-control', id='surname_ar', autoComplete='off', type='text', maxLength=15,
                                placeholder='Surname')])

#############################################          NHS         #####################################################

nhs_qt = html.Div(html.P('NHS number', className='formlabel'), style={'margin-top': '5%'})
nhs_qc = html.Div(html.P('NHS number', className='formlabel'), style={'margin-top': '5%'})
nhs_qr = html.Div(html.P('NHS number', className='formlabel'), style={'margin-top': '5%'})

nhs_rt = html.Div(children=
                 [dbc.Input(className='form-control', id='nhs_at', autoComplete='off', type='text', maxLength=12,
                            placeholder='*** *** ****')])
nhs_rc = html.Div(children=
                 [dbc.Input(className='form-control', id='nhs_ac', autoComplete='off', type='text', maxLength=12,
                            placeholder='*** *** ****')])
nhs_rr = html.Div(children=
                 [dbc.Input(className='form-control', id='nhs_ar', autoComplete='off', type='text', maxLength=12,
                            placeholder='*** *** ****')])

#############################################          DOB         #####################################################

doby_qt = html.Div(html.P('Date of birth', className='formlabel'), style={'margin-top': '5%'})
doby_qc = html.Div(html.P('Date of birth', className='formlabel'), style={'margin-top': '5%'})
doby_qr = html.Div(html.P('Date of birth', className='formlabel'), style={'margin-top': '5%'})

doby_rt = html.Div(children=[dbc.Input(id='dob_at', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
doby_rc = html.Div(children=[dbc.Input(id='dob_ac', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
doby_rr = html.Div(children=[dbc.Input(id='dob_ar', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])

#############################################         Parity       #####################################################

parity_qt = html.Div(html.P('Parity', className='formlabel'), style={'margin-top': '5%'})
parity_qc = html.Div(html.P('Parity', className='formlabel'), style={'margin-top': '5%'})
parity_qr = html.Div(html.P('Parity', className='formlabel'), style={'margin-top': '5%'})

parity_rt = html.Div(children=
                    [dbc.Input(className='form-control', autoComplete='off', id='parity_at', type='text', maxLength=2,
                               placeholder='Maximum 10')])
parity_rc = html.Div(children=
                    [dbc.Input(className='form-control', autoComplete='off', id='parity_ac', type='text', maxLength=2,
                               placeholder='Maximum 10')])
parity_rr = html.Div(children=
                    [dbc.Input(className='form-control', autoComplete='off', id='parity_ar', type='text', maxLength=2,
                               placeholder='Maximum 10')])


#############################################           EDD        #####################################################

edd_qt = html.Div(html.P('Estimated Delivery Date', className='formlabel'), style={'margin-top': '5%'})
edd_qc = html.Div(html.P('Estimated Delivery Date', className='formlabel'), style={'margin-top': '5%'})
edd_qr = html.Div(html.P('Estimated Delivery Date', className='formlabel'), style={'margin-top': '5%'})

edd_rt = html.Div(children=[dbc.Input(id='edd_at', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
edd_rc = html.Div(children=[dbc.Input(id='edd_ac', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
edd_rr = html.Div(children=[dbc.Input(id='edd_ar', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])

#############################################           Del        #####################################################

del_qt = html.Div(html.P('Delivered?', className='formlabel'), style={'margin-top': '5%'})
del_qc = html.Div(html.P('Delivered?', className='formlabel'), style={'margin-top': '5%'})
del_qr = html.Div(html.P('Delivered?', className='formlabel'), style={'margin-top': '5%'})

del_rt = html.Div(
    children=[
        html.Div([dbc.RadioItems(id='del_at', labelStyle={'color': 'grey', 'margin-right': '25px'},
                                 options=[{'label': d_yesno['1'], 'value': 1}, {'label': d_yesno['2'], 'value': 2}],
                                 inline=True)])])

del_rc = html.Div(
    children=[
        html.Div([dbc.RadioItems(id='del_ac', labelStyle={'color': 'grey', 'margin-right': '25px'},
                                 options=[{'label': d_yesno['1'], 'value': 1}, {'label': d_yesno['2'], 'value': 2}],
                                 inline=True)])])

del_rr = html.Div(
    children=[
        html.Div([dbc.RadioItems(id='del_ar', labelStyle={'color': 'grey', 'margin-right': '25px'},
                                 options=[{'label': d_yesno['1'], 'value': 1}, {'label': d_yesno['2'], 'value': 2}],
                                 inline=True)])])

#############################################         Deldate      #####################################################

deldate_qt = html.Div(html.P('Delivery date', className='formlabel'), style={'margin-top': '5%'})
deldate_qc = html.Div(html.P('Delivery date', className='formlabel'), style={'margin-top': '5%'})
deldate_qr = html.Div(html.P('Delivery date', className='formlabel'), style={'margin-top': '5%'})

deldate_rt = html.Div(children=[dbc.Input(id='deldate_at', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
deldate_rc = html.Div(children=[dbc.Input(id='deldate_ac', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
deldate_rr = html.Div(children=[dbc.Input(id='deldate_ar', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])

#########################################           Mobile Phone        ################################################

tel_qt = html.Div(html.P('Mobile telephone', className='formlabel'), style={'margin-top': '5%'})
tel_qc = html.Div(html.P('Mobile telephone', className='formlabel'), style={'margin-top': '5%'})
tel_qr = html.Div(html.P('Mobile telephone', className='formlabel'), style={'margin-top': '5%'})

tel_rt = html.Div(children=[dbc.Input(id='tel_at', type='text', autoComplete='off', maxLength=12, placeholder='07** ******')])
tel_rc = html.Div(children=[dbc.Input(id='tel_ac', type='text', autoComplete='off', maxLength=12, placeholder='07** ******')])
tel_rr = html.Div(children=[dbc.Input(id='tel_ar', type='text', autoComplete='off', maxLength=12, placeholder='07** ******')])


############################################          Vaccine      #####################################################

vacc_qt = html.Div(html.P('COVID vaccine received?', className='formlabel'), style={'margin-top': '5%'})
vacc_qc = html.Div(html.P('COVID vaccine received?', className='formlabel'), style={'margin-top': '5%'})
vacc_qr = html.Div(html.P('COVID vaccine received?', className='formlabel'), style={'margin-top': '5%'})

vacc_rt = html.Div(
    children=[html.Div([dbc.RadioItems(id='vaccine_at', labelStyle={'color': 'grey', 'margin-right': '25px'},
                                       options=[
                                           {'label': d_vacc_doses['1'], 'value': 1},
                                           {'label': d_vacc_doses['2'], 'value': 2},
                                           {'label': d_vacc_doses['3'], 'value': 3}],
                                       inline=True)])])

vacc_rc = html.Div(
    children=[html.Div([dbc.RadioItems(id='vaccine_ac', labelStyle={'color': 'grey', 'margin-right': '25px'},
                                       options=[
                                           {'label': d_vacc_doses['1'], 'value': 1},
                                           {'label': d_vacc_doses['2'], 'value': 2},
                                           {'label': d_vacc_doses['3'], 'value': 3}],
                                       inline=True)])])

vacc_rr = html.Div(
    children=[html.Div([dbc.RadioItems(id='vaccine_ar', labelStyle={'color': 'grey', 'margin-right': '25px'},
                                       options=[
                                           {'label': d_vacc_doses['1'], 'value': 1},
                                           {'label': d_vacc_doses['2'], 'value': 2},
                                           {'label': d_vacc_doses['3'], 'value': 3}],
                                       inline=True)])])

#########################################          Vaccine Dose 1      #################################################

vac1date_qt = html.Div(html.P('Dose 1 - date', className='formlabel'), style={'margin-top': '5%'})
vac1date_qc = html.Div(html.P('Dose 1 - date', className='formlabel'), style={'margin-top': '5%'})
vac1date_qr = html.Div(html.P('Dose 1 - date', className='formlabel'), style={'margin-top': '5%'})

vac1date_rt = html.Div(children=[dbc.Input(id='dose1date_at', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
vac1date_rc = html.Div(children=[dbc.Input(id='dose1date_ac', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
vac1date_rr = html.Div(children=[dbc.Input(id='dose1date_ar', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])

#########################################          Vaccine Dose 2      #################################################

vac2date_qt = html.Div(html.P('Dose 2 - date', className='formlabel'), style={'margin-top': '5%'})
vac2date_qc = html.Div(html.P('Dose 2 - date', className='formlabel'), style={'margin-top': '5%'})
vac2date_qr = html.Div(html.P('Dose 2 - date', className='formlabel'), style={'margin-top': '5%'})

vac2date_rt = html.Div(children=[dbc.Input(id='dose2date_at', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
vac2date_rc = html.Div(children=[dbc.Input(id='dose2date_ac', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
vac2date_rr = html.Div(children=[dbc.Input(id='dose2date_ar', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])


#########################################          Vaccine Which      #################################################

vacwhich_qt = html.Div(html.P('Vaccine - manufacturer', className='formlabel'), style={'margin-top': '5%'})
vacwhich_qc = html.Div(html.P('Vaccine - manufacturer', className='formlabel'), style={'margin-top': '5%'})
vacwhich_qr = html.Div(html.P('Vaccine - manufacturer', className='formlabel'), style={'margin-top': '5%'})

vacwhich1_rt = html.Div(children=[dbc.Checklist(id='vactype1_at', className='checkCustom',
                                               options=[
                                                   {'label': d_vacc_typ['0'], 'value': 0},
                                                   {'label': d_vacc_typ['1'], 'value': 1},
                                                   {'label': d_vacc_typ['2'], 'value': 2}],
                                               labelStyle={'color': 'grey', 'text-align': 'left'},
                                               labelCheckedStyle={'color': '#319997'})])
vacwhich1_rc = html.Div(children=[dbc.Checklist(id='vactype1_ac', className='checkCustom',
                                               options=[
                                                   {'label': d_vacc_typ['0'], 'value': 0},
                                                   {'label': d_vacc_typ['1'], 'value': 1},
                                                   {'label': d_vacc_typ['2'], 'value': 2}],
                                               labelStyle={'color': 'grey', 'text-align': 'left'},
                                               labelCheckedStyle={'color': '#319997'})])
vacwhich1_rr = html.Div(children=[dbc.Checklist(id='vactype1_ar', className='checkCustom',
                                               options=[
                                                   {'label': d_vacc_typ['0'], 'value': 0},
                                                   {'label': d_vacc_typ['1'], 'value': 1},
                                                   {'label': d_vacc_typ['2'], 'value': 2}],
                                               labelStyle={'color': 'grey', 'text-align': 'left'},
                                               labelCheckedStyle={'color': '#319997'})])

vacwhich2_rt = html.Div(children=
                       [dbc.Checklist(id='vactype2_at', options=[{'label': d_vacc_typ['3'], 'value': 3},
                                                                {'label': d_vacc_typ['4'], 'value': 4}, ],
                                      labelStyle={'color': 'grey',
                                                  'text-align': 'left'})])
vacwhich2_rc = html.Div(children=
                       [dbc.Checklist(id='vactype2_ac', options=[{'label': d_vacc_typ['3'], 'value': 3},
                                                                {'label': d_vacc_typ['4'], 'value': 4}, ],
                                      labelStyle={'color': 'grey',
                                                  'text-align': 'left'})])
vacwhich2_rr = html.Div(children=
                       [dbc.Checklist(id='vactype2_ar', options=[{'label': d_vacc_typ['3'], 'value': 3},
                                                                {'label': d_vacc_typ['4'], 'value': 4}, ],
                                      labelStyle={'color': 'grey',
                                                  'text-align': 'left'})])

#########################################         COVID Test 90 d      #################################################

covidtest_qt = html.Div(
    children=[html.P('COVID test in last 90 days? \U0001f6a9', className='formlabel', id='covidtest_qt'),
              tooltip_covidtest_t], style={'margin-top': '5%'})
covidtest_qc = html.Div(
    children=[html.P('COVID test in last 90 days? \U0001f6a9', className='formlabel', id='covidtest_qc'),
              tooltip_covidtest_c], style={'margin-top': '5%'})
covidtest_qr = html.Div(
    children=[html.P('COVID test in last 90 days? \U0001f6a9', className='formlabel', id='covidtest_qr'),
              tooltip_covidtest_r], style={'margin-top': '5%'})

covidtest_rt = html.Div(children=[html.Div([
    dbc.RadioItems(id='covidtest_at', labelStyle={'color': 'grey', 'margin-right': '25px'},
                   options=[
                       {'label': d_yesno['1'], 'value': 1},
                       {'label': d_yesno['2'], 'value': 2}],
                   inline=True)])])

covidtest_rc = html.Div(children=[html.Div([
    dbc.RadioItems(id='covidtest_ac', labelStyle={'color': 'grey', 'margin-right': '25px'},
                   options=[
                       {'label': d_yesno['1'], 'value': 1},
                       {'label': d_yesno['2'], 'value': 2}],
                   inline=True)])])

covidtest_rr = html.Div(children=[html.Div([
    dbc.RadioItems(id='covidtest_ar', labelStyle={'color': 'grey', 'margin-right': '25px'},
                   options=[
                       {'label': d_yesno['1'], 'value': 1},
                       {'label': d_yesno['2'], 'value': 2}],
                   inline=True)])])

###########################################         COVID Status      ##################################################

covidstatus_qt = html.Div(html.P('Test result', className='formlabel', id='covidstatus_q'), style={'margin-top': '5%'})
covidstatus_qc = html.Div(html.P('Test result', className='formlabel', id='covidstatus_q'), style={'margin-top': '5%'})
covidstatus_qr = html.Div(html.P('Test result', className='formlabel', id='covidstatus_q'), style={'margin-top': '5%'})

covidstatus_rt = html.Div(children=[html.Div(
    [dbc.RadioItems(id='covidstatus_at', labelStyle={'color': 'grey', 'margin-right': '25px'},
                    options=[
                        {'label': d_cov_status['1'], 'value': 1},
                        {'label': d_cov_status['2'], 'value': 2},
                        {'label': d_cov_status['3'], 'value': 3}],
                    inline=True)])])

covidstatus_rc = html.Div(children=[html.Div(
    [dbc.RadioItems(id='covidstatus_ac', labelStyle={'color': 'grey', 'margin-right': '25px'},
                    options=[
                        {'label': d_cov_status['1'], 'value': 1},
                        {'label': d_cov_status['2'], 'value': 2},
                        {'label': d_cov_status['3'], 'value': 3}],
                    inline=True)])])

covidstatus_rr = html.Div(children=[html.Div(
    [dbc.RadioItems(id='covidstatus_ar', labelStyle={'color': 'grey', 'margin-right': '25px'},
                    options=[
                        {'label': d_cov_status['1'], 'value': 1},
                        {'label': d_cov_status['2'], 'value': 2},
                        {'label': d_cov_status['3'], 'value': 3}],
                    inline=True)])])

###########################################          COVID Swab       ##################################################

covswabdate_qt = html.Div(html.P('COVID swab - date', className='formlabel'), style={'margin-top': '5%'})
covswabdate_qc = html.Div(html.P('COVID swab - date', className='formlabel'), style={'margin-top': '5%'})
covswabdate_qr = html.Div(html.P('COVID swab - date', className='formlabel'), style={'margin-top': '5%'})

covswabdate_rt = html.Div(children=[dbc.Input(id='covidswabdate_at', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
covswabdate_rc = html.Div(children=[dbc.Input(id='covidswabdate_ac', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
covswabdate_rr = html.Div(children=[dbc.Input(id='covidswabdate_ar', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])

##########################################          COVID Admit       ##################################################

covadmit_qt = html.Div(
    children=[html.P('COVID related hospital admission? \U0001f6a9', className='formlabel', id="covidadmit_qt"),
              tooltip_covidadmit_t], style={'margin-top': '5%'})
covadmit_qc = html.Div(
    children=[html.P('COVID related hospital admission? \U0001f6a9', className='formlabel', id="covidadmit_qc"),
              tooltip_covidadmit_c], style={'margin-top': '5%'})
covadmit_qr = html.Div(
    children=[html.P('COVID related hospital admission? \U0001f6a9', className='formlabel', id="covidadmit_qr"),
              tooltip_covidadmit_r], style={'margin-top': '5%'})

covadmit_rt = html.Div(children=
                      [html.Div([dbc.RadioItems(id='covidadmit_at', labelStyle={'color': 'grey', 'margin-right': '25px'},
                                                options=[
                                                    {'label': d_yesno['1'], 'value': 1},
                                                    {'label': d_yesno['2'], 'value': 2}],
                                                inline=True)])])

covadmit_rc = html.Div(children=
                      [html.Div([dbc.RadioItems(id='covidadmit_ac', labelStyle={'color': 'grey', 'margin-right': '25px'},
                                                options=[
                                                    {'label': d_yesno['1'], 'value': 1},
                                                    {'label': d_yesno['2'], 'value': 2}],
                                                inline=True)])])

covadmit_rr = html.Div(children=
                      [html.Div([dbc.RadioItems(id='covidadmit_ar', labelStyle={'color': 'grey', 'margin-right': '25px'},
                                                options=[
                                                    {'label': d_yesno['1'], 'value': 1},
                                                    {'label': d_yesno['2'], 'value': 2}],
                                                inline=True)])])



########################################          COVID Admit Date       ###############################################

covadmitdate_qt = html.P('Admission - date', className='formlabel')
covadmitdate_qc = html.P('Admission - date', className='formlabel')
covadmitdate_qr = html.P('Admission - date', className='formlabel')

covadmitdate_rt = html.Div(children=[dbc.Input(id='covidadmitdate_at', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
covadmitdate_rc = html.Div(children=[dbc.Input(id='covidadmitdate_ac', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
covadmitdate_rr = html.Div(children=[dbc.Input(id='covidadmitdate_ar', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])

########################################        COVID Discharge Date      ##############################################

covdischargedate_qt = html.P('Discharge - date', className='formlabel')
covdischargedate_qc = html.P('Discharge - date', className='formlabel')
covdischargedate_qr = html.P('Discharge - date', className='formlabel')

covdischargedate_rt = html.Div(children=[dbc.Input(id='coviddischdate_at', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
covdischargedate_rc = html.Div(children=[dbc.Input(id='coviddischdate_ac', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])
covdischargedate_rr = html.Div(children=[dbc.Input(id='coviddischdate_ar', debounce=True, className='form-control', autoComplete='off', type='text', maxLength=10, placeholder='dd/MM/yyyy')])

########################################        Speaking sentences        ##############################################

sentences_qt = html.Div(
    children=[html.P('Completes 2 sentences \U0001f6a9', className='formlabel', id='sentences_qt'), tooltip_sentences_t],
    style={'margin-top': '5%'})
sentences_qc = html.Div(
    children=[html.P('Completes 2 sentences \U0001f6a9', className='formlabel', id='sentences_qc'), tooltip_sentences_c],
    style={'margin-top': '5%'})
sentences_qr = html.Div(
    children=[html.P('Completes 2 sentences \U0001f6a9', className='formlabel', id='sentences_qr'), tooltip_sentences_r],
    style={'margin-top': '5%'})

sentences_rt = html.Div(children=
                       [html.Div([dbc.RadioItems(id='sentences_at', labelStyle={'color': 'grey', 'margin-right': '40px'},
                                                 options=[
                                                     {'label': d_yesno['1'], 'value': 1},
                                                     {'label': d_yesno['2'], 'value': 2}],
                                                 inline=True)])])
sentences_rc = html.Div(children=
                       [html.Div([dbc.RadioItems(id='sentences_ac', labelStyle={'color': 'grey', 'margin-right': '40px'},
                                                 options=[
                                                     {'label': d_yesno['1'], 'value': 1},
                                                     {'label': d_yesno['2'], 'value': 2}],
                                                 inline=True)])])
sentences_rr = html.Div(children=
                       [html.Div([dbc.RadioItems(id='sentences_ar', labelStyle={'color': 'grey', 'margin-right': '40px'},
                                                 options=[
                                                     {'label': d_yesno['1'], 'value': 1},
                                                     {'label': d_yesno['2'], 'value': 2}],
                                                 inline=True)])])

#########################################       Rapid Walking Test        ##############################################

rwt_qt = html.Div(children=[html.P('Rapid Walking Test \U0001f6a9', className='formlabel', id='rwt_qt'), tooltip_rwt_t],
                 style={'margin-top': '5%'})
rwt_qc = html.Div(children=[html.P('Rapid Walking Test \U0001f6a9', className='formlabel', id='rwt_qc'), tooltip_rwt_c],
                 style={'margin-top': '5%'})
rwt_qr = html.Div(children=[html.P('Rapid Walking Test \U0001f6a9', className='formlabel', id='rwt_qr'), tooltip_rwt_r],
                 style={'margin-top': '5%'})

rwt_rt = html.Div(id='rwt_at',
                 style={'display': 'inline-block', 'opacity': 0},
                 children=[
                     html.Div([dbc.Input(id='spo2_1at', type='text', autoComplete='off', maxLength=2, placeholder='Pre SpO2',
                                         style={'width': '110px'})],
                              style={'display': 'inline-block'}),
                     html.Div([dbc.Input(id='spo2_2at', type='text', autoComplete='off', maxLength=2, placeholder='Post SpO2',
                                         style={'width': '110px'})],
                              style={'right': '0', 'margin-left': '35px', 'margin-right': '0',
                                     'display': 'inline-block'})])
rwt_rc = html.Div(id='rwt_ac',
                 style={'display': 'inline-block'},
                 children=[
                     html.Div([dbc.Input(id='spo2_1ac', type='text', autoComplete='off', maxLength=2, placeholder='Pre SpO2',
                                         style={'width': '110px'})],
                              style={'display': 'inline-block'}),
                     html.Div([dbc.Input(id='spo2_2ac', type='text', autoComplete='off', maxLength=2, placeholder='Post SpO2',
                                         style={'width': '110px'})],
                              style={'right': '0', 'margin-left': '35px', 'margin-right': '0',
                                     'display': 'inline-block'})])
rwt_rr = html.Div(id='rwt_ar',
                 style={'display': 'inline-block'},
                 children=[
                     html.Div([dbc.Input(id='spo2_1ar', type='text', autoComplete='off', maxLength=2, placeholder='Pre SpO2',
                                         style={'width': '110px'})],
                              style={'display': 'inline-block'}),
                     html.Div([dbc.Input(id='spo2_2ar', type='text', autoComplete='off', maxLength=2, placeholder='Post SpO2',
                                         style={'width': '110px'})],
                              style={'right': '0', 'margin-left': '35px', 'margin-right': '0',
                                     'display': 'inline-block'})])


#########################################       Woman d_symptoms Cur        ##############################################

covsymp_qt = html.Div(html.P('Symptoms - current', className='formlabel'), style={'margin-top': '5%'})
covsymp_qc = html.Div(html.P('Symptoms - current', className='formlabel'), style={'margin-top': '5%'})
covsymp_qr = html.Div(html.P('Symptoms - current', className='formlabel'), style={'margin-top': '5%'})

tsym1_rt = html.Div(children=
                   [dbc.Checklist(id='tsym1_at',
                                  options=[{'label': d_symptoms['0'], 'value': 0},
                                           {'label': d_symptoms['1'], 'value': 1}],
                                  labelStyle={'color': 'grey', 'text-align': 'left'})])

tsym2_rt = html.Div(children=
                   [dbc.Checklist(id='tsym2_at', options=[{'label': d_symptoms['2'], 'value': 2},
                                                         {'label': d_symptoms['3'], 'value': 3}],
                                  labelStyle={'color': 'grey', 'text-align': 'left'})])

tsym3_rt = html.Div(children=
                   [dbc.Checklist(id='tsym3_at', options=[{'label': d_symptoms['4'], 'value': 4},
                                                         {'label': d_symptoms['5'], 'value': 5}],
                                  labelStyle={'color': 'grey', 'text-align': 'left'})])

tsym4_rt = html.Div(children=
                   [dbc.Checklist(id='tsym4_at',
                                  options=[{'label': d_symptoms['6'], 'value': 6}, {'label': d_symptoms['7'], 'value': 7}],
                                  labelStyle={'color': 'grey', 'text-align': 'left'})])

tsym1_rc = html.Div(children=
                   [dbc.Checklist(id='tsym1_ac',
                                  options=[{'label': d_symptoms['0'], 'value': 0},
                                           {'label': d_symptoms['1'], 'value': 1}],
                                  labelStyle={'color': 'grey', 'text-align': 'left'})])

tsym2_rc = html.Div(children=
                   [dbc.Checklist(id='tsym2_ac', options=[{'label': d_symptoms['2'], 'value': 2},
                                                         {'label': d_symptoms['3'], 'value': 3}],
                                  labelStyle={'color': 'grey', 'text-align': 'left'})])

tsym3_rc = html.Div(children=
                   [dbc.Checklist(id='tsym3_ac', options=[{'label': d_symptoms['4'], 'value': 4},
                                                         {'label': d_symptoms['5'], 'value': 5}],
                                  labelStyle={'color': 'grey', 'text-align': 'left'})])

tsym4_rc = html.Div(children=
                   [dbc.Checklist(id='tsym4_ac',
                                  options=[{'label': d_symptoms['6'], 'value': 6}, {'label': d_symptoms['7'], 'value': 7}],
                                  labelStyle={'color': 'grey', 'text-align': 'left'})])

tsym1_rr = html.Div(children=
                   [dbc.Checklist(id='tsym1_ar',
                                  options=[{'label': d_symptoms['0'], 'value': 0},
                                           {'label': d_symptoms['1'], 'value': 1}],
                                  labelStyle={'color': 'grey', 'text-align': 'left'})])

tsym2_rr = html.Div(children=
                   [dbc.Checklist(id='tsym2_ar', options=[{'label': d_symptoms['2'], 'value': 2},
                                                         {'label': d_symptoms['3'], 'value': 3}],
                                  labelStyle={'color': 'grey', 'text-align': 'left'})])

tsym3_rr = html.Div(children=
                   [dbc.Checklist(id='tsym3_ar', options=[{'label': d_symptoms['4'], 'value': 4},
                                                         {'label': d_symptoms['5'], 'value': 5}],
                                  labelStyle={'color': 'grey', 'text-align': 'left'})])

tsym4_rr = html.Div(children=
                   [dbc.Checklist(id='tsym4_ar',
                                  options=[{'label': d_symptoms['6'], 'value': 6}, {'label': d_symptoms['7'], 'value': 7}],
                                  labelStyle={'color': 'grey', 'text-align': 'left'})])


#########################################       Risk Factors Woman        ##############################################

covrisksw_qt = html.Div(html.P('Risk factors - woman', className='formlabel'), style={'margin-top': '5%'})
covrisksw_qc = html.Div(html.P('Risk factors - woman', className='formlabel'), style={'margin-top': '5%'})
covrisksw_qr = html.Div(html.P('Risk factors - woman', className='formlabel'), style={'margin-top': '5%'})

risksw1_rt = html.Div(children=
                     [dbc.Checklist(id='risksw1_at', options=[{'label': d_risk_woman['0'], 'value': 0},
                                                             {'label': d_risk_woman['1'], 'value': 1},
                                                             {'label': d_risk_woman['2'], 'value': 2}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

risksw2_rt = html.Div(children=
                     [dbc.Checklist(id='risksw2_at', options=[{'label': d_risk_woman['3'], 'value': 3},
                                                             {'label': d_risk_woman['4'],
                                                              'value': 4}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'}), tooltip_diabetes_t])

risksw3_rt = html.Div(children=
                     [dbc.Checklist(id='risksw3_at',
                                    options=[{'label': d_risk_woman['5'], 'value': 5},
                                             {'label': d_risk_woman['6'], 'value': 6},
                                             {'label': d_risk_woman['7'], 'value': 7}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'}), tooltip_steroids_t])

risksw4_rt = html.Div(children=
                     [dbc.Checklist(id='risksw4_at', options=[{'label': d_risk_woman['8'], 'value': 8},
                                                             {'label': d_risk_woman['9'], 'value': 9},
                                                             {'label': d_risk_woman['10'], 'value': 10}
                                                             ],
                                    labelStyle={'color': 'grey', 'text-align': 'left'}), tooltip_anaemia_t])

risksw1_rc = html.Div(children=
                     [dbc.Checklist(id='risksw1_ac', options=[{'label': d_risk_woman['0'], 'value': 0},
                                                             {'label': d_risk_woman['1'], 'value': 1},
                                                             {'label': d_risk_woman['2'], 'value': 2}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

risksw2_rc = html.Div(children=
                     [dbc.Checklist(id='risksw2_ac', options=[{'label': d_risk_woman['3'], 'value': 3},
                                                             {'label': d_risk_woman['4'],
                                                              'value': 4}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'}), tooltip_diabetes_c])

risksw3_rc = html.Div(children=
                     [dbc.Checklist(id='risksw3_ac',
                                    options=[{'label': d_risk_woman['5'], 'value': 5},
                                             {'label': d_risk_woman['6'], 'value': 6},
                                             {'label': d_risk_woman['7'], 'value': 7}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'}), tooltip_steroids_c])

risksw4_rc = html.Div(children=
                     [dbc.Checklist(id='risksw4_ac', options=[{'label': d_risk_woman['8'], 'value': 8},
                                                             {'label': d_risk_woman['9'], 'value': 9},
                                                             {'label': d_risk_woman['10'], 'value': 10}
                                                             ],
                                    labelStyle={'color': 'grey', 'text-align': 'left'}), tooltip_anaemia_c])

risksw1_rr = html.Div(children=
                     [dbc.Checklist(id='risksw1_ar', options=[{'label': d_risk_woman['0'], 'value': 0},
                                                             {'label': d_risk_woman['1'], 'value': 1},
                                                             {'label': d_risk_woman['2'], 'value': 2}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

risksw2_rr = html.Div(children=
                     [dbc.Checklist(id='risksw2_ar', options=[{'label': d_risk_woman['3'], 'value': 3},
                                                             {'label': d_risk_woman['4'],
                                                              'value': 4}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'}), tooltip_diabetes_r])

risksw3_rr = html.Div(children=
                     [dbc.Checklist(id='risksw3_ar',
                                    options=[{'label': d_risk_woman['5'], 'value': 5},
                                             {'label': d_risk_woman['6'], 'value': 6},
                                             {'label': d_risk_woman['7'], 'value': 7}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'}), tooltip_steroids_r])

risksw4_rr = html.Div(children=
                     [dbc.Checklist(id='risksw4_ar', options=[{'label': d_risk_woman['8'], 'value': 8},
                                                             {'label': d_risk_woman['9'], 'value': 9},
                                                             {'label': d_risk_woman['10'], 'value': 10}
                                                             ],
                                    labelStyle={'color': 'grey', 'text-align': 'left'}), tooltip_anaemia_r])



#########################################       Risk Factors Baby         ##############################################

covrisksb_qt = html.Div(html.P('Risk factors - baby', className='formlabel'), style={'margin-top': '5%'})
covrisksb_qc = html.Div(html.P('Risk factors - baby', className='formlabel'), style={'margin-top': '5%'})
covrisksb_qr = html.Div(html.P('Risk factors - baby', className='formlabel'), style={'margin-top': '5%'})

risksb1_rt = html.Div(children=
                     [dbc.Checklist(id='risksb1_at', options=[{'label': d_risk_baby['0'], 'value': 0}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

risksb2_rt = html.Div(children=
                     [dbc.Checklist(id='risksb2_at', options=[{'label': d_risk_baby['1'], 'value': 1}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

risksb3_rt = html.Div(children=
                     [dbc.Checklist(id='risksb3_at', options=[{'label': d_risk_baby['2'], 'value': 2}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

risksb4_rt = html.Div(children=
                     [dbc.Checklist(id='risksb4_at', options=[{'label': d_risk_baby['3'], 'value': 3},
                                                             {'label': d_risk_baby['4'], 'value': 4}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])
risksb1_rc = html.Div(children=
                     [dbc.Checklist(id='risksb1_ac', options=[{'label': d_risk_baby['0'], 'value': 0}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

risksb2_rc = html.Div(children=
                     [dbc.Checklist(id='risksb2_ac', options=[{'label': d_risk_baby['1'], 'value': 1}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

risksb3_rc = html.Div(children=
                     [dbc.Checklist(id='risksb3_ac', options=[{'label': d_risk_baby['2'], 'value': 2}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

risksb4_rc = html.Div(children=
                     [dbc.Checklist(id='risksb4_ac', options=[{'label': d_risk_baby['3'], 'value': 3},
                                                             {'label': d_risk_baby['4'], 'value': 4}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])
risksb1_rr = html.Div(children=
                     [dbc.Checklist(id='risksb1_ar', options=[{'label': d_risk_baby['0'], 'value': 0}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

risksb2_rr = html.Div(children=
                     [dbc.Checklist(id='risksb2_ar', options=[{'label': d_risk_baby['1'], 'value': 1}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

risksb3_rr = html.Div(children=
                     [dbc.Checklist(id='risksb3_ar', options=[{'label': d_risk_baby['2'], 'value': 2}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

risksb4_rr = html.Div(children=
                     [dbc.Checklist(id='risksb4_ar', options=[{'label': d_risk_baby['3'], 'value': 3},
                                                             {'label': d_risk_baby['4'], 'value': 4}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])


#########################################       Treatments Woman          ##############################################

covrx_qt = html.Div(html.P('COVID treatment mother [current]', className='formlabel'), style={'margin-top': '5%'})
covrx_qc = html.Div(html.P('COVID treatment mother [current]', className='formlabel'), style={'margin-top': '5%'})
covrx_qr = html.Div(html.P('COVID treatment mother [current]', className='formlabel'), style={'margin-top': '5%'})

covrxw1_rt = html.Div(children=
                     [dbc.Checklist(id='covrxw1_at', options=[{'label': d_treatment_list['0'], 'value': 0},
                                                             {'label': d_treatment_list['1'], 'value': 1}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

covrxw2_rt = html.Div(children=
                     [dbc.Checklist(id='covrxw2_at', options=[{'label': d_treatment_list['2'], 'value': 2},
                                                             {'label': d_treatment_list['3'], 'value': 3},
                                                             {'label': d_treatment_list['4'], 'value': 4}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

covrxw3_rt = html.Div(children=
                     [dbc.Checklist(id='covrxw3_at', options=[{'label': d_treatment_list['5'], 'value': 5},
                                                             {'label': d_treatment_list['6'], 'value': 6},
                                                             {'label': d_treatment_list['7'], 'value': 7}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

covrxw4_rt = html.Div(children=
                     [dbc.Checklist(id='covrxw4_at', options=[{'label': d_treatment_list['8'], 'value': 8},
                                                             {'label': d_treatment_list['9'], 'value': 9}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

covrxw1_rc = html.Div(children=
                     [dbc.Checklist(id='covrxw1_ac', options=[{'label': d_treatment_list['0'], 'value': 0},
                                                             {'label': d_treatment_list['1'], 'value': 1}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

covrxw2_rc = html.Div(children=
                     [dbc.Checklist(id='covrxw2_ac', options=[{'label': d_treatment_list['2'], 'value': 2},
                                                             {'label': d_treatment_list['3'], 'value': 3},
                                                             {'label': d_treatment_list['4'], 'value': 4}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

covrxw3_rc = html.Div(children=
                     [dbc.Checklist(id='covrxw3_ac', options=[{'label': d_treatment_list['5'], 'value': 5},
                                                             {'label': d_treatment_list['6'], 'value': 6},
                                                             {'label': d_treatment_list['7'], 'value': 7}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

covrxw4_rc = html.Div(children=
                     [dbc.Checklist(id='covrxw4_ac', options=[{'label': d_treatment_list['8'], 'value': 8},
                                                             {'label': d_treatment_list['9'], 'value': 9}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

covrxw1_rr = html.Div(children=
                     [dbc.Checklist(id='covrxw1_ar', options=[{'label': d_treatment_list['0'], 'value': 0},
                                                             {'label': d_treatment_list['1'], 'value': 1}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

covrxw2_rr = html.Div(children=
                     [dbc.Checklist(id='covrxw2_ar', options=[{'label': d_treatment_list['2'], 'value': 2},
                                                             {'label': d_treatment_list['3'], 'value': 3},
                                                             {'label': d_treatment_list['4'], 'value': 4}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

covrxw3_rr = html.Div(children=
                     [dbc.Checklist(id='covrxw3_ar', options=[{'label': d_treatment_list['5'], 'value': 5},
                                                             {'label': d_treatment_list['6'], 'value': 6},
                                                             {'label': d_treatment_list['7'], 'value': 7}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

covrxw4_rr = html.Div(children=
                     [dbc.Checklist(id='covrxw4_ar', options=[{'label': d_treatment_list['8'], 'value': 8},
                                                             {'label': d_treatment_list['9'], 'value': 9}],
                                    labelStyle={'color': 'grey', 'text-align': 'left'})])

####################################       Clinical Assessments Woman         ##########################################

covclinassess_qt = html.Div(html.P('Woman - Clinical Assessments', className='formlabel'), style={'margin-top': '5%'})
covclinassess_qc = html.Div(html.P('Woman - Clinical Assessments', className='formlabel'), style={'margin-top': '5%'})
covclinassess_qr = html.Div(html.P('Woman - Clinical Assessments', className='formlabel'), style={'margin-top': '5%'})

clin1assess1_rt = html.Div(children=
                          [dbc.Checklist(id='clin1assess1_at', options=[{'label': d_assess_1['0'], 'value': 0}],
                                         labelStyle={'color': 'grey', 'text-align': 'left'})])

clin1assess2_rt = html.Div(children=
                          [dbc.Checklist(id='clin1assess2_at', options=[{'label': d_assess_1['1'], 'value': 1}],
                                         labelStyle={'color': 'grey', 'text-align': 'left'})])

clin1assess3_rt = html.Div(children=
                          [dbc.Checklist(id='clin1assess3_at', options=[{'label': d_assess_1['2'], 'value': 2}],
                                         labelStyle={'color': 'grey', 'text-align': 'left'})])

clin1assess4_rt = html.Div(children=
                          [dbc.Checklist(id='clin1assess4_at',
                                         options=[{'label': d_assess_1['3'], 'value': 3}],
                                         labelStyle={'color': 'grey', 'text-align': 'left'})])

clin1assess1_rc = html.Div(children=
                          [dbc.Checklist(id='clin1assess1_ac', options=[{'label': d_assess_1['0'], 'value': 0}],
                                         labelStyle={'color': 'grey', 'text-align': 'left'})])

clin1assess2_rc = html.Div(children=
                          [dbc.Checklist(id='clin1assess2_ac', options=[{'label': d_assess_1['1'], 'value': 1}],
                                         labelStyle={'color': 'grey', 'text-align': 'left'})])

clin1assess3_rc = html.Div(children=
                          [dbc.Checklist(id='clin1assess3_ac', options=[{'label': d_assess_1['2'], 'value': 2}],
                                         labelStyle={'color': 'grey', 'text-align': 'left'})])

clin1assess4_rc = html.Div(children=
                          [dbc.Checklist(id='clin1assess4_ac',
                                         options=[{'label': d_assess_1['3'], 'value': 3}],
                                         labelStyle={'color': 'grey', 'text-align': 'left'})])


clin1assess1_rr = html.Div(children=
                          [dbc.Checklist(id='clin1assess1_ar', options=[{'label': d_assess_2['0'], 'value': 0},
                                                                       {'label': d_assess_2['1'], 'value': 1},
                                                                       {'label': d_assess_2['2'], 'value': 2}],
                                         labelStyle={'color': 'grey', 'text-align': 'left'})])

clin1assess2_rr = html.Div(children=
                          [dbc.Checklist(id='clin1assess2_ar', options=[{'label': d_assess_2['3'], 'value': 3},
                                                                       {'label': d_assess_2['4'], 'value': 4}],
                                         labelStyle={'color': 'grey', 'text-align': 'left'})])

clin1assess3_rr = html.Div(children=
                          [dbc.Checklist(id='clin1assess3_ar', options=[{'label': d_assess_2['5'], 'value': 5},
                                                                       {'label': d_assess_2['6'], 'value': 6}],
                                         labelStyle={'color': 'grey', 'text-align': 'left'})])

clin1assess4_rr = html.Div(children=
                          [dbc.Checklist(id='clin1assess4_ar', options=[{'label': d_assess_2['7'], 'value': 7},
                                                                       {'label': d_assess_2['8'], 'value': 8},
                                                                       {'label': d_assess_2['9'], 'value': 9}],
                                         labelStyle={'color': 'grey', 'text-align': 'left'})])


####################################            Fetal Heart Rate              ##########################################

fetalheart_qt = html.Div(html.P('Fetal Heart Rate', className='formlabel'), style={'margin-top': '5%'})
fetalheart_qc = html.Div(html.P('Fetal Heart Rate', className='formlabel'), style={'margin-top': '5%'})
fetalheart_qr = html.Div(html.P('Fetal Heart Rate', className='formlabel'), style={'margin-top': '5%'})

fhr_rt = html.Div(children=
                 [dbc.Input(className='form-control', id='fhr_at', type='text', autoComplete='off', maxLength=3,
                            placeholder='FHR - bpm')])
fhr_rc = html.Div(children=
                 [dbc.Input(className='form-control', id='fhr_ac', type='text', autoComplete='off', maxLength=3,
                            placeholder='FHR - bpm')])
fhr_rr = html.Div(children=
                 [dbc.Input(className='form-control', id='fhr_ar', type='text', autoComplete='off', maxLength=3,
                            placeholder='FHR - bpm')])


######################################                Labour                  ##########################################

labour_qt = html.Div(html.P('Symptoms of labour?', className='formlabel'), style={'margin-top': '5%'})
labour_qc = html.Div(html.P('Symptoms of labour?', className='formlabel'), style={'margin-top': '5%'})
labour_qr = html.Div(html.P('Symptoms of labour?', className='formlabel'), style={'margin-top': '5%'})

labour_rt = html.Div(children=
            [html.Div(
                [dbc.RadioItems(id='labour_at', labelStyle={'color': 'grey', 'margin-right': '40px'},
                    options=[{'label': d_yesno['1'], 'value': 1}, {'label': d_yesno['2'], 'value': 2}],
                    inline=True)])])

labour_rc = html.Div(children=
            [html.Div(
                [dbc.RadioItems(id='labour_ac', labelStyle={'color': 'grey', 'margin-right': '40px'},
                    options=[{'label': d_yesno['1'], 'value': 1}, {'label': d_yesno['2'], 'value': 2}],
                    inline=True)])])

labour_rr = html.Div(children=
            [html.Div(
                [dbc.RadioItems(id='labour_ar', labelStyle={'color': 'grey', 'margin-right': '40px'},
                    options=[{'label': d_yesno['1'], 'value': 1}, {'label': d_yesno['2'], 'value': 2}],
                    inline=True)])])


###################################               Fetal Concerns                  ######################################

fetalconcerns_qt = html.Div(html.P('Concerns with baby?', className='formlabel'), style={'margin-top': '5%'})
fetalconcerns_qc = html.Div(html.P('Concerns with baby?', className='formlabel'), style={'margin-top': '5%'})
fetalconcerns_qr = html.Div(html.P('Concerns with baby?', className='formlabel'), style={'margin-top': '5%'})

fetalconcerns_rt = html.Div(children=
            [html.Div(
                [dbc.RadioItems(id='fetconcerns_at', labelStyle={'color': 'grey', 'margin-right': '40px'},
                    options=[{'label': d_yesno['1'], 'value': 1}, {'label': d_yesno['2'], 'value': 2}],
                    inline=True)])])

fetalconcerns_rc = html.Div(children=
            [html.Div(
                [dbc.RadioItems(id='fetconcerns_ac', labelStyle={'color': 'grey', 'margin-right': '40px'},
                    options=[{'label': d_yesno['1'], 'value': 1}, {'label': d_yesno['2'], 'value': 2}],
                    inline=True)])])

fetalconcerns_rr = html.Div(children=
            [html.Div(
                [dbc.RadioItems(id='fetconcerns_ar', labelStyle={'color': 'grey', 'margin-right': '40px'},
                    options=[{'label': d_yesno['1'], 'value': 1}, {'label': d_yesno['2'], 'value': 2}],
                    inline=True)])])


datacovid2 = {'page_src': 'community',
              'datetime_d': '',
              'triageloc_d': '',
              'surname_d': 'Smith',
              'nhs_d': '123 345 1234',
              'dob_d': '30/04/1980',
              'parity_d': '0',
              'edd_d': '21/02/2021',
              'del_d': '2',
              'deldate_d': '01/03/2021',
              'tel_d': '07496 354021',
              'vaccine_d': '2',
              'dose1date_d': '',
              'dose2date_d': '',
              'vactype1_d': '',
              'vactype2_d': '',
              'covidtest_d': '',
              'covidstatus_d': '3',
              'covidswabdate_d': 'Click to enter',
              'covidadmit_d': '',
              'admitdate_d': 'Click to enter',
              'dischdate_d': 'Click to enter',
              'sentences_d': '1',
              'spo2_1': '95',
              'spo2_2': '82',
              'tsym1_d': ['', '1'],
              'tsym2_d': ['2', '3'],
              'tsym3_d': ['', ''],
              'tsym4_d': ['6', ''],
              'risksw1_d': ['0', '1'],
              'risksw2_d': '',
              'risksw3_d': '',
              'risksw4_d': '',
              'risksb1_d': ['0', '1'],
              'risksb2_d': ['2', '3'],
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
              'labour_d': '2',
              'fetconcern_d': '2',
              'fhr_d': '172',
              'risksw1d': '1',
              'risksw2d': '2',
              'risksw3d': '5'}


###################################               Junk Code Unused                ######################################
#
# covxray_q = html.Div(html.P('Chest Xray', className='formlabel'), style={'margin-top': '5%'})
# covctpaq_q = html.Div(html.P('CTPA or Q scan', className='formlabel'), style={'margin-top': '5%'})
# covhdu_q = html.Div(html.P('Critical care', className='formlabel'), style={'margin-top': '5%'})
# covfetus_q = html.Div(html.P('COVID treatment baby', className='formlabel'), style={'margin-top': '5%'})
# covticc_q = html.Div(html.P('Ambulatory pathway - TICC-19', className='formlabel'), style={'margin-top': '5%'})
# covfreetext_q = html.Div(html.P('Other relevant notes', className='formlabel'), style={'margin-top': '5%'})
# covclinassesshide_q = html.Div(html.P('Clinical Assessments', className='formlabel'), style={'visibility': 'hidden'})
#
#
#
#
# test_r = html.Div(children=
#                      [dbc.Input(className='form-control', id='test_a', type='text', maxLength=10,
#                                 placeholder='dd/MM/yyyy')])
#
# nhs_r = html.Div(children=
#                  [dbc.Input(className='form-control', id='nhs_a', type='text', maxLength=4,
#                             placeholder='Last 4 digits')])
#
# doby_r = html.Div(children=
#                   [dcc.DatePickerSingle(id='dob_a', min_date_allowed=dt(1970, 1, 1),
#                                         max_date_allowed=dt(2021, 12, 31), placeholder='Click to enter')])
#
# parity_r = html.Div(children=
#                     [dbc.Input(className='form-control', id='parity_a', type='text', maxLength=2,
#                                placeholder='Maximum 10')])
#
# edd_r = html.Div(
#     children=
#     [dcc.DatePickerSingle(id='edd_a', min_date_allowed=dt(2020, 1, 1),
#                           max_date_allowed=dt(2021, 12, 31), placeholder='Click to enter')],
# )
#
# del_r = html.Div(
#     children=[
#         html.Div([dbc.RadioItems(id='del_a', labelStyle={'color': 'grey', 'margin-right': '25px'},
#                                  options=[{'label': d_yesno['1'], 'value': 1}, {'label': d_yesno['2'], 'value': 2}],
#                                  inline=True)])])
#
# deldate_r = html.Div(children=
#                      [dcc.DatePickerSingle(id='deldate_a', min_date_allowed=dt(2020, 1, 1),
#                                            max_date_allowed=dt(2021, 12, 31), placeholder='Click to enter')])
#
# tel_r = html.Div(children=[dbc.Input(id='tel_a', type='text', maxLength=12, placeholder='07000 123456')])
#
# vac1_r = html.Div(
#     children=[html.Div([dbc.RadioItems(id='vaccine_a', labelStyle={'color': 'grey', 'margin-right': '25px'},
#                                        options=[
#                                            {'label': d_vacc_doses['1'], 'value': 1},
#                                            {'label': d_vacc_doses['2'], 'value': 2},
#                                            {'label': d_vacc_doses['3'], 'value': 3}],
#                                        inline=True)])])
#
# vac1date_r = html.Div(children=[
#     dcc.DatePickerSingle(id='dose1date_a', min_date_allowed=dt(2020, 1, 1),
#                          max_date_allowed=dt(2021, 12, 31), placeholder='Click to enter')])
#
# vac2date_r = html.Div(children=
#                       [dcc.DatePickerSingle(id='dose2date_a', min_date_allowed=dt(2020, 1, 1),
#                                             max_date_allowed=dt(2021, 12, 31), placeholder='Click to enter')])
#
# vacwhich1_r = html.Div(children=[dbc.Checklist(id='vactype1_a', className='checkCustom',
#                                                options=[
#                                                    {'label': d_vacc_typ['0'], 'value': 0},
#                                                    {'label': d_vacc_typ['1'], 'value': 1},
#                                                    {'label': d_vacc_typ['2'], 'value': 2}],
#                                                labelStyle={'color': 'grey', 'text-align': 'left'},
#                                                labelCheckedStyle={'color': '#319997'})])
#
# vacwhich2_r = html.Div(style={'display': 'inline-block', 'transform': 'translate(0, -30%)'},
#                        children=
#                        [dbc.Checklist(id='vactype2_a', options=[{'label': d_vacc_typ['3'], 'value': 3},
#                                                                 {'label': d_vacc_typ['4'], 'value': 4}, ],
#                                       labelStyle={'color': 'grey',
#                                                   'text-align': 'left'})])
#
# covidtest_r = html.Div(children=[html.Div([
#     dbc.RadioItems(id='covidtest_a', labelStyle={'color': 'grey', 'margin-right': '25px'},
#                    options=[
#                        {'label': d_yesno['1'], 'value': 1},
#                        {'label': d_yesno['2'], 'value': 2}],
#                    inline=True)])])
#
# covidstatus_r = html.Div(children=[html.Div(
#     [dbc.RadioItems(id='covidstatus_a', labelStyle={'color': 'grey', 'margin-right': '25px'},
#                     options=[
#                         {'label': d_cov_status['1'], 'value': 1},
#                         {'label': d_cov_status['2'], 'value': 2},
#                         {'label': d_cov_status['3'], 'value': 3}],
#                     inline=True)])])
#
# covswabdate_r = html.Div(children=
#                          [dcc.DatePickerSingle(id='covidswabdate_a',
#                                                min_date_allowed=dt(2020, 1, 1),
#                                                max_date_allowed=dt(2021, 12, 31),
#                                                placeholder='Click to enter')],
#                          )
#
# covadmit_r = html.Div(children=
#                       [html.Div([dbc.RadioItems(id='covidadmit_a', labelStyle={'color': 'grey', 'margin-right': '25px'},
#                                                 options=[
#                                                     {'label': d_yesno['1'], 'value': 1},
#                                                     {'label': d_yesno['2'], 'value': 2}],
#                                                 inline=True)])])
#
# covadmitdate_r = html.Div(children=
#                           [dcc.DatePickerSingle(id='admitdate_a',
#                                                 min_date_allowed=dt(2020, 1, 1),
#                                                 max_date_allowed=dt(2021, 12, 31),
#                                                 placeholder='Click to enter')])
#
# covdischargedate_r = html.Div(children=
#                               [dcc.DatePickerSingle(id='dischdate_a',
#                                                     min_date_allowed=dt(2020, 1, 1),
#                                                     max_date_allowed=dt(2021, 12, 31),
#                                                     placeholder='Click to enter')],
#                               )
#
# sentences_r = html.Div(children=
#                        [html.Div([dbc.RadioItems(id='sentences_a', labelStyle={'color': 'grey', 'margin-right': '40px'},
#                                                  options=[
#                                                      {'label': d_yesno['1'], 'value': 1},
#                                                      {'label': d_yesno['2'], 'value': 2}],
#                                                  inline=True)])])
#
# rwthide_r = html.Div(style={'visibility': 'hidden'},
#                      id='rwt_a',
#                      children=[
#                          html.Div([dbc.Input(id='spo2_1', type='text', maxLength=2, placeholder='Pre SpO2',
#                                              style={'width': '110px'})],
#                                   style={'display': 'inline-block'}),
#                          html.Div([dbc.Input(id='spo2_2', type='text', maxLength=2, placeholder='Post SpO2',
#                                              style={'width': '110px'})],
#                                   style={'right': '0', 'margin-left': '35px', 'margin-right': '0',
#                                          'display': 'inline-block'})])
#
# rwt_r = html.Div(id='rwt_a',
#                  style={'display': 'inline-block', 'transform': 'translate(0, -20%)'},
#                  children=[
#                      html.Div([dbc.Input(id='spo2_1', type='text', maxLength=2, placeholder='Pre SpO2',
#                                          style={'width': '110px'})],
#                               style={'display': 'inline-block'}),
#                      html.Div([dbc.Input(id='spo2_2', type='text', maxLength=2, placeholder='Post SpO2',
#                                          style={'width': '110px'})],
#                               style={'right': '0', 'margin-left': '35px', 'margin-right': '0',
#                                      'display': 'inline-block'})])
#
# tsym1_r = html.Div(children=
#                    [dbc.Checklist(id='tsym1_a',
#                                   options=[{'label': d_symptoms['0'], 'value': 0},
#                                            {'label': d_symptoms['1'], 'value': 1}],
#                                   labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# tsym2_r = html.Div(children=
#                    [dbc.Checklist(id='tsym2_a', options=[{'label': d_symptoms['2'], 'value': 2},
#                                                          {'label': d_symptoms['3'], 'value': 3}],
#                                   labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# tsym3_r = html.Div(children=
#                    [dbc.Checklist(id='tsym3_a', options=[{'label': d_symptoms['4'], 'value': 4},
#                                                          {'label': d_symptoms['5'], 'value': 5}],
#                                   labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# tsym4_r = html.Div(children=
#                    [dbc.Checklist(id='tsym4_a',
#                                   options=[{'label': d_symptoms['6'], 'value': 6}, {'label': d_symptoms['7'], 'value': 7}],
#                                   labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# risksw1_r = html.Div(children=
#                      [dbc.Checklist(id='risksw1_a', options=[{'label': d_risk_woman['0'], 'value': 0},
#                                                              {'label': d_risk_woman['1'], 'value': 1},
#                                                              {'label': d_risk_woman['2'], 'value': 2}],
#                                     labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# risksw2_r = html.Div(children=
#                      [dbc.Checklist(id='risksw2_a', options=[{'label': d_risk_woman['3'], 'value': 3},
#                                                              {'label': d_risk_woman['4'],
#                                                               'value': 4}],
#                                     labelStyle={'color': 'grey', 'text-align': 'left'}), tooltip_diabetes])
#
# risksw3_r = html.Div(children=
#                      [dbc.Checklist(id='risksw3_a',
#                                     options=[{'label': d_risk_woman['5'], 'value': 5},
#                                              {'label': d_risk_woman['6'], 'value': 6},
#                                              {'label': d_risk_woman['7'], 'value': 7}],
#                                     labelStyle={'color': 'grey', 'text-align': 'left'}), tooltip_steroids])
#
# risksw4_r = html.Div(children=
#                      [dbc.Checklist(id='risksw4_a', options=[{'label': d_risk_woman['8'], 'value': 8},
#                                                              {'label': d_risk_woman['9'], 'value': 9},
#                                                              {'label': d_risk_woman['10'], 'value': 10}
#                                                              ],
#                                     labelStyle={'color': 'grey', 'text-align': 'left'}), tooltip_anaemia])
#
# risksb1_r = html.Div(children=
#                      [dbc.Checklist(id='risksb1_a', options=[{'label': d_risk_baby['0'], 'value': 0}],
#                                     labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# risksb2_r = html.Div(children=
#                      [dbc.Checklist(id='risksb2_a', options=[{'label': d_risk_baby['1'], 'value': 1}],
#                                     labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# risksb3_r = html.Div(children=
#                      [dbc.Checklist(id='risksb3_a', options=[{'label': d_risk_baby['2'], 'value': 2}],
#                                     labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# risksb4_r = html.Div(children=
#                      [dbc.Checklist(id='risksb4_a', options=[{'label': d_risk_baby['3'], 'value': 3},
#                                                              {'label': d_risk_baby['4'], 'value': 4}],
#                                     labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# covticc_r = html.Div(children=
# [html.Div(
#     [dbc.RadioItems(id='ticc_a', labelStyle={'color': 'grey', 'margin-right': '40px'},
#                     options=[{'label': d_yesno['1'], 'value': 1}, {'label': d_yesno['2'], 'value': 2}],
#                     inline=True)])],
# )
#
# covxray_r = html.Div(children=
# [html.Div(
#     [dbc.RadioItems(id='cxr_a', labelStyle={'color': 'grey', 'margin-right': '40px'},
#                     options=[{'label': d_yesno['1'], 'value': 1}, {'label': d_yesno['2'], 'value': 2}],
#                     inline=True)])],
# )
#
# covctpaq_r = html.Div(children=
# [html.Div(
#     [dbc.RadioItems(id='ctpa_a', labelStyle={'color': 'grey', 'margin-right': '40px'},
#                     options=[{'label': d_yesno['1'], 'value': 1},
#                              {'label': d_yesno['2'], 'value': 2}],
#                     inline=True)])],
# )
#
# covrxw1_r = html.Div(children=
#                      [dbc.Checklist(id='covrxw1_a', options=[{'label': d_treatment_list['0'], 'value': 0},
#                                                              {'label': d_treatment_list['1'], 'value': 1}],
#                                     labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# covrxw2_r = html.Div(children=
#                      [dbc.Checklist(id='covrxw2_a', options=[{'label': d_treatment_list['2'], 'value': 2},
#                                                              {'label': d_treatment_list['3'], 'value': 3},
#                                                              {'label': d_treatment_list['4'], 'value': 4}],
#                                     labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# covrxw3_r = html.Div(children=
#                      [dbc.Checklist(id='covrxw3_a', options=[{'label': d_treatment_list['5'], 'value': 5},
#                                                              {'label': d_treatment_list['6'], 'value': 6},
#                                                              {'label': d_treatment_list['7'], 'value': 7}],
#                                     labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# covrxw4_r = html.Div(children=
#                      [dbc.Checklist(id='covrxw4_a', options=[{'label': d_treatment_list['8'], 'value': 8},
#                                                              {'label': d_treatment_list['9'], 'value': 9}],
#                                     labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# covfreetext_r = html.Div(children=
#                          dcc.Textarea(id='covtext_a', value='', style={'width': '100%', 'height': '10%'}),
#                          style={'width': '100%', 'height': '10%'})
#
# clin1assess1_r = html.Div(children=
#                           [dbc.Checklist(id='clin1assess1_a', options=[{'label': d_assess_1['0'], 'value': 0}],
#                                          labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# clin1assess2_r = html.Div(children=
#                           [dbc.Checklist(id='clin1assess2_a', options=[{'label': d_assess_1['1'], 'value': 1}],
#                                          labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# clin1assess3_r = html.Div(children=
#                           [dbc.Checklist(id='clin1assess3_a', options=[{'label': d_assess_1['2'], 'value': 2}],
#                                          labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# clin1assess4_r = html.Div(children=
#                           [dbc.Checklist(id='clin1assess4_a',
#                                          options=[{'label': d_assess_1['3'], 'value': 3}],
#                                          labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# clinassess1hide_r = html.Div(
#     style={'visibility': 'hidden'},
#     id='clin1_a',
#     children=[
#         dbc.Checklist(id='clinassess1_a', options=[{'label': 'Chest XRay', 'value': 1}],
#                       labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# clinassess2hide_r = html.Div(
#     style={'display': 'inline-block', 'transform': 'translate(0, -30%)', 'visibility': 'hidden'},
#     id='clin2_a',
#     children=[
#         dbc.Checklist(id='clinassess2_a', options=[{'label': 'CTPA or VQ scan', 'value': 2}],
#                       labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# clinassess3hide_r = html.Div(id='clin3_a',
#                              style={'display': 'inline-block', 'transform': 'translate(0, -30%)',
#                                     'visibility': 'hidden'},
#                              children=[
#                                  dbc.Checklist(id='clinassess3_a', options=[{'label': 'Echocardiogram', 'value': 3}],
#                                                labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# clinassess4hide_r = html.Div(id='clin4_a',
#                              style={'display': 'inline-block', 'transform': 'translate(0, -30%)',
#                                     'visibility': 'hidden'},
#                              children=[
#                                  dbc.Checklist(id='clinassess4_a',
#                                                options=[{'label': 'Growth scan [<14 days ago]', 'value': 4}],
#                                                labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# clin2assess1_r = html.Div(children=
#                           [dbc.Checklist(id='clin2assess1_a', options=[{'label': d_assess_2['0'], 'value': 0},
#                                                                        {'label': d_assess_2['1'], 'value': 1},
#                                                                        {'label': d_assess_2['2'], 'value': 2}],
#                                          labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# clin2assess2_r = html.Div(children=
#                           [dbc.Checklist(id='clin2assess2_a', options=[{'label': d_assess_2['3'], 'value': 3},
#                                                                        {'label': d_assess_2['4'], 'value': 4}],
#                                          labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# clin2assess3_r = html.Div(children=
#                           [dbc.Checklist(id='clin2assess3_a', options=[{'label': d_assess_2['5'], 'value': 5},
#                                                                        {'label': d_assess_2['6'], 'value': 6}],
#                                          labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# clin2assess4_r = html.Div(children=
#                           [dbc.Checklist(id='clin2assess4_a', options=[{'label': d_assess_2['7'], 'value': 7},
#                                                                        {'label': d_assess_2['8'], 'value': 8},
#                                                                        {'label': d_assess_2['9'], 'value': 9}],
#                                          labelStyle={'color': 'grey', 'text-align': 'left'})])
#
# labour_r = html.Div(children=
# [html.Div(
#     [dbc.RadioItems(id='labour_a', labelStyle={'color': 'grey', 'margin-right': '40px'},
#                     options=[{'label': d_yesno['1'], 'value': 1}, {'label': d_yesno['2'], 'value': 2}],
#                     inline=True)])],
# )
#
# fetalconcerns_r = html.Div(children=
# [html.Div(
#     [dbc.RadioItems(id='fetconcerns_a', labelStyle={'color': 'grey', 'margin-right': '40px'},
#                     options=[{'label': d_yesno['1'], 'value': 1}, {'label': d_yesno['2'], 'value': 2}],
#                     inline=True)])])
#
# fhr_r = html.Div(children=
#                  [dbc.Input(className='form-control', id='fhr_a', type='text', maxLength=3,
#                             placeholder='FHR - bpm')])
#
# vaccine = ['No', 'One dose', 'Two doses']
# vactype_list = ['Pfizer', 'Oxford - AZ', 'Moederna', 'Other']
# symptom_list = ['None', 'Temp \u226537.8', 'Shortness of breath', 'Dry cough', 'Chest pain', 'Loss of smell/ taste',
#                 'GI disturbance', 'Skin rash']
# risks_woman_list = ['None', 'Ethnicity - Black or Asian origin', 'BMI \u226530', 'Hypertension [PIH/PET or Essential]',
#                     'Diabetes [Type 1 or 2]',
#                     'Kidney or inflammatory bowel disease', 'Uses oral steroids or Biologics', 'Transplant recipient',
#                     'HIV or other immunuosuppressed', 'Anaemia [Hb<105]'
#                     ]
# risks_baby_list = ['None', 'Reduced fetal movements', 'Known SGA', 'Other']
# treatments_list = ['None', 'Prednisolone', 'Tocilizumab', 'Remdesivir', 'Aspirin', 'LMWH - Tinzaparin', 'Vitamin D',
#                    'Iron', 'Dexamethsaone - baby', 'Magnesium sulphate - baby']
# assessments1_list = ['CXR', 'CPTA/VQ scan', 'ECHO', 'Obstetric scan - growth']
# assessments2_list = ['CXR - normal', 'CXR - abnormal', 'ECHO - normal', 'ECHO - abnormal', 'Growth - normal',
#                      'Growth - SGA; normal Doppler', 'Growth - SGA; abnormal Doppler']
