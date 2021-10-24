dt = datetime.datetime.now() - datetime.timedelta(days=1)
timestamp = datetime.datetime.now()
current_lines = pd.DataFrame(columns=['line_offered_at','market_id','event_id','sportsbook_id','event_date','participant_id','spread_total','decimal_odds','american_odds'],data=[])
for x in range(8):
    dt = dt + datetime.timedelta(days=1)
    event_ids = pysbr.EventsByDate(nfl.league_id, dt).ids()
    odds_data = pysbr.queries.currentlines.CurrentLines(event_ids, nfl.market_ids(['Point Spreads','Money Lines','Totals']), sportsbooks['sportsbook_id'].tolist()).list()
    for bet in odds_data:
        bet_row = pd.DataFrame(columns=['line_offered_at','market_id','event_id','sportsbook_id','event_date','participant_id','spread_total','decimal_odds','american_odds'],data=[[timestamp,bet['market id'],bet['event id'],bet['sportsbook id'],bet['datetime'],bet['participant id'],bet['spread / total'], bet['decimal odds'], bet['american odds']]])
        current_lines = current_lines.append(bet_row, ignore_index=True)