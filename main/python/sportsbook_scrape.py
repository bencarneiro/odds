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

