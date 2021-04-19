import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas
import datetime as dt
import datetime
import time
from dash.dependencies import Input, Output
from flask_app import flask_app
date_a = datetime.datetime.now().strftime("%d %b %Y")

def sidebar_comp():
    return html.Div(
        id="sidebar_comp",
        className="sidebar-1",
        style={},
        children=[
            html.Div(
                [
                html.P("Date: %s" % date_a, style={'font-weight':'600'})

            ])

        ])
