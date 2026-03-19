#!/usr/bin/python3

import argparse
import logging

# conf du logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def set_case(nom: str, prenom: str) -> str:
    formatted = f"{nom.upper()} {prenom.capitalize()}"
    logging.info(f"Nom formaté : {formatted}")
    return formatted

def main() -> None:
    parser = argparse.ArgumentParser(description="Script d'exemple avec argparse et logging")
    
    parser.add_argument("nom", help="Nom de la personne", type=str)
    parser.add_argument("prenom", help="Prénom de la personne", type=str)
    
    args = parser.parse_args()

    result = set_case(args.nom, args.prenom)
    
    print(f"Nom formaté : {result}")

if __name__ == "__main__":
    main()