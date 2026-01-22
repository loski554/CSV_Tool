# CSV TOOL - CSV to JSON Converter

## 📌 Description Projet
Ce projet est un script python avec interface graphique permettant de :
- lire un fichier CSV,
- valider des données selon une struture (user, age, email),
- exporter les données valides au format JSON dans un nouveau fichier,
- afficher un tableau d'utilisateurs valides dans une interface graphique.

![Interface Graphique Tkinter](./screenshots/screenshot_1.png)

## 🛠️ Technologies utilisées
- Python 3 - langage du projet
- Argparse (interface en ligne de commande)
- csv / JSON (extensions fichiers)
- Logging (gestion erreur console)
- ttkbootstrap (interface graphique)

## 📂 Structure du projet
```
- main.py > instructions + CLI (ligne de commande) + GUI (interface graphique)
- reader.py > lecture fichier CSV
- validator.py > validation des données
- exporter.py > export fichier JSON
- app.py > interface graphique
- README.md
- requirements.txt > fichier avec packages python nécessaire
```

## ➡️ Utilisation
1. Cloner le projet dans vos documents :
```bash
git clone https://github.com/loski554/CSV_Tool
cd CSV_Tool
```

2. Créer un environnement virtuel dans le dossier csv_tool:

*Pour eviter les confilts entre versions et packages*
```bash
python -m venv env
source env/bin/activate # ou .\env\Scripts\activate sous Windows
```

3. Installer les requirements:
```bash
pip install -r requirements.txt
```

4. Lancer le projet:
```bash
python main.py ./input_csv.csv ./data.json #remplacer les fichiers si besoin
```

## 🧠 Points techniques mis en avant
- architecture code modulaire,
- séparations des fonctions,
- gestions des erreurs avec logging,
- interface graphique tkinter
  
## ✍️ Auteur
Projet réalisé par **Lucas Goulain/loski554**
