import csv, logging

#Fonction qui lit et renvoie les données d'un fichier csv dans une liste.
def read_csv(fi):
    lst_users = []
    try:
        logging.info(f"Lecture du fichier CSV : {fi}")

        with open(fi, newline = '', encoding = 'utf-8') as csvfile:
            content = csv.DictReader(csvfile)
            
            for row in content:
                lst_users.append(row)

    except FileNotFoundError:
        logging.error("Fichier CSV introuvable")
    
    return lst_users