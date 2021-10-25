from pysbr import *

import mysql.connector

cnx = mysql.connector.connect(user='ben', password='',
                              host='127.0.0.1',
                              database='odds')

nfl = NFL()
teams_inserts = []
for team in nfl.league_config()['teams']:
    team_data = [(team['sbr abbreviation'], team['abbreviation'], team['team id'], team['name'], team['nickname'], team['location'])]
    teams_inserts += team_data
add_sportsbook_query = "INSERT INTO `nfl_teams` (`sbr_abbreviation`, `abbreviation`, `team_id`, `name`, `nickname`, `location`) VALUES (%s,%s,%s,%s,%s,%s)"
cursor = cnx.cursor()
cursor.executemany(add_sportsbook_query, teams_inserts)
cnx.commit()
cnx.close()

print(teams_inserts)