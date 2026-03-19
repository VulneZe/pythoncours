# Python Cours

Repository contenant les exercices et exemples du cours de Python.

## Contenu

- `analyse.py` : Script d'exemple utilisant argparse et logging
- `modules/` : Modules Python réutilisables
- `app.log` : Fichier de logs généré par les scripts

## Utilisation

### analyse.py

Script qui formate un nom et prénom en utilisant argparse pour les arguments en ligne de commande et logging pour enregistrer les opérations.

```bash
python3 analyse.py "Nom" "Prénom"
```

Exemple :
```bash
python3 analyse.py "Doe" "john"
# Output: Nom formaté : DOE John
```

## Structure

- **argparse** : Gestion des arguments en ligne de commande
- **logging** : Enregistrement des logs dans un fichier
- **Modules** : Code réutilisable organisé dans le dossier `modules/`

## Prérequis

- Python 3.x
- Aucune dépendance externe requise
