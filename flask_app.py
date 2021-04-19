from flask import Flask
import dash_html_components as html
import pathlib
import base64
import io
import dash
from dash import Dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_table

server = Flask(__name__)
flask_app = dash.Dash(
    __name__,
    server=server,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],

)


flask_app.title = 'Maternity Information System'
server = flask_app.server
flask_app.config.suppress_callback_exceptions = True

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()
