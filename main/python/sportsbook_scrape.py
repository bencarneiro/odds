import pysbr
import pandas as pd
import sqlite3
import datetime

nfl = pysbr.NFL()
sb = pysbr.Sportsbook()

# Create table of sportsbooks
sportsbook_keys_json = sb.sportsbook_config()['sportsbooks']
sportsbooks = pd.DataFrame(columns=['system_id','sportsbook_id','name','alias'], data=[])
for book in sportsbook_keys_json:
    book_row = pd.DataFrame(columns=['system_id','sportsbook_id','name','alias'], data=[[book['system sportsbook id'], book['sportsbook id'], book['name'], book['alias']]])
    sportsbooks = sportsbooks.append(book_row, ignore_index=True)

# Create Table of NFL Teams
nfl_teams = pd.DataFrame(columns=['sbr_abbreviation','abbreviation','team_id','name','nickname','location'],data=[])
for team in nfl.league_config()['teams']:
    team_row = pd.DataFrame(columns=['sbr_abbreviation','abbreviation','team_id','name','nickname','location'],data=[[team['sbr abbreviation'], team['abbreviation'],team['team id'],team['name'],team['nickname'],team['location']]])
    nfl_teams = nfl_teams.append(team_row, ignore_index=True)
    print(team)
print(nfl_teams)