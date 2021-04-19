import dash_html_components as html
from navbar import navbar_comp
from sidepanel import sidebar_comp
from flask_app import flask_app
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from datetime import date as dt
from airtable import Airtable
import json
from apps.codebank import *
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate


###############################################  splash  ###############################################################


###############################################  splash  ###############################################################

# app.clientside_callback(
#     """
#     function validatedate(inputText){
#         var dateformat = /^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$/;
#         if(inputText.match(dateformat)){
#             return "is-valid form-control"}
#         else if ((inputText.equals("dd/MM/yyyy") or inputText.equals(" ")){
#             return "form-control"}
#   }
#     """,
#     Output('edd_ac', 'className'),
#     Input('edd_ac', 'value'),
#)


#########################################  Callback Community  #########################################################
#
# @app.callback([Output('surname_ac', 'className'),
#                Output('nhs_ac', 'className'),
#                Output('dob_ac', 'className'),
#                Output('parity_ac', 'className'),
#                Output('edd_ac', 'className'),
#                Output('deldate_ac', 'className'),
#                Output('tel_ac', 'className'),
#                Output('dose1date_ac', 'className'),
#                Output('dose2date_ac', 'className'),
#                Output('covidswabdate_ac', 'className'),
#                Output('covidadmitdate_ac', 'className'),
#                Output('coviddischdate_ac', 'className'),
#                Output('spo2_1c', 'className'),
#                Output('spo2_2c', 'className'),
#                Output('fhr_ac', 'className'),
#
#                ],
#
#               [Input('surname_ac', 'value'),
#                Input('nhs_ac', 'value'),
#                Input('dob_ac', 'value'),
#                Input('parity_ac', 'value'),
#                # # # # # #
#                Input('del_ac', 'value'),
#                Input('edd_ac', 'value'),
#                Input('deldate_ac', 'value'),
#                Input('tel_ac', 'value'),
#                # # # # #
#                Input('vaccine_ac', 'value'),
#                Input('vactype1_ac', 'value'),
#                Input('vactype2_ac', 'value'),
#                Input('dose1date_ac', 'value'),
#                Input('dose2date_ac', 'value'),
#                # # # # #
#                Input('covidtest_ac', 'value'),
#                Input('covidstatus_ac', 'value'),
#                Input('covidswabdate_ac', 'value'),
#                # # # # #
#                Input('covidadmit_ac', 'value'),
#                Input('covidadmitdate_ac', 'value'),
#                Input('coviddischdate_ac', 'value'),
#                # # # # #
#                Input('sentences_ac', 'value'),
#                Input('spo2_1c', 'value'),
#                Input('spo2_2c', 'value'),
#                # # # #
#                Input('tsym1_ac', 'value'),
#                Input('tsym2_ac', 'value'),
#                Input('tsym3_ac', 'value'),
#                Input('tsym4_ac', 'value'),
#                # # # #
#                Input('risksw1_ac', 'value'),
#                Input('risksw2_ac', 'value'),
#                Input('risksw3_ac', 'value'),
#                Input('risksw4_ac', 'value'),
#                # # # #
#                Input('risksb1_ac', 'value'),
#                Input('risksb2_ac', 'value'),
#                Input('risksb3_ac', 'value'),
#                Input('risksb4_ac', 'value'),
#                # # # #
#                Input('covrxw1_ac', 'value'),
#                Input('covrxw2_ac', 'value'),
#                Input('covrxw3_ac', 'value'),
#                Input('covrxw4_ac', 'value'),
#                # # #
#                Input('clin1assess1_ac', 'value'),
#                Input('clin1assess2_ac', 'value'),
#                Input('clin1assess3_ac', 'value'),
#                Input('clin1assess4_ac', 'value'),
#                # # #
#                Input('labour_ac', 'value'),
#                Input('fetconcerns_ac', 'value'),
#                Input('fhr_ac', 'value')],
#                ####
#               [State('data_com', 'data'),
#                State('session', 'data')], prevent_initial_call=False)
#
# def check_contentc(in_surname, in_nhs, in_dob, in_parity, in_del, in_edd, in_deldate, in_tel, in_vacc, in_vacctype1,
#                    in_vacctype2, in_vacd1, in_vacd2,
#                    in_covtest, in_covstatus, in_covtestdate, in_covadmit, in_covadmitdate, in_covdischargedate,
#                    in_sentences, in_spO21, in_spO22, in_tsym1, in_tsym2,
#                    in_tsym3, in_tsym4, in_risksw1, in_risksw2, in_risksw3, in_risksw4, in_risksb1, in_risksb2,
#                    in_risksb3, in_risksb4, in_covrx1,
#                    in_covrx2, in_covrx3, in_covrx4, in_clinass1, in_clinass2, in_clinass3, in_clinass4, in_labour,
#                    in_fetconcerns, in_fhr, data_com, datacovid):
#
#
#     datacovid_str = ''
#
#     if "data_com" in locals() is False:
#         data_com = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
#     elif data_com is None:
#         data_com = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
#
#     ctx1 = dash.callback_context
#
#     if not ctx1.triggered:
#         input_id = 'No clicks yet'
#     else:
#         input_id = ctx1.triggered[0]['prop_id'].split('.')[0]
#         datacovid['triageloc_d'] = 'community'
#         datacovid_str = json.dumps(datacovid)
#
#     ## 1.  woman surname  ######################################
#     if input_id == 'surname_ac':
#         x = data_com
#         if in_surname == datacovid['surname_d'] or in_surname is None:
#             return x
#         elif (in_surname != datacovid[
#             'surname_d'] and in_surname is not None) is True and in_surname.isnumeric() is False:
#             datacovid['surname_ac'] = in_surname
#             datacovid_str = json.dumps(datacovid)
#             x[15] = datacovid_str
#             x[0] = 'is-valid form-control'
#             return x
#         elif (in_surname != datacovid['surname_d'] or in_surname is None) is True and in_surname.isnumeric() is True:
#             x[0] = 'is-invalid form-control'
#             return x
#
#     ## 2.  NHS Number  ######################################
#     if input_id == 'nhs_ac':
#         x = data_com
#         if in_nhs == datacovid['nhs_d'] or in_nhs is None:
#             return x
#         elif (in_nhs != datacovid['nhs_d'] and in_nhs is not None) is True and in_nhs.isnumeric() is False:
#             x[1] = 'is-invalid form-control'
#             return x
#         elif (in_nhs != datacovid['nhs_d'] and in_nhs is not None) is True and in_nhs.isnumeric() is True:
#             datacovid['nhs_ac'] = in_nhs
#             datacovid_str = json.dumps(datacovid)
#             x[15] = datacovid_str
#             x[1] = 'is-valid form-control'
#             return x
#
#     ## 3.  Date of birth  ######################################
#     if input_id == 'doby_ac':
#         x = data_com
#         if in_dob == datacovid['doby_d'] or in_dob is None:
#             return x
#         elif in_dob != datacovid['doby_d'] and in_dob is not None:
#             temp = valid_date(in_dob)
#             if temp:
#                 datacovid['doby_d'] = in_dob
#                 datacovid_str = json.dumps(datacovid)
#                 x[15] = datacovid_str
#                 x[2] = 'is-valid form-control'
#                 return x
#             else:
#                 x[2] = 'is-invalid form-control'
#                 return x
#
#     ## 4.  Parity  ######################################
#     if input_id == 'parity_ac':
#         x = data_com
#         if in_parity == datacovid['parity_d'] or in_parity is None:
#             return x
#         elif (in_parity != datacovid['parity_d'] and in_parity is not None) is True and in_parity.isnumeric() is False:
#             x[3] = 'is-invalid form-control'
#             return x
#         elif (in_parity != datacovid['parity_d'] and in_parity is not None) is True and in_parity.isnumeric() is True:
#             datacovid['parity_d'] = in_parity
#             datacovid_str = json.dumps(datacovid)
#             x[15] = datacovid_str
#             x[3] = 'is-valid form-control'
#             return x
#
#     ## 5.  EDD  ######################################
#     if input_id == 'edd_ac':
#         x = data_com
#         if in_edd == datacovid['edd_d'] or in_edd is None:
#             return x
#         elif in_edd != datacovid['edd_d'] and in_edd is not None:
#             temp = valid_date(in_edd)
#             if temp:
#                 datacovid['edd_d'] = in_edd
#                 datacovid_str = json.dumps(datacovid)
#                 x[15] = datacovid_str
#                 x[4] = 'is-valid form-control'
#                 return x
#             else:
#                 x[4] = 'is-invalid form-control'
#                 return x
#
#     ## 6.  Delivered  ######################################
#     if input_id == 'del_ac':
#         x = data_com
#         datacovid['del_d'] = in_del
#         datacovid_str = json.dumps(datacovid)
#         return x
#
#     ## 7.  Deldate  ######################################
#     if input_id == 'deldate_ac':
#         if in_deldate == datacovid['deldate_d'] or in_deldate is None:
#             return x
#         elif in_deldate != datacovid['deldate_d'] and in_deldate is not None:
#             temp = valid_date(in_deldate)
#             if temp:
#                 datacovid['deldate_d'] = in_deldate
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[5] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[5] = 'is-invalid form-control'
#                 return output_c
#
#     ## 8.  Telephone number  ######################################
#     if input_id == 'tel_ac':
#         tel_input = in_tel.replace(' ', '')
#         if tel_input == datacovid['tel_d'] or tel_input is None:
#             return x
#         elif (tel_input != datacovid['tel_d'] and tel_input is not None) is True and tel_input.isnumeric() is False:
#             output_c = x
#             output_c[6] = 'is-invalid form-control'
#             return output_c
#         elif (tel_input != datacovid['tel_d'] and tel_input is not None) is True and tel_input.isnumeric() is True:
#             datacovid['tel_d'] = tel_input
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[6] = 'is-valid form-control'
#             return output_c
#
#     ## 9.  Had vaccine  ######################################
#     if input_id == 'vaccine_ac':
#         datacovid['vaccine_d'] = in_vacc
#         return x
#
#     ## 10.  Dose 1 date  ######################################
#     if input_id == 'dose1date_ac':
#         if in_vacd1 == datacovid['dose1date_d'] or in_vacd1 is None:
#             return x
#         elif in_vacd1 != datacovid['dose1date_d'] and in_vacd1 is not None:
#             temp = valid_date(in_vacd1)
#             if temp:
#                 datacovid['dose1date_d'] = in_vacd1
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[7] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[7] = 'is-invalid form-control'
#                 return output_c
#
#     ## 11.  Dose 2 date  ######################################
#     if input_id == 'dose2date_ac':
#         if in_vacd2 == datacovid['dose2date_d'] or in_vacd2 is None:
#             return x
#         elif in_vacd2 != datacovid['dose2date_d'] and in_vacd2 is not None:
#             temp = valid_date(in_vacd2)
#             if temp:
#                 datacovid['dose1date_d'] = in_vacd2
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[8] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[8] = 'is-invalid form-control'
#                 return output_c
#
#     ## 12.  Vaccine type  ######################################
#     if input_id == 'vactype1_ac':
#         datacovid['vactype1_d'] = in_vacctype1
#         return x
#
#     ## 13.  Vaccine type  ######################################
#     if input_id == 'vactype2_ac':
#         datacovid['vactype2_d'] = in_vacctype2
#         return x
#
#     ## 14.  COVID status  ######################################
#     if input_id == 'covidtest_ac':
#         datacovid['covidtest_d'] = in_covtest
#         return x
#
#     ## 14.  COVID status  ######################################
#     if input_id == 'covidstatus_ac':
#         datacovid['covidstatus_d'] = in_covstatus
#         return x
#
#     ## 15.  Swab date  ######################################
#     if input_id == 'covidswabdate_ac':
#         if in_covtestdate == datacovid['covidswabdate_d'] or in_covtestdate is None:
#             return x
#         elif in_covtestdate != datacovid['covidswabdate_d'] and in_covtestdate is not None:
#             temp = valid_date(in_covtestdate)
#             if temp:
#                 datacovid['covidswabdate_d'] = in_covtestdate
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[9] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[9] = 'is-invalid form-control'
#                 return output_c
#     ## 16.  Admission COVID  ######################################
#     if input_id == 'covidadmit_ac':
#         datacovid['covidadmit_d'] = in_covadmit
#         return x
#
#     ## 17.  Admission date  ######################################
#     if input_id == 'covidadmitdate_ac':
#         if in_covadmitdate == datacovid['covidadmitdate_d'] or in_covadmitdate is None:
#             return x
#         elif in_covadmitdate != datacovid['covidadmitdate_d'] and in_covadmitdate is not None:
#             temp = valid_date(in_covtestdate)
#             if temp:
#                 datacovid['covidadmitdate_d'] = in_covadmitdate
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[10] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[10] = 'is-invalid form-control'
#                 return output_c
#
#     ## 18.  Discharge date  ######################################
#     if input_id == 'coviddischdate_ac':
#         if in_covdischargedate == datacovid['coviddischdate_d'] or in_covdischargedate is None:
#             return x
#         elif in_covdischargedate != datacovid['coviddischdate_d'] and in_covdischargedate is not None:
#             temp = valid_date(in_covdischargedate)
#             if temp:
#                 datacovid['coviddischdate_d'] = in_covdischargedate
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[10] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[10] = 'is-invalid form-control'
#                 return output_c
#
#     ## 19.  Sentences  ######################################
#     if input_id == 'sentences_ac':
#         datacovid['sentences_d'] = in_sentences
#         return x
#
#     ## 20.  SpO2 - 1  ######################################
#     if input_id == 'spo2_1c':
#         if in_spO21 == datacovid['spo2_1'] or in_spO21 is None:
#             return x
#         elif (in_spO21 != datacovid['spo2_1'] and in_spO21 is not None) is True and in_spO21.isnumeric() is False:
#             output_c = x
#             output_c[12] = 'is-invalid form-control'
#             return output_c
#         elif (in_spO21 != datacovid[
#             'spo2_1'] and in_spO21 is not None) is True and in_spO21.isnumeric() is True and int(
#             in_spO21) > 49 and int(in_spO21) < 100:
#             datacovid['spo2_1'] = in_spO21
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[12] = 'is-valid form-control'
#             return output_c
#
#     ## 21.  SpO2 - 2  ######################################
#     if input_id == 'spo2_2c':
#         if in_spO22 == datacovid['spo2_2'] or in_spO22 is None:
#             return x
#         elif (in_spO22 != datacovid['spo2_2'] and in_spO22 is not None) is True and in_spO22.isnumeric() is False:
#             output_c = x
#             output_c[13] = 'is-invalid form-control'
#             return output_c
#         elif (in_spO22 != datacovid[
#             'spo2_2'] and in_spO22 is not None) is True and in_spO22.isnumeric() is True and int(
#             in_spO22) > 49 and int(in_spO22) < 100:
#             datacovid['spo2_2'] = in_spO22
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[13] = 'is-valid form-control'
#             return output_c
#
#     ## 22.  tsym1_ac  ######################################
#     if input_id == 'tsym1_ac':
#         datacovid['tsym1_d'] = in_tsym1
#         return x
#
#     ## 23.  tsym2_ac  ######################################
#     if input_id == 'tsym2_ac':
#         datacovid['tsym2_d'] = in_tsym2
#         return x
#
#     ## 24.  tsym3_ac  ######################################
#     if input_id == 'tsym3_ac':
#         datacovid['tsym3_d'] = in_tsym3
#         return x
#
#     ## 25.  tsym4_ac  ######################################
#     if input_id == 'tsym4_ac':
#         datacovid['tsym4_d'] = in_tsym4
#         return x
#
#     ## 26.  risksw1_ac  #####################################
#     if input_id == 'risksw1_ac':
#         datacovid['risksw1_d'] = in_risksw1
#         return x
#
#     ## 27.  risksw2_ac  #####################################
#     if input_id == 'risksw2_ac':
#         datacovid['risksw2_d'] = in_risksw2
#         return x
#
#     ## 28.  risksw3_ac  #####################################
#     if input_id == 'risksw3_ac':
#         datacovid['risksw3_d'] = in_risksw3
#         return x
#
#     ## 29.  risksw4_ac  #####################################
#     if input_id == 'risksw4_ac':
#         datacovid['risksw4_d'] = in_risksw4
#         return x
#
#     ## 30.  risksb1_ac  #####################################
#     if input_id == 'risksb1_ac':
#         datacovid['risksb1_d'] = in_risksb1
#         return x
#
#     ## 31.  risksb2_ac  #####################################
#     if input_id == 'risksb2_ac':
#         datacovid['risksb2_d'] = in_risksb2
#         return x
#
#     ## 32.  risksb3_ac  #####################################
#     if input_id == 'risksb3_ac':
#         datacovid['risksb3_d'] = in_risksb3
#         return x
#
#     ## 33.  risksb4_ac  #####################################
#     if input_id == 'risksb4_ac':
#         datacovid['risksb4_d'] = in_risksb4
#         return x
#
#     ## 34.  covrxw1_ac  #####################################
#     if input_id == 'covrxw1_ac':
#         datacovid['covrxw1_d'] = in_covrx1
#         return x
#
#     ## 35.  covrxw2_ac  #####################################
#     if input_id == 'covrxw2_ac':
#         datacovid['covrxw2_d'] = in_covrx2
#         return x
#
#     ## 36.  covrxw3_ac  #####################################
#     if input_id == 'covrxw3_ac':
#         datacovid['covrxw3_d'] = in_covrx3
#         return x
#
#     ## 37.  covrxw4_ac  #####################################
#     if input_id == 'covrxw4_ac':
#         datacovid['covrxw4_d'] = in_covrx4
#         return x
#
#     ## 38.  covrxw1_ac  #####################################
#     if input_id == 'clin1assess1_ac':
#         datacovid['clin1assess1_d'] = in_clinass1
#         return x
#
#     ## 39.  covrxw2_ac  #####################################
#     if input_id == 'clin1assess2_ac':
#         datacovid['clin1assess2_d'] = in_clinass2
#         return x
#
#     ## 40.  covrxw3_ac  #####################################
#     if input_id == 'clin1assess3_ac':
#         datacovid['clin1assess3_d'] = in_clinass3
#         return x
#
#     ## 41.  covrxw4_ac  #####################################
#     if input_id == 'clin1assess4_ac':
#         datacovid['clin1assess4_d'] = in_clinass4
#         return x
#     ## 42.  covrxw4_ac  #####################################
#     if input_id == 'labour_ac':
#         datacovid['labour_d'] = in_labour
#         return x
#     ## 43.  covrxw4_ac  #####################################
#     if input_id == 'fetconcerns_ac':
#         datacovid['fetconcern_d'] = in_fetconcerns
#         return x
#     ## 44.  Telephone number  ######################################
#     if input_id == 'fhr_ac':
#         if in_fhr == datacovid['fhr_d'] or in_fhr is None:
#             return x
#         elif (in_fhr != datacovid['fhr_d'] and in_fhr is not None) is True and in_fhr.isnumeric() is False:
#             output_c = x
#             output_c[14] = 'is-invalid form-control'
#             return output_c
#         elif (in_fhr != datacovid['fhr_d'] and in_fhr is not None) is True and in_fhr.isnumeric() is True:
#             datacovid['fhr_d'] = in_fhr
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[14] = 'is-valid form-control'
#             return output_c
#
#
# #########################################  Callback Telephone  #########################################################
#
# @app.callback([Output('surname_at', 'className'),
#                Output('nhs_at', 'className'),
#                Output('dob_at', 'className'),
#                Output('parity_at', 'className'),
#                Output('edd_at', 'className'),
#                Output('deldate_at', 'className'),
#                Output('tel_at', 'className'),
#                Output('dose1date_at', 'className'),
#                Output('dose2date_at', 'className'),
#                Output('covidswabdate_at', 'className'),
#                Output('covidadmitdate_at', 'className'),
#                Output('coviddischdate_at', 'className'),
#                Output('spo2_1', 'className'),
#                Output('spo2_2', 'className'),
#                Output('fhr_at', 'className'),
#                Output('data2', 'value')],
#
#               [Input('surname_at', 'value'),
#                Input('nhs_at', 'value'),
#                Input('dob_at', 'value'),
#                Input('parity_at', 'value'),
#                # # # # # #
#                Input('del_at', 'value'),
#                Input('edd_at', 'value'),
#                Input('deldate_at', 'value'),
#                Input('tel_at', 'value'),
#                # # # # #
#                Input('vaccine_at', 'value'),
#                Input('vactype1_at', 'value'),
#                Input('vactype2_at', 'value'),
#                Input('dose1date_at', 'value'),
#                Input('dose2date_at', 'value'),
#                # # # # #
#                Input('covidtest_at', 'value'),
#                Input('covidstatus_at', 'value'),
#                Input('covidswabdate_at', 'value'),
#                # # # # #
#                Input('covidadmit_at', 'value'),
#                Input('covadmitdate_at', 'value'),
#                Input('coviddischdate_at', 'value'),
#                # # # # #
#                Input('sentences_at', 'value'),
#                Input('spo2_1t', 'value'),
#                Input('spo2_2t', 'value'),
#                # # # #
#                Input('tsym1_at', 'value'),
#                Input('tsym2_at', 'value'),
#                Input('tsym3_at', 'value'),
#                Input('tsym4_at', 'value'),
#                # # # #
#                Input('risksw1_at', 'value'),
#                Input('risksw2_at', 'value'),
#                Input('risksw3_at', 'value'),
#                Input('risksw4_at', 'value'),
#                # # # #
#                Input('risksb1_at', 'value'),
#                Input('risksb2_at', 'value'),
#                Input('risksb3_at', 'value'),
#                Input('risksb4_at', 'value'),
#                # # # #
#                Input('covrxw1_at', 'value'),
#                Input('covrxw2_at', 'value'),
#                Input('covrxw3_at', 'value'),
#                Input('covrxw4_at', 'value'),
#                # #
#                Input('clinassess1_at', 'value'),
#                Input('clinassess2_at', 'value'),
#                Input('clinassess3_at', 'value'),
#                Input('clinassess4_at', 'value'),
#                # #
#                Input('labour_at', 'value'),
#                Input('fetconcerns_at', 'value'),
#                Input('fhr_at', 'value')],
#               State('session', 'data'), prevent_initial_call=False)
# def check_contentt(in_surname, in_nhs, in_dob, in_parity, in_del, in_edd, in_deldate, in_tel, in_vacc, in_vacctype1,
#                    in_vacctype2, in_vacd1, in_vacd2,
#                    in_covtest, in_covstatus, in_covtestdate, in_covadmit, in_covadmitdate, in_covdischargedate,
#                    in_sentences, in_spO21, in_spO22, in_tsym1, in_tsym2,
#                    in_tsym3, in_tsym4, in_risksw1, in_risksw2, in_risksw3, in_risksw4, in_risksb1, in_risksb2,
#                    in_risksb3, in_risksb4, in_covrx1,
#                    in_covrx2, in_covrx3, in_covrx4, in_clinass1, in_clinass2, in_clinass3, in_clinass4, in_labour,
#                    in_fetconcerns, in_fhr, datacovid):
#
#     x = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]
#     ctx2 = dash.callback_context
#
#     if not ctx2.triggered:
#         input_id = 'No clicks yet'
#     else:
#         input_id = ctx2.triggered[0]['prop_id'].split('.')[0]
#         datacovid['triageloc_d'] = 'telephone'
#
#     ## 1.  woman surname  ######################################
#     if input_id == 'surname_at':
#         if in_surname == datacovid['surname_d'] or in_surname is None:
#             return x
#         elif (in_surname != datacovid[
#             'surname_d'] and in_surname is not None) is True and in_surname.isnumeric() is False:
#             datacovid['surname_at'] = in_surname
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[0] = 'is-valid form-control'
#             return output_c
#         elif (in_surname != datacovid['surname_d'] or in_surname is None) is True and in_surname.isnumeric() is True:
#             output_c = x
#             output_c[0] = 'is-invalid form-control'
#             return output_c
#
#     ## 2.  NHS Number  ######################################
#     if input_id == 'nhs_at':
#         if in_nhs == datacovid['nhs_d'] or in_nhs is None:
#             return x
#         elif (in_nhs != datacovid['nhs_d'] and in_nhs is not None) is True and in_nhs.isnumeric() is False:
#             output_c = x
#             output_c[1] = 'is-invalid form-control'
#             return output_c
#         elif (in_nhs != datacovid['nhs_d'] and in_nhs is not None) is True and in_nhs.isnumeric() is True:
#             datacovid['nhs_at'] = in_nhs
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[1] = 'is-valid form-control'
#             return output_c
#
#     ## 3.  Date of birth  ######################################
#     if input_id == 'doby_at':
#         if in_dob == datacovid['doby_d'] or in_dob is None:
#             return x
#         elif in_dob != datacovid['doby_d'] and in_dob is not None:
#             temp = valid_date(in_dob)
#             if temp:
#                 datacovid['doby_d'] = in_dob
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[2] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[2] = 'is-invalid form-control'
#                 return output_c
#
#     ## 4.  Parity  ######################################
#     if input_id == 'parity_at':
#         if in_parity == datacovid['parity_d'] or in_parity is None:
#             return x
#         elif (in_parity != datacovid['parity_d'] and in_parity is not None) is True and in_parity.isnumeric() is False:
#             output_c = x
#             output_c[3] = 'is-invalid form-control'
#             return output_c
#         elif (in_parity != datacovid['parity_d'] and in_parity is not None) is True and in_parity.isnumeric() is True:
#             datacovid['parity_d'] = in_parity
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[3] = 'is-valid form-control'
#             return output_c
#
#     ## 5.  EDD  ######################################
#     if input_id == 'edd_at':
#         if in_edd == datacovid['edd_d'] or in_edd is None:
#             return x
#         elif in_edd != datacovid['edd_d'] and in_edd is not None:
#             temp = valid_date(in_edd)
#             if temp:
#                 datacovid['edd_d'] = in_edd
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[4] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[4] = 'is-invalid form-control'
#                 return output_c
#
#     ## 6.  Delivered  ######################################
#     if input_id == 'del_at':
#         datacovid['del_d'] = in_del
#         return x
#
#     ## 7.  Deldate  ######################################
#     if input_id == 'deldate_at':
#         if in_deldate == datacovid['deldate_d'] or in_deldate is None:
#             return x
#         elif in_deldate != datacovid['deldate_d'] and in_deldate is not None:
#             temp = valid_date(in_deldate)
#             if temp:
#                 datacovid['dose1date_d'] = in_deldate
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[5] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[5] = 'is-invalid form-control'
#                 return output_c
#
#     ## 8.  Telephone number  ######################################
#     if input_id == 'tel_at':
#         tel_input = in_tel.replace(' ', '')
#         if tel_input == datacovid['tel_d'] or tel_input is None:
#             return x
#         elif (tel_input != datacovid['tel_d'] and tel_input is not None) is True and tel_input.isnumeric() is False:
#             output_c = x
#             output_c[6] = 'is-invalid form-control'
#             return output_c
#         elif (tel_input != datacovid['tel_d'] and tel_input is not None) is True and tel_input.isnumeric() is True:
#             datacovid['tel_d'] = tel_input
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[6] = 'is-valid form-control'
#             return output_c
#
#     ## 9.  Had vaccine  ######################################
#     if input_id == 'vaccine_at':
#         datacovid['vaccine_d'] = in_vacc
#         return x
#
#     ## 10.  Dose 1 date  ######################################
#     if input_id == 'dose1date_at':
#         if in_vacd1 == datacovid['dose1date_d'] or in_vacd1 is None:
#             return x
#         elif in_vacd1 != datacovid['dose1date_d'] and in_vacd1 is not None:
#             temp = valid_date(in_vacd1)
#             if temp:
#                 datacovid['dose1date_d'] = in_vacd1
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[7] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[7] = 'is-invalid form-control'
#                 return output_c
#
#     ## 11.  Dose 2 date  ######################################
#     if input_id == 'dose2date_at':
#         if in_vacd2 == datacovid['dose2date_d'] or in_vacd2 is None:
#             return x
#         elif in_vacd2 != datacovid['dose2date_d'] and in_vacd2 is not None:
#             temp = valid_date(in_vacd2)
#             if temp:
#                 datacovid['dose1date_d'] = in_vacd2
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[8] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[8] = 'is-invalid form-control'
#                 return output_c
#
#     ## 12.  Vaccine type  ######################################
#     if input_id == 'vactype1_at':
#         datacovid['vactype1_d'] = in_vacctype1
#         return x
#
#     ## 13.  Vaccine type  ######################################
#     if input_id == 'vactype2_at':
#         datacovid['vactype2_d'] = in_vacctype2
#         return x
#
#     ## 14.  COVID status  ######################################
#     if input_id == 'covidtest_at':
#         datacovid['covidtest_d'] = in_covtest
#         return x
#
#     ## 14.  COVID status  ######################################
#     if input_id == 'covidstatus_at':
#         datacovid['covidstatus_d'] = in_covstatus
#         return x
#
#     ## 15.  Swab date  ######################################
#     if input_id == 'covidswabdate_at':
#         if in_covtestdate == datacovid['covidswabdate_d'] or in_covtestdate is None:
#             return x
#         elif in_covtestdate != datacovid['covidswabdate_d'] and in_covtestdate is not None:
#             temp = valid_date(in_covtestdate)
#             if temp:
#                 datacovid['covidswabdate_d'] = in_covtestdate
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[9] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[9] = 'is-invalid form-control'
#                 return output_c
#     ## 16.  Admission COVID  ######################################
#     if input_id == 'covidadmit_at':
#         datacovid['covidadmit_d'] = in_covadmit
#         return x
#
#     ## 17.  Admission date  ######################################
#     if input_id == 'covidadmitdate_at':
#         if in_covadmitdate == datacovid['covidadmitdate_d'] or in_covadmitdate is None:
#             return x
#         elif in_covadmitdate != datacovid['covidadmitdate_d'] and in_covadmitdate is not None:
#             temp = valid_date(in_covtestdate)
#             if temp:
#                 datacovid['covidadmitdate_d'] = in_covadmitdate
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[10] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[10] = 'is-invalid form-control'
#                 return output_c
#
#     ## 18.  Discharge date  ######################################
#     if input_id == 'coviddischdate_at':
#         if in_covdischargedate == datacovid['coviddischdate_d'] or in_covdischargedate is None:
#             return x
#         elif in_covdischargedate != datacovid['coviddischdate_d'] and in_covdischargedate is not None:
#             temp = valid_date(in_covdischargedate)
#             if temp:
#                 datacovid['coviddischdate_d'] = in_covdischargedate
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[10] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[10] = 'is-invalid form-control'
#                 return output_c
#
#     ## 19.  Sentences  ######################################
#     if input_id == 'sentences_at':
#         datacovid['sentences_d'] = in_sentences
#         return x
#
#     ## 20.  SpO2 - 1  ######################################
#     if input_id == 'spo2_1c':
#         if in_spO21 == datacovid['spo2_1'] or in_spO21 is None:
#             return x
#         elif (in_spO21 != datacovid['spo2_1'] and in_spO21 is not None) is True and in_spO21.isnumeric() is False:
#             output_c = x
#             output_c[12] = 'is-invalid form-control'
#             return output_c
#         elif (in_spO21 != datacovid[
#             'spo2_1'] and in_spO21 is not None) is True and in_spO21.isnumeric() is True and int(
#             in_spO21) > 49 and int(in_spO21) < 100:
#             datacovid['spo2_1'] = in_spO21
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[12] = 'is-valid form-control'
#             return output_c
#
#     ## 21.  SpO2 - 2  ######################################
#     if input_id == 'spo2_2c':
#         if in_spO22 == datacovid['spo2_2'] or in_spO22 is None:
#             return x
#         elif (in_spO22 != datacovid['spo2_2'] and in_spO22 is not None) is True and in_spO22.isnumeric() is False:
#             output_c = x
#             output_c[13] = 'is-invalid form-control'
#             return output_c
#         elif (in_spO22 != datacovid[
#             'spo2_2'] and in_spO22 is not None) is True and in_spO22.isnumeric() is True and int(
#             in_spO22) > 49 and int(in_spO22) < 100:
#             datacovid['spo2_2'] = in_spO22
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[13] = 'is-valid form-control'
#             return output_c
#
#     ## 22.  tsym1_at  ######################################
#     if input_id == 'tsym1_at':
#         datacovid['tsym1_d'] = in_tsym1
#         return x
#
#     ## 23.  tsym2_at  ######################################
#     if input_id == 'tsym2_at':
#         datacovid['tsym2_d'] = in_tsym2
#         return x
#
#     ## 24.  tsym3_at  ######################################
#     if input_id == 'tsym3_at':
#         datacovid['tsym3_d'] = in_tsym3
#         return x
#
#     ## 25.  tsym4_at  ######################################
#     if input_id == 'tsym4_at':
#         datacovid['tsym4_d'] = in_tsym4
#         return x
#
#     ## 26.  risksw1_at  #####################################
#     if input_id == 'risksw1_at':
#         datacovid['risksw1_d'] = in_risksw1
#         return x
#
#     ## 27.  risksw2_at  #####################################
#     if input_id == 'risksw2_at':
#         datacovid['risksw2_d'] = in_risksw2
#         return x
#
#     ## 28.  risksw3_at  #####################################
#     if input_id == 'risksw3_at':
#         datacovid['risksw3_d'] = in_risksw3
#         return x
#
#     ## 29.  risksw4_at  #####################################
#     if input_id == 'risksw4_at':
#         datacovid['risksw4_d'] = in_risksw4
#         return x
#
#     ## 30.  risksb1_at  #####################################
#     if input_id == 'risksb1_at':
#         datacovid['risksb1_d'] = in_risksb1
#         return x
#
#     ## 31.  risksb2_at  #####################################
#     if input_id == 'risksb2_at':
#         datacovid['risksb2_d'] = in_risksb2
#         return x
#
#     ## 32.  risksb3_at  #####################################
#     if input_id == 'risksb3_at':
#         datacovid['risksb3_d'] = in_risksb3
#         return x
#
#     ## 33.  risksb4_at  #####################################
#     if input_id == 'risksb4_at':
#         datacovid['risksb4_d'] = in_risksb4
#         return x
#
#     ## 34.  covrxw1_at  #####################################
#     if input_id == 'covrxw1_at':
#         datacovid['covrxw1_d'] = in_covrx1
#         return x
#
#     ## 35.  covrxw2_at  #####################################
#     if input_id == 'covrxw2_at':
#         datacovid['covrxw2_d'] = in_covrx2
#         return x
#
#     ## 36.  covrxw3_at  #####################################
#     if input_id == 'covrxw3_at':
#         datacovid['covrxw3_d'] = in_covrx3
#         return x
#
#     ## 37.  covrxw4_at  #####################################
#     if input_id == 'covrxw4_at':
#         datacovid['covrxw4_d'] = in_covrx4
#         return x
#
#     ## 38.  covrxw1_at  #####################################
#     if input_id == 'clin1assess1_at':
#         datacovid['clin1assess1_d'] = in_clinass1
#         return x
#
#     ## 39.  covrxw2_at  #####################################
#     if input_id == 'clin1assess2_at':
#         datacovid['clin1assess2_d'] = in_clinass2
#         return x
#
#     ## 40.  covrxw3_at  #####################################
#     if input_id == 'clin1assess3_at':
#         datacovid['clin1assess3_d'] = in_clinass3
#         return x
#
#     ## 41.  covrxw4_at  #####################################
#     if input_id == 'clin1assess4_at':
#         datacovid['clin1assess4_d'] = in_clinass4
#         return x
#     ## 42.  covrxw4_at  #####################################
#     if input_id == 'labour_at':
#         datacovid['labour_d'] = in_labour
#         return x
#     ## 43.  covrxw4_at  #####################################
#     if input_id == 'fetconcerns_at':
#         datacovid['fetconcern_d'] = in_fetconcerns
#         return x
#     ## 44.  Telephone number  ######################################
#     if input_id == 'fhr_at':
#         if in_fhr == datacovid['fhr_d'] or in_fhr is None:
#             return x
#         elif (in_fhr != datacovid['fhr_d'] and in_fhr is not None) is True and in_fhr.isnumeric() is False:
#             output_c = x
#             output_c[14] = 'is-invalid form-control'
#             return output_c
#         elif (in_fhr != datacovid['fhr_d'] and in_fhr is not None) is True and in_fhr.isnumeric() is True:
#             datacovid['fhr_d'] = in_fhr
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[14] = 'is-valid form-control'
#             return output_c
#
#
# #########################################  Callback RBHDoor  #########################################################
#
# @app.callback([Output('surname_ar', 'className'),
#                Output('nhs_ar', 'className'),
#                Output('dob_ar', 'className'),
#                Output('parity_ar', 'className'),
#                Output('edd_ar', 'className'),
#                Output('deldate_ar', 'className'),
#                Output('tel_ar', 'className'),
#                Output('dose1date_ar', 'className'),
#                Output('dose2date_ar', 'className'),
#                Output('covidswabdate_ar', 'className'),
#                Output('covidadmitdate_ar', 'className'),
#                Output('coviddischdate_ar', 'className'),
#                Output('spo2_1r', 'className'),
#                Output('spo2_2r', 'className'),
#                Output('fhr_ar', 'className'),
#                Output('data3', 'value')],
#
#               [Input('surname_ar', 'value'),
#                Input('nhs_ar', 'value'),
#                Input('dob_ar', 'value'),
#                Input('parity_ar', 'value'),
#                # # # # # #
#                Input('del_ar', 'value'),
#                Input('edd_ar', 'value'),
#                Input('deldate_ar', 'value'),
#                Input('tel_ar', 'value'),
#                # # # # #
#                Input('vaccine_ar', 'value'),
#                Input('vactype1_ar', 'value'),
#                Input('vactype2_ar', 'value'),
#                Input('dose1date_ar', 'value'),
#                Input('dose2date_ar', 'value'),
#                # # # # #
#                Input('covidtest_ar', 'value'),
#                Input('covidstatus_ar', 'value'),
#                Input('covidswabdate_ar', 'value'),
#                # # # # #
#                Input('covidadmit_ar', 'value'),
#                Input('covidadmitdate_ar', 'value'),
#                Input('coviddischdate_ar', 'value'),
#                # # # # #
#                Input('sentences_ar', 'value'),
#                Input('spo2_1r', 'value'),
#                Input('spo2_2r', 'value'),
#                # # # #
#                Input('tsym1_ar', 'value'),
#                Input('tsym2_ar', 'value'),
#                Input('tsym3_ar', 'value'),
#                Input('tsym4_ar', 'value'),
#                # # # #
#                Input('risksw1_ar', 'value'),
#                Input('risksw2_ar', 'value'),
#                Input('risksw3_ar', 'value'),
#                Input('risksw4_ar', 'value'),
#                # # # #
#                Input('risksb1_ar', 'value'),
#                Input('risksb2_ar', 'value'),
#                Input('risksb3_ar', 'value'),
#                Input('risksb4_ar', 'value'),
#                # # # #
#                Input('covrxw1_ar', 'value'),
#                Input('covrxw2_ar', 'value'),
#                Input('covrxw3_ar', 'value'),
#                Input('covrxw4_ar', 'value'),
#                # #
#                Input('clinassess1_ar', 'value'),
#                Input('clinassess2_ar', 'value'),
#                Input('clinassess3_ar', 'value'),
#                Input('clinassess4_ar', 'value'),
#                # #
#                Input('labour_ar', 'value'),
#                Input('fetconcerns_ar', 'value'),
#                Input('fhr_ar', 'value')],
#               State('session', 'data'), prevent_initial_call=False)
# def check_contentr(in_surname, in_nhs, in_dob, in_parity, in_del, in_edd, in_deldate, in_tel, in_vacc, in_vacctype1,
#                    in_vacctype2, in_vacd1, in_vacd2,
#                    in_covtest, in_covstatus, in_covtestdate, in_covadmit, in_covadmitdate, in_covdischargedate,
#                    in_sentences, in_spO21, in_spO22, in_tsym1, in_tsym2,
#                    in_tsym3, in_tsym4, in_risksw1, in_risksw2, in_risksw3, in_risksw4, in_risksb1, in_risksb2,
#                    in_risksb3, in_risksb4, in_covrx1,
#                    in_covrx2, in_covrx3, in_covrx4, in_clinass1, in_clinass2, in_clinass3, in_clinass4, in_labour,
#                    in_fetconcerns, in_fhr, datacovid):
#
#     x = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
#     ctx3 = dash.callback_context
#
#     if not ctx3.triggered:
#         input_id = 'No clicks yet'
#     else:
#         input_id = ctx3.triggered[0]['prop_id'].split('.')[0]
#         datacovid['triageloc_d'] = 'rbh'
#
#     ## 1.  woman surname  ######################################
#     if input_id == 'surname_ar':
#         if in_surname == datacovid['surname_d'] or in_surname is None:
#             return x
#         elif (in_surname != datacovid[
#             'surname_d'] and in_surname is not None) is True and in_surname.isnumeric() is False:
#             datacovid['surname_ar'] = in_surname
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[0] = 'is-valid form-control'
#             return output_c
#         elif (in_surname != datacovid['surname_d'] or in_surname is None) is True and in_surname.isnumeric() is True:
#             output_c = x
#             output_c[0] = 'is-invalid form-control'
#             return output_c
#
#     ## 2.  NHS Number  ######################################
#     if input_id == 'nhs_ar':
#         if in_nhs == datacovid['nhs_d'] or in_nhs is None:
#             return x
#         elif (in_nhs != datacovid['nhs_d'] and in_nhs is not None) is True and in_nhs.isnumeric() is False:
#             output_c = x
#             output_c[1] = 'is-invalid form-control'
#             return output_c
#         elif (in_nhs != datacovid['nhs_d'] and in_nhs is not None) is True and in_nhs.isnumeric() is True:
#             datacovid['nhs_ar'] = in_nhs
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[1] = 'is-valid form-control'
#             return output_c
#
#     ## 3.  Date of birth  ######################################
#     if input_id == 'doby_ar':
#         if in_dob == datacovid['doby_d'] or in_dob is None:
#             return x
#         elif in_dob != datacovid['doby_d'] and in_dob is not None:
#             temp = valid_date(in_dob)
#             if temp:
#                 datacovid['doby_d'] = in_dob
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[2] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[2] = 'is-invalid form-control'
#                 return output_c
#
#     ## 4.  Parity  ######################################
#     if input_id == 'parity_ar':
#         if in_parity == datacovid['parity_d'] or in_parity is None:
#             return x
#         elif (in_parity != datacovid['parity_d'] and in_parity is not None) is True and in_parity.isnumeric() is False:
#             output_c = x
#             output_c[3] = 'is-invalid form-control'
#             return output_c
#         elif (in_parity != datacovid['parity_d'] and in_parity is not None) is True and in_parity.isnumeric() is True:
#             datacovid['parity_d'] = in_parity
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[3] = 'is-valid form-control'
#             return output_c
#
#     ## 5.  EDD  ######################################
#     if input_id == 'edd_ar':
#         if in_edd == datacovid['edd_d'] or in_edd is None:
#             return x
#         elif in_edd != datacovid['edd_d'] and in_edd is not None:
#             temp = valid_date(in_edd)
#             if temp:
#                 datacovid['edd_d'] = in_edd
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[4] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[4] = 'is-invalid form-control'
#                 return output_c
#
#     ## 6.  Delivered  ######################################
#     if input_id == 'del_ar':
#         datacovid['del_d'] = in_del
#         return x
#
#     ## 7.  Deldate  ######################################
#     if input_id == 'deldate_ar':
#         if in_deldate == datacovid['deldate_d'] or in_deldate is None:
#             return x
#         elif in_deldate != datacovid['deldate_d'] and in_deldate is not None:
#             temp = valid_date(in_deldate)
#             if temp:
#                 datacovid['dose1date_d'] = in_deldate
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[5] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[5] = 'is-invalid form-control'
#                 return output_c
#
#     ## 8.  Telephone number  ######################################
#     if input_id == 'tel_ar':
#         tel_input = in_tel.replace(' ', '')
#         if tel_input == datacovid['tel_d'] or tel_input is None:
#             return x
#         elif (tel_input != datacovid['tel_d'] and tel_input is not None) is True and tel_input.isnumeric() is False:
#             output_c = x
#             output_c[6] = 'is-invalid form-control'
#             return output_c
#         elif (tel_input != datacovid['tel_d'] and tel_input is not None) is True and tel_input.isnumeric() is True:
#             datacovid['tel_d'] = tel_input
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[6] = 'is-valid form-control'
#             return output_c
#
#     ## 9.  Had vaccine  ######################################
#     if input_id == 'vaccine_ar':
#         datacovid['vaccine_d'] = in_vacc
#         return x
#
#     ## 10.  Dose 1 date  ######################################
#     if input_id == 'dose1date_ar':
#         if in_vacd1 == datacovid['dose1date_d'] or in_vacd1 is None:
#             return x
#         elif in_vacd1 != datacovid['dose1date_d'] and in_vacd1 is not None:
#             temp = valid_date(in_vacd1)
#             if temp:
#                 datacovid['dose1date_d'] = in_vacd1
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[7] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[7] = 'is-invalid form-control'
#                 return output_c
#
#     ## 11.  Dose 2 date  ######################################
#     if input_id == 'dose2date_ar':
#         if in_vacd2 == datacovid['dose2date_d'] or in_vacd2 is None:
#             return x
#         elif in_vacd2 != datacovid['dose2date_d'] and in_vacd2 is not None:
#             temp = valid_date(in_vacd2)
#             if temp:
#                 datacovid['dose1date_d'] = in_vacd2
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[8] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[8] = 'is-invalid form-control'
#                 return output_c
#
#     ## 12.  Vaccine type  ######################################
#     if input_id == 'vactype1_ar':
#         datacovid['vactype1_d'] = in_vacctype1
#         return x
#
#     ## 13.  Vaccine type  ######################################
#     if input_id == 'vactype2_ar':
#         datacovid['vactype2_d'] = in_vacctype2
#         return x
#
#     ## 14.  COVID status  ######################################
#     if input_id == 'covidtest_ar':
#         datacovid['covidtest_d'] = in_covtest
#         return x
#
#     ## 14.  COVID status  ######################################
#     if input_id == 'covidstatus_ar':
#         datacovid['covidstatus_d'] = in_covstatus
#         return x
#
#     ## 15.  Swab date  ######################################
#     if input_id == 'covidswabdate_ar':
#         if in_covtestdate == datacovid['covidswabdate_d'] or in_covtestdate is None:
#             return x
#         elif in_covtestdate != datacovid['covidswabdate_d'] and in_covtestdate is not None:
#             temp = valid_date(in_covtestdate)
#             if temp:
#                 datacovid['covidswabdate_d'] = in_covtestdate
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[9] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[9] = 'is-invalid form-control'
#                 return output_c
#     ## 16.  Admission COVID  ######################################
#     if input_id == 'covidadmit_ar':
#         datacovid['covidadmit_d'] = in_covadmit
#         return x
#
#     ## 17.  Admission date  ######################################
#     if input_id == 'covidadmitdate_ar':
#         if in_covadmitdate == datacovid['covidadmitdate_d'] or in_covadmitdate is None:
#             return x
#         elif in_covadmitdate != datacovid['covidadmitdate_d'] and in_covadmitdate is not None:
#             temp = valid_date(in_covtestdate)
#             if temp:
#                 datacovid['covidadmitdate_d'] = in_covadmitdate
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[10] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[10] = 'is-invalid form-control'
#                 return output_c
#
#     ## 18.  Discharge date  ######################################
#     if input_id == 'coviddischdate_ar':
#         if in_covdischargedate == datacovid['coviddischdate_d'] or in_covdischargedate is None:
#             return x
#         elif in_covdischargedate != datacovid['coviddischdate_d'] and in_covdischargedate is not None:
#             temp = valid_date(in_covdischargedate)
#             if temp:
#                 datacovid['coviddischdate_d'] = in_covdischargedate
#                 datacovid_str = json.dumps(datacovid)
#                 output_c = x
#                 output_c[15] = datacovid_str
#                 output_c[10] = 'is-valid form-control'
#                 return output_c
#             else:
#                 output_c = x
#                 output_c[10] = 'is-invalid form-control'
#                 return output_c
#
#     ## 19.  Sentences  ######################################
#     if input_id == 'sentences_ar':
#         datacovid['sentences_d'] = in_sentences
#         return x
#
#     ## 20.  SpO2 - 1  ######################################
#     if input_id == 'spo2_1c':
#         if in_spO21 == datacovid['spo2_1'] or in_spO21 is None:
#             return x
#         elif (in_spO21 != datacovid['spo2_1'] and in_spO21 is not None) is True and in_spO21.isnumeric() is False:
#             output_c = x
#             output_c[12] = 'is-invalid form-control'
#             return output_c
#         elif (in_spO21 != datacovid[
#             'spo2_1'] and in_spO21 is not None) is True and in_spO21.isnumeric() is True and int(
#             in_spO21) > 49 and int(in_spO21) < 100:
#             datacovid['spo2_1'] = in_spO21
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[12] = 'is-valid form-control'
#             return output_c
#
#     ## 21.  SpO2 - 2  ######################################
#     if input_id == 'spo2_2c':
#         if in_spO22 == datacovid['spo2_2'] or in_spO22 is None:
#             return x
#         elif (in_spO22 != datacovid['spo2_2'] and in_spO22 is not None) is True and in_spO22.isnumeric() is False:
#             output_c = x
#             output_c[13] = 'is-invalid form-control'
#             return output_c
#         elif (in_spO22 != datacovid[
#             'spo2_2'] and in_spO22 is not None) is True and in_spO22.isnumeric() is True and int(
#             in_spO22) > 49 and int(in_spO22) < 100:
#             datacovid['spo2_2'] = in_spO22
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[13] = 'is-valid form-control'
#             return output_c
#
#     ## 22.  tsym1_ar  ######################################
#     if input_id == 'tsym1_ar':
#         datacovid['tsym1_d'] = in_tsym1
#         return x
#
#     ## 23.  tsym2_ar  ######################################
#     if input_id == 'tsym2_ar':
#         datacovid['tsym2_d'] = in_tsym2
#         return x
#
#     ## 24.  tsym3_ar  ######################################
#     if input_id == 'tsym3_ar':
#         datacovid['tsym3_d'] = in_tsym3
#         return x
#
#     ## 25.  tsym4_ar  ######################################
#     if input_id == 'tsym4_ar':
#         datacovid['tsym4_d'] = in_tsym4
#         return x
#
#     ## 26.  risksw1_ar  #####################################
#     if input_id == 'risksw1_ar':
#         datacovid['risksw1_d'] = in_risksw1
#         return x
#
#     ## 27.  risksw2_ar  #####################################
#     if input_id == 'risksw2_ar':
#         datacovid['risksw2_d'] = in_risksw2
#         return x
#
#     ## 28.  risksw3_ar  #####################################
#     if input_id == 'risksw3_ar':
#         datacovid['risksw3_d'] = in_risksw3
#         return x
#
#     ## 29.  risksw4_ar  #####################################
#     if input_id == 'risksw4_ar':
#         datacovid['risksw4_d'] = in_risksw4
#         return x
#
#     ## 30.  risksb1_ar  #####################################
#     if input_id == 'risksb1_ar':
#         datacovid['risksb1_d'] = in_risksb1
#         return x
#
#     ## 31.  risksb2_ar  #####################################
#     if input_id == 'risksb2_ar':
#         datacovid['risksb2_d'] = in_risksb2
#         return x
#
#     ## 32.  risksb3_ar  #####################################
#     if input_id == 'risksb3_ar':
#         datacovid['risksb3_d'] = in_risksb3
#         return x
#
#     ## 33.  risksb4_ar  #####################################
#     if input_id == 'risksb4_ar':
#         datacovid['risksb4_d'] = in_risksb4
#         return x
#
#     ## 34.  covrxw1_ar  #####################################
#     if input_id == 'covrxw1_ar':
#         datacovid['covrxw1_d'] = in_covrx1
#         return x
#
#     ## 35.  covrxw2_ar  #####################################
#     if input_id == 'covrxw2_ar':
#         datacovid['covrxw2_d'] = in_covrx2
#         return x
#
#     ## 36.  covrxw3_ar  #####################################
#     if input_id == 'covrxw3_ar':
#         datacovid['covrxw3_d'] = in_covrx3
#         return x
#
#     ## 37.  covrxw4_ar  #####################################
#     if input_id == 'covrxw4_ar':
#         datacovid['covrxw4_d'] = in_covrx4
#         return x
#
#     ## 38.  covrxw1_ar  #####################################
#     if input_id == 'clin1assess1_ar':
#         datacovid['clin1assess1_d'] = in_clinass1
#         return x
#
#     ## 39.  covrxw2_ar  #####################################
#     if input_id == 'clin1assess2_ar':
#         datacovid['clin1assess2_d'] = in_clinass2
#         return x
#
#     ## 40.  covrxw3_ar  #####################################
#     if input_id == 'clin1assess3_ar':
#         datacovid['clin1assess3_d'] = in_clinass3
#         return x
#
#     ## 41.  covrxw4_ar  #####################################
#     if input_id == 'clin1assess4_ar':
#         datacovid['clin1assess4_d'] = in_clinass4
#         return x
#     ## 42.  covrxw4_ar  #####################################
#     if input_id == 'labour_ar':
#         datacovid['labour_d'] = in_labour
#         return x
#     ## 43.  covrxw4_ar  #####################################
#     if input_id == 'fetconcerns_ar':
#         datacovid['fetconcern_d'] = in_fetconcerns
#         return x
#     ## 44.  Telephone number  ######################################
#     if input_id == 'fhr_ar':
#         if in_fhr == datacovid['fhr_d'] or in_fhr is None:
#             return x
#         elif (in_fhr != datacovid['fhr_d'] and in_fhr is not None) is True and in_fhr.isnumeric() is False:
#             output_c = x
#             output_c[14] = 'is-invalid form-control'
#             return output_c
#         elif (in_fhr != datacovid['fhr_d'] and in_fhr is not None) is True and in_fhr.isnumeric() is True:
#             datacovid['fhr_d'] = in_fhr
#             datacovid_str = json.dumps(datacovid)
#             output_c = x
#             output_c[15] = datacovid_str
#             output_c[14] = 'is-valid form-control'
#             return output_c
#

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
    'vaccine_d': '',
    'dose1date_d': 'Click to enter',
    'dose2date_d': 'Click to enter',
    'vactype1_d': '',
    'vactype2_d': '',
    'covidtest_d': '',
    'covidstatus_d': '',
    'covidswabdate_d': 'Click to enter',
    'covidadmit_d': '',
    'covidadmitdate_d': 'Click to enter',
    'coviddischdate_d': 'Click to enter',
    'sentences_d': '',
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
    'covrxw1_d': '',
    'covrxw2_d': '',
    'covrxw3_d': '',
    'covrxw4_d': '',
    'labour_d': '',
    'fetconcern_d': '',
    'fhr_d': ''
}
