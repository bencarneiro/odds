dt = datetime.datetime.now() - datetime.timedelta(days=3)
timestamp = datetime.datetime.now()
games = pysbr.EventsByDate(nfl.league_id, dt).list()
games_table = pd.DataFrame(columns=['recorded_at','participant_id_1','participant_id_2','participant_name_1','participant_name_2','is_home_1','is_home_2','score_1','score_2','sport_id','league_id','season_id','event_id','description','location','event_status','event_date'],data=[])
for game in games:
    participant_id_1 = game['participants'][0]['participant id']
    participant_id_2 = game['participants'][1]['participant id']   
    participant_name_1 = game['participants'][0]['source']['name']
    participant_name_2 = game['participants'][1]['source']['name']
    is_home_1 = game['participants'][0]['is home']
    is_home_2 = game['participants'][1]['is home']
    score_1 = 0
    score_2 = 0
    for score in game['scores']:
        if score['participant id'] == participant_id_1:
            score_1 += score['points scored'] 
        if score['participant id'] == participant_id_2:
            score_2 += score['points scored'] 
    game_row = pd.DataFrame(columns=['recorded_at','participant_id_1','participant_id_2','participant_name_1','participant_name_2','is_home_1','is_home_2','score_1','score_2','sport_id','league_id','season_id','event_id','description','location','event_status','event_date'],data=[[timestamp,participant_id_1,participant_id_2,participant_name_1,participant_name_2,is_home_1,is_home_2,score_1,score_2,game['sport id'],game['league id'],game['season id'],game['event id'],game['description'],game['location'],game['event status'],game['datetime']]])
    games_table = games_table.append(game_row)
games_table