import pandas as pd
import plotly.express as px
import logging
import os
import pycountry
import plotly.graph_objects as go
import pycountry_convert as pc
from config import config as cfg
from figure_util import (
    create_choropleth, create_time_series,
    create_histogram_with_time_series, create_age_structure_chart, create_donut_chart
)

# Configuration du logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def get_continent(country_name):
    """ Retourne le continent d'un pays donné en utilisant pycountry_convert. """
    try:
        country_code = pc.country_name_to_country_alpha2(country_name)
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        continent_map = {
            "AF": "Afrique",
            "AS": "Asie",
            "EU": "Europe",
            "NA": "Amérique du Nord",
            "SA": "Amérique du Sud",
            "OC": "Océanie"
        }
        return continent_map.get(continent_code, "Autre")
    except Exception:
        logging.warning(f"⚠️ Pays inconnu : {country_name}")
        return "Autre"


def translate_country_names(df):
    """ Traduit les noms des pays dans la colonne 'Country Name' en utilisant pycountry. """
    if "Country Name" not in df.columns:
        logging.warning("⚠️ La colonne 'Country Name' est manquante dans le DataFrame.")
        return df

    def translate_name(country_name):
        try:
            country = pycountry.countries.get(name=country_name)
            return country.name if country else country_name
        except Exception:
            return country_name

    df["Country Name"] = df["Country Name"].apply(translate_name)
    logging.info("✅ Noms des pays traduits avec succès.")
    return df



def aggregate_by_continent(df):
    """ Regroupe les valeurs par continent en sommant les indicateurs des pays. """
    if "Continent" not in df.columns:
        logging.error("❌ La colonne 'Continent' est absente du DataFrame.")
        return None

    for col in df.columns:
        if col not in ["Country Name", "Continent"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.drop(columns=["Country Name"], errors="ignore")
    return df.groupby("Continent").sum()


import plotly.express as px

def generate_choropleth(data, indicator, year, selected_country=None):
    """
    Génère une carte choroplèthe et met à jour la série temporelle correspondante.
    """
    if indicator not in data:
        logging.error(f"❌ Indicateur {indicator} non trouvé dans les données.")
        return go.Figure()

    df = data[indicator]
    if str(year) not in df.columns:
        logging.error(f"❌ L'année {year} n'existe pas dans {indicator}.")
        return go.Figure()

    df_filtered = df[['Country Name', str(year)]].dropna()

    fig = px.choropleth(
        df_filtered,
        locations='Country Name',
        locationmode='country names',
        color=str(year),
        hover_name='Country Name',
        title=f"{clean_label(indicator)} ({year})",
        color_continuous_scale="Viridis",
        template="plotly_dark"
    )

    # Ajout d'un contour et d'une couleur spéciale pour le pays sélectionné
    if selected_country and selected_country in df_filtered['Country Name'].values:
        selected_value = df_filtered[df_filtered['Country Name'] == selected_country][str(year)].values[0]
        fig.add_trace(go.Scattergeo(
            locations=[selected_country],
            locationmode='country names',
            text=[selected_country],
            marker=dict(
                size=15,  # Augmenter la taille du marqueur pour bien le voir
                color='red',  # Couleur bien distincte
                line=dict(width=3, color='white')  # Contour blanc
            ),
            name=f"Pays sélectionné : {selected_country} ({selected_value})"
        ))

    fig.update_layout(
        margin=dict(l=10, r=50, t=50, b=10),  # ✅ Plus d'espace à droite
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type="natural earth",
            center={"lat": 10, "lon": 10},  # ✅ Centre légèrement ajusté
        ),
    )

    return fig



def generate_histogram_with_time_series(data, countries):
    """ Génère un histogramme pour comparer plusieurs indicateurs. """
    indicators = ["taux_fertilite_femme_modif", "esperance_de_vie_modif"]
    return create_histogram_with_time_series(data, indicators, countries)


def generate_age_structure_chart(data, year, country):
    """ Génère un diagramme en barres montrant la répartition par âge. """
    return create_age_structure_chart(
        data['pop_de_0_14_modif'],
        data['pop_de_15_64_modif'],
        data['pop_de_65_et_plus_modif'],
        year, country
    )


def generate_donut_chart(data, indicators):
    """
    Génère un diagramme en anneau pour afficher la répartition des indicateurs sélectionnés par continent.
    """
    continent_sums = {}

    for indicator in indicators:
        if indicator in data:
            df = data[indicator]
            if "Country Name" in df.columns:
                df["Continent"] = df["Country Name"].apply(get_continent)

                grouped_data = df.groupby("Continent").sum().drop(columns=["Country Name"], errors="ignore")

                for continent, value in grouped_data.sum(axis=1).items():
                    if continent not in continent_sums:
                        continent_sums[continent] = 0
                    continent_sums[continent] += value

    # Vérification des données
    if not continent_sums or all(value == 0 for value in continent_sums.values()):
        logging.warning("⚠️ Données vides pour le donut chart.")
        return go.Figure()

    # Création du donut chart
    fig = go.Figure()

    fig.add_trace(go.Pie(
        labels=list(continent_sums.keys()),
        values=list(continent_sums.values()),
        hole=0.4
    ))

    fig.update_layout(
        title="Répartition des indicateurs sélectionnés par continent",
        template="plotly_dark"
    )

    return fig

def clean_label(indicator):
    """ Nettoie le nom de l'indicateur en supprimant les underscores et en corrigeant les mots-clés. """
    label = indicator.replace("_modif", "").replace("_", " ")

    # Dictionnaire de corrections pour rendre les labels plus lisibles
    corrections = {
        "morta homme": "Mortalité homme",
        "morta femme": "Mortalité femme",
        "morta inf brut": "Mortalité infantile brute",
        "morta inf fille": "Mortalité infantile fille",
        "morta inf garcon": "Mortalité infantile garçon",
        "morta enfant": "Mortalité enfant",
        "esperance de vie femme": "Espérance de vie femme",
        "esperance de vie homme": "Espérance de vie homme",
        "esperance de vie": "Espérance de vie",
        "pop urbaine": "Population urbaine",
        "pop refugie": "Population réfugiée",
        "pop de 0 14": "Population 0-14 ans",
        "pop de 15 64": "Population 15-64 ans",
        "pop de 65 plus": "Population 65 ans et plus",
        "migration nette": "Migration nette",
        "croissance pop": "Croissance démographique",
        "PIB": "Produit Intérieur Brut"
    }

    # Appliquer les corrections
    for key, value in corrections.items():
        if key in label:
            label = label.replace(key, value)

    return label.capitalize()  # Met la première lettre en majuscule



def generate_time_series(data, countries, indicators):
    """ Génère un graphique de série temporelle avec des couleurs améliorées. """
    fig = go.Figure()

    colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880']  # Palette de couleurs
    color_idx = 0

    for indicator in indicators:
        if indicator not in data:
            logging.warning(f"⚠️ Indicateur {indicator} absent des données.")
            continue

        df = data[indicator]

        for country in countries:
            if "Country Name" in df.columns:
                df_filtered = df[df["Country Name"] == country]
                years = [col for col in df_filtered.columns if col.isdigit()]
                values = df_filtered[years].values.flatten()

                fig.add_trace(go.Scatter(
                    x=years,
                    y=values,
                    mode='lines+markers',
                    name=f"{clean_label(indicator)} - {country}",  # ✅ Appliquer clean_label()
                    line=dict(color=colors[color_idx % len(colors)], width=2),
                    marker=dict(size=6)
                ))

                color_idx += 1  # Incrémenter l'index couleur

    fig.update_layout(
        title="Série temporelle des indicateurs",
        xaxis_title="Année",
        yaxis_title="Valeur",
        template="plotly_dark",
        hovermode="x unified",
        legend=dict(font=dict(size=12))
    )
    return fig



def generate_stacked_histogram(data, country, indicators):
    """ Crée un histogramme empilé avec des labels propres et une meilleure lisibilité. """
    fig = go.Figure()

    colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880']  # Palette de couleurs
    color_idx = 0

    for indicator in indicators:
        if indicator not in data:
            logging.warning(f"⚠️ Indicateur {indicator} absent des données.")
            continue

        df = data[indicator]
        df_filtered = df[df["Country Name"] == country]

        if df_filtered.empty:
            logging.warning(f"⚠️ Pas de données pour {country} dans {indicator}.")
            continue

        years = [col for col in df_filtered.columns if col.isdigit()]
        values = df_filtered[years].values.flatten()

        fig.add_trace(go.Bar(
            x=years,
            y=values,
            name=f"{clean_label(indicator)} - {country}",  # ✅ Appliquer clean_label()
            marker=dict(color=colors[color_idx % len(colors)], opacity=0.7)  # ✅ Ajuster l'opacité
        ))

        color_idx += 1  # Changer de couleur

    fig.update_layout(
        barmode='stack',
        title=f"Évolution des indicateurs pour {country}",
        xaxis_title="Année",
        yaxis_title="Valeur",
        template="plotly_dark",
        hovermode="x unified",
        legend=dict(font=dict(size=12))
    )
    return fig


def clean_country_name(country_name):
    """
    Corrige les noms de pays en français pour qu'ils correspondent à ceux de pycountry.
    """
    country_corrections = {
    "Aruba": "Aruba",
    "Angola": "Angola",
    "Albanie": "Albania",
    "Andorre": "Andorra",
    "Émirats arabes unis": "United Arab Emirates",
    "Argentine": "Argentina",
    "Arménie": "Armenia",
    "Samoa américaines": "American Samoa",
    "Antigua-et-Barbuda": "Antigua and Barbuda",
    "Australie": "Australia",
    "Autriche": "Austria",
    "Azerbaïdjan": "Azerbaijan",
    "Burundi": "Burundi",
    "Belgique": "Belgium",
    "Bénin": "Benin",
    "Burkina Faso": "Burkina Faso",
    "Bangladesh": "Bangladesh",
    "Bulgarie": "Bulgaria",
    "Bahreïn": "Bahrain",
    "Bahamas": "Bahamas",
    "Bosnie-Herzégovine": "Bosnia and Herzegovina",
    "Bélarus": "Belarus",
    "Belize": "Belize",
    "Bermudes": "Bermuda",
    "Bolivie": "Bolivia",
    "Brésil": "Brazil",
    "Barbade": "Barbados",
    "Brunéi Darussalam": "Brunei Darussalam",
    "Bhoutan": "Bhutan",
    "Botswana": "Botswana",
    "République centrafricaine": "Central African Republic",
    "Canada": "Canada",
    "Suisse": "Switzerland",
    "Chili": "Chile",
    "Chine": "China",
    "Côte d'Ivoire": "Ivory Coast",
    "Cameroun": "Cameroon",
    "Congo, République démocratique du": "Democratic Republic of the Congo",
    "Congo, République du": "Republic of the Congo",
    "Colombie": "Colombia",
    "Comores": "Comoros",
    "Costa Rica": "Costa Rica",
    "Cuba": "Cuba",
    "Curacao": "Curacao",
    "Chypre": "Cyprus",
    "République tchèque": "Czech Republic",
    "Allemagne": "Germany",
    "Djibouti": "Djibouti",
    "Dominique": "Dominica",
    "Danemark": "Denmark",
    "République dominicaine": "Dominican Republic",
    "Algérie": "Algeria",
    "Équateur": "Ecuador",
    "Égypte, République arabe d'": "Egypt, Arab Republic of",
    "Érythrée": "Eritrea",
    "Espagne": "Spain",
    "Estonie": "Estonia",
    "Éthiopie": "Ethiopia",
    "Finlande": "Finland",
    "Fidji": "Fiji",
    "France": "France",
    "Îles Féroé": "Faroe Islands",
    "Micronésie, États fédérés de": "Micronesia, Federated States of",
    "Gabon": "Gabon",
    "Royaume-Uni": "United Kingdom",
    "Géorgie": "Georgia",
    "Ghana": "Ghana",
    "Gibraltar": "Gibraltar",
    "Guinée": "Guinea",
    "Gambie": "Gambia",
    "Guinée-Bissau": "Guinea-Bissau",
    "Guinée équatoriale": "Equatorial Guinea",
    "Grèce": "Greece",
    "Grenade": "Grenada",
    "Groenland": "Greenland",
    "Guatemala": "Guatemala",
    "Guam": "Guam",
    "Guyana": "Guyana",
    "Chine, RAS de Hong Kong": "Hong Kong SAR, China",
    "Honduras": "Honduras",
    "Croatie": "Croatia",
    "Haïti": "Haiti",
    "Hongrie": "Hungary",
    "Indonésie": "Indonesia",
    "Île de Man": "Isle of Man",
    "Inde": "India",
    "Irlande": "Ireland",
    "Iran, République islamique d'": "Iran, Islamic Republic of",
    "Iraq": "Iraq",
    "Islande": "Iceland",
    "Israël": "Israel",
    "Italie": "Italy",
    "Jamaïque": "Jamaica",
    "Jordanie": "Jordan",
    "Japon": "Japan",
    "Kazakhstan": "Kazakhstan",
    "Kenya": "Kenya",
    "République kirghize": "Kyrgyz Republic",
    "Cambodge": "Cambodia",
    "Kiribati": "Kiribati",
    "Saint-Kitts-et-Nevis": "Saint Kitts and Nevis",
    "Corée, République de": "Korea, Republic of",
    "Koweït": "Kuwait",
    "République démocratique populaire lao": "Lao People's Democratic Republic",
    "Liban": "Lebanon",
    "Libéria": "Liberia",
    "Libye": "Libya",
    "Sainte-Lucie": "Saint Lucia",
    "Liechtenstein": "Liechtenstein",
    "Sri Lanka": "Sri Lanka",
    "Lesotho": "Lesotho",
    "Lituanie": "Lithuania",
    "Luxembourg": "Luxembourg",
    "Lettonie": "Latvia",
    "Chine": "China",
    "Saint-Martin (fr)": "Saint Martin (French part)",
    "Maroc": "Morocco",
    "Monaco": "Monaco",
    "Moldova": "Moldova",
    "Madagascar": "Madagascar",
    "Maldives": "Maldives",
    "Mexique": "Mexico",
    "Îles Marshall": "Marshall Islands",
    "Macédoine du Nord": "North Macedonia",
    "Mali": "Mali",
    "Malte": "Malta",
    "Myanmar": "Myanmar",
    "Monténégro": "Montenegro",
    "Mongolie": "Mongolia",
    "Mariannes": "Northern Mariana Islands",
    "Mozambique": "Mozambique",
    "Mauritanie": "Mauritania",
    "Maurice": "Mauritius",
    "Malawi": "Malawi",
    "Malaisie": "Malaysia",
    "Namibie": "Namibia",
    "Nouvelle-Calédonie": "New Caledonia",
    "Niger": "Niger",
    "Nigéria": "Nigeria",
    "Nicaragua": "Nicaragua",
    "Pays-Bas": "Netherlands",
    "Norvège": "Norway",
    "Népal": "Nepal",
    "Nauru": "Nauru",
    "Nouvelle-Zélande": "New Zealand",
    "Oman": "Oman",
    "Pakistan": "Pakistan",
    "Panama": "Panama",
    "Pérou": "Peru",
    "Philippines": "Philippines",
    "Palaos": "Palau",
    "Papouasie-Nouvelle-Guinée": "Papua New Guinea",
    "Pologne": "Poland",
    "Porto Rico": "Puerto Rico",
    "Corée, République démocratique de": "Korea, Democratic People's Republic of",
    "Portugal": "Portugal",
    "Paraguay": "Paraguay",
    "Polynésie française": "French Polynesia",
    "Qatar": "Qatar",
    "Roumanie": "Romania",
    "Fédération de Russie": "Russian Federation",
    "Rwanda": "Rwanda",
    "Arabie saoudite": "Saudi Arabia",
    "Soudan": "Sudan",
    "Sénégal": "Senegal",
    "Singapour": "Singapore",
    "Îles Salomon": "Solomon Islands",
    "Sierra Leone": "Sierra Leone",
    "El Salvador": "El Salvador",
    "Saint-Marin": "San Marino",
    "Somalie": "Somalia",
    "Serbie": "Serbia",
    "Soudan du Sud": "South Sudan",
    "Sao Tomé-et-Principe": "Sao Tome and Principe",
    "Suriname": "Suriname",
    "République slovaque": "Slovak Republic",
    "Slovénie": "Slovenia",
    "Suède": "Sweden",
    "Eswatini": "Eswatini",
    "Sint Maarten (Dutch part)": "Sint Maarten (Dutch part)",
    "Seychelles": "Seychelles",
    "République arabe syrienne": "Syrian Arab Republic",
    "Îles Turques-et-Caïques": "Turks and Caicos Islands",
    "Tchad": "Chad",
    "Togo": "Togo",
    "Thaïlande": "Thailand",
    "Tadjikistan": "Tajikistan",
    "Turkménistan": "Turkmenistan",
    "Timor-Leste": "Timor-Leste",
    "Tonga": "Tonga",
    "Trinité-et-Tobago": "Trinidad and Tobago",
    "Tunisie": "Tunisia",
    "Turquie": "Turkey",
    "Tuvalu": "Tuvalu",
    "Tanzanie": "Tanzania",
    "Ouganda": "Uganda",
    "Ukraine": "Ukraine",
    "Uruguay": "Uruguay",
    "États-Unis": "United States",
    "Ouzbékistan": "Uzbekistan",
    "Saint-Vincent-et-les Grenadines": "Saint Vincent and the Grenadines",
    "Venezuela": "Venezuela",
    "Îles Vierges (EU)": "Virgin Islands (U.S.)",
    "Viet Nam": "Vietnam",
    "Vanuatu": "Vanuatu",
    "Samoa": "Samoa",
    "Yémen, Rép. du": "Yemen, Rep.",
    "Afrique du Sud": "South Africa",
    "Zambie": "Zambia",
    "Zimbabwe": "Zimbabwe",

        "Région administrative spéciale de Macao": "Macao",

        "Égypte, République arabe d’": "Egypt",
        "Hong Kong SAR, China": "Hong Kong",
        "Iran, République islamique d’": "Iran",
        "Macao SAR, China": "Macao",


        "Virgin Islands (U.S.)": "United States Virgin Islands",
        "Yemen, Rep.": "Yemen"

    }
    return country_corrections.get(country_name, country_name)



def get_data(file_key):
    """
    Charge un fichier CSV basé sur la clé donnée dans `config['data_files']`.
    Applique des corrections sur les noms de pays, ajoute la colonne 'Continent' et convertit les données numériques.
    """
    file_path = os.path.join(cfg.get("app_data_dir", ""), cfg["data_files"].get(file_key, ""))

    # 🚨 Vérification du chemin du fichier
    print(f"🔍 Vérification du chemin pour {file_key} : {file_path}")

    if not os.path.exists(file_path):
        print(f"❌ ERREUR : Le fichier {file_path} n'existe pas.")
        return None

    try:
        df = pd.read_csv(file_path)
        if df.empty:
            logging.warning(f"Le fichier {file_key} est vide.")
            return None

        # Appliquer la correction des noms de pays
        df["Country Name"] = df["Country Name"].apply(clean_country_name)

        # Traduire les noms des pays en anglais
        df = translate_country_names(df)

        # Ajouter la colonne 'Continent'
        df["Continent"] = df["Country Name"].apply(get_continent)

        # Vérification après correction
        for country in df["Country Name"].unique():
            found = pycountry.countries.get(name=country)
            if found is None:
                print(f"⚠️ Pays toujours inconnu après correction : {country}")
            else:
                print(f"✅ {country} reconnu comme {found.name}")

        # Conversion des colonnes d'années en numérique
        for col in df.columns:
            if col.isdigit():
                df[col] = pd.to_numeric(df[col], errors="coerce")

        logging.info(f"✅ Fichier {file_key} chargé avec succès.")
        return df
    except pd.errors.EmptyDataError:
        logging.error(f"Le fichier {file_key} est vide ou mal formaté.")
        return None
    except Exception as e:
        logging.error(f"Erreur lors du chargement de {file_key}: {e}")
        return None