from navbar import navbar_comp
from datetime import datetime, timedelta
from qbank import *
from apps.codebank import *
from apps.home import gen_sidebar
from datetime import date as dt
from flask_app import flask_app
from apps.sbarfunctions import *
from datatemplates import *
from costRF import *
import dash_bootstrap_components as dbc
import dash_html_components as html
from apps.report import *
from flask import Flask, render_template, make_response

import dash
import pdfkit


#############################################    Data Templates    #####################################################


#############################################    Local Functions   #####################################################


def gen_sbar():
    return html.Div(
        id='sbar_left',
        style={'height': '80%', 'margin-top': '10%', 'padding-top': '2.5vH', 'background-color': c_red,
               'border': '3px solid',
               'border-color': 'black', 'border-radius': '25px', 'padding': '10px'},
        children=[
            dbc.Row(dbc.Col(dbc.Container(
                children=[
                    dbc.Row(html.H5(id='settingstr', children='', className="sbarheader"), justify="center",
                            align="center",
                            className="h-50"),
                ]), width=12), style={'padding-top': '0.5vH', 'height': '7.5vH'}, className="h-50"),
            dbc.Row([
                dbc.Col(html.Div(id='sbar_s', style={'background-color': c_red},
                                 children=[
                                     html.Img(src='/assets/s_high.png', id='image_b',
                                              style={'width': '60px', 'height': '60px'})]), className="h-50", width=1),
                dbc.Col(dbc.Container(
                    children=[
                        dbc.Row(html.P(id='', children='', className="sbartext"),
                                style={'padding-top': '0.5%'}, className="h-50"),
                        dbc.Row(html.P(id='situation0', children='', className="sbartext"),
                                style={'padding-top': '0.5%'}, className="h-50"),
                        dbc.Row(html.P(id='situation1', children='', className="sbartext"),
                                style={'padding-top': '0.5%'}, className="h-50"),
                    ]), width=11),
            ], style={'height': '10.0vH', 'padding-top': '0.5%'}),
            dbc.Row([
                dbc.Col(html.Div(id='sbar_s', style={'background-color': c_red},
                                 children=[
                                     html.Img(src='/assets/b_high.png', id='image_b',
                                              style={'width': '60px', 'height': '60px'})]), className="h-50", width=1),

                dbc.Col(dbc.Container(
                    children=[

                        dbc.Row(html.P(id='background0', children='', className="sbartext"), className="h-50"),
                        dbc.Row(html.P(id='background1', children='', className="sbartext"), className="h-50"),
                        dbc.Row(html.P(id='background2', children='', className="sbartext"), className="h-50"),
                    ]), width=11),
            ], style={'height': '7.5vH', 'padding-top': '0.5%'}),
            dbc.Row([
                dbc.Col(html.Div(id='sbar_s', style={'background-color': c_red},
                                 children=[
                                     html.Img(src='/assets/a_high.png', id='image_b',
                                              style={'width': '60px', 'height': '60px'})]),
                        width=1),

                dbc.Col(dbc.Container(
                    children=[
                        dbc.Row(html.P('Symptoms:', className="sbartext", style={'font-weight': '600'}),
                                style={'padding-top': '0.5%'},
                                className="h-50"),
                        dbc.Row(html.P(id='assess0', className="sbartext"), style={'padding-top': '0.5%'},
                                className="h-50"),
                        html.Br(),
                        dbc.Row(html.P('Risk Factors:', className="sbartext", style={'font-weight': '600'}),
                                style={'padding-top': '0.5%'},
                                className="h-50"),
                        dbc.Row(html.P(id='assess1', className="sbartext"), style={'padding-top': '0.5%'},
                                className="h-50"),
                        dbc.Row(html.P(id='assess2', className="sbartext"), style={'padding-top': '0.5%'},
                                className="h-50"),
                        dbc.Row(html.P(id='assess3', className="sbartext"), style={'padding-top': '0.5%'},
                                className="h-50")
                    ]), width=11),
            ], style={'height': '15vH', 'padding-top': '0.5%'}),
            dbc.Row([
                dbc.Col(html.Div(id='sbar_s', style={'background-color': c_red},
                                 children=[
                                     html.Img(src='/assets/r_high.png', id='image_b',
                                              style={'width': '60px', 'height': '60px'})]),
                        width=1),
                dbc.Col(dbc.Container(
                    children=[
                        dbc.Row(html.P(id='response0', className="sbartext", style={'font-weight': '600'}),
                                style={'padding-top': '1%'}, className="h-50"),
                        dbc.Row(html.P(id='response1', className="sbartext"), style={'padding-top': '1%'},
                                className="h-50"),
                        dbc.Row(html.P(id='response2', className="sbartext"), style={'padding-top': '1%'},
                                className="h-50"),
                        dbc.Row(html.P(id='response3', className="sbartext"), style={'padding-top': '1%'},
                                className="h-50"),
                    ]), width=11),
            ], style={'height': '7.5vH'})

        ])


def gen_infobar():
    return html.Div(
        id='infobar',
        style={'height': '80%', 'margin-top': '17.5%', 'padding-top': '2.5vH', 'color': 'black',
               'border': '3px solid',
               'border-color': '#319997', 'border-radius': '25px', 'padding': '10px'},
        children=[
            dbc.Row(dbc.Col(dbc.Container(
                children=[
                    dbc.Row(html.H5(id='', children='Local COVID Testing', className="sbarheader_r"), justify="center",
                            align="center", className="h-50"),
                ]), width=12), style={'padding-top': '0.5vH', 'height': '5vH'}),
            dbc.Row([
                dbc.Col(dbc.Container(
                    children=[
                        dbc.Row(html.P(children='', className="sbartext_r"), style={'padding-top': '0.5%'},
                                className="h-50"),
                        dbc.Row(html.P(children='', className="sbartext_r"), style={'padding-top': '0.5%'},
                                className="h-50"),
                    ]), width=12),
            ], style={'height': '10vH'}),
            dbc.Row([
                dbc.Col(dbc.Container(
                    children=[
                        dbc.Row(html.P(children='', className="sbartext_r"), style={'padding-top': '1%'},
                                className="h-50"),
                        dbc.Row(html.P(children='', className="sbartext_r"), style={'padding-top': '1%'},
                                className="h-50"),
                        dbc.Row(html.P(children='', className="sbartext_r"), style={'padding-top': '1%'},
                                className="h-50"),
                    ]), width=12),
            ], style={'height': '8.5vH'}),
            dbc.Row([
                dbc.Col(dbc.Container(
                    children=[
                        dbc.Row(html.P(className="sbartext_r"), style={'padding-top': '1%'}, className="h-50"),
                        dbc.Row(html.P(className="sbartext_r"), style={'padding-top': '1%'}, className="h-50"),
                        dbc.Row(html.P(className="sbartext_r"), style={'padding-top': '1%'}, className="h-50"),
                        dbc.Row(html.P(className="sbartext_r"), style={'padding-top': '1%'}, className="h-50"),
                    ]), width=12),
            ], style={'height': '12.5vH'}),
            dbc.Row([
                dbc.Col(dbc.Container(
                    children=[
                        dbc.Row(html.P(className="sbartext_r"), style={'padding-top': '1%'}, className="h-50"),
                        dbc.Row(html.P(className="sbartext_r"), style={'padding-top': '1%'}, className="h-50"),
                        dbc.Row(html.P(className="sbartext_r"), style={'padding-top': '1%'}, className="h-50"),
                        dbc.Row(html.P(className="sbartext_r"), style={'padding-top': '1%'}, className="h-50"),
                    ]), width=12),
            ], style={'height': '0.5'}),
            html.Br(),
            html.Br(),
            html.Div([html.Button(id='print_pdf', children='Print', n_clicks=0)],
                     style={'display': 'inline-block'})
        ])

    # return html.Div(
    #     id='info_bar',
    #     style={'height': '80%', 'margin-top': '20%', 'padding-top': '2.5vH', 'color': 'black',
    #            'border': '0.25px solid',
    #            'border-color': '#319997', 'border-radius': '25px', 'padding': '10px'},
    #     children=[
    #         dbc.Row([
    #             dbc.Col(html.Div(id='infotitle', style={'padding-top': '1%'},
    #                              children=[html.P('Local COVID Testing Centres', className="sbarheader_r")]), width=12)],
    #             style={'padding-top': '0.5vH', 'height': '5vH'}),
    #         dbc.Row([
    #             dbc.Col(html.Div(id='info1', style={'padding-top': '1%'},
    #                              children=[html.P('University of Reading', className="sbartext_r")]), width=12)],
    #             style={'padding-top': '0.5vH', 'height': '5vH'}),
    #         dbc.Row([
    #             dbc.Col(html.Div(id='info2', style={'padding-top': '1%'},
    #                              children=[html.P('Prospect Park', className="sbartext_r")]), width=12)],
    #             style={'padding-top': '0.5vH', 'height': '5vH'})
    #     ])


#############################################    Local Functions   #####################################################
# @app.callback(Output('1', ''),
#               Input('print_pdf', 'n_clicks'))
# def pdfoutput(btn):
#
#     ctx1 = dash.callback_context
#     if not ctx1.triggered:
#         input_id = 'No clicks yet'
#     else:
#         rendered = render_template('pdf_template.html', app)
#         pdf = pdfkit.from_string(rendered, False)
#         response = make_response(pdf)
#         response.headers['Content-Type'] = 'application/pdf'
#         response.headers['Content-Disposition'] = 'attachment; filename=c:/output.pdf'
#
#     return ''


@flask_app.callback([Output('settingstr', 'children'), Output('situation0', 'children'), Output('situation1', 'children'),
               Output('background0', 'children'), Output('background1', 'children'), Output('background2', 'children'),
               Output('assess0', 'children'), Output('assess1', 'children'), Output('assess2', 'children'),
               Output('assess3', 'children'), Output('response0', 'children'), Output('response1', 'children'),
               Output('response2', 'children'), Output('response3', 'children')],
              Input('session', 'data'))
def update_data(data):
    sbarsource = 'community'

    setting_str, situation, background1, background2, symptom_str, womanrisk_str, babyrisk_str, \
    treatments_str, outcome1_str, outcome2_str, risk, vaccine_str, pstatus = getsbardata(data, sbarsource)

    class sbar:
        """ Point class represents and manipulates x,y coords. """

        def __init__(self):
            self.setting = ''
            self.risk = ''
            self.situation0 = ''
            self.situation1 = ''
            self.background0 = ''
            self.background1 = ''
            self.background2 = ''
            self.assess0 = ''
            self.assess1 = ''
            self.assess2 = ''
            self.assess3 = ''
            self.response0 = ''
            self.response1 = ''
            self.response2 = ''
            self.response3 = ''
            self.name = ''
            self.nhs = ''
            self.dob = ''
            self.mob = ''
            self.date = ''

    test = 'banana'
    sbar_fill = sbar()

    if data['page_src'] == 'community':
        sbar_fill.name = 'Ms %s' % data['surname_d']
        sbar_fill.nhs = data['nhs_d']
        sbar_fill.dob = data['doby_d']
        sbar_fill.mob = data['tel_d']
        if pstatus == 'AN':
            sbar_fill.date = 'EDD %s' % data['edd_d']
        elif pstatus == 'PN':
            sbar_fill.date = 'Delivered %s' % data['deldate_d']
        sbar_fill.setting = setting_str
        sbar_fill.risk = risk
        sbar_fill.situation0 = str(situation[0])
        sbar_fill.situation1 = str(situation[1])
        sbar_fill.background0 = background1
        if background2:
            sbar_fill.background1 = background2
            sbar_fill.background2 = vaccine_str
        else:
            sbar_fill.background1 = vaccine_str

        sbar_fill.assess0 = symptom_str
        sbar_fill.assess1 = 'Woman:  ' + womanrisk_str
        sbar_fill.assess2 = 'Baby:  ' + babyrisk_str
        sbar_fill.assess3 = treatments_str
        sbar_fill.response0 = outcome1_str
        sbar_fill.response1 = outcome2_str
        sbar_fill.response2 = ''
        sbar_fill.response3 = ''

        setting = 'community'
        completeReport(sbar_fill, setting)

    return sbar_fill.setting, sbar_fill.situation0, sbar_fill.situation1, sbar_fill.background0, \
           sbar_fill.background1, sbar_fill.background2, sbar_fill.assess0, sbar_fill.assess1, \
           sbar_fill.assess2, sbar_fill.assess3, sbar_fill.response0, sbar_fill.response1, sbar_fill.response2, \
           sbar_fill.response3


#############################################    Local Functions   #####################################################


#############################################      Layout Div      #####################################################

# Banner
banner = banner_main

# Left column
left_bar = html.Div(
    id="left-column",
    className="two columns",
    style={'position': 'absolute', 'background-color': '#fcfcfc', 'left': 0, 'padding-left': '60px',
           'top': '6.275vH', 'height': '93.725vH', 'overflow': 'hidden'},
    children=[
        html.Div(
            id="s_1",
            style={'position': 'relative', 'width': '100%', 'justify-content': 'center',
                   'padding-left': '7.5%', 'right': '0'},
            children=[]
        ),

    ])
# 'z-index': '2000'
# Right column
layout = html.Div(
    id="right-column",
    className="ten columns",
    style={'position': 'absolute', 'background-color': '#f3fffe', 'left': '12.5%', 'padding': '1.55%',
           'width': '87.5%', 'height': '93.75vH', 'top': '8vH', 'flex-direction': 'column', 'overflow': 'auto',
           },
    children=[
        html.Div(
            id="i_1",
            className='text-center',
            style={'position': 'relative', 'width': '100%', 'justify-content': 'center',
                   'left': '0', 'right': '0', 'top': 0, 'bottom': 10},
            children=[
                html.Img(src='/assets/communityStream.png', style={'height': '17.0vW'})
            ]
        ),
        html.Div(
            id="i_2",
            style={'position': 'relative', 'width': '100%', 'justify-content': 'center', 'display': 'table',
                   'vertical-align': 'top',
                   'left': '0', 'right': '0', 'bottom': '0', 'top': '10'},
            children=[html.Div(
                children=[
                    html.Div(id="i_2l",
                             style={'float': 'left',
                                    'width': '60%', 'height': '60%',
                                    'padding': '10px',
                                    'justify-content': 'center'},
                             children=[
                                 gen_sbar()
                             ]),
                    html.Div(id="i_2r",
                             style={'float': 'left',
                                    'width': '35%', 'height': '60%',
                                    'padding': '10px',
                                    'justify-content': 'center'},
                             children=[
                                 gen_infobar()
                             ])
                ],
            )],
        ),

    ])

############################################
