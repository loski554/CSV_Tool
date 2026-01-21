import argparse, logging
from reader import read_csv
from validator import validate
from exporter import export_json
from app import Application

#Fonction qui prend les arguments passer en CLI par l'utilisateur.
def parse_arguments():
    parser = argparse.ArgumentParser(prog='csv_tool', description='Conversion CSV en JSON')

    parser.add_argument('input_file', help='Chemin du fichier CSV')
    parser.add_argument('output_file', help='Chemin du fichier JSON')

    args = parser.parse_args()

    return args

#Script principal
def main():

    logging.info("Démarrage du programme")

    args = parse_arguments()
    logging.info(f"Fichier d'entrée : {args.input_file}")
    logging.info(f"Fichier de sortie : {args.output_file}")

    data = read_csv(args.input_file)
    logging.info(f"{len(data)} lignes lues")

    valid_data = validate(data)
    logging.info(f"{len(valid_data)} lignes valides")

    success = export_json(valid_data, args.output_file)

    if success:
        print(f'Export réussi dans: "{args.output_file}".')
        logging.info("Export JSON terminé avec succès")
    else:
        print("Aucune donnée valide à exporter.")
        logging.error("Export impossible : aucune donnée valide")

    
    #Lancer l'interface graphique
    if valid_data:
        app = Application(valid_data)
        app.mainloop()
        logging.info("Interface graphique fermée")


#--MAIN--#

if __name__ == '__main__':

    #config de logging classique
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
    
    #appel du script principal
    main()
