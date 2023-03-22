# BDD-AVANCE
## Description

Ce projet a pour but de réaliser un entrepôt de données afin de faire des analyses sur des matchs de football européens. Le jeu de données que l'on a utilisé contient des matchs, de plusieurs ligues européennes, joués de 2008 à 2016. A cause d'une limite d'espace, nous avons contraint les données à seulement 2 ligues et 2 années :
* France Ligue 1
* Netherlands Eredivisie   
et   
* 2015
* 2016   

Mais il suffit d'enlever les conditionnelles lors des écritures des lignes du fichier facts.csv dans le script script_parse_data_warehouse.py pour lever cette restriction.

## Jeu de données d'origine
Toutes les informations sont sur Kaggle : https://www.kaggle.com/datasets/hugomathien/soccer

## Etapes de construction
Pour retrouver le même entrepôt de données, il faut :

1. Télécharger sur Kaggle le .sqlite du jeu de données.
1. Ensuite, réalisez les lignes de codes suivantes dans votre terminal afin de générer les fichiers csv de chaque table :
    ```bash
    sqlite3 database.sqlite '.headers on' '.mode csv' '.once match.csv' 'select * from match'
    ```
    ```bash
    sqlite3 database.sqlite '.headers on' '.mode csv' '.once team.csv' 'select * from team'
    ```
    ```bash
    sqlite3 database.sqlite '.headers on' '.mode csv' '.once country.csv' 'select * from country'
    ```
    ```bash
    sqlite3 database.sqlite '.headers on' '.mode csv' '.once league.csv' 'select * from league'
    ```

1. Maintenant que l'on a les différents csv, le plus important et de filtrer la table match afin de créer notre table de faits. Vous pouvez donc exécuter cette ligne de commande afin de générer un nouveau fichier csv avec seulement les attributs voulus :
    ```bash
    python3 extraction_match_csv.py
    ```

1. A partir d'ici, les attributs contenant les évènements sont des listes de balises xml. Il est important de garder les valeurs nécessaires (surtout de bien les séparer en valeur unique). On génère alors le fichier csv final de la table de faits avec le fichier csv de la dimension Date correspondant :
    ```bash
    python3 script_parse_data_warehouse.py
    ```

    **Listes des fichiers csv que vous devez avoir à la fin :**    
    * team.csv
    * country.csv
    * league.csv
    * match_date.csv
    * facts.csv

1. Nous avons utlisé SQLDevelopper, ce qui nous a permis de créer notre entrepôt de données en important directement les fichiers csv finaux ci-dessus.

