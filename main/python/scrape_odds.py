from pysbr import *
nfl = NFL()

import mysql.connector

import datetime

cnx = mysql.connector.connect(user='ben', password='',
                              host='127.0.0.1',
                              database='odds')
cursor = cnx.cursor()

# define sportsbook ids
book_ids = []
check_sportsbook_query = "SELECT sportsbook_id FROM sportsbooks"
cursor.execute(check_sportsbook_query)
for (sportsbook_id,) in cursor:
    if sportsbook_id not in book_ids:
        book_ids += [sportsbook_id]



dt = datetime.datetime.now() - datetime.timedelta(days=2)
timestamp = datetime.datetime.now()

odds_inserts = []
for x in range(9):
    dt = dt + datetime.timedelta(days=1)
    event_ids = EventsByDate(nfl.league_id, dt).ids()
    odds_data = CurrentLines(event_ids, nfl.market_ids(['Point Spreads','Money Lines','Totals']), book_ids).list()
    for bet in odds_data:
        bet_row = [(timestamp,bet['market id'],bet['event id'],bet['sportsbook id'],bet['datetime'],bet['participant id'],bet['spread / total'], bet['decimal odds'], bet['american odds'])]
        odds_inserts += bet_row  

insert_odds_query = "INSERT INTO `nfl_odds` (`line_offered_at`, `market_id`, `event_id`, `sportsbook_id`,  `event_date`, `participant_id`, `spread_total`, `decimal_odds`, `american_odds`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
cursor = cnx.cursor()
cursor.executemany(insert_odds_query, odds_inserts)
cnx.commit()
cnx.close()



# current_lines = pd.DataFrame(columns=['line_offered_at','market_id','event_id','sportsbook_id','event_date','participant_id','spread_total','decimal_odds','american_odds'],data=[])
# for x in range(8):
#     dt = dt + datetime.timedelta(days=1)
#     event_ids = pysbr.EventsByDate(nfl.league_id, dt).ids()
#     odds_data = pysbr.queries.currentlines.CurrentLines(event_ids, nfl.market_ids(['Point Spreads','Money Lines','Totals']), sportsbooks['sportsbook_id'].tolist()).list()
#     for bet in odds_data:
#         bet_row = pd.DataFrame(columns=['line_offered_at','market_id','event_id','sportsbook_id','event_date','participant_id','spread_total','decimal_odds','american_odds'],data=[[timestamp,bet['market id'],bet['event id'],bet['sportsbook id'],bet['datetime'],bet['participant id'],bet['spread / total'], bet['decimal odds'], bet['american odds']]])
#         current_lines = current_lines.append(bet_row, ignore_index=True)