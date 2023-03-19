''' PROJECT OF DATA BASE EVOLVED -- 03-2023
    This script generates the fact table csv and the date table csv.
'''

import csv
import xml.etree.ElementTree as ET
from datetime import datetime

compt_event_id = 0

# Going through match_csv to sort the data
with open('raw-aggregate.csv', mode='r') as match_csv:
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

    # Each iteration of the loop is focused on 1 match with several events
    for row in csv_reader:

        tree_goal = ET.fromstring(row["goal"])
        tree_shoton = ET.fromstring(row["shoton"])
        tree_shotoff = ET.fromstring(row["shotoff"])
        tree_foulcommit = ET.fromstring(row["foulcommit"])
        tree_corner = ET.fromstring(row["corner"])
        tree_cross = ET.fromstring(row["cross"])
        tree_card = ET.fromstring(row["card"])
        tree_possession = ET.fromstring(row["possession"])

        # tab_match_goals contains all goals of the current match, tab_match_shoton contains all shoton events of the current match, etc...
        tab_match_goals = []
        tab_match_shoton = []
        tab_match_shotoff = []
        tab_match_foulcommit = []
        tab_match_corner = []
        tab_match_cross = []
        tab_match_card = []
        tab_match_possession = []

        # We add the different values of the events in tabs
        # These lines add the different values of the tags in tables to then process them as xml file
        for child in tree_shoton:
            tab_match_shoton.append(child)

        for child in tree_shotoff:
            tab_match_shotoff.append(child)

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

        # This part selects useful data for the fact table in the list attributes of the initial dataset
        for elt in tab_match_shoton:
            found = False

            for child in elt:
                if child.tag == "team":
                    found = True
                    tab_involved_team_id.append(child.text)
            if not found:
                tab_involved_team_id.append("")

            tab_event_id.append(compt_event_id)
            compt_event_id = compt_event_id + 1

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
            found = False

            for child in elt:
                if child.tag == "team":
                    found = True
                    tab_involved_team_id.append(child.text)
            if not found:
                tab_involved_team_id.append("")

            tab_event_id.append(compt_event_id)
            compt_event_id = compt_event_id + 1

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
            found = False

            for child in elt:
                if child.tag == "team":
                    found = True
                    tab_involved_team_id.append(child.text)
            if not found:
                tab_involved_team_id.append("")

            tab_event_id.append(compt_event_id)
            compt_event_id = compt_event_id + 1

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
            found = False

            for child in elt:
                if child.tag == "team":
                    found = True
                    tab_involved_team_id.append(child.text)
            if not found:
                tab_involved_team_id.append("")


            tab_event_id.append(compt_event_id)
            compt_event_id = compt_event_id + 1

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
            found = False

            for child in elt:
                if child.tag == "team":
                    found = True
                    tab_involved_team_id.append(child.text)
            if not found:
                tab_involved_team_id.append("")

            tab_event_id.append(compt_event_id)
            compt_event_id = compt_event_id + 1

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
            found = False

            for child in elt:
                if child.tag == "team":
                    found = True
                    tab_involved_team_id.append(child.text)
            if not found:
                tab_involved_team_id.append("")

            tab_event_id.append(compt_event_id)
            compt_event_id = compt_event_id + 1

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
            found = False

            for child in elt:
                if child.tag == "team":
                    found = True
                    tab_involved_team_id.append(child.text)
            if not found:
                tab_involved_team_id.append("")

            tab_event_id.append(compt_event_id)
            compt_event_id = compt_event_id + 1

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
            foundAway = False
            foundHome = False
            for child in elt_pos:
                

                if child.tag == "homepos":
                    foundHome = True
                    tab_home_team_pos.append(child.text)

                if child.tag == "awaypos":
                    foundAway = True
                    tab_away_team_pos.append(child.text)

            if (not foundHome) or (not foundAway):
                tab_home_team_pos.append("") 
                tab_away_team_pos.append("")

            tab_event_id.append(compt_event_id)
            compt_event_id = compt_event_id + 1    

            tab_type.append("possession")
            tab_home_team_id.append(row["home_team_api_id"])
            tab_away_team_id.append(row["away_team_api_id"])
            tab_match_id.append(row["id"])
            tab_country_id.append(row["country_id"])
            tab_date.append(row["date"])
            tab_involved_team_id.append("")
            tab_league_id.append(row["league_id"])

# Generates the CSV file of the Match_date dimension
day_name = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
seen_date = []

with open('match_date.csv', mode='w') as date_csv:
    fieldnames = ['match_date','day','month','year','weekday']
    writer = csv.DictWriter(date_csv, fieldnames=fieldnames)

    writer.writeheader()


    for i in range(len(tab_date)):
        # We avoid duplicated dates
        if tab_date[i] not in seen_date and int(tab_date[i][0:4]) >= 2015:
            seen_date.append(tab_date[i])
            day = int(tab_date[i][8:10])
            month = int(tab_date[i][5:7])
            year = int(tab_date[i][0:4])
            weekday = day_name[datetime(year, month, day, 0, 0, 0).weekday()]
            
            writer.writerow({'match_date' : tab_date[i],
                            'day' : day,
                            'month' : month,
                            'year' : year,
                            'weekday' : weekday})

# We overwrite the csv file with the retrieved data
with open('fact_table_after_script.csv', mode='w', newline='') as new_csv:
    fieldnames = ['event_id', 'type','home_team_id','away_team_id','match_id','country_id','league_id','date','involved_team_id','home_team_pos','away_team_pos']
    writer = csv.DictWriter(new_csv, fieldnames=fieldnames)

    writer.writeheader()
    
    #This is used to count the amount of events written in the output file. This is important to limit the amount of tuples eventually added to the data warehouse,
    #since our university doesn't allow us to insert an unlimited amount of tuples.
    cpt = 0
    for i in range(len(tab_event_id)):
        
        # We choose only 4 leagues because SQLDeveloper can't have too many rows in the same table.
        if (tab_league_id[i] == '4769' or tab_league_id[i] == '13274' or tab_league_id[i] == '15722' or tab_league_id[i] == '19694') and int(tab_date[i][0:4]) >= 2015:
            cpt = cpt + 1
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
                
