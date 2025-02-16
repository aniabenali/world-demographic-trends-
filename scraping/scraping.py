'''{taux de mortalite brut}
import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.DYN.CDRT.IN?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "morta_brut"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''

'''{taux de mortalite femme}

import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.DYN.AMRT.FE?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "morta_femme"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''

'''{taux de mortalite homme}

import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.DYN.AMRT.MA?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "morta_homme"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''

'''{taux de mortalite infantile brut}

import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.DYN.IMRT.IN?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "morta_inf"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''

'''{taux de mortalite infantile fille}

import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.DYN.IMRT.FE.IN?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "morta_inf_fille"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''

'''{taux de mortalite infantile garcon}

import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.DYN.IMRT.MA.IN?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "morta_inf_garcon"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''

'''{taux de natalite }
import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.DYN.CBRT.IN?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "taux_natalite"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''


'''{PIB }

import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/NY.GDP.PCAP.CD?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "PIB"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''

'''{taux de fertilite femme}
import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.DYN.TFRT.IN?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "taux_fertilite"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''

'''{migration nette}
import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SM.POP.NETM?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "migration_nette"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")

'''

'''{esperance de vie}
import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.DYN.LE00.IN?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "esperence_de_vie"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")

'''

'''{esperence de vie homme}
import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.DYN.LE00.MA.IN?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "esperence_de_vie_homme"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")

'''


'''{esperence de vie femme}
import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.DYN.LE00.FE.IN?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "esperence_de_vie_femme"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''

'''{croissance de la population}
import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.POP.GROW?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "croissance_de_la_pop"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''

'''{ croissance de la population}
import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.POP.GROW?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "croissance_de_la_pop"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''

''' {pop de 15 a 64 ans }
import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.POP.1564.TO.ZS?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "pop_de_15_64"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''

'''{pop de 65 ans et plus}
import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.POP.65UP.TO.ZS?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "pop_de_65_et_plus"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''

'''{pop refugie}
import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SM.POP.REFG?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "pop_refugie"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")

'''

'''{population urbaine}
import requests
import os

# URL du fichier CSV de la Banque mondiale
url = "https://api.worldbank.org/v2/fr/indicator/SP.URB.TOTL.IN.ZS?downloadformat=csv"

# Nom du fichier à enregistrer
filename = "pop_urbaine"  # Le fichier est un ZIP contenant plusieurs CSV

# Récupération du dossier de travail actuel (celui ouvert dans VS Code)
current_dir = os.getcwd()
file_path = os.path.join(current_dir, filename)

# Téléchargement du fichier
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès : {file_path}")
else:
    print(f"Échec du téléchargement. Code HTTP : {response.status_code}")

import zipfile

# Définir le dossier de destination pour extraire les fichiers
extract_folder = current_dir  # Tu peux changer ce chemin si besoin

# Vérifier si le fichier ZIP existe avant d'extraire
if os.path.exists(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Fichiers extraits dans : {extract_folder}")
else:
    print("Le fichier ZIP n'existe pas, extraction annulée.")
'''