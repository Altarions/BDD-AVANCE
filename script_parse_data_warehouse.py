#but de ce fichier : récupérer les données interessantes et construire la table de fait

import csv
import xml.etree.ElementTree as ET

compt = 0

# Going through match_csv to sort the data
with open('fact_table_before_script.csv', mode='r') as match_csv:
    csv_reader = csv.DictReader(match_csv)

    # Create the tab for retrieve the values of some attributs
    tab_event_id = []
    tab_type = []
    tab_involved_team_id = []
    tab_home_team_id = []
    tab_away_team_id = []
    tab_match_id = []
    tab_home_team_pos = []
    tab_away_team_pos = []
    tab_country_id = []
    tab_date = []
    tab_league_id = []

    #Ici, row est une ligne représentant un match
    for row in csv_reader:

        tree_goal = ET.fromstring(row["goal"])
        tree_shoton = ET.fromstring(row["shoton"])
        tree_shotoff = ET.fromstring(row["shotoff"])
        tree_foulcommit = ET.fromstring(row["foulcommit"])
        tree_corner = ET.fromstring(row["corner"])
        tree_cross = ET.fromstring(row["cross"])
        tree_card = ET.fromstring(row["card"])
        tree_possession = ET.fromstring(row["possession"])

        #tab_match_goals contient tous les buts de ce match
        tab_match_goals = []
        tab_match_shoton = []
        tab_match_shotoff = []
        tab_match_foulcommit = []
        tab_match_corner = []
        tab_match_cross = []
        tab_match_card = []
        tab_match_possession = []

        #ces lignes ajoutent les différentes valeurs des balises dans des tableaux,
        #pour par la suite les traiter en tant que fichier xml
        for child in tree_shoton:
            tab_match_shoton.append(child)

        for child in tree_shotoff:
            tab_match_shoton.append(child)

        for child in tree_goal:
            tab_match_goals.append(child)

        for child in tree_foulcommit:
            tab_match_foulcommit.append(child)

        for child in tree_corner:
            tab_match_corner.append(child)

        for child in tree_cross:
            tab_match_cross.append(child)

        for child in tree_card:
            tab_match_card.append(child)

        for child in tree_possession:
            tab_match_possession.append(child)

        #cette partie selectionne les données utiles pour la table de faits dans les attributs listes du jeu de données initial
        for elt in tab_match_shoton:
            for child in elt:
                if child.tag == "team":
                    #print(child.tag, " : ", child.text)
                    tab_involved_team_id.append(child.text)

            tab_event_id.append(compt)
            compt = compt + 1

            tab_type.append("shoton")
            tab_home_team_id.append(row["home_team_api_id"])
            tab_away_team_id.append(row["away_team_api_id"])
            tab_match_id.append(row["id"])
            tab_country_id.append(row["country_id"])
            tab_date.append(row["date"])
            tab_home_team_pos.append("")
            tab_away_team_pos.append("")
            tab_league_id.append(row["league_id"])

        for elt in tab_match_goals:
            for child in elt:
                if child.tag == "team":
                    #print(child.tag, " : ", child.text)
                    tab_involved_team_id.append(child.text)

            tab_event_id.append(compt)
            compt = compt + 1

            tab_type.append("goal")
            tab_home_team_id.append(row["home_team_api_id"])
            tab_away_team_id.append(row["away_team_api_id"])
            tab_match_id.append(row["id"])
            tab_country_id.append(row["country_id"])
            tab_date.append(row["date"])
            tab_home_team_pos.append("")
            tab_away_team_pos.append("")
            tab_league_id.append(row["league_id"])

        for elt in tab_match_shotoff:
            for child in elt:
                if child.tag == "team":
                    #print(child.tag, " : ", child.text)
                    tab_involved_team_id.append(child.text)

            tab_event_id.append(compt)
            compt = compt + 1

            tab_type.append("shotoff")
            tab_home_team_id.append(row["home_team_api_id"])
            tab_away_team_id.append(row["away_team_api_id"])
            tab_match_id.append(row["id"])
            tab_country_id.append(row["country_id"])
            tab_date.append(row["date"])
            tab_home_team_pos.append("")
            tab_away_team_pos.append("")
            tab_league_id.append(row["league_id"])

        for elt in tab_match_foulcommit:
            for child in elt:
                if child.tag == "team":
                    tab_involved_team_id.append(child.text)

            tab_event_id.append(compt)
            compt = compt + 1

            tab_type.append("foulcommit")
            tab_home_team_id.append(row["home_team_api_id"])
            tab_away_team_id.append(row["away_team_api_id"])
            tab_match_id.append(row["id"])
            tab_country_id.append(row["country_id"])
            tab_date.append(row["date"])
            tab_home_team_pos.append("")
            tab_away_team_pos.append("")
            tab_league_id.append(row["league_id"])

        for elt in tab_match_corner:
            for child in elt:
                if child.tag == "team":
                    #print(child.tag, " : ", child.text)
                    tab_involved_team_id.append(child.text)

            tab_event_id.append(compt)
            compt = compt + 1

            tab_type.append("corner")
            tab_home_team_id.append(row["home_team_api_id"])
            tab_away_team_id.append(row["away_team_api_id"])
            tab_match_id.append(row["id"])
            tab_country_id.append(row["country_id"])
            tab_date.append(row["date"])
            tab_home_team_pos.append("")
            tab_away_team_pos.append("")
            tab_league_id.append(row["league_id"])

        for elt in tab_match_cross:
            for child in elt:
                if child.tag == "team":
                    #print(child.tag, " : ", child.text)
                    tab_involved_team_id.append(child.text)

            tab_event_id.append(compt)
            compt = compt + 1

            tab_type.append("cross")
            tab_home_team_id.append(row["home_team_api_id"])
            tab_away_team_id.append(row["away_team_api_id"])
            tab_match_id.append(row["id"])
            tab_country_id.append(row["country_id"])
            tab_date.append(row["date"])
            tab_home_team_pos.append("")
            tab_away_team_pos.append("")
            tab_league_id.append(row["league_id"])

        for elt in tab_match_card:
            for child in elt:
                if child.tag == "team":
                    tab_involved_team_id.append(child.text)

            tab_event_id.append(compt)
            compt = compt + 1

            tab_type.append("card")
            tab_home_team_id.append(row["home_team_api_id"])
            tab_away_team_id.append(row["away_team_api_id"])
            tab_match_id.append(row["id"])
            tab_country_id.append(row["country_id"])
            tab_date.append(row["date"])
            tab_home_team_pos.append("")
            tab_away_team_pos.append("")
            tab_league_id.append(row["league_id"])

        if len(tab_match_possession) > 0:
            elt_pos = tab_match_possession[-1]

            for child in elt_pos:
                if child.tag == "homepos":
                    tab_home_team_pos.append(child.text)

                if child.tag == "awaypos":
                    tab_away_team_pos.append(child.text)

                tab_event_id.append(compt)
                compt = compt + 1

            tab_type.append("possession")
            tab_home_team_id.append(row["home_team_api_id"])
            tab_away_team_id.append(row["away_team_api_id"])
            tab_match_id.append(row["id"])
            tab_country_id.append(row["country_id"])
            tab_date.append(row["date"])
            tab_involved_team_id.append("")
            tab_league_id.append(row["league_id"])

# We overwrite the csv file with the retrieved data
with open('fact_table_after_script.csv', mode='w', newline='') as new_csv:
    fieldnames = ['event_id', 'type','home_team_id','away_team_id','match_id','country_id','league_id','date','involved_team_id','home_team_pos','away_team_pos']
    writer = csv.DictWriter(new_csv, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(len(tab_event_id)):
        print("event id : ",tab_event_id[i])
        print("i : ", i)

        writer.writerow(
            {'event_id': tab_event_id[i],
             'type': tab_type[i],
             'home_team_id': tab_home_team_id[i],
             'away_team_id': tab_away_team_id[i],
             'match_id': tab_match_id[i],
             'country_id': tab_country_id[i],
             'league_id': tab_league_id[i],
             'date': tab_date[i],
             'involved_team_id': tab_involved_team_id[i],
             'home_team_pos': tab_home_team_pos[i],
             'away_team_pos': tab_away_team_pos[i]
             })
