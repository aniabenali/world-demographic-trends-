# 🌍 World Demographic Trends  

Ce projet propose un **tableau de bord interactif** permettant d’explorer les **dynamiques démographiques mondiales** à travers plusieurs visualisations basées sur des données de la **Banque Mondiale**.  

## 🌐 Application en ligne  
Accédez au **tableau de bord en ligne** ici : [ici](https://example.com)  

## 🖼️ Aperçu du tableau de bord  
Voici un aperçu du tableau de bord :  
![Capture d’écran du dashboard](assets/dashboard_preview.png)  

## 🎯 Objectifs  
Grâce à cet outil, il est possible de :  

✅ **Analyser les tendances démographiques** : suivre l’évolution de la **fertilité**, de l’**espérance de vie** et de la **croissance de la population** à travers différents pays et périodes.  
✅ **Comparer les indicateurs entre pays et continents** : visualiser les **écarts et similitudes** en matière de **migration**, de **répartition par âge** et d’**urbanisation**.  
✅ **Évaluer l’impact des dynamiques démographiques sur la santé publique** : identifier les **défis liés au vieillissement** et aux **systèmes de santé**.

## 🗺️ Graphiques et Sélections Utilisateur  

Découvrez les différentes visualisations disponibles dans le tableau de bord : 
| Type de graphique            | Sélection utilisateur                        | Données utilisées                                       | Objectif                                                |
|------------------------------|----------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
| **Carte Choroplèthe**         | Pays, indicateur, année                      | Tous les indicateurs                                     | Visualisation géographique                               |
| **Série Temporelle**          | Plusieurs pays, plusieurs indicateurs       | espérance_de_vie_modif, taux_fertilite_femme_modif, PIB_modif, migration_nette_modif | Comparaison d’indicateurs dans le temps                 |
| **Histogramme**               | Plusieurs pays, indicateur                  | taux_fertilite_femme_modif, esperance_de_vie_modif       | Comparaison de pays sur un indicateur                   |
| **Diagramme en Barres**       | Pays, année                                 | pop_de_0_14_modif, pop_de_15_64_modif, pop_de_65_et_plus_modif | Répartition par âge                                     |
| **Diagramme en Anneau (Donut Chart)** | Continent, plusieurs indicateurs        | croissance_de_la_pop_modif, PIB_modif, migration_nette_modif, pop_refugie_modif | Répartition des indicateurs sélectionnés par continent |

## 🚀 Technologies utilisées  
- **Python** (Dash, Plotly, Pandas)  
- **Données** : Banque Mondiale  
- **Hébergement** : GitHub  

## 📌 Installation et exécution  

```python
# Installer les dépendances nécessaires
pip install dash plotly pandas

# Lancer l'application Dash
python app.py
