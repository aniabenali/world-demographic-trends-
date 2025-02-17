import dash
from dash import dcc, html, Input, Output
from dash.exceptions import PreventUpdate
from dash import ctx
from dash import State
import plotly.graph_objects as go
import logging
from config import config as cfg
from util import (
    get_data, generate_choropleth, generate_time_series,
    generate_age_structure_chart, generate_donut_chart, generate_stacked_histogram, get_continent, clean_label
)

# Configuration du logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Charger les données
data = {key: get_data(key) for key in cfg['data_files']}

# Indicateurs pour l'histogramme (Ajout de "pop_urbaine_modif")
histogram_indicators = {
    "esperance_de_vie_modif": "Espérance de vie",
    "taux_fertilite_femme_modif": "Taux de fertilité",
    "natalite_modif": "Taux de natalité",
    "pop_urbaine_modif": "Population urbaine"  # ✅ Remplacement
}

# Couleurs associées aux continents
continent_colors = {
    "A": "#FFA07A",  # Afrique
    "N": "#FFD700",  # Amérique du Nord
    "S": "#9370DB",  # Amérique du Sud
    "As": "#90EE90",  # Asie
    "E": "#87CEEB",  # Europe
    "O": "#FF69B4",  # Océanie
}

# **📌 Mapping des Continents avec une seule lettre**
continent_abbr = {
    "Afrique": "A",
    "Amérique du Nord": "N",
    "Amérique du Sud": "S",
    "Asie": "As",
    "Europe": "E",
    "Océanie": "O"
}

# Indicateurs disponibles dans la liste déroulante (Ajout de "pop_0_14_modif")
dropdown_indicators = {key: value for key, value in data.items() if key not in histogram_indicators}
dropdown_indicators["pop_de_0_14_modif"] = data.get("pop_de_0_14_modif")  # ✅ Ajout

# Initialisation de l'application Dash
app = dash.Dash(__name__, suppress_callback_exceptions=True,assets_folder="assets")
#app.title = "Évolution démographique mondiale"

# Layout de l'application
app.layout = html.Div(id="app-container",className="container", children=[
    html.Button("☰", id="toggle-nav", n_clicks=0, className="toggle-button"),
    # Nav-Bar (20% de la largeur, s'étend sur toute la hauteur)
    html.Div(id="nav-bar",className="nav-bar", children=[
        html.H3("Paramètres", className="nav-title"),
        html.Div(className="nav-section", children=[
            html.Label("Sélectionnez une année :", className="dropdown-label"),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': str(year), 'value': year} for year in cfg['Years'] if year < 2023],
                value=cfg['Years'][-2],
                className="dcc-dropdown"
            ),
        ]),
        html.Div(className="nav-section", children=[
            html.Label("Sélectionnez un pays :", className="dropdown-label"),
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in data['esperance_de_vie_modif']['Country Name'].unique()],
                value='France',
                className="dcc-dropdown"
            ),
        ]),
        html.Div(className="nav-section", children=[
            html.Label("Sélectionnez des indicateurs :", className="dropdown-label"),
            dcc.Dropdown(
                id='indicator-dropdown',
                options=[{'label': clean_label(key), 'value': key} for key in dropdown_indicators],
                value=["esperance_de_vie_modif"],
                multi=True,
                className="dcc-dropdown"
            ),
        ]),


        # Menu de sélection pour le donut
        html.Div(className="nav-section", children=[
            html.Label("Sélectionnez les indicateurs pour le donut :", className="dropdown-label"),
            dcc.Dropdown(
                id='donut-indicator-dropdown',
                options=[
                    {'label': "Croissance de la population", 'value': 'croissance_de_la_pop_modif'},
                    {'label': "PIB", 'value': 'PIB_modif'},
                    {'label': "Migration nette", 'value': 'migration_nette_modif'},
                    {'label': "Population réfugiée", 'value': 'pop_refugie_modif'}
                ],
                value=['PIB_modif'],
                multi=True,
                className="dcc-dropdown"
            ),
        ]),
    ],style={"display": "block"}),

    # Zone principale (80% de la largeur)
    html.Div(id="main-content",className="main-content", children=[
        html.H1("Évolution démographique mondiale", id="main-title", className="main-title-class"),
        # En haut : Carte choroplèthe et histogramme/série temporelle
        html.Div(className="top-section", children=[
            # Carte choroplèthe
            html.Div(className="graph-wrapper", children=[
                dcc.Graph(id='choropleth-map', className="graph", style={'height': '280px', 'width': '97%'})
            ]),
            # Histogramme/série temporelle
            html.Div(className="graph-wrapper", children=[
                # Checklist des indicateurs pour l'histogramme
                html.Div(className="indicators-container", children=[
                    html.Label("Sélectionnez les indicateurs à afficher :", className="dropdown-label"),
                    dcc.Checklist(
                        id='histogram-indicators',
                        options=[{'label':clean_label(label),  'value': key} for key, label in histogram_indicators.items()],
                        value=['esperance_de_vie_modif'],
                        inline=True,
                        className="dcc-checklist"
                    ),
                ]),
                dcc.Graph(id='time-series-histogram', className="graph", style={'height': '100%'} ),
            ]),
        ]),

        # En bas : Donut à gauche et diagramme en barres à droite
        html.Div(className="bottom-section", children=[
            # Donut à gauche (plus large)
            html.Div(className="graph-wrapper donut-container", children=[
                dcc.Graph(id='donut-chart', className="graph",style={'height': '280px', 'width': '95%'}),
                # Légende intégrée dans le donut
                html.Div(className="legend-container", children=[
                    html.H4(className="legend-title"),
                    html.Div([
                        html.Div(className="legend-box", children=[
                            html.Div(style={'backgroundColor': continent_colors[abbr]}),
                            html.Span(f"{abbr} = {name}", className="legend-text")
                        ]) for name, abbr in continent_abbr.items()
                    ]),html.Div(id='donut-selected-year', className="legend-year")
                ]),
            ]),
            # Diagramme en barres à droite (moins large)
            html.Div(className="graph-wrapper bar-container", children=[
                dcc.Graph(id='age-structure', className="graph", style={'height': '305px', 'width': '100%'})
            ]),
        ]),
    ]),
])
# Callbacks
@app.callback(
    [Output('choropleth-map', 'figure'),
     Output('time-series-histogram', 'figure')],
    [Input('year-dropdown', 'value'),
     Input('country-dropdown', 'value'),
     Input('indicator-dropdown', 'value'),
     Input('histogram-indicators', 'value')]
)
def update_graphs(year, country, selected_indicators, selected_histogram_indicators):
    choropleth_fig = generate_choropleth(data, selected_indicators[0] if selected_indicators else "esperance_de_vie_modif", year, country)

    # Créer une figure vide par défaut
    time_series_fig = go.Figure()

    # Ajouter les courbes si des indicateurs sont sélectionnés
    if selected_indicators:
        time_series_fig = generate_time_series(data, [country], selected_indicators)

    # Ajouter les histogrammes si des indicateurs sont cochés
    if selected_histogram_indicators:
        histogram_fig = generate_stacked_histogram(data, country, selected_histogram_indicators)

        for trace in histogram_fig.data:
            trace.marker.opacity = 0.7  # Semi-transparent
            trace.yaxis = "y2"
            time_series_fig.add_trace(trace)

    # ✅ Modifier la position de la légende (haut-droite)
    time_series_fig.update_layout(
        legend=dict(
            x=1.05,  # 🔹 Placer la légende légèrement en dehors du graphique
            y=1.3,  # 🔹 Monter encore plus haut
            xanchor="left",
            yanchor="top",
            font=dict(size=12, color="white"),
            bgcolor="rgba(0,0,0,0)",  # Fond transparent pour éviter d'obscurcir
        ),
        yaxis2=dict(
            overlaying="y",
            side="right",
            showgrid=False
        ),
        plot_bgcolor="rgba(0,0,0,0)",  # ✅ Supprimer le fond gris
        paper_bgcolor="#1E2B38",  # ✅ Fond principal
        font=dict(color="white"),  # ✅ Texte blanc pour lisibilité
        margin=dict(l=20, r=150, t=80, b=50)  # 🔹 Augmenter la marge à droite pour laisser de la place
    )

    return choropleth_fig, time_series_fig


@app.callback(
    Output('age-structure', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('country-dropdown', 'value')]
)
def update_age_structure(year, country):
    return generate_age_structure_chart(data, year, [country])

@app.callback(
    [Output('donut-chart', 'figure'),
     Output('donut-selected-year', 'children')],  # ✅ Ajout de l'Output pour l'année
    [Input('year-dropdown', 'value'),  # ✅ Utilise l'année sélectionnée dans le dropdown principal
     Input('donut-indicator-dropdown', 'value')]
)
def update_donut_chart(selected_year, selected_indicators):
    if not selected_indicators:
        return go.Figure(), f"Année : {selected_year}"  # ✅ Affiche l'année même si le donut est vide

    fig = go.Figure()
    hole_size = 0.25  # Taille du premier trou

    for idx, indicator in enumerate(selected_indicators):
        if indicator not in data:
            continue

        df = data[indicator]

        if str(selected_year) not in df.columns:
            logging.warning(f"⚠️ Année {selected_year} non disponible pour {indicator}")
            continue

        df_filtered = df[['Country Name', str(selected_year)]].dropna()
        df_filtered["Continent"] = df_filtered["Country Name"].apply(get_continent)

        df_filtered["Continent"] = df_filtered["Continent"].apply(lambda x: continent_abbr.get(x, None))
        df_filtered = df_filtered.dropna(subset=["Continent"])
        continent_sums = df_filtered.groupby("Continent")[str(selected_year)].sum().to_dict()

        # ✅ **Normalisation en pourcentage**
        total = sum(continent_sums.values())
        if total > 0:
            continent_sums = {key: (value / total) * 100 for key, value in continent_sums.items()}

        if not continent_sums or all(value == 0 for value in continent_sums.values()):
            logging.warning(f"⚠️ Pas de données exploitables pour {indicator}")
            continue

        # **Ajout d'un Donut avec des labels bien espacés**
        fig.add_trace(go.Pie(
            labels=list(continent_sums.keys()),
            values=[round(v, 2) for v in continent_sums.values()],
            hole=hole_size,
            name=indicator.replace('_modif', '').replace('_', ' '),
            textinfo='percent+label',
            textposition='outside',
            textfont_size=12,
            marker=dict(colors=[continent_colors[c] for c in continent_sums.keys()]),
            pull=[0.15] * len(continent_sums),
            insidetextorientation="horizontal",
            automargin=True,
            texttemplate='%{label}: %{value:.2f}%'
        ))

        hole_size += 0.12  # ✅ Ajuste la taille du trou pour bien coller les anneaux

    fig.update_layout(
        title_font_size=16,
        title_x=0.5,
        showlegend=False,  # ✅ Désactiver la légende Plotly pour éviter les doublons
        paper_bgcolor='#1E2B38',
        font=dict(color="white"),
        annotations=[dict(text="Indicateurs", x=0.5, y=0.5, font_size=18, showarrow=False)],
        margin=dict(l=20, r=20, t=50, b=10),
    )

    fig.update_layout(
        legend=dict(
            x=1,  # Positionne la légende à l'extérieur du graphique
            y=1,  # Place la légende en haut à droite
            xanchor="right",  # Ancre la légende sur le côté droit
            yanchor="top",  # Ancre la légende en haut
            bgcolor="rgba(0,0,0,0)"  # Fond transparent pour éviter qu'il ne cache les valeurs
        ),
        margin=dict(l=20, r=150, t=50, b=40),  # Ajoute un peu d'espace à droite pour la légende
        plot_bgcolor="rgba(0,0,0,0)",  # Supprime le fond gris
        paper_bgcolor="#1E2B38",  # Harmonise avec le fond général
        font=dict(color="white")  # Assure la lisibilité
    )

    return fig, f"Année : {selected_year}"



import dash
from dash import dcc, html, Input, Output
from dash.exceptions import PreventUpdate
from dash import ctx
from dash import State
import plotly.graph_objects as go
import logging
from config import config as cfg
from util import (
    get_data, generate_choropleth, generate_time_series,
    generate_age_structure_chart, generate_donut_chart, generate_stacked_histogram, get_continent, clean_label
)

# Configuration du logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Charger les données
data = {key: get_data(key) for key in cfg['data_files']}

# Indicateurs pour l'histogramme (Ajout de "pop_urbaine_modif")
histogram_indicators = {
    "esperance_de_vie_modif": "Espérance de vie",
    "taux_fertilite_femme_modif": "Taux de fertilité",
    "natalite_modif": "Taux de natalité",
    "pop_urbaine_modif": "Population urbaine"  # ✅ Remplacement
}

# Couleurs associées aux continents
continent_colors = {
    "A": "#FFA07A",  # Afrique
    "N": "#FFD700",  # Amérique du Nord
    "S": "#9370DB",  # Amérique du Sud
    "As": "#90EE90",  # Asie
    "E": "#87CEEB",  # Europe
    "O": "#FF69B4",  # Océanie
}

# **📌 Mapping des Continents avec une seule lettre**
continent_abbr = {
    "Afrique": "A",
    "Amérique du Nord": "N",
    "Amérique du Sud": "S",
    "Asie": "As",
    "Europe": "E",
    "Océanie": "O"
}

# Indicateurs disponibles dans la liste déroulante (Ajout de "pop_0_14_modif")
dropdown_indicators = {key: value for key, value in data.items() if key not in histogram_indicators}
dropdown_indicators["pop_de_0_14_modif"] = data.get("pop_de_0_14_modif")  # ✅ Ajout

# Initialisation de l'application Dash
app = dash.Dash(__name__, suppress_callback_exceptions=True,assets_folder="assets")
app.title = "Évolution démographique mondiale"

# Layout de l'application
app.layout = html.Div(id="app-container",className="container", children=[
    html.Button(" Masquer ⏩menu", id="toggle-nav", n_clicks=0, className="toggle-button"),
    # Nav-Bar (20% de la largeur, s'étend sur toute la hauteur)
    html.Div(id="nav-bar",className="nav-bar", children=[
        html.H3("Paramètres", className="nav-title"),
        html.Div(className="nav-section", children=[
            html.Label("Sélectionnez une année :", className="dropdown-label"),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': str(year), 'value': year} for year in cfg['Years'] if year < 2023],
                value=cfg['Years'][-2],
                className="dcc-dropdown"
            ),
        ]),
        html.Div(className="nav-section", children=[
            html.Label("Sélectionnez un pays :", className="dropdown-label"),
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in data['esperance_de_vie_modif']['Country Name'].unique()],
                value='France',
                className="dcc-dropdown"
            ),
        ]),
        html.Div(className="nav-section", children=[
            html.Label("Sélectionnez des indicateurs :", className="dropdown-label"),
            dcc.Dropdown(
                id='indicator-dropdown',
                options=[{'label': clean_label(key), 'value': key} for key in dropdown_indicators],
                value=["esperance_de_vie_modif"],
                multi=True,
                className="dcc-dropdown"
            ),
        ]),


        # Menu de sélection pour le donut
        html.Div(className="nav-section", children=[
            html.Label("Sélectionnez les indicateurs pour le donut :", className="dropdown-label"),
            dcc.Dropdown(
                id='donut-indicator-dropdown',
                options=[
                    {'label': "Croissance de la population", 'value': 'croissance_de_la_pop_modif'},
                    {'label': "PIB", 'value': 'PIB_modif'},
                    {'label': "Migration nette", 'value': 'migration_nette_modif'},
                    {'label': "Population réfugiée", 'value': 'pop_refugie_modif'}
                ],
                value=['PIB_modif'],
                multi=True,
                className="dcc-dropdown"
            ),
        ]),
    ],style={"display": "block"}),

    # Zone principale (80% de la largeur)
    html.Div(id="main-content",className="main-content", children=[
        # En haut : Carte choroplèthe et histogramme/série temporelle
        html.Div(className="top-section", children=[
            # Carte choroplèthe
            html.Div(className="graph-wrapper", children=[
                dcc.Graph(id='choropleth-map', className="graph", style={'height': '300px', 'width': '98%'})
            ]),
            # Histogramme/série temporelle
            html.Div(className="graph-wrapper", children=[
                # Checklist des indicateurs pour l'histogramme
                html.Div(className="indicators-container", children=[
                    html.Label("Sélectionnez les indicateurs à afficher :", className="dropdown-label"),
                    dcc.Checklist(
                        id='histogram-indicators',
                        options=[{'label':clean_label(label),  'value': key} for key, label in histogram_indicators.items()],
                        value=['esperance_de_vie_modif'],
                        inline=True,
                        className="dcc-checklist"
                    ),
                ]),
                dcc.Graph(id='time-series-histogram', className="graph", style={'height': '100%'} ),
            ]),
        ]),

        # En bas : Donut à gauche et diagramme en barres à droite
        html.Div(className="bottom-section", children=[
            # Donut à gauche (plus large)
            html.Div(className="graph-wrapper donut-container", children=[
                dcc.Graph(id='donut-chart', className="graph",style={'height': '280px', 'width': '95%'}),
                # Légende intégrée dans le donut
                html.Div(className="legend-container", children=[
                    html.H4(className="legend-title"),
                    html.Div([
                        html.Div(className="legend-box", children=[
                            html.Div(style={'backgroundColor': continent_colors[abbr]}),
                            html.Span(f"{abbr} = {name}", className="legend-text")
                        ]) for name, abbr in continent_abbr.items()
                    ]),html.Div(id='donut-selected-year', className="legend-year")
                ]),
            ]),
            # Diagramme en barres à droite (moins large)
            html.Div(className="graph-wrapper bar-container", children=[
                dcc.Graph(id='age-structure', className="graph", style={'height': '305px', 'width': '100%'})
            ]),
        ]),
    ]),
])
# Callbacks
@app.callback(
    [Output('choropleth-map', 'figure'),
     Output('time-series-histogram', 'figure')],
    [Input('year-dropdown', 'value'),
     Input('country-dropdown', 'value'),
     Input('indicator-dropdown', 'value'),
     Input('histogram-indicators', 'value')]
)
def update_graphs(year, country, selected_indicators, selected_histogram_indicators):
    choropleth_fig = generate_choropleth(data, selected_indicators[0] if selected_indicators else "esperance_de_vie_modif", year, country)

    # Créer une figure vide par défaut
    time_series_fig = go.Figure()

    # Ajouter les courbes si des indicateurs sont sélectionnés
    if selected_indicators:
        time_series_fig = generate_time_series(data, [country], selected_indicators)

    # Ajouter les histogrammes si des indicateurs sont cochés
    if selected_histogram_indicators:
        histogram_fig = generate_stacked_histogram(data, country, selected_histogram_indicators)

        for trace in histogram_fig.data:
            trace.marker.opacity = 0.7  # Semi-transparent
            trace.yaxis = "y2"
            time_series_fig.add_trace(trace)

    # ✅ Modifier la position de la légende (haut-droite)
    time_series_fig.update_layout(
        legend=dict(
            x=1.05,  # 🔹 Placer la légende légèrement en dehors du graphique
            y=1.3,  # 🔹 Monter encore plus haut
            xanchor="left",
            yanchor="top",
            font=dict(size=12, color="white"),
            bgcolor="rgba(0,0,0,0)",  # Fond transparent pour éviter d'obscurcir
        ),
        yaxis2=dict(
            overlaying="y",
            side="right",
            showgrid=False
        ),
        plot_bgcolor="rgba(0,0,0,0)",  # ✅ Supprimer le fond gris
        paper_bgcolor="#1E2B38",  # ✅ Fond principal
        font=dict(color="white"),  # ✅ Texte blanc pour lisibilité
        margin=dict(l=20, r=150, t=80, b=50)  # 🔹 Augmenter la marge à droite pour laisser de la place
    )

    return choropleth_fig, time_series_fig


@app.callback(
    Output('age-structure', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('country-dropdown', 'value')]
)
def update_age_structure(year, country):
    return generate_age_structure_chart(data, year, [country])

@app.callback(
    [Output('donut-chart', 'figure'),
     Output('donut-selected-year', 'children')],  # ✅ Ajout de l'Output pour l'année
    [Input('year-dropdown', 'value'),  # ✅ Utilise l'année sélectionnée dans le dropdown principal
     Input('donut-indicator-dropdown', 'value')]
)
def update_donut_chart(selected_year, selected_indicators):
    if not selected_indicators:
        return go.Figure(), f"Année : {selected_year}"  # ✅ Affiche l'année même si le donut est vide

    fig = go.Figure()
    hole_size = 0.25  # Taille du premier trou

    for idx, indicator in enumerate(selected_indicators):
        if indicator not in data:
            continue

        df = data[indicator]

        if str(selected_year) not in df.columns:
            logging.warning(f"⚠️ Année {selected_year} non disponible pour {indicator}")
            continue

        df_filtered = df[['Country Name', str(selected_year)]].dropna()
        df_filtered["Continent"] = df_filtered["Country Name"].apply(get_continent)

        df_filtered["Continent"] = df_filtered["Continent"].apply(lambda x: continent_abbr.get(x, None))
        df_filtered = df_filtered.dropna(subset=["Continent"])
        continent_sums = df_filtered.groupby("Continent")[str(selected_year)].sum().to_dict()

        # ✅ **Normalisation en pourcentage**
        total = sum(continent_sums.values())
        if total > 0:
            continent_sums = {key: (value / total) * 100 for key, value in continent_sums.items()}

        if not continent_sums or all(value == 0 for value in continent_sums.values()):
            logging.warning(f"⚠️ Pas de données exploitables pour {indicator}")
            continue

        # **Ajout d'un Donut avec des labels bien espacés**
        fig.add_trace(go.Pie(
            labels=list(continent_sums.keys()),
            values=[round(v, 2) for v in continent_sums.values()],
            hole=hole_size,
            name=indicator.replace('_modif', '').replace('_', ' '),
            textinfo='percent+label',
            textposition='outside',
            textfont_size=12,
            marker=dict(colors=[continent_colors[c] for c in continent_sums.keys()]),
            pull=[0.15] * len(continent_sums),
            insidetextorientation="horizontal",
            automargin=True,
            texttemplate='%{label}: %{value:.2f}%'
        ))

        hole_size += 0.12  # ✅ Ajuste la taille du trou pour bien coller les anneaux

    fig.update_layout(
        title_font_size=16,
        title_x=0.5,
        showlegend=False,  # ✅ Désactiver la légende Plotly pour éviter les doublons
        paper_bgcolor='#1E2B38',
        font=dict(color="white"),
        annotations=[dict(text="Indicateurs", x=0.5, y=0.5, font_size=18, showarrow=False)],
        margin=dict(l=20, r=20, t=50, b=10),
    )

    fig.update_layout(
        legend=dict(
            x=1,  # Positionne la légende à l'extérieur du graphique
            y=1,  # Place la légende en haut à droite
            xanchor="right",  # Ancre la légende sur le côté droit
            yanchor="top",  # Ancre la légende en haut
            bgcolor="rgba(0,0,0,0)"  # Fond transparent pour éviter qu'il ne cache les valeurs
        ),
        margin=dict(l=20, r=150, t=50, b=40),  # Ajoute un peu d'espace à droite pour la légende
        plot_bgcolor="rgba(0,0,0,0)",  # Supprime le fond gris
        paper_bgcolor="#1E2B38",  # Harmonise avec le fond général
        font=dict(color="white")  # Assure la lisibilité
    )

    return fig, f"Année : {selected_year}"



@app.callback(
    [Output("nav-bar", "className"),
     Output("main-content", "className"),
     Output("toggle-nav", "children")],
    [Input("toggle-nav", "n_clicks")],
    [State("nav-bar", "className"), State("main-content", "className")]
)
def toggle_sidebar(n_clicks, nav_class, main_class):
    if n_clicks % 2 == 1:
        return "nav-bar hidden", "main-content expanded", "⏪ Afficher le menu"
    else:
        return "nav-bar", "main-content", "⏩ Masquer le menu"

server = app.server
if __name__ == '__main__':
    app.run_server(debug=False)

