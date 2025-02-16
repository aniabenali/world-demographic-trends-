'''{country only}
import pandas as pd

# Charger les données du ficher "Metadata_Country_API_NY.GDP.PCAP.CD_DS2_fr_csv_v2_5083" dans le dossier ZIP 
country = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/Code.py/country.csv")

# Supprimer la 5e colonne (indexée à partir de 0)
country = country.drop(country.columns[4], axis=1)

# Filtrer le tableau 'country' pour ne garder que les pays réels (en excluant 'Agrégats')
country_filtered = country[~country['Income_Group'].isin(['Agrégats'])]

print(country_filtered.head())
'''

'''{PIB}

df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/PIB/PIB.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]

#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])
# Vérifier le résultat
print(df.head())

# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]

# Afficher le DataFrame filtré
print(df)

df.to_csv("les_taux/PIB/PIB_modif.csv", index=False)

'''

'''{taux mortalite brut}

df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/morta_brut/Morta_brut.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())

# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]

# telcharger le nv tab
df.to_csv("les_taux/morta_brut/morta_modif.csv", index=False)

'''


'''{taux mortalite femme}

df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/morta_brut/morta_femme.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/morta_brut/morta_femme_modif.csv", index=False)
'''



'''{ taux de mortalite homme}


df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/morta_brut/morta_homme.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/morta_brut/morta_homme_modif.csv", index=False)
'''



'''{taux de natalite}


df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/natalite/natalite.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/natalite/natalite_modif.csv", index=False)
'''


'''{taux de mortalite infantile brut}

df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/morta_infantile/morta_inf_brut.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/morta_infantile/morta_inf_brut_modif.csv", index=False)
'''


'''{taux de mortalite infantile fille }

df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/morta_infantile/morta_inf_fille.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/morta_infantile/morta_inf_fille_modif.csv", index=False)
'''

'''{ taux de mortalite infantile garcon }

df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/morta_infantile/morta_inf_garcon.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/morta_infantile/morta_inf_garcon_modif.csv", index=False)
'''


'''{ croissance de la population }


df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/croissance_pop/croissance_de_la_pop.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/croissance_pop/croissance_de_la_pop_modif.csv", index=False)
'''


'''{esperance de vie brut}

df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/esperance_de_vie/esperance_de_vie.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/esperance_de_vie/esperance_de_vie_modif.csv", index=False)
'''

'''{esperance de vie femme}

df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/esperance_de_vie/esperance_de_vie_femme.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/esperance_de_vie/esperance_de_vie_femme_modif.csv", index=False)
'''

'''{esperance de vie homme}

df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/esperance_de_vie/esperance_de_vie_homme.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/esperance_de_vie/esperance_de_vie_homme_modif.csv", index=False)
'''

'''{fertilite}

df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/fertilite/taux_fertilite_femme.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/fertilite/taux_fertilite_femme_modif.csv", index=False)
'''

'''{migration}

df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/migration/migration_nette.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/migration/migration_nette_modif.csv", index=False)
'''

'''{population age de 0 a 14 ans }


df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/population_age/pop_de_0_14.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/population_age/pop_de_0_14_modif.csv", index=False)
'''

'''{population age de 15 a 64 ans }



df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/population_age/pop_de_15_64.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/population_age/pop_de_15_64_modif.csv", index=False)
'''


'''{population age de 15 a 64 ans }


df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/population_age/pop_de_65_et_plus.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/population_age/pop_de_65_et_plus_modif.csv", index=False)
'''


'''{population urbaine}


df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/population_urbaine/pop_urbaine.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/population_urbaine/pop_urbaine_modif.csv", index=False)
'''


'''{population urbaine}


df = pd.read_csv("C:/Users/pc/Downloads/web_scrap2/les_taux/refug/pop_refugie.csv", sep=",",  skiprows=4)
print(df.head())  # Afficher les premières lignes du DataFrame pour vérifier

df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
print(df.head())  # Vérifier que les colonnes ont été supprimées


# Sélectionner les colonnes à partir de 2017
df = df.loc[:, ["Country Name"] + [str(year) for year in range(2000, 2024)]]
#supprimer les lignes index [1 et 3]
df = df.drop(index=[1, 3])

# Vérifier le résultat
print(df.head())
# Filtrer le tableau  pour ne garder que les pays présents dans 'country_filtered'
df= df[df['Country Name'].isin(country_filtered['Country Name'])]

# Afficher les premières lignes du tableau filtré
print(df)

# Liste des entités à supprimer
to_remove = ["Îles Anglo-Normandes", "Îles Caïmans", "Îles Vierges britanniques", "Cisjordanie et Gaza", "Kosovo"]

# Filtrer les pays en excluant les entités de la liste 'to_remove'
df  = df[~df['Country Name'].isin(to_remove)]
# telcharger le nv tab
df.to_csv("les_taux/refug/pop_refugie_modif.csv", index=False)
'''