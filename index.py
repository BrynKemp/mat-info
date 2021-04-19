from datatemplates import *
import dash_core_components as dcc
import dash_html_components as html
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from dash.dependencies import Input, Output, ClientsideFunction
from apps.codebank import *
import json

## Page files
from flask_app import flask_app
from apps import home, communitytriage, rbhtriage, telephonetriage, experiment

#############################################      MAIN LAYOUT   #######################################################

covdatastore = dcc.Store(id='session', storage_type='session')

flask_app.layout = html.Div(
    style={'display': 'inline-block', 'margin-bottom': '0%', 'padding-bottom': '0%',
           'background-color': '#f3fffe', 'overflow-y': 'hidden'},
    id="app-container",
    children=[
        dcc.Location(id='url', refresh=False),
        covdatastore,
        #dcc.Store(id='session', data=covid_data),
        html.Div(children=[dbc.Input(id='data1', type='text', value='')], style={'display': 'none'}),
        html.Div(children=[dbc.Input(id='data2', type='text', value='')], style={'display': 'none'}),
        html.Div(children=[dbc.Input(id='data3', type='text', value='')], style={'display': 'none'}),
        html.Div(id='banner'),
        html.Div(id='left-bar'),
        html.Div(id='page-content')
    ])


#############################################    Callbacks Index   #####################################################

@flask_app.callback([Output('banner', 'children'), Output('page-content', 'children'), Output('left-bar', 'children')],
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/home':
        return banner_splash, home.layout, home.left_bar
    elif pathname == '/communitytriage':
        return banner_main, communitytriage.layout, home.left_bar
    elif pathname == '/experiment':
        #experiment.layout.write_html("c:/banana.html")
        return banner_main, experiment.layout, home.left_bar

    else:
        return banner_splash, home.layout, home.left_bar
    #
    #
    # elif pathname == '/rbhtriage':
    #     return rbhtriage.layout
    # elif pathname == '/telephonetriage':
    #     return telephonetriage.layout


@flask_app.callback(Output('store', 'data'),
              [Input('data1', 'value'), Input('data2', 'value'), Input('data3', 'value')])
def update_data(data1, data2, data3):
    if data1 != '':
        return json.loads(data1)
    if data1 != '':
        return json.loads(data2)
    if data1 != '':
        return json.loads(data3)

#############################################    Local Functions   #####################################################


#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("dob_ac").value;
#     tempclass = document.getElementById("dob_ac").className;
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
#                 document.getElementById("dob_ac").className ="is-valid2 form-control";
#                 return;
#             }
#             if (deltad>=13){
#                 document.getElementById("dob_ac").className ="is-valid form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("dob_ac").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("dob_ac").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('dob_ac', 'children'),
#     Input('dob_ac', 'value'),
# )

#############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("edd_ac").value;
#     tempclass = document.getElementById("edd_ac").className;
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
#                 document.getElementById("edd_ac").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad>=16){
#                 document.getElementById("edd_ac").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("edd_ac").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("edd_ac").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('edd_ac', 'children'),
#     Input('edd_ac', 'value'),
# )
#
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("deldate_ac").value;
#     tempclass = document.getElementById("deldate_ac").className;
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
#                 document.getElementById("deldate_ac").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("deldate_ac").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("deldate_ac").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("deldate_ac").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('deldate_rc', 'children'),
#     Input('deldate_ac', 'value'),
# )
#
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("dose1date_ac").value;
#     tempclass = document.getElementById("dose1date_ac").className;
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
#                 document.getElementById("dose1date_ac").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("dose1date_ac").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("dose1date_ac").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("dose1date_ac").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('dose1date_rc', 'children'),
#     Input('dose1date_ac', 'value'),
# )
#
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("dose2date_ac").value;
#     tempclass = document.getElementById("dose2date_ac").className;
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
#                 document.getElementById("dose2date_ac").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("dose2date_ac").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("dose2date_ac").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("dose2date_ac").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('dose2date_rc', 'children'),
#     Input('dose2date_ac', 'value'),
# )
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("covidswabdate_ac").value;
#     tempclass = document.getElementById("covidswabdate_ac").className;
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
#                 document.getElementById("covidswabdate_ac").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("covidswabdate_ac").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("covidswabdate_ac").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("covidswabdate_ac").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('covidswabdate_rc', 'children'),
#     Input('covidswabdate_ac', 'value'),
# )
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("covidadmitdate_ac").value;
#     tempclass = document.getElementById("covidadmitdate_ac").className;
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
#                 document.getElementById("covidadmitdate_ac").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("covidadmitdate_ac").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("covidadmitdate_ac").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("covidadmitdate_ac").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('covidadmitdate_rc', 'children'),
#     Input('covidadmitdate_ac', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("coviddischdate_ac").value;
#     tempclass = document.getElementById("coviddischdate_ac").className;
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
#                 document.getElementById("coviddischdate_ac").className ="is-valid form-control";
#                 return;
#             }
#             if (deltad<0){
#                 document.getElementById("coviddischdate_ac").className ="is-valid2 form-control";
#                 return;
#             }
#         }
#     if (test=="no"&& var_txt !=0){
#             document.getElementById("coviddischdate_ac").className = "is-invalid form-control";
#             return;
#         }
#     if (var_txt ==''){
#            document.getElementById("coviddischdate_ac").className = "is-neutral form-control";
#            return;
#         }
#     }
#     """,
#     Output('coviddischdate_rc', 'children'),
#     Input('coviddischdate_ac', 'value'),
# )
#
# #############################################    Local Functions   #####################################################
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("nhs_ac").value;
#     tempclass = document.getElementById("nhs_ac").className;
#     regex_num = /^([SW])\w+([0-9]{4})$/
#     var test = (regex_num.test(var_txt)) ?
#        document.getElementById("nhs_ac").className ="is-valid form-control" : document.getElementById("nhs_ac").className ="is-invalid form-control";
#     }
#     """,
#     Output('nhs_rc', 'children'),
#     Input('nhs_ac', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("tel_ac").value;
#     tempclass = document.getElementById("tel_ac").className;
#     regex_telnum = /^(\+44\s?7\d{3}|\(?07\d{3}\)?)\s?\d{3}\s?\d{3}$/
#     var test = (regex_telnum.test(var_txt)) ?
#        document.getElementById("tel_ac").className ="is-valid form-control" : document.getElementById("tel_ac").className ="is-invalid form-control";
#     }
#     """,
#     Output('tel_rc', 'children'),
#     Input('tel_ac', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("parity_ac").value;
#     tempclass = document.getElementById("parity_ac").className;
#     regex_num = /^([SW])\w+([0-9]{2})$/
#     var test = (regex_num.test(var_txt)) ?
#        document.getElementById("parity_ac").className ="is-valid form-control" : document.getElementById("parity_ac").className ="is-invalid form-control";
#     }
#     """,
#     Output('parity_rc', 'children'),
#     Input('parity_ac', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt1 = document.getElementById("spo2_1c").value;
#     var_txt2 = document.getElementById("spo2_2c").value;
#     tempclass = document.getElementById("spo2_1c").className;
#     regex_num = /^([SW])\w+([0-9]{3})$/
#     var test1 = (regex_num.test(var_txt1)) ?
#        document.getElementById("spo2_1c").className ="is-valid form-control" : document.getElementById("spo2_1c").className ="is-invalid form-control";
#     }
#      var test2 = (regex_num.test(var_txt2)) ?
#        document.getElementById("spo2_2c").className ="is-valid form-control" : document.getElementById("spo2_2c").className ="is-invalid form-control";
#     }
#
#     """,
#     Output('rwt_rc', 'children'),
#     Input('rwt_ac', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("fhr_ac").value;
#     tempclass = document.getElementById("fhr_ac").className;
#     regex_num = /^([SW])\w+([0-9]{3})$/
#     var test = (regex_num.test(var_txt)) ?
#        document.getElementById("fhr_ac").className ="is-valid form-control" : document.getElementById("fhr_ac").className ="is-invalid form-control";
#     }
#     """,
#     Output('fhr_rc', 'children'),
#     Input('fhr_ac', 'value'),
# )
#
# app.clientside_callback(
#     """
#     function(inputValue){
#     var_txt = document.getElementById("surname_ac").value;
#     tempclass = document.getElementById("surname_ac").className;
#     regex_num = /^[a-zA-Z]+$/
#     var test = (regex_num.test(var_txt)) ?
#        document.getElementById("surname_ac").className ="is-valid form-control" : document.getElementById("surname_ac").className ="is-invalid form-control";
#     }
#     """,
#     Output('surname_rc', 'children'),
#     Input('surname_ac', 'value'),
# )

if __name__ == '__main__':
    flask_app.run_server(debug=True)
