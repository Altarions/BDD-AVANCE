import csv

# Going through match_csv to sort the data
with open('projet/outmatch.csv', mode='r') as match_csv:
    csv_reader = csv.DictReader(match_csv)

    # Create the tab for retrieve the values of some attributs
    tab_id = []
    tab_country_id = []
    tab_league_id = []
    tab_date = []
    tab_home_team_api_id = []
    tab_away_team_api_id = []
    tab_goal = []
    tab_shoton = []
    tab_shotoff = []
    tab_foulcommit = []
    tab_card = []
    tab_cross = []
    tab_corner = []
    tab_possession = []

    for row in csv_reader:
    
        # We want only lines with all events which aren't null (at least one of these events)
        if(row["goal"] != "" or row["shoton"] != "" or row["shotoff"] != "" or row["foulcommit"] != "" or row["card"] != "" or row["cross"] != "" or row["corner"] != "" or row["possession"] != ""):
            tab_id.append(row["id"])
            tab_country_id.append(row["country_id"])
            tab_league_id.append(row["league_id"])
            tab_date.append(row["date"])
            tab_home_team_api_id.append(row["home_team_api_id"])
            tab_away_team_api_id.append(row["away_team_api_id"])
            tab_goal.append(row["goal"])
            tab_shoton.append(row["shoton"])
            tab_shotoff.append(row["shotoff"])
            tab_foulcommit.append(row["foulcommit"])
            tab_card.append(row["card"])
            tab_cross.append(row["cross"])
            tab_corner.append(row["corner"])
            tab_possession.append(row["possession"])
    

# We overwrite the csv file with the retrieved data
with open('raw-aggregate.csv', mode='w') as new_csv:
    fieldnames = ['id', 'country_id', 'league_id', 'date', 'home_team_api_id', 'away_team_api_id', 'goal', 'shoton', 'shotoff', 'foulcommit', 'card', 'cross', 'corner', 'possession']
    writer = csv.DictWriter(new_csv, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(len(tab_id)):
        writer.writerow({'id' : tab_id[i], 'country_id' : tab_country_id[i], 'league_id' : tab_league_id[i], 'date' : tab_date[i], 'home_team_api_id' : tab_home_team_api_id[i], 'away_team_api_id' : tab_away_team_api_id[i], 'goal' : tab_goal[i], 'shoton' : tab_shoton[i], 'shotoff' : tab_shotoff[i], 'foulcommit' : tab_foulcommit[i], 'card' : tab_card[i], 'cross' : tab_cross[i], 'corner' : tab_corner[i], 'possession' : tab_possession[i]})
