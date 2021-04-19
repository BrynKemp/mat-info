from callbacks import *
from navbar import navbar_comp
import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas
import datetime
import time
from datetime import datetime, timedelta
from dash.dependencies import Input, Output, ClientsideFunction
from flask_app import flask_app
from apps.codebank import *
from datatemplates import *
from qbank import *
# from apps.home import gen_sidebar
from callbacks import *
import json


#############################################    Local Functions   #####################################################
def tri_community():
    return html.Div(
        id='tri_community',
        style={'position': 'relative', 'float': 'center', 'border': '3px solid #319997', 'border-radius': '6px',
               'margin': '0.25%', 'padding': '1%', 'width': '100%', 'margin-bottom': '2vH'},
        children=[
            html.Div(id='comm_filled', style={'display': 'none'}),
            html.Div(children=[dbc.Input(id='data_com', type='text', value='')], style={'display': 'none'}),
            html.Div([
                html.H6('COVID Triage - Community', style={'font-weight': '600'}),
            ]),
            html.Br(),
            html.Div(
                style={},
                children=[
                    html.Div([
                        html.H5('Pregnancy - Demographics', style={'font-weight': 'bold'}),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Row([
                            # Q1
                            dbc.Col(surname_qc, width=1),
                            dbc.Col(surname_rc, width=1),
                            dbc.Col(html.P(), width=1),
                            # Q2
                            dbc.Col(nhs_qc, width=1),
                            dbc.Col(nhs_rc, width=1),
                            dbc.Col(html.P(), width=1),
                            # Q3
                            dbc.Col(doby_qc, width=1),
                            dbc.Col(doby_rc, width=1),
                            dbc.Col(html.P(), width=1),
                            # Q4
                            dbc.Col(parity_qc, width=1),
                            dbc.Col(parity_rc, width=2),
                        ]),
                        html.Br(),
                        dbc.Row([
                            # Q5
                            dbc.Col(del_qc, width=1),
                            dbc.Col(del_rc, width=2),
                            # Q6
                            dbc.Col(edd_qc, width=1),
                            dbc.Col(edd_rc, width=1),
                            dbc.Col(html.P(), width=1),
                            # Q7
                            dbc.Col(deldate_qc, width=1),
                            dbc.Col(deldate_rc, width=2),
                            # Q7
                            dbc.Col(tel_qc, width=1),
                            dbc.Col(tel_rc, width=2),
                        ])], style={'border': '1px solid #319997', 'border-radius': '6px', 'padding': '0.5%',
                                    'padding-bottom': '20px'}),

                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        html.H5('COVID - Test Status', style={'font-weight': 'bold'}),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Row([
                            # Q9
                            dbc.Col(vacc_qc, width=1),
                            dbc.Col(vacc_rc, width=2),
                            # Q10
                            dbc.Col(vacwhich_qc, width=1),
                            dbc.Col(vacwhich1_rc, width=1),
                            dbc.Col(vacwhich2_rc, width=1),
                            # Q11
                            dbc.Col(vac1date_qc, width=1),
                            dbc.Col(vac1date_rc, width=2),
                            # Q12
                            dbc.Col(vac2date_qc, width=1),
                            dbc.Col(vac2date_rc, width=2),

                        ]),
                        html.Br(),
                        dbc.Row([
                            # Q13
                            dbc.Col(covidtest_qc, width=1),
                            dbc.Col(covidtest_rc, width=2),
                            # Q14
                            dbc.Col(covidstatus_qc, width=1),
                            dbc.Col(covidstatus_rc, width=2),
                            # Q15
                            dbc.Col(covswabdate_qc, width=1),
                            dbc.Col(covswabdate_rc, width=2),

                        ]),
                        html.Br(),
                        dbc.Row([
                            # Q16
                            dbc.Col(covadmit_qc, width=1),
                            dbc.Col(covadmit_rc, width=2),
                            # Q17
                            dbc.Col(covadmitdate_qc, width=1),
                            dbc.Col(covadmitdate_rc, width=2),
                            # Q18
                            dbc.Col(covdischargedate_qc, width=1),
                            dbc.Col(covdischargedate_rc, width=2),
                        ]),
                        html.Br(),
                        html.Br(),

                    ], style={'border': '1px solid #319997', 'border-radius': '6px', 'padding': '0.5%',
                              'padding-bottom': '20px'}),
                ]),
            ### Row ###
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div(
                style={},
                children=[
                    html.Div([
                        html.H5('COVID - Clinical Assessment', style={'font-weight': 'bold'}),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Row([
                            # Q19
                            dbc.Col(sentences_qc, width=2),
                            dbc.Col(sentences_rc, width=2),
                            dbc.Col(rwt_qc, width=1),
                            dbc.Col(rwt_rc, width=4),
                        ]),
                        html.Br(),
                        dbc.Row([
                            # Q20
                            dbc.Col(covsymp_qc, width=2),
                            dbc.Col(tsym1_rc, width=2),
                            dbc.Col(tsym2_rc, width=2),
                            # 21
                            dbc.Col(tsym3_rc, width=2),
                            # 22
                            dbc.Col(tsym4_rc, width=2),
                        ]),
                        ### Row ###
                        html.Br(),
                        dbc.Row([
                            dbc.Col(covrisksw_qc, width=2),
                            dbc.Col(risksw1_rc, width=2),
                            # Q24
                            dbc.Col(risksw2_rc, width=2),
                            # Q25
                            dbc.Col(risksw3_rc, width=2),
                            # Q26
                            dbc.Col(risksw4_rc, width=2),
                        ]),
                        html.Br(),
                        ### Row ###
                        dbc.Row([
                            dbc.Col(covrisksb_qc, width=2),
                            # Q27
                            dbc.Col(risksb1_rc, width=2),
                            # Q28
                            dbc.Col(risksb2_rc, width=2),
                            # Q29
                            dbc.Col(risksb3_rc, width=2),
                            # Q30
                            dbc.Col(risksb4_rc, width=2),
                        ]),
                        html.Br(),
                        ### Row ###
                        dbc.Row([
                            # Q31
                            dbc.Col(covrx_qc, width=2),
                            dbc.Col(covrxw1_rc, width=2),
                            # Q32
                            dbc.Col(covrxw2_rc, width=2),
                            # Q33
                            dbc.Col(covrxw3_rc, width=2),
                            # Q34
                            dbc.Col(covrxw4_rc, width=2),
                        ]),
                        html.Br(),
                        ### Row ###
                        dbc.Row([
                            dbc.Col(covclinassess_qc, width=2),
                            # Q27
                            dbc.Col(clin1assess1_rc, width=2),
                            # Q28
                            dbc.Col(clin1assess2_rc, width=2),
                            # Q29
                            dbc.Col(clin1assess3_rc, width=2),
                            # Q30
                            dbc.Col(clin1assess4_rc, width=2)
                        ]),
                        html.Br(),

                        dbc.Row([
                            dbc.Col(labour_qc, width=2),
                            # Q27
                            dbc.Col(labour_rc, width=2),
                            dbc.Col(fetalconcerns_qc, width=2),
                            # Q29
                            dbc.Col(fetalconcerns_rc, width=2),
                        ]),

                        html.Br(),
                        dbc.Row([
                            dbc.Col(fetalheart_qc, width=2),
                            # Q30
                            dbc.Col(fhr_rc, width=2),
                        ]),
                        ### Row ###
                        #    dbc.Col(covfreetext_qc, width=2),
                        # ]),
                        # dbc.Row([
                        #    dbc.Col(covfreetext_rc, width=10),

                        # ]),

                    ], style={'border': '1px solid #319997', 'border-radius': '6px', 'padding': '0.5%',
                              'padding-bottom': '20px'}),

                    html.Br(),
                    html.Div(children=[
                        html.Div([html.Button(id='communitytriage_btn_confirm', children='Confirm', n_clicks=0)],
                                 style={'margin-right': '10px', 'display': 'inline-block'}),
                        # html.Div([html.A(html.Button(id='communitytriage_btn_confirm', children='Confirm', n_clicks=0),
                        #                  href='/experiment')],
                        #          style={'margin-right': '10px', 'display': 'inline-block'}),
                        html.Div([html.Button(id='communitytriage_btn_cancel', children='Cancel', n_clicks=0)],
                                 style={'display': 'inline-block'})])

                ])
        ])


############################################      Callback Page    #####################################################

@flask_app.callback([Output('session', 'data'),
              Output('url', 'pathname')],
              [Input('communitytriage_btn_confirm', 'n_clicks')],
              [State('surname_ac', 'value'),
               State('nhs_ac', 'value'),
               State('dob_ac', 'value'),
               # # # # # # 4
               State('parity_ac', 'value'),
               State('del_ac', 'value'),
               State('edd_ac', 'value'),
               State('deldate_ac', 'value'),
               # # # # # 8
               State('tel_ac', 'value'),
               State('vaccine_ac', 'value'),
               State('vactype1_ac', 'value'),
               State('vactype2_ac', 'value'),
               State('dose1date_ac', 'value'),
               # # # # # 13
               State('dose2date_ac', 'value'),
               State('covidtest_ac', 'value'),
               State('covidstatus_ac', 'value'),
               State('covidswabdate_ac', 'value'),
               # # # # # 17
               State('covidadmit_ac', 'value'),
               State('covidadmitdate_ac', 'value'),
               State('coviddischdate_ac', 'value'),
               # # # # # 20
               State('sentences_ac', 'value'),
               State('spo2_1ac', 'value'),
               State('spo2_2ac', 'value'),
               # # # # 23
               State('tsym1_ac', 'value'),
               State('tsym1_ac', 'value'),
               State('tsym3_ac', 'value'),
               State('tsym4_ac', 'value'),
               # # # # 30
               State('risksw1_ac', 'value'),
               State('risksw2_ac', 'value'),
               State('risksw3_ac', 'value'),
               State('risksw4_ac', 'value'),

               State('risksb1_ac', 'value'),
               State('risksb2_ac', 'value'),
               State('risksb3_ac', 'value'),
               State('risksb4_ac', 'value'),
               # # # # 34
               State('covrxw1_ac', 'value'),
               State('covrxw2_ac', 'value'),
               State('covrxw3_ac', 'value'),
               State('covrxw4_ac', 'value'),
               # # # 38
               State('clin1assess1_ac', 'value'),
               State('clin1assess2_ac', 'value'),
               State('clin1assess3_ac', 'value'),
               State('clin1assess4_ac', 'value'),
               # # # 40
               State('labour_ac', 'value'),
               State('fetconcerns_ac', 'value'),
               State('fhr_ac', 'value'),
               ], prevent_initial_call=False)
def grabData(btn_confirm, surname_ac, nhs_ac, doby_ac, parity_ac, del_ac, edd_ac, deldate_ac, tel_ac, vacc_ac, vactype1_ac,
             vactype2_ac, dose1date_ac, dose2date_ac, covidtest_ac, covidstatus_ac, covidswabdate_ac, covidadmit_ac,
             covidadmitdate_ac, coviddischdate_ac, sentences_ac, spo2_1ac, spo2_2ac, tsym1_ac, tsym2_ac, tsym3_ac,
             tsym4_ac, risksw1_ac, risksw2_ac, risksw3_ac, risksw4_ac, risksb1_ac, risksb2_ac, risksb3_ac, risksb4_ac,
             covrxw1_ac, covrxw2_ac, covrxw3_ac, covrxw4_ac, clin1assess1_ac, clin1assess2_ac, clin1assess3_ac,
             clin1assess4_ac, labour_ac, fetconcerns_ac, fhr_ac):

    ctx1 = dash.callback_context
    if not ctx1.triggered:
        input_id = 'No clicks yet'
    else:
        input_id = ctx1.triggered[0]['prop_id'].split('.')[0]

    if input_id == 'communitytriage_btn_confirm':
        create_str = datetime.datetime.now()
        sbar_str = create_str.strftime('%d-%b-%Y, %H:%M')
        tempcomdata = datacovid2
        tempcomdata['datetime_d'] = str(sbar_str)
        tempcomdata['triageloc_d'] = str('community')

        if surname_ac:
            tempcomdata['surname_d'] = surname_ac
        if nhs_ac:
            tempcomdata['nhs_d'] = nhs_ac
        if doby_ac:
            tempcomdata['doby_d'] = doby_ac
        if parity_ac:
            tempcomdata['parity_d'] = parity_ac
        if edd_ac:
            tempcomdata['edd_d'] = edd_ac
        if del_ac:
            tempcomdata['del_d'] = del_ac
        if deldate_ac:
            tempcomdata['deldate_d'] = deldate_ac
        if tel_ac:
            tempcomdata['tel_d'] = tel_ac
        if vacc_ac:
            tempcomdata['vaccine_d'] = vacc_ac
        if dose1date_ac:
            tempcomdata['dose1date_d'] = dose1date_ac
        if dose2date_ac:
            tempcomdata['dose2date_d'] = dose2date_ac
        if vactype1_ac:
            tempcomdata['vactype1_d'] = vactype1_ac
        if vactype1_ac:
            tempcomdata['vactype2_d'] = vactype1_ac
        if covidtest_ac:
            tempcomdata['covidtest_d'] = covidtest_ac
        if covidstatus_ac:
            tempcomdata['covidstatus_d'] = covidstatus_ac
        if covidswabdate_ac:
            tempcomdata['covidswabdate_d'] = covidswabdate_ac
        if covidadmit_ac:
            tempcomdata['covidadmit_d'] = covidadmit_ac
        if covidadmitdate_ac:
            tempcomdata['admitdate_d'] = covidadmitdate_ac
        if coviddischdate_ac:
            tempcomdata['dischdate_d'] = coviddischdate_ac
        if sentences_ac:
            tempcomdata['sentences_d'] = sentences_ac
        if spo2_1ac:
            tempcomdata['spo2_1'] = spo2_1ac
        if spo2_2ac:
            tempcomdata['spo2_2'] = spo2_2ac
        if tsym1_ac:
            tempcomdata['tsym1_d'] = tsym1_ac
        if tsym2_ac:
            tempcomdata['tsym2_d'] = tsym2_ac
        if tsym3_ac:
            tempcomdata['tsym3_d'] = tsym3_ac
        if tsym4_ac:
            tempcomdata['tsym4_d'] = tsym4_ac
        if risksw1_ac:
            tempcomdata['risksw1_d'] = risksw1_ac
        if risksw2_ac:
            tempcomdata['risksw2_d'] = risksw2_ac
        if risksw3_ac:
            tempcomdata['risksw3_d'] = risksw3_ac
        if risksw4_ac:
            tempcomdata['risksw4_d'] = risksw4_ac
        if risksb1_ac:
            tempcomdata['risksb1_d'] = risksb1_ac
        if risksb2_ac:
            tempcomdata['risksb2_d'] = risksb2_ac
        if risksb3_ac:
            tempcomdata['risksb3_d'] = risksb3_ac
        if risksb4_ac:
            tempcomdata['risksb4_d'] = risksb4_ac
        if clin1assess1_ac:
            tempcomdata['clin1assess1_d'] = clin1assess1_ac
        if clin1assess2_ac:
            tempcomdata['clin1assess2_d'] = clin1assess2_ac
        if clin1assess3_ac:
            tempcomdata['clin1assess3_d'] = clin1assess3_ac
        if clin1assess4_ac:
            tempcomdata['clin1assess4_d'] = clin1assess4_ac
        if covrxw1_ac:
            tempcomdata['covrxw1_d'] = covrxw1_ac
        if covrxw2_ac:
            tempcomdata['covrxw2_d'] = covrxw2_ac
        if covrxw3_ac:
            tempcomdata['covrxw3_d'] = covrxw3_ac
        if covrxw4_ac:
            tempcomdata['covrxw4_d'] = covrxw4_ac
        if clin1assess4_ac:
            tempcomdata['clin1assess4_d'] = clin1assess4_ac
        if clin1assess4_ac:
            tempcomdata['clin1assess4_d'] = clin1assess4_ac
        if clin1assess4_ac:
            tempcomdata['clin1assess4_d'] = clin1assess4_ac
        if labour_ac:
            tempcomdata['labour_d'] = labour_ac
        if fetconcerns_ac:
            tempcomdata['fetconcern_d'] = fetconcerns_ac
        if fhr_ac:
            tempcomdata['fhr_d'] = fhr_ac

        # tempcomdata = {
        #     'page_src': 'community',
        #     'datetime_d': sbar_str,
        #     'triageloc_d': 'community',
        #     'surname_d': surname_ac,
        #     'nhs_d': nhs_ac,
        #     'dob_d': doby_ac,
        #     'parity_d': parity_ac,
        #     'edd_d': edd_ac,
        #     'del_d': del_ac,
        #     'deldate_d': deldate_ac,
        #     'tel_d': tel_ac,
        #     'vaccine_d': vacc_ac,
        #     'dose1date_d': dose1date_ac,
        #     'dose2date_d': dose2date_ac,
        #     'vactype1_d': vactype1_ac,
        #     'vactype2_d': vactype2_ac,
        #     'covidtest_d': covidtest_ac,
        #     'covidstatus_d': covidstatus_ac,
        #     'covidswabdate_d': covidswabdate_ac,
        #     'covidadmit_d': covidadmit_ac,
        #     'admitdate_d': covidadmitdate_ac,
        #     'dischdate_d': coviddischdate_ac,
        #     'sentences_d': sentences_ac,
        #     'spo2_1': spo2_1ac,
        #     'spo2_2': spo2_2ac,
        #     'tsym1_d': tsym1_ac,
        #     'tsym2_d': tsym2_ac,
        #     'tsym3_d': tsym3_ac,
        #     'tsym4_d': tsym4_ac,
        #     'risksw1_d': risksw1_ac,
        #     'risksw2_d': risksw2_ac,
        #     'risksw3_d': risksw3_ac,
        #     'risksw4_d': risksw4_ac,
        #     'risksb1_d': risksb1_ac,
        #     'risksb2_d': risksb2_ac,
        #     'risksb3_d': risksb3_ac,
        #     'risksb4_d': risksb4_ac,
        #     'clin1assess1_d': clin1assess1_ac,
        #     'clin1assess2_d': clin1assess2_ac,
        #     'clin1assess3_d': clin1assess3_ac,
        #     'clin1assess4_d': clin1assess4_ac,
        #     'clin2assess1_d': '',
        #     'clin2assess2_d': '',
        #     'clin2assess3_d': '',
        #     'clin2assess4_d': '',
        #     'covrxw1_d': covrxw1_ac,
        #     'covrxw2_d': covrxw2_ac,
        #     'covrxw3_d': covrxw3_ac,
        #     'covrxw4_d': covrxw4_ac,
        #     'labour_d': labour_ac,
        #     'fetconcern_d': fetconcerns_ac,
        #     'fhr_d': fhr_ac}
        pathname = '/experiment'
        return tempcomdata, pathname


#############################################      Layout Div      #####################################################

# Banner
banner = banner_nosplash

# Left column
left_bar = html.Div(
    id="left-column",
    className="two columns",
    style={'position': 'absolute', 'background-color': '#f3fffe', 'left': 0, 'padding-left': '50px',
           'top': '6.275vH', 'height': '93.725vH', 'overflow': 'hidden'},
    children=[
        html.Div(
            id="s_1",
            style={'position': 'absolute', 'width': '100%', 'justify-content': 'center',
                   'padding-left': '7.5%', 'right': '0'},
            children=[]
        ),

    ])

# Right column
layout = html.Div(
    id="right-column",
    className="ten columns",
    style={'position': 'absolute', 'background-color': '#f3fffe', 'left': '12.5%', 'padding': '1.55%',
           'width': '87.5%', 'height': '93.75vH', 'top': '8vH', 'flex-direction': 'column', 'overflow': 'auto'},
    children=[
        html.Div(
            id="home_i_1",
            style={'top': '0'},
            children=[]
        ),
        html.Div(
            id="home_i_2",
            style={'position': 'relative', 'top': '15%', 'bottom': '10%', 'width': '100%',
                   'justify-content': 'center',
                   'left': 'auto', 'right': '5%'},
            children=[html.Div(
                children=[

                ],
            )],
        ),
        html.Div(
            id="home_i_3",
            style={'position': 'relative', 'width': '100%', 'justify-content': 'center',
                   'left': '0', 'right': '0', 'top': 0, 'bottom': 10},
            children=[tri_community()]
        )])

#############################################      Layout Div      #####################################################

flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt = document.getElementById("dob_ac").value;
    tempclass = document.getElementById("dob_ac").className;
    regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
    var test = (regex_date.test(var_txt)) ?
        "yes" : "no";
    if (test=="yes" && var_txt !=0){
            var year  = 60 * 60 * 24/ 365.25;
            var currentTime = new Date();
            var st = inputValue;
            var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
            var dt = new Date(st.replace(pattern,'$3-$2-$1'));
            var delta = (currentTime - dt);
            var deltad = delta/(60*60*24*1000*365.25);
            console.log(deltad)
            if (deltad<13){
                document.getElementById("dob_ac").className ="is-valid2 form-control";
                return;
            }
            if (deltad>=13){
                document.getElementById("dob_ac").className ="is-valid form-control";
                return;
            }
        }     
    if (test=="no"&& var_txt !=0){
            document.getElementById("dob_ac").className = "is-invalid form-control";
            return;
        }
    if (var_txt ==''){
           document.getElementById("dob_ac").className = "is-neutral form-control";
           return;
        }
    }
    """,
    Output('dob_ac', 'children'),
    Input('dob_ac', 'value'),
)

#############################################    Local Functions   #####################################################

flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt = document.getElementById("edd_ac").value;
    tempclass = document.getElementById("edd_ac").className;
    regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
    var test = (regex_date.test(var_txt)) ?
        "yes" : "no";
    if (test=="yes" && var_txt !=0){
            var year  = 60 * 60 * 24/ 365.25;
            var currentTime = new Date();
            var st = inputValue;
            var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
            var dt = new Date(st.replace(pattern,'$3-$2-$1'));
            var delta = (currentTime - dt);
            var deltad = delta/(60*60*24*1000);
            console.log(deltad)
            if (deltad<16){
                document.getElementById("edd_ac").className ="is-valid form-control";
                return;
            }
            if (deltad>=16){
                document.getElementById("edd_ac").className ="is-valid2 form-control";
                return;
            }
        }
    if (test=="no"&& var_txt !=0){
            document.getElementById("edd_ac").className = "is-invalid form-control";
            return;
        }
    if (var_txt ==''){
           document.getElementById("edd_ac").className = "is-neutral form-control";
           return;
        }
    }
    """,
    Output('edd_ac', 'children'),
    Input('edd_ac', 'value'),
)

#############################################    Local Functions   #####################################################

flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt = document.getElementById("deldate_ac").value;
    tempclass = document.getElementById("deldate_ac").className;
    regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
    var test = (regex_date.test(var_txt)) ?
        "yes" : "no";
    if (test=="yes" && var_txt !=0){
            var year  = 60 * 60 * 24/ 365.25;
            var currentTime = new Date();
            var st = inputValue;
            var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
            var dt = new Date(st.replace(pattern,'$3-$2-$1'));
            var delta = (currentTime - dt);
            var deltad = delta/(60*60*24*1000);
            console.log(deltad)
            if (deltad>=0){
                document.getElementById("deldate_ac").className ="is-valid form-control";
                return;
            }
            if (deltad<0){
                document.getElementById("deldate_ac").className ="is-valid2 form-control";
                return;
            }
        }
    if (test=="no"&& var_txt !=0){
            document.getElementById("deldate_ac").className = "is-invalid form-control";
            return;
        }
    if (var_txt ==''){
           document.getElementById("deldate_ac").className = "is-neutral form-control";
           return;
        }
    }
    """,
    Output('deldate_ac', 'children'),
    Input('deldate_ac', 'value'),
)

#############################################    Local Functions   #####################################################

flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt = document.getElementById("dose1date_ac").value;
    tempclass = document.getElementById("dose1date_ac").className;
    regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
    var test = (regex_date.test(var_txt)) ?
        "yes" : "no";
    if (test=="yes" && var_txt !=0){
            var year  = 60 * 60 * 24/ 365.25;
            var currentTime = new Date();
            var st = inputValue;
            var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
            var dt = new Date(st.replace(pattern,'$3-$2-$1'));
            var delta = (currentTime - dt);
            var deltad = delta/(60*60*24*1000);
            console.log(deltad)
            if (deltad>=0){
                document.getElementById("dose1date_ac").className ="is-valid form-control";
                return;
            }
            if (deltad<0){
                document.getElementById("dose1date_ac").className ="is-valid2 form-control";
                return;
            }
        }
    if (test=="no"&& var_txt !=0){
            document.getElementById("dose1date_ac").className = "is-invalid form-control";
            return;
        }
    if (var_txt ==''){
           document.getElementById("dose1date_ac").className = "is-neutral form-control";
           return;
        }
    }
    """,
    Output('dose1date_ac', 'children'),
    Input('dose1date_ac', 'value'),
)

#############################################    Local Functions   #####################################################

flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt = document.getElementById("dose2date_ac").value;
    tempclass = document.getElementById("dose2date_ac").className;
    regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
    var test = (regex_date.test(var_txt)) ?
        "yes" : "no";
    if (test=="yes" && var_txt !=0){
            var year  = 60 * 60 * 24/ 365.25;
            var currentTime = new Date();
            var st = inputValue;
            var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
            var dt = new Date(st.replace(pattern,'$3-$2-$1'));
            var delta = (currentTime - dt);
            var deltad = delta/(60*60*24*1000);
            console.log(deltad)
            if (deltad>=0){
                document.getElementById("dose2date_ac").className ="is-valid form-control";
                return;
            }
            if (deltad<0){
                document.getElementById("dose2date_ac").className ="is-valid2 form-control";
                return;
            }
        }
    if (test=="no"&& var_txt !=0){
            document.getElementById("dose2date_ac").className = "is-invalid form-control";
            return;
        }
    if (var_txt ==''){
           document.getElementById("dose2date_ac").className = "is-neutral form-control";
           return;
        }
    }
    """,
    Output('dose2date_ac', 'children'),
    Input('dose2date_ac', 'value'),
)
#############################################    Local Functions   #####################################################

flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt = document.getElementById("covidswabdate_ac").value;
    tempclass = document.getElementById("covidswabdate_ac").className;
    regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
    var test = (regex_date.test(var_txt)) ?
        "yes" : "no";
    if (test=="yes" && var_txt !=0){
            var year  = 60 * 60 * 24/ 365.25;
            var currentTime = new Date();
            var st = inputValue;
            var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
            var dt = new Date(st.replace(pattern,'$3-$2-$1'));
            var delta = (currentTime - dt);
            var deltad = delta/(60*60*24*1000);
            console.log(deltad)
            if (deltad>=0){
                document.getElementById("covidswabdate_ac").className ="is-valid form-control";
                return;
            }
            if (deltad<0){
                document.getElementById("covidswabdate_ac").className ="is-valid2 form-control";
                return;
            }
        }
    if (test=="no"&& var_txt !=0){
            document.getElementById("covidswabdate_ac").className = "is-invalid form-control";
            return;
        }
    if (var_txt ==''){
           document.getElementById("covidswabdate_ac").className = "is-neutral form-control";
           return;
        }
    }
    """,
    Output('covidswabdate_ac', 'children'),
    Input('covidswabdate_ac', 'value'),
)
#############################################    Local Functions   #####################################################

flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt = document.getElementById("covidadmitdate_ac").value;
    tempclass = document.getElementById("covidadmitdate_ac").className;
    regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
    var test = (regex_date.test(var_txt)) ?
        "yes" : "no";
    if (test=="yes" && var_txt !=0){
            var year  = 60 * 60 * 24/ 365.25;
            var currentTime = new Date();
            var st = inputValue;
            var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
            var dt = new Date(st.replace(pattern,'$3-$2-$1'));
            var delta = (currentTime - dt);
            var deltad = delta/(60*60*24*1000);
            console.log(deltad)
            if (deltad>=0){
                document.getElementById("covidadmitdate_ac").className ="is-valid form-control";
                return;
            }
            if (deltad<0){
                document.getElementById("covidadmitdate_ac").className ="is-valid2 form-control";
                return;
            }
        }
    if (test=="no"&& var_txt !=0){
            document.getElementById("covidadmitdate_ac").className = "is-invalid form-control";
            return;
        }
    if (var_txt ==''){
           document.getElementById("covidadmitdate_ac").className = "is-neutral form-control";
           return;
        }
    }
    """,
    Output('covidadmitdate_ac', 'children'),
    Input('covidadmitdate_ac', 'value'),
)

flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt = document.getElementById("coviddischdate_ac").value;
    tempclass = document.getElementById("coviddischdate_ac").className;
    regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
    var test = (regex_date.test(var_txt)) ?
        "yes" : "no";
    if (test=="yes" && var_txt !=0){
            var year  = 60 * 60 * 24/ 365.25;
            var currentTime = new Date();
            var st = inputValue;
            var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
            var dt = new Date(st.replace(pattern,'$3-$2-$1'));
            var delta = (currentTime - dt);
            var deltad = delta/(60*60*24*1000);
            console.log(deltad)
            if (deltad>=0){
                document.getElementById("coviddischdate_ac").className ="is-valid form-control";
                return;
            }
            if (deltad<0){
                document.getElementById("coviddischdate_ac").className ="is-valid2 form-control";
                return;
            }
        }
    if (test=="no"&& var_txt !=0){
            document.getElementById("coviddischdate_ac").className = "is-invalid form-control";
            return;
        }
    if (var_txt ==''){
           document.getElementById("coviddischdate_ac").className = "is-neutral form-control";
           return;
        }
    }
    """,
    Output('coviddischdate_ac', 'children'),
    Input('coviddischdate_ac', 'value'),
)

#############################################    Local Functions   #####################################################

flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt = document.getElementById("nhs_ac").value;
    tempclass = document.getElementById("nhs_ac").className;
    regex_num = /^[0-9\s]{12}$/
    if (var_txt=='') {
    document.getElementById("nhs_ac").className ="is-neutral form-control"
    return;
    } 
    var test = (regex_num.test(var_txt)) ?
       document.getElementById("nhs_ac").className ="is-valid form-control" : document.getElementById("nhs_ac").className ="is-invalid form-control";
    }
    """,
    Output('nhs_ac', 'children'),
    Input('nhs_ac', 'value'),
)

flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt = document.getElementById("tel_ac").value;
    tempclass = document.getElementById("tel_ac").className;
    regex_telnum = /^(\+44\s?7\d{3}|\(?07\d{3}\)?)\s?\d{3}\s?\d{3}$/
    if (var_txt=='') {
    document.getElementById("tel_ac").className ="is-neutral form-control"
    return;
    } 
    var test = (regex_telnum.test(var_txt)) ?
       document.getElementById("tel_ac").className ="is-valid form-control" : document.getElementById("tel_ac").className ="is-invalid form-control";
    }
    """,
    Output('tel_ac', 'children'),
    Input('tel_ac', 'value'),
)

flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt = document.getElementById("parity_ac").value;
    tempclass = document.getElementById("parity_ac").className;
    regex_num = /^[0-9]{1}$/
    if (var_txt=='') {
    document.getElementById("parity_ac").className ="is-neutral form-control"
    return;
    } 
    var test = (regex_num.test(var_txt)) ?
       document.getElementById("parity_ac").className ="is-valid form-control" : document.getElementById("parity_ac").className ="is-invalid form-control";
    }
    """,
    Output('parity_ac', 'children'),
    Input('parity_ac', 'value'),
)

flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt1 = document.getElementById("spo2_1ac").value;
    tempclass = document.getElementById("spo2_1ac").className;
    regex_num = /^[0-9]{2}$/
    if (var_txt=='') {
    document.getElementById("spo2_1ac").className ="is-neutral form-control"
    return;
    } 
    var test1 = (regex_num.test(var_txt1)) ?
       document.getElementById("spo2_1ac").className ="is-valid form-control" : document.getElementById("spo2_1ac").className ="is-invalid form-control";
    }
    """,
    Output('spo2_1ac', 'children'),
    Input('spo2_1ac', 'value'),
)
flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt1 = document.getElementById("spo2_2ac").value;
    tempclass = document.getElementById("spo2_2ac").className;
    if (var_txt=='') {
    document.getElementById("spo2_2ac").className ="is-neutral form-control"
    return;
    } 
    regex_num = /^[0-9]{2}$/
    var test1 = (regex_num.test(var_txt1)) ?
       document.getElementById("spo2_2ac").className ="is-valid form-control" : document.getElementById("spo2_2ac").className ="is-invalid form-control";
    }
    """,
    Output('spo2_2ac', 'children'),
    Input('spo2_2ac', 'value'),
)

flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt = document.getElementById("fhr_ac").value;
    tempclass = document.getElementById("fhr_ac").className;
    regex_num = /^[0-9]{3}$/
    if (var_txt=='') {
    document.getElementById("fhr_ac").className ="is-neutral form-control"
    return;
    } 
    var test = (regex_num.test(var_txt)) ?
       document.getElementById("fhr_ac").className ="is-valid form-control" : document.getElementById("fhr_ac").className ="is-invalid form-control";
    }
    """,
    Output('fhr_ac', 'children'),
    Input('fhr_ac', 'value'),
)

flask_app.clientside_callback(
    """
    function(inputValue){
    var_txt = document.getElementById("surname_ac").value;
    tempclass = document.getElementById("surname_ac").className;
    regex_num = /^[a-zA-Z]+$/
    if (var_txt=='') {
    document.getElementById("surname_ac").className ="is-neutral form-control"
    return;
    } 
    var test = (regex_num.test(var_txt)) ?
       document.getElementById("surname_ac").className ="is-valid form-control" : document.getElementById("surname_ac").className ="is-invalid form-control";
    }
    """,
    Output('surname_ac', 'children'),
    Input('surname_ac', 'value'),
)
