import os

appDataPath = "appdata"
assetsPath = "assets"

if os.path.isdir(appDataPath):
    app_data_dir = appDataPath
    assets_dir = assetsPath
else:
    app_data_dir = './appdata'  # Chemin relatif par défaut
    assets_dir = './assets'

config = {
    'app_data_dir': app_data_dir,
    'assets_dir': assets_dir,  # ✅ Correction du nom de clé
    'cache_dir': 'cache',
    'cache_threshold': 50,
    'debug': True,  # ✅ Ajout d'une option pour activer le mode Debug
    'Years': list(range(2000, 2024)),  # ✅ Simplification de la liste
    'latest_date': '2023',
    'logging_format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'plotly_config': {
        'World': {
            'zoom': 1,
            'centre': [0, 0],
            'maxp': 98
        }
    },
    #'geojson_file': 'World.geojson',  # ✅ Ajout du fichier GeoJSON
    'data_files': {
        'pop_de_0_14_modif': 'pop_de_0_14_modif.csv',
        'pop_urbaine_modif': 'pop_urbaine_modif.csv',
        'pop_refugie_modif': 'pop_refugie_modif.csv',
        'morta_homme_modif': 'morta_homme_modif.csv',
        'morta_modif': 'morta_modif.csv',
        'morta_femme_modif': 'morta_femme_modif.csv',
        'morta_inf_brut_modif': 'morta_inf_brut_modif.csv',
        'morta_inf_fille_modif': 'morta_inf_fille_modif.csv',
        'morta_inf_garcon_modif': 'morta_inf_garcon_modif.csv',
        'natalite_modif': 'natalite_modif.csv',
        'PIB_modif': 'PIB_modif.csv',
        'esperance_de_vie_femme_modif': 'esperance_de_vie_femme_modif.csv',
        'esperance_de_vie_homme_modif': 'esperance_de_vie_homme_modif.csv',
        'esperance_de_vie_modif': 'esperance_de_vie_modif.csv',
        'taux_fertilite_femme_modif': 'taux_fertilite_femme_modif.csv',
        'migration_nette_modif': 'migration_nette_modif.csv',
        'croissance_de_la_pop_modif': 'croissance_de_la_pop_modif.csv',
        'pop_de_15_64_modif': 'pop_de_15_64_modif.csv',
        'pop_de_65_et_plus_modif': 'pop_de_65_et_plus_modif.csv'


},

'colors': {
        'esperance_de_vie_modif': '#1f77b4',
        'taux_fertilite_femme_modif': '#ff7f0e',
        'natalite_modif': '#2ca02c',
        'PIB_modif': '#d62728'
    },

    # ✅ Correction : Définition des indicateurs pour l'histogramme
    'histogram_indicators': {
        'esperance_de_vie_modif': 'Espérance de vie',
        'taux_fertilite_femme_modif': 'Taux de fertilité',
        'natalite_modif': 'Taux de natalité',
        'pop_de_0_14_modif': 'Population'
}
}