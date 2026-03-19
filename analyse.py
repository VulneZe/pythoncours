#!/usr/bin/python3

# import des modules nécessaires
import argparse  # Pour gérer les arguments en ligne de commande
import logging    # Pour enregistrer des logs dans un fichier

# conf du logging
# Les logs seront sauvegardés dans le fichier "app.log"
logging.basicConfig(
    filename="app.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

# Fonction qui formate le nom et prénom
def set_case(nom: str, prenom: str) -> str:
    """Met le nom en majuscules et le prénom avec première lettre majuscule"""
    formatted = f"{nom.upper()} {prenom.capitalize()}"
    logging.info(f"Nom formaté : {formatted}")  # Enregistre dans le log
    return formatted

# Fonction principale du programme
def main() -> None:
    # Création du parser pour analyser les arguments de la ligne de commande
    parser = argparse.ArgumentParser(description="Script d'exemple pour argparse")

    # Ajout des arguments attendus : nom et prénom (obligatoires)
    parser.add_argument("nom", help="Nom de la personne", type=str)
    parser.add_argument("prenom", help="Prénom de la personne", type=str)

    # Analyse des arguments passés en ligne de commande
    args = parser.parse_args()

    # Utilisation des arguments pour appeler la fonction de formatage
    formatted_string = set_case(args.nom, args.prenom)

    # Affichage du résultat à l'utilisateur
    print(f"Nom formaté : {formatted_string}")

# Point d'entrée du programme
if __name__ == "__main__":
    main()

"""
GLOSSAIRE DES TERMES UTILISÉS :

parser = sert à analyser et interpréter les arguments passés en ligne de commande
argparse = module Python qui permet de créer des interfaces en ligne de commande
parser.add_argument() = sert à définir un argument que le script peut recevoir
args = objet contenant les valeurs des arguments après analyse
args.parse_args() = sert à analyser les arguments et les convertir en objet utilisable
logging = module qui permet d'enregistrer des messages de log dans un fichier
logging.basicConfig() = sert à configurer le système de logging (fichier, niveau, format)
logging.info() = sert à enregistrer un message d'information dans le log
.upper() = méthode qui convertit une chaîne en majuscules
.capitalize() = méthode qui met la première lettre en majuscule et le reste en minuscules
if __name__ == "__main__" = sert à faire exécuter le code seulement quand le script est lancé directement
"""