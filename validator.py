import logging

#Fonction qui vérifie si les données sont correctes et présentes.
def validate(data):
    valid_users = []

    for user in data:
        try:
            if user['name'] and user['email'] and user['age'].isdigit():
                user['age'] = int(user['age'])
                valid_users.append(user)
            else:
                continue
        except KeyError:
            logging.warning("Clé manquante dans une ligne ignorée")
    
    return valid_users