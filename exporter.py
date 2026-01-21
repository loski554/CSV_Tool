import json, logging

#Fonction exporter les données dans un fichier .json
def export_json(data, output_file):
    if not data:
        logging.error("Aucune donnée valide à exporter")
        return False
    else:
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
        
        logging.info(f"Données exportées dans {output_file}")
        return True