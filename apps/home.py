from navbar import navbar_comp
import dash_html_components as html
import datetime
from apps.codebank import *
from flask_app import flask_app
import dash_bootstrap_components as dbc
import dash_html_components as html
from apps.communitytriage import tri_community
from dash.dependencies import Input, Output, ClientsideFunction

#############################################    Local Functions   #####################################################

date_a = datetime.datetime.now().strftime("%d %b %Y")

def gen_sidebar():
    return html.Div(
        id="gen_sidebar",
        className="sidebar-1",
        style={},
        children=[
            html.Div(
                [
                    html.P("Date: %s" % date_a, style={'font-weight': '600'}),

                ])

        ])


def gen_splash():
    return html.Div(
        style={'position': 'absolute', 'margin': '0.2%', 'padding': '1%', 'width': '100%', 'top': '15vH'},
        id="gen_splash",
        children=[
            html.Div([
                html.Img(src='/assets/flogo_hq.png', style={'width': '60%', 'height': '35%'})

            ], className='text-center'),
            html.Br(),
            html.Br(),
            html.Div([
                html.Div([html.A(
                    html.Button(id="splash_btn_dash", children="Dashboard", n_clicks=0, className="button-large",
                                ), href='')], style={'width': '80%', 'padding': '10px', 'display': 'inline'}),

                html.Div(
                    [html.A(html.Button(id="splash_btn_triage", children="Triage", n_clicks=0, className="button-large",
                                        ), href='/telephonetriage')],
                    style={'width': '80%', 'padding': '10px', 'display': 'inline'}),

                html.Div([html.A(
                    html.Button(id="splash_btn_comm", children="Community", n_clicks=0, className="button-large",
                                ), href='/communitytriage')],
                    style={'width': '80%', 'padding': '10px', 'display': 'inline'}),

                html.Div([html.A(html.Button(id="splash_btn_rbh", children="RBH", n_clicks=0, className="button-large",
                                             ), href='/rbhtriage')],
                         style={'width': '80%', 'padding': '10px', 'display': 'inline'}),
            ], className='text-center')],
    )


#############################################      Layout Div      #####################################################

banner = banner_splash

# Left column
left_bar = html.Div(
    id="left-column",
    className="two columns",
    style={'position': 'relative', 'background-color': '#fcfcfc', 'left': 0, 'padding-left': '50px',
           'top': 0, 'height': '93.75vH', 'overflow-x': 'hidden'},
    children=[
        html.Div(
            id="s_1",
            style={'position': 'relative', 'width': '100%', 'justify-content': 'center',
                   'padding-left': '7.5%', 'right': '0'},
            children=[]
        ),

    ])

# Right column
layout = html.Div(
    id="right-column",
    className="ten columns",
    style={'position': 'absolute', 'background-color': '#f3fffe', 'left': '12.5%', 'padding': '2%',
           'width': '88.15%', 'height': '93.75vH', 'top': '8vH', 'flex-direction': 'column', 'overflow-y': 'auto'},
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
            children=[gen_splash()]
        )])

############################################     Home Callbacks    #####################################################
