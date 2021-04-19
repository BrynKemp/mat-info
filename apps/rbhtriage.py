from navbar import navbar_comp
from qbank import *
from apps.codebank import *
from apps.home import gen_sidebar
from dash.dependencies import Input, Output, ClientsideFunction
from flask_app import flask_app


#############################################    Local Functions   #####################################################

def tri_rbh():
    return html.Div(
        id='tri_rbh',
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
                            dbc.Col(surname_qr, width=1),
                            dbc.Col(surname_rr, width=1),
                            dbc.Col(html.P(), width=1),
                            # Q2
                            dbc.Col(nhs_qr, width=1),
                            dbc.Col(nhs_rr, width=1),
                            dbc.Col(html.P(), width=1),
                            # Q3
                            dbc.Col(doby_qr, width=1),
                            dbc.Col(doby_rr, width=1),
                            dbc.Col(html.P(), width=1),
                            # Q4
                            dbc.Col(parity_qr, width=1),
                            dbc.Col(parity_rr, width=2),
                        ]),
                        html.Br(),
                        dbc.Row([
                            # Q5
                            dbc.Col(del_qr, width=1),
                            dbc.Col(del_rr, width=2),
                            # Q6
                            dbc.Col(edd_qr, width=1),
                            dbc.Col(edd_rr, width=1),
                            dbc.Col(html.P(), width=1),
                            # Q7
                            dbc.Col(deldate_qr, width=1),
                            dbc.Col(deldate_rr, width=2),
                            # Q7
                            dbc.Col(tel_qr, width=1),
                            dbc.Col(tel_rr, width=2),
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
                            dbc.Col(vacc_qr, width=1),
                            dbc.Col(vacc_rr, width=2),
                            # Q10
                            dbc.Col(vacwhich_qr, width=1),
                            dbc.Col(vacwhich1_rr, width=1),
                            dbc.Col(vacwhich2_rr, width=1),
                            # Q11
                            dbc.Col(vac1date_qr, width=1),
                            dbc.Col(vac1date_rr, width=2),
                            # Q12
                            dbc.Col(vac2date_qr, width=1),
                            dbc.Col(vac2date_rr, width=2),

                        ]),
                        html.Br(),
                        dbc.Row([
                            # Q13
                            dbc.Col(covidtest_qr, width=1),
                            dbc.Col(covidtest_rr, width=2),
                            # Q14
                            dbc.Col(covidstatus_qr, width=1),
                            dbc.Col(covidstatus_rr, width=2),
                            # Q15
                            dbc.Col(covswabdate_qr, width=1),
                            dbc.Col(covswabdate_rr, width=2),

                        ]),
                        html.Br(),
                        dbc.Row([
                            # Q16
                            dbc.Col(covadmit_qr, width=1),
                            dbc.Col(covadmit_rr, width=2),
                            # Q17
                            dbc.Col(covadmitdate_qr, width=1),
                            dbc.Col(covadmitdate_rr, width=2),
                            # Q18
                            dbc.Col(covdischargedate_qr, width=1),
                            dbc.Col(covdischargedate_rr, width=2),
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
                            dbc.Col(sentences_qr, width=2),
                            dbc.Col(sentences_rr, width=2),
                            dbc.Col(rwt_qr, width=1),
                            dbc.Col(rwt_rr, width=4),
                        ]),
                        html.Br(),
                        dbc.Row([
                            # Q20
                            dbc.Col(covsymp_qr, width=2),
                            dbc.Col(tsym1_rr, width=2),
                            dbc.Col(tsym2_rr, width=2),
                            # 21
                            dbc.Col(tsym3_rr, width=2),
                            # 22
                            dbc.Col(tsym4_rr, width=2),
                        ]),
                        ### Row ###
                        html.Br(),
                        dbc.Row([
                            dbc.Col(covrisksw_qr, width=2),
                            dbc.Col(risksw1_rr, width=2),
                            # Q24
                            dbc.Col(risksw2_rr, width=2),
                            # Q25
                            dbc.Col(risksw3_rr, width=2),
                            # Q26
                            dbc.Col(risksw4_rr, width=2),
                        ]),
                        html.Br(),
                        ### Row ###
                        dbc.Row([
                            dbc.Col(covrisksb_qr, width=2),
                            # Q27
                            dbc.Col(risksb1_rr, width=2),
                            # Q28
                            dbc.Col(risksb2_rr, width=2),
                            # Q29
                            dbc.Col(risksb3_rr, width=2),
                            # Q30
                            dbc.Col(risksb4_rr, width=2),
                        ]),
                        html.Br(),
                        ### Row ###
                        dbc.Row([
                            # Q31
                            dbc.Col(covrx_qr, width=2),
                            dbc.Col(covrxw1_rr, width=2),
                            # Q32
                            dbc.Col(covrxw2_rr, width=2),
                            # Q33
                            dbc.Col(covrxw3_rr, width=2),
                            # Q34
                            dbc.Col(covrxw4_rr, width=2),
                        ]),
                        html.Br(),
                        ### Row ###
                        dbc.Row([
                            dbc.Col(covclinassess_qr, width=2),
                            # Q27
                            dbc.Col(clin1assess1_rr, width=2),
                            # Q28
                            dbc.Col(clin1assess2_rr, width=2),
                            # Q29
                            dbc.Col(clin1assess3_rr, width=2),
                            # Q30
                            dbc.Col(clin1assess4_rr, width=2)
                        ]),
                        html.Br(),

                        dbc.Row([
                            dbc.Col(fetalconcerns_qr, width=2),
                            # Q29
                            dbc.Col(fetalconcerns_rr, width=2),
                            dbc.Col(labour_qr, width=2),
                            # Q27
                            dbc.Col(labour_rr, width=2),
                            # Q28

                            # Q30

                        ]),
                        html.Br(),
                        dbc.Row([
                            dbc.Col(fetalheart_qr, width=2),
                            # Q30
                            dbc.Col(fhr_rr, width=2),
                        ]),
                        ### Row ###
                        #    dbc.Col(covfreetext_qr, width=2),
                        # ]),
                        # dbc.Row([
                        #    dbc.Col(covfreetext_rr, width=10),

                        # ]),

                    ], style={'border': '1px solid #319997', 'border-radius': '6px', 'padding': '0.5%',
                                    'padding-bottom': '20px'}),

                    html.Br(),
                    html.Div(children=[
                        html.Div([html.Button(id='rbhtriage_btn_confirm', children='Confirm', n_clicks=0)],
                                 style={'margin-right': '10px', 'display': 'inline-block'}),
                        html.Div([html.Button(id='rbhtriage_btn_cancel', children='Cancel', n_clicks=0)],
                                 style={'display': 'inline-block'})])

                ])
        ])


#############################################      Layout Div      #####################################################

# Banner
banner = banner_main

# Left column
# Left column
left_bar = html.Div(
    id="left-column",
    className="two columns",
    style={'position': 'absolute', 'background-color': '#fcfcfc', 'left': 0, 'padding-left': '50px',
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
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("dob_ar").value;
#     tempclass = document.getElementById("dob_ar").className;
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
#                 document.getElementById("dob_ar").className ="is-valid2 form-control";
#                 return;
#             }
#             if (deltad>=13){
#                 document.getElementById("dob_ar").className ="is-valid form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("dob_ar").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("dob_ar").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('dob_rr', 'children'),
#     Input('dob_ar', 'value'),
# )
#
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("edd_ar").value;
#     tempclass = document.getElementById("edd_ar").className;
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
#                 document.getElementById("edd_ar").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad>=16){
#                 document.getElementById("edd_ar").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("edd_ar").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("edd_ar").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('edd_rr', 'children'),
#     Input('edd_ar', 'value'),
# )
#
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("deldate_ar").value;
#     tempclass = document.getElementById("deldate_ar").className;
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
#                 document.getElementById("deldate_ar").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("deldate_ar").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("deldate_ar").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("deldate_ar").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('deldate_rr', 'children'),
#     Input('deldate_ar', 'value'),
# )
#
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("dose1date_ar").value;
#     tempclass = document.getElementById("dose1date_ar").className;
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
#                 document.getElementById("dose1date_ar").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("dose1date_ar").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("dose1date_ar").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("dose1date_ar").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('dose1date_rr', 'children'),
#     Input('dose1date_ar', 'value'),
# )
#
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("dose2date_ar").value;
#     tempclass = document.getElementById("dose2date_ar").className;
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
#                 document.getElementById("dose2date_ar").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("dose2date_ar").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("dose2date_ar").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("dose2date_ar").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('dose2date_rr', 'children'),
#     Input('dose2date_ar', 'value'),
# )
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("covidswabdate_ar").value;
#     tempclass = document.getElementById("covidswabdate_ar").className;
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
#                 document.getElementById("covidswabdate_ar").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("covidswabdate_ar").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("covidswabdate_ar").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("covidswabdate_ar").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('covidswabdate_rr', 'children'),
#     Input('covidswabdate_ar', 'value'),
# )
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("covidadmitdate_ar").value;
#     tempclass = document.getElementById("covidadmitdate_ar").className;
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
#                 document.getElementById("covidadmitdate_ar").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("covidadmitdate_ar").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("covidadmitdate_ar").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("covidadmitdate_ar").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('covidadmitdate_rr', 'children'),
#     Input('covidadmitdate_ar', 'value'),
# )
#
#
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("coviddischdate_ar").value;
#     tempclass = document.getElementById("coviddischdate_ar").className;
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
#                 document.getElementById("coviddischdate_ar").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("coviddischdate_ar").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("coviddischdate_ar").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("coviddischdate_ar").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('coviddischdate_rr', 'children'),
#     Input('coviddischdate_ar', 'value'),
# )
#
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("nhs_ar").value;
#     tempclass = document.getElementById("nhs_ar").className;
#     regex_num = /^([SW])\w+([0-9]{4})$/
#     var test = (regex_num.test(var_txt)) ?
#        document.getElementById("nhs_ar").className ="is-valid form-control" : document.getElementById("nhs_ar").className ="is-invalid form-control";
#     }
#     """,
#     Output('nhs_rr', 'children'),
#     Input('nhs_ar', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("tel_ar").value;
#     tempclass = document.getElementById("tel_ar").className;
#     regex_telnum = /^(\+44\s?7\d{3}|\(?07\d{3}\)?)\s?\d{3}\s?\d{3}$/
#     var test = (regex_telnum.test(var_txt)) ?
#        document.getElementById("tel_ar").className ="is-valid form-control" : document.getElementById("tel_ar").className ="is-invalid form-control";
#     }
#     """,
#     Output('tel_rr', 'children'),
#     Input('tel_ar', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("parity_ar").value;
#     tempclass = document.getElementById("parity_ar").className;
#     regex_num = /^([SW])\w+([0-9]{2})$/
#     var test = (regex_num.test(var_txt)) ?
#        document.getElementById("parity_ar").className ="is-valid form-control" : document.getElementById("parity_ar").className ="is-invalid form-control";
#     }
#     """,
#     Output('parity_rr', 'children'),
#     Input('parity_ar', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt1 = document.getElementById("spo2_1r").value;
#     var_txt2 = document.getElementById("spo2_2r").value;
#     tempclass = document.getElementById("spo2_1r").className;
#     regex_num = /^([SW])\w+([0-9]{3})$/
#     var test1 = (regex_num.test(var_txt1)) ?
#        document.getElementById("spo2_1r").className ="is-valid form-control" : document.getElementById("spo2_1r").className ="is-invalid form-control";
#     }
#      var test2 = (regex_num.test(var_txt2)) ?
#        document.getElementById("spo2_2r").className ="is-valid form-control" : document.getElementById("spo2_2r").className ="is-invalid form-control";
#     }
#
#     """,
#     Output('rwt_rr', 'children'),
#     Input('rwt_ar', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("fhr_ar").value;
#     tempclass = document.getElementById("fhr_ar").className;
#     regex_num = /^([SW])\w+([0-9]{3})$/
#     var test = (regex_num.test(var_txt)) ?
#        document.getElementById("fhr_ar").className ="is-valid form-control" : document.getElementById("fhr_ar").className ="is-invalid form-control";
#     }
#     """,
#     Output('fhr_rr', 'children'),
#     Input('fhr_ar', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("surname_ar").value;
#     tempclass = document.getElementById("surname_ar").className;
#     regex_num = /^[a-zA-Z]+$/
#     var test = (regex_num.test(var_txt)) ?
#        document.getElementById("surname_ar").className ="is-valid form-control" : document.getElementById("surname_ar").className ="is-invalid form-control";
#     }
#     """,
#     Output('surname_rr', 'children'),
#     Input('surname_ar', 'value'),
# )
#

