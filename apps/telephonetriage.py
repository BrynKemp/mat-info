from navbar import navbar_comp
from apps.codebank import *
from qbank import *
from apps.codebank import *
from apps.home import gen_sidebar

from navbar import navbar_comp
from qbank import *
from apps.codebank import *
from apps.home import gen_sidebar
from dash.dependencies import Input, Output, ClientsideFunction
from flask_app import flask_app

#############################################    Local Functions   #####################################################

def tri_telephone():
    return html.Div(
        id='tri_telephone',
        style={'position': 'relative', 'float': 'center', 'border': '3px solid #319997', 'border-radius': '6px',
               'margin': '0.25%', 'padding': '1%', 'width': '100%', 'margin-bottom': '2vH'},
        children=[
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
                            dbc.Col(surname_qt, width=1),
                            dbc.Col(surname_rt, width=1),
                            dbc.Col(html.P(), width=1),
                            # Q2
                            dbc.Col(nhs_qt, width=1),
                            dbc.Col(nhs_rt, width=1),
                            dbc.Col(html.P(), width=1),
                            # Q3
                            dbc.Col(doby_qt, width=1),
                            dbc.Col(doby_rt, width=1),
                            dbc.Col(html.P(), width=1),
                            # Q4
                            dbc.Col(parity_qt, width=1),
                            dbc.Col(parity_rt, width=2),
                        ]),
                        html.Br(),
                        dbc.Row([
                            # Q5
                            dbc.Col(del_qt, width=1),
                            dbc.Col(del_rt, width=2),
                            # Q6
                            dbc.Col(edd_qt, width=1),
                            dbc.Col(edd_rt, width=1),
                            dbc.Col(html.P(), width=1),
                            # Q7
                            dbc.Col(deldate_qt, width=1),
                            dbc.Col(deldate_rt, width=2),
                            # Q7
                            dbc.Col(tel_qt, width=1),
                            dbc.Col(tel_rt, width=2),
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
                            dbc.Col(vacc_qt, width=1),
                            dbc.Col(vacc_rt, width=2),
                            # Q10
                            dbc.Col(vacwhich_qt, width=1),
                            dbc.Col(vacwhich1_rt, width=1),
                            dbc.Col(vacwhich2_rt, width=1),
                            # Q11
                            dbc.Col(vac1date_qt, width=1),
                            dbc.Col(vac1date_rt, width=2),
                            # Q12
                            dbc.Col(vac2date_qt, width=1),
                            dbc.Col(vac2date_rt, width=2),

                        ]),
                        html.Br(),
                        dbc.Row([
                            # Q13
                            dbc.Col(covidtest_qt, width=1),
                            dbc.Col(covidtest_rt, width=2),
                            # Q14
                            dbc.Col(covidstatus_qt, width=1),
                            dbc.Col(covidstatus_rt, width=2),
                            # Q15
                            dbc.Col(covswabdate_qt, width=1),
                            dbc.Col(covswabdate_rt, width=2),

                        ]),
                        html.Br(),
                        dbc.Row([
                            # Q16
                            dbc.Col(covadmit_qt, width=1),
                            dbc.Col(covadmit_rt, width=2),
                            # Q17
                            dbc.Col(covadmitdate_qt, width=1),
                            dbc.Col(covadmitdate_rt, width=2),
                            # Q18
                            dbc.Col(covdischargedate_qt, width=1),
                            dbc.Col(covdischargedate_rt, width=2),
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
                            dbc.Col(sentences_qt, width=2),
                            dbc.Col(sentences_rt, width=2),
                            dbc.Col(rwt_qt, width=1),
                            dbc.Col(rwt_rt, width=4),
                        ]),
                        html.Br(),
                        dbc.Row([
                            # Q20
                            dbc.Col(covsymp_qt, width=2),
                            dbc.Col(tsym1_rt, width=2),
                            dbc.Col(tsym2_rt, width=2),
                            # 21
                            dbc.Col(tsym3_rt, width=2),
                            # 22
                            dbc.Col(tsym4_rt, width=2),
                        ]),
                        ### Row ###
                        html.Br(),
                        dbc.Row([
                            dbc.Col(covrisksw_qt, width=2),
                            dbc.Col(risksw1_rt, width=2),
                            # Q24
                            dbc.Col(risksw2_rt, width=2),
                            # Q25
                            dbc.Col(risksw3_rt, width=2),
                            # Q26
                            dbc.Col(risksw4_rt, width=2),
                        ]),
                        html.Br(),
                        ### Row ###
                        dbc.Row([
                            dbc.Col(covrisksb_qt, width=2),
                            # Q27
                            dbc.Col(risksb1_rt, width=2),
                            # Q28
                            dbc.Col(risksb2_rt, width=2),
                            # Q29
                            dbc.Col(risksb3_rt, width=2),
                            # Q30
                            dbc.Col(risksb4_rt, width=2),
                        ]),
                        html.Br(),
                        ### Row ###
                        dbc.Row([
                            # Q31
                            dbc.Col(covrx_qt, width=2),
                            dbc.Col(covrxw1_rt, width=2),
                            # Q32
                            dbc.Col(covrxw2_rt, width=2),
                            # Q33
                            dbc.Col(covrxw3_rt, width=2),
                            # Q34
                            dbc.Col(covrxw4_rt, width=2),
                        ]),
                        html.Br(),
                        ### Row ###
                        dbc.Row([
                            dbc.Col(covclinassess_qt, width=2),
                            # Q27
                            dbc.Col(clin1assess1_rt, width=2),
                            # Q28
                            dbc.Col(clin1assess2_rt, width=2),
                            # Q29
                            dbc.Col(clin1assess3_rt, width=2),
                            # Q30
                            dbc.Col(clin1assess4_rt, width=2)
                        ]),
                        html.Br(),

                        dbc.Row([
                            dbc.Col(fetalconcerns_qt, width=2),
                            # Q29
                            dbc.Col(fetalconcerns_rt, width=2),
                            dbc.Col(labour_qt, width=2),
                            # Q27
                            dbc.Col(labour_rt, width=2),
                            # Q28

                            # Q30

                        ]),
                        html.Br(),
                        dbc.Row([
                            dbc.Col(fetalheart_qt, width=2),
                            # Q30
                            dbc.Col(fhr_rt, width=2),
                        ]),
                        ### Row ###
                        #    dbc.Col(covfreetext_qt, width=2),
                        # ]),
                        # dbc.Row([
                        #    dbc.Col(covfreetext_rt, width=10),

                        # ]),

                    ], style={'border': '1px solid #319997', 'border-radius': '6px', 'padding': '0.5%',
                                    'padding-bottom': '20px'}),

                    html.Br(),
                    html.Div(children=[
                        html.Div([html.Button(id='telephonetriage_btn_confirm', children='Confirm', n_clicks=0)],
                                 style={'margin-right': '10px', 'display': 'inline-block'}),
                        html.Div([html.Button(id='telephonetriage_btn_cancel', children='Cancel', n_clicks=0)],
                                 style={'display': 'inline-block'})])

                ])
        ])


#############################################      Layout Div      #####################################################

banner = banner_main

# Left column
# Left column
left_bar = html.Div(
    id="left-column",
    className="two columns",
    style={'position': 'absolute', 'background-color': '#fcfcfc', 'left': 0, 'padding-left': '50px',
           'top': '6.275vH', 'height': '93.725vH','overflow': 'hidden'},
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
    style={'position': 'absolute', 'background-color': '#e1f9f8', 'left': '12.5%', 'padding': '1.55%',
           'width': '87.5%', 'height': '93.75vH', 'top': '8vH', 'flex-direction': 'column', 'overflow': 'auto',
           'z-index': '2000'},
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
                   'left': '0', 'right': '0', 'top': 0},
            children=[]
        )])

#############################################      Layout Div      #####################################################

#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("dob_at").value;
#     tempclass = document.getElementById("dob_at").className;
#     regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
#     var test = (regex_date.test(var_txt)) ?
#         "yes" : "no";
#     if (test=="yes" && var_txt !=0){
#             var year  = 60 * 60 * 24/ 365.25;
#             var currentTime = new Date();
#             var st = inputValue;
#             var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
#             var dt = new Date(st.replace(pattern,'$3-$2-$1'));
#             var delta = (currentTime - dt);
#             var deltad = delta/(60*60*24*1000*365.25);
#             console.log(deltad)
#             if (deltad<13){
#                 document.getElementById("dob_at").className ="is-valid2 form-control";
#                 return;
#             }
#             if (deltad>=13){
#                 document.getElementById("dob_at").className ="is-valid form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("dob_at").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("dob_at").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('dob_rt', 'children'),
#     Input('dob_at', 'value'),
# )
#
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("edd_at").value;
#     tempclass = document.getElementById("edd_at").className;
#     regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
#     var test = (regex_date.test(var_txt)) ?
#         "yes" : "no";
#     if (test=="yes" && var_txt !=0){
#             var year  = 60 * 60 * 24/ 365.25;
#             var currentTime = new Date();
#             var st = inputValue;
#             var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
#             var dt = new Date(st.replace(pattern,'$3-$2-$1'));
#             var delta = (currentTime - dt);
#             var deltad = delta/(60*60*24*1000);
#             console.log(deltad)
#             if (deltad<16){
#                 document.getElementById("edd_at").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad>=16){
#                 document.getElementById("edd_at").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("edd_at").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("edd_at").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('edd_rt', 'children'),
#     Input('edd_at', 'value'),
# )
#
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("deldate_at").value;
#     tempclass = document.getElementById("deldate_at").className;
#     regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
#     var test = (regex_date.test(var_txt)) ?
#         "yes" : "no";
#     if (test=="yes" && var_txt !=0){
#             var year  = 60 * 60 * 24/ 365.25;
#             var currentTime = new Date();
#             var st = inputValue;
#             var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
#             var dt = new Date(st.replace(pattern,'$3-$2-$1'));
#             var delta = (currentTime - dt);
#             var deltad = delta/(60*60*24*1000);
#             console.log(deltad)
#             if (deltad>=0){
#                 document.getElementById("deldate_at").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("deldate_at").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("deldate_at").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("deldate_at").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('deldate_rt', 'children'),
#     Input('deldate_at', 'value'),
# )
#
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("dose1date_at").value;
#     tempclass = document.getElementById("dose1date_at").className;
#     regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
#     var test = (regex_date.test(var_txt)) ?
#         "yes" : "no";
#     if (test=="yes" && var_txt !=0){
#             var year  = 60 * 60 * 24/ 365.25;
#             var currentTime = new Date();
#             var st = inputValue;
#             var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
#             var dt = new Date(st.replace(pattern,'$3-$2-$1'));
#             var delta = (currentTime - dt);
#             var deltad = delta/(60*60*24*1000);
#             console.log(deltad)
#             if (deltad>=0){
#                 document.getElementById("dose1date_at").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("dose1date_at").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("dose1date_at").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("dose1date_at").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('dose1date_rt', 'children'),
#     Input('dose1date_at', 'value'),
# )
#
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("dose2date_at").value;
#     tempclass = document.getElementById("dose2date_at").className;
#     regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
#     var test = (regex_date.test(var_txt)) ?
#         "yes" : "no";
#     if (test=="yes" && var_txt !=0){
#             var year  = 60 * 60 * 24/ 365.25;
#             var currentTime = new Date();
#             var st = inputValue;
#             var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
#             var dt = new Date(st.replace(pattern,'$3-$2-$1'));
#             var delta = (currentTime - dt);
#             var deltad = delta/(60*60*24*1000);
#             console.log(deltad)
#             if (deltad>=0){
#                 document.getElementById("dose2date_at").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("dose2date_at").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("dose2date_at").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("dose2date_at").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('dose2date_rt', 'children'),
#     Input('dose2date_at', 'value'),
# )
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("covidswabdate_at").value;
#     tempclass = document.getElementById("covidswabdate_at").className;
#     regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
#     var test = (regex_date.test(var_txt)) ?
#         "yes" : "no";
#     if (test=="yes" && var_txt !=0){
#             var year  = 60 * 60 * 24/ 365.25;
#             var currentTime = new Date();
#             var st = inputValue;
#             var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
#             var dt = new Date(st.replace(pattern,'$3-$2-$1'));
#             var delta = (currentTime - dt);
#             var deltad = delta/(60*60*24*1000);
#             console.log(deltad)
#             if (deltad>=0){
#                 document.getElementById("covidswabdate_at").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("covidswabdate_at").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("covidswabdate_at").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("covidswabdate_at").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('covidswabdate_rt', 'children'),
#     Input('covidswabdate_at', 'value'),
# )
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("covidadmitdate_at").value;
#     tempclass = document.getElementById("covidadmitdate_at").className;
#     regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
#     var test = (regex_date.test(var_txt)) ?
#         "yes" : "no";
#     if (test=="yes" && var_txt !=0){
#             var year  = 60 * 60 * 24/ 365.25;
#             var currentTime = new Date();
#             var st = inputValue;
#             var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
#             var dt = new Date(st.replace(pattern,'$3-$2-$1'));
#             var delta = (currentTime - dt);
#             var deltad = delta/(60*60*24*1000);
#             console.log(deltad)
#             if (deltad>=0){
#                 document.getElementById("covidadmitdate_at").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("covidadmitdate_at").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("covidadmitdate_at").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("covidadmitdate_at").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('covidadmitdate_rt', 'children'),
#     Input('covidadmitdate_at', 'value'),
# )
#
#
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("coviddischdate_at").value;
#     tempclass = document.getElementById("coviddischdate_at").className;
#     regex_date = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
#     var test = (regex_date.test(var_txt)) ?
#         "yes" : "no";
#     if (test=="yes" && var_txt !=0){
#             var year  = 60 * 60 * 24/ 365.25;
#             var currentTime = new Date();
#             var st = inputValue;
#             var pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
#             var dt = new Date(st.replace(pattern,'$3-$2-$1'));
#             var delta = (currentTime - dt);
#             var deltad = delta/(60*60*24*1000);
#             console.log(deltad)
#             if (deltad>=0){
#                 document.getElementById("coviddischdate_at").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("coviddischdate_at").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("coviddischdate_at").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("coviddischdate_at").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('coviddischdate_rt', 'children'),
#     Input('coviddischdate_at', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("nhs_at").value;
#     tempclass = document.getElementById("nhs_at").className;
#     regex_num = /^([SW])\w+([0-9]{4})$/
#     var test = (regex_num.test(var_txt)) ?
#        document.getElementById("nhs_at").className ="is-valid form-control" : document.getElementById("nhs_at").className ="is-invalid form-control";
#     }
#     """,
#     Output('nhs_rt', 'children'),
#     Input('nhs_at', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("tel_at").value;
#     tempclass = document.getElementById("tel_at").className;
#     regex_telnum = /^(\+44\s?7\d{3}|\(?07\d{3}\)?)\s?\d{3}\s?\d{3}$/
#     var test = (regex_telnum.test(var_txt)) ?
#        document.getElementById("tel_at").className ="is-valid form-control" : document.getElementById("tel_at").className ="is-invalid form-control";
#     }
#     """,
#     Output('tel_rt', 'children'),
#     Input('tel_at', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("parity_at").value;
#     tempclass = document.getElementById("parity_at").className;
#     regex_num = /^([SW])\w+([0-9]{2})$/
#     var test = (regex_num.test(var_txt)) ?
#        document.getElementById("parity_at").className ="is-valid form-control" : document.getElementById("parity_at").className ="is-invalid form-control";
#     }
#     """,
#     Output('parity_rt', 'children'),
#     Input('parity_at', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt1 = document.getElementById("spo2_1t").value;
#     var_txt2 = document.getElementById("spo2_2t").value;
#     tempclass = document.getElementById("spo2_1t").className;
#     regex_num = /^([SW])\w+([0-9]{3})$/
#     var test1 = (regex_num.test(var_txt1)) ?
#        document.getElementById("spo2_1t").className ="is-valid form-control" : document.getElementById("spo2_1t").className ="is-invalid form-control";
#     }
#      var test2 = (regex_num.test(var_txt2)) ?
#        document.getElementById("spo2_2t").className ="is-valid form-control" : document.getElementById("spo2_2t").className ="is-invalid form-control";
#     }
#
#     """,
#     Output('rwt_rt', 'children'),
#     Input('rwt_at', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("fhr_at").value;
#     tempclass = document.getElementById("fhr_at").className;
#     regex_num = /^([SW])\w+([0-9]{3})$/
#     var test = (regex_num.test(var_txt)) ?
#        document.getElementById("fhr_at").className ="is-valid form-control" : document.getElementById("fhr_at").className ="is-invalid form-control";
#     }
#     """,
#     Output('fhr_rt', 'children'),
#     Input('fhr_at', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("surname_at").value;
#     tempclass = document.getElementById("surname_at").className;
#     regex_num = /^[a-zA-Z]+$/
#     var test = (regex_num.test(var_txt)) ?
#        document.getElementById("surname_at").className ="is-valid form-control" : document.getElementById("surname_at").className ="is-invalid form-control";
#     }
#     """,
#     Output('surname_rt', 'children'),
#     Input('surname_at', 'value'),
# )
