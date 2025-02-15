import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import logging
import pycountry_convert as pc

# Configuration du logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

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




def create_choropleth(data, indicator, year):
    """
    Crée une carte choroplèthe pour un indicateur donné.
    """
    if indicator not in data:
        logging.error(f"❌ Indicateur {indicator} non trouvé dans les données.")
        return go.Figure()

    df = data[indicator]
    if str(year) not in df.columns:
        logging.error(f"❌ L'année {year} n'existe pas dans {indicator}.")
        return go.Figure()

    df_filtered = df[['Country Name', str(year)]].dropna()

    logging.info(f"✅ Création de la carte choroplèthe pour {clean_label(indicator)} en {year}")

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

    fig.update_layout(geo=dict(showframe=False, showcoastlines=True))
    return fig


def create_time_series(data, countries, indicators):
    """
    Crée un graphique linéaire montrant l'évolution de plusieurs indicateurs pour plusieurs pays.
    """
    fig = go.Figure()

    for indicator in indicators:
        if indicator not in data:
            logging.warning(f"⚠️ Indicateur {indicator} absent des données.")
            continue

        df = data[indicator]
        for country in countries:
            df_filtered = df[df["Country Name"] == country]
            years = [col for col in df_filtered.columns if col.isdigit()]
            values = df_filtered[years].values.flatten()

            fig.add_trace(go.Scatter(
                x=years,
                y=values,
                mode='lines+markers',
                name=f"{clean_label(indicator)} ({country})"
            ))

    fig.update_layout(
        title="Évolution des indicateurs sélectionnés",
        xaxis_title="Année",
        yaxis_title="Valeur",
        template="plotly_dark",
        hovermode="x unified"
    )
    return fig


def create_histogram_with_time_series(data, indicators, countries):
    """
    Crée un histogramme superposé avec la série temporelle pour plusieurs pays et indicateurs.
    """
    fig = go.Figure()

    colors = {
        "taux_fertilite_femme_modif": "#FF6384",
        "esperance_de_vie_modif": "#36A2EB",
        "migration_nette_modif": "#FFCE56"
    }

    # Ajouter les histogrammes
    for indicator in indicators:
        if indicator not in data:
            logging.warning(f"⚠️ Indicateur {indicator} absent des données.")
            continue

        df = data[indicator]
        for country in countries:
            df_filtered = df[df["Country Name"] == country]
            years = [col for col in df_filtered.columns if col.isdigit()]
            values = df_filtered[years].values.flatten()

            fig.add_trace(go.Bar(
                x=years,
                y=values,
                name=f"{clean_label(indicator)} ({country})",
                marker=dict(color=colors.get(indicator, "#9966FF")),  # Couleur par défaut
                opacity=0.8
            ))

    # Ajouter la série temporelle
    for indicator in indicators:
        if indicator not in data:
            continue

        df = data[indicator]
        for country in countries:
            df_filtered = df[df["Country Name"] == country]
            years = [col for col in df_filtered.columns if col.isdigit()]
            values = df_filtered[years].values.flatten()

            fig.add_trace(go.Scatter(
                x=years,
                y=values,
                mode='lines+markers',
                name=f"{indicator} ({country})",
                line=dict(width=2)
            ))

    fig.update_layout(
        title="Comparaison des indicateurs",
        xaxis_title="Année",
        yaxis_title="Valeur",
        template="plotly_dark",
        barmode='overlay',
        hovermode="x unified"
    )

    return fig


def get_continent(country_name):
    """
    Retourne le continent d'un pays donné en utilisant pycountry_convert.
    """
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
        return "Autre"


def create_age_structure_chart(df_0_14, df_15_64, df_65_plus, year, countries):
    """
    Crée un diagramme en barres montrant la répartition par âge.
    """
    fig = go.Figure()

    for country in countries:
        data_values = []
        labels = ['0-14', '15-64', '65+']

        for df, label in zip([df_0_14, df_15_64, df_65_plus], labels):
            try:
                value = df[df['Country Name'] == country][str(year)].values[0]
                data_values.append(max(value, 0))  # Évite les valeurs négatives
            except (IndexError, KeyError):
                logging.warning(f"⚠️ Données manquantes pour {label} en {year} pour {country}")
                data_values.append(0)

        fig.add_trace(go.Bar(
            x=labels,
            y=data_values,
            name=country
        ))

    if not fig.data:
        logging.error("❌ Aucun pays sélectionné ou données manquantes.")

    fig.update_layout(
        title=f"Répartition par âge en {year}",
        xaxis_title="Tranche d'âge",
        yaxis_title="Population (%)",
        template="plotly_dark",
        barmode="group"
    )

    return fig


def create_donut_chart(data):
    """
    Crée un diagramme en anneau pour afficher une répartition des indicateurs sélectionnés
    en regroupant les pays en continents.
    """
    fig = go.Figure()

    if "Autre" in data:
        del data["Autre"]

    fig.add_trace(go.Pie(
        labels=list(data.keys()),
        values=list(data.values()),
        hole=0.4
    ))

    fig.update_layout(
        title="Répartition des indicateurs sélectionnés par continent",
        template="plotly_dark"
    )
    return fig
