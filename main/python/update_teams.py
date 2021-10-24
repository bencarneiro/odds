# Create Table of NFL Teams
nfl_teams = pd.DataFrame(columns=['sbr_abbreviation','abbreviation','team_id','name','nickname','location'],data=[])
for team in nfl.league_config()['teams']:
    team_row = pd.DataFrame(columns=['sbr_abbreviation','abbreviation','team_id','name','nickname','location'],data=[[team['sbr abbreviation'], team['abbreviation'],team['team id'],team['name'],team['nickname'],team['location']]])
    nfl_teams = nfl_teams.append(team_row, ignore_index=True)
    print(team)
print(nfl_teams)