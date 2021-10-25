# import pandas as pd
# import datetime

import mysql.connector

cnx = mysql.connector.connect(user='ben', password='',
                              host='127.0.0.1',
                              database='odds')
cursor = cnx.cursor()

drop_query = (
    "DROP ALL TABLES
)

create_sportsbooks = (
    "CREATE TABLE `sportsbooks` ("
    "  `sportsbook_id` int(11) NOT NULL,"
    "  `system_id` int(11),"
    "  `name` text NOT NULL,"
    "  `alias` text"
    ") ENGINE=InnoDB"
)

create_nfl_teams = (
    "CREATE TABLE `nfl_teams` ("
    "`sbr_abbreviation` VARCHAR(256),"
    "`abbreviation` VARCHAR(256),"
    "`team_id` INT,"
    "`name` VARCHAR(256),"
    "`nickname` VARCHAR(256),"
    "`location` VARCHAR(256)"
    ") ENGINE=InnoDB"
)


cursor.execute(test_query)
cnx.close()