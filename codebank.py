import dash_html_components as html
from navbar import navbar_comp
from flask_app import flask_app
import datetime as datetime
import dash_bootstrap_components as dbc
import dash_html_components as html
import re

############################################      Colour codes      ####################################################

c_green1 = 'rgb(225, 249, 248)'
c_green2 = 'rgb(228, 244, 243)'
c_green3 = 'rgb(0, 172, 173)'
c_green4 = 'rgb(49, 153, 151)'
c_blue = 'rgb(39, 52, 139)'
c_orange = 'rgb(234, 91, 12)'
c_red = 'rgb(229, 27, 32)'


#########################################      Universal Functions      ################################################

def valid_date(datestring):
    try:
        mat = re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', datestring)
        if mat is not None:
            datetime.datetime(*(map(int, mat.groups()[-1::-1])))
            return True
    except ValueError:
        pass
    return False

#############################################      Layout Div      #####################################################

right_style1 = {'position': 'absolute', 'background-color': '#e4f4f3', 'left': '12.5%',
           'width': '88.15%', 'height': '92vH', 'top': '8vH'}

right_style4 = {'position': 'relative', 'width': '100%', 'justify-content': 'center',
                   'left': '0', 'right': '0'}

left_style1 = {'position': 'absolute', 'background-color': '#fcfcfc', 'left': 0, 'padding-left': '50px',
           'height': '92vH', 'top': '6.3vH', 'padding': '1.5%'}

left_style2 = {'position': 'absolute', 'width': '100%', 'justify-content': 'center',
                   'padding-left': '7.5%', 'right': '0'}

banner_style1 = {'display': 'flex', 'height': '8vH', 'width': '100vW'},

triage_style1 = {'position': 'absolute', 'float': 'center', 'border': '3px solid #319997', 'border-radius': '6px',
                 'margin': '1.5%', 'padding': '1%', 'width': '92%'}

triage_style2 = {'border': '1px solid #319997', 'border-radius': '6px', 'padding': '0.5%',
                 'padding-bottom': '20px'}

triage_style3 = {'border': '1px solid #319997', 'border-radius': '6px', 'padding': '0.5%',
                 'padding-bottom': '20px'}
triage_style4 = {'border': '1px solid #319997', 'border-radius': '6px', 'padding': '0.5%',
                 'padding-bottom': '20px'}

triage_btn1_style = {'position': 'absolute', 'top': '15%', 'bottom': '10%', 'width': '100%',
                     'justify-content': 'center',
                     'left': 'auto', 'right': '5%'}
triage_btn2_style = {'position': 'relative', 'width': '100%', 'justify-content': 'center',
                     'left': '0', 'right': '0'}

banner_nosplash = html.Div(
    id="banner",
    className="banner",
    style={'position': 'relative', 'display': 'flex', 'height': '9vH', 'top': 0},
    children=[
        html.Div(
            id="sblogo",
            style={'position': 'absolute', 'left': 20, 'top': '10%', 'height': '5.75%'},
            children=[
                html.Img(src='/assets/navbar_notext.png.png', className="banner_Img2",
                         style={'position': 'absolute', 'height': '6.5vH'})]),
        html.Div([navbar_comp()], style={'position': 'relative', 'height': '0'},
                 ),
        html.Img(src='/assets/greennhs.png',
                 style={'position': 'relative', 'right': 10, 'height': '8.5vH'})
    ])

banner_splash = html.Div(
    id="banner",
    className="banner",
    style={'display': 'flex', 'height': '8vH', 'width': '100vW'},
    children=[
        dbc.Row([
            dbc.Col(
                html.Div(
                    html.Img(
                        src='/assets/navbar_notext.png',
                        className="banner_Img2",
                        style={'height': '6.5vH'})),
                style={'position': 'absolute', 'top': '0.5vH', 'opacity': 0, 'left': 5},
                width=2,
            ),
            dbc.Col(
                navbar_comp(),
                style={'position': 'absolute', 'left': '15%', 'top': '4.0vh', 'height': '0'},
                width=2
            ),
            dbc.Col(
                html.Div(),
                width=7,
            ),
            dbc.Col(
                html.Img(src='/assets/greennhs.png',
                         style={'position': 'relative', 'right': 10, 'height': '7.5vH'}),
                width=1,
                style={'position': 'absolute','right': 10, 'top': 1},
            ),

        ], style={'width': '100vW'})
    ]
)

banner_main = html.Div(
    id="banner",
    className="banner",
    style={'display': 'flex', 'height': '8vH', 'width': '100vW'},
    children=[
        dbc.Row([
            dbc.Col(
                html.Div(
                    html.Img(
                        src='/assets/navbar_notext.png',
                        className="banner_Img2",
                        style={'height': '6.5vH'})),
                style={'position': 'absolute', 'top': '0.5vH', 'opacity': 100, 'left': 5},
                width=2,
            ),
            dbc.Col(
                navbar_comp(),
                style={'position': 'absolute', 'left': '12.5%', 'top': '4.0vh', 'height': '0'},
                width=2
            ),
            dbc.Col(
                html.Div(),
                width=7,
            ),
            dbc.Col(
                html.Img(src='/assets/greennhs.png',
                         style={'position': 'relative', 'right': 0, 'height': '7.5vH'}),
                width=1,
                style={'position': 'absolute','right': 10, 'top': 1},
            ),

        ], style={'width': '100vW'})
    ]
)




