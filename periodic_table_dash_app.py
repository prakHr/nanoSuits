import pymatgen.core as pg
from pymatgen.core import Element
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Fetch details of an Element
def get_atomic_mass_of_an_element(element_name):
    element = pg.Element(element_name)
    atomic_mass = element.Z
    return atomic_mass

# Get all elements
def get_all_elements():
    elements = list(Element)
    element_names = []
    for element in elements:
        element_names += [str(element)]
    return element_names

def create_app():
    element_names = get_all_elements()
    themess = [
        theme for theme in dir(dbc.themes)
        if not theme.startswith("_")
    ]   

    themes = {}
    for theme in themess:
        themes[f"{theme}"] = eval(f"dbc.themes.{theme}")
    
    app = Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

    app.layout = dbc.Container([
        html.Link(
            id="theme-link",
            rel="stylesheet",
            href=dbc.themes.BOOTSTRAP
        ),
        html.H1(
            "Periodic Table Element Explorer",
            className="text-center my-4"
        ),
        html.Hr(),
        # Theme selector
        dbc.Row([
            dbc.Col([
                dbc.Label("Select Application Theme"),
                dcc.Dropdown(
                    options=[
                        {"label": name, "value": name}
                        for name in themes.keys()
                    ],
                    value="BOOTSTRAP",
                    id="theme-dropdown",
                    clearable=False
                )

            ], width=6)
        ], justify="center", className="mb-4"),
        # Element selector
        dbc.Row([
            dbc.Col([
                dbc.Label("Select an Element"),
                dcc.Dropdown(
                    options=[
                        {"label": element, "value": element}
                        for element in element_names
                    ],
                    value=element_names[0],
                    id="demo-dropdown",
                    clearable=False
                )
            ], width=6)
        ], justify="center", className="mb-4"),
        # Output section
        dbc.Card([
            dbc.CardBody([
                html.H4("Element Information"),
                html.Div(
                    id="dd-output-container",
                    className="mt-3"
                )
            ])
        ], className="mt-4")

    ], fluid=True, className="p-4")


    # Update element information
    @app.callback(
        Output("dd-output-container", "children"),
        Input("demo-dropdown", "value")
    )
    def update_output(atomic_element_name):
        atomic_mass = get_atomic_mass_of_an_element(atomic_element_name)
        return dbc.Alert(
            f"The atomic number of {atomic_element_name} is: {atomic_mass}",
            color="success"
        )
    # Dynamically change theme
    @app.callback(
        Output("theme-link", "href"),
        Input("theme-dropdown", "value")
    )
    def update_theme(theme_name):
        return themes[theme_name]
    return app

def run_dash_app(app):
    app.run(debug=True)

if __name__ == "__main__":
    app = create_app()
    run_dash_app(app)
