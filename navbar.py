import dash_bootstrap_components as dbc
import dash_html_components as html


def navbar_comp():
    return dbc.NavbarSimple(
        children=[
            html.Div(
                dbc.NavItem(dbc.NavLink("Home", href="/home")),
                style={'font-size': '1.5rem', 'margin-right': '15px', 'margin-top': '7.5%'}),
            html.Div(
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Telephone", href="/telephonetriage", style={'font-size': '1.3rem'}),
                        dbc.DropdownMenuItem("Community", href="/communitytriage", style={'font-size': '1.3rem'}),
                        dbc.DropdownMenuItem("RBH Front Door", href="/rbhtriage", style={'font-size': '1.3rem'}),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Triage Assessments",
                ), style={'font-size': '1.5rem', 'margin-left': '15px', 'margin-right': '15px', 'margin-top': '7.5%'}),
            html.Div(
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Mother", href="/datamother", style={'font-size': '1.3rem'}),
                        dbc.DropdownMenuItem("Fetus", href="/datafetus", style={'font-size': '1.3rem'}),
                        dbc.DropdownMenuItem("Baby", href="/datababy", style={'font-size': '1.3rem'}),
                        dbc.DropdownMenuItem("Laboratory", href="/datalab", style={'font-size': '1.3rem'}),
                        dbc.DropdownMenuItem("Physiology", href="/dataphys", style={'font-size': '1.3rem'}),
                        dbc.DropdownMenuItem("Outcomes", href="/dataoutcomes", style={'font-size': '1.3rem'}),

                    ],
                    nav=True,
                    in_navbar=True,
                    label="Database",
                ), style={'font-size': '1.5rem', 'margin-left': '15px', 'margin-right': '15px', 'margin-top': '7.5%'}),
            html.Div(
                dbc.NavItem(dbc.NavLink("About", href="/about")),
                style={'font-size': '1.5rem', 'margin-left': '15px', 'margin-right': '15px', 'margin-top': '7.5%'}),
            html.Div(
                dbc.NavItem(dbc.NavLink("Menu", href="/menu")),
                style={'font-size': '1.5rem', 'margin-left': '15px', 'margin-right': '15px', 'margin-top': '7.5%'}),

        ],
        style={'position': 'absolute', 'font-size': '1.3rem', 'margin-top': '10px', 'left': '0', 'font:color': 'white',
               'text-decoration': 'none important!'},
        color='#00ACAD',
        dark=False)
