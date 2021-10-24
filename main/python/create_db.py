# import pandas as pd
# import datetime

import mysql.connector

cnx = mysql.connector.connect(user='ben', password='',
                              host='127.0.0.1',
                              database='odds')
cursor = cnx.cursor()

drop_query = (
    "DROP TABLE sportsbooks"
)

test_query = (
    "CREATE TABLE `sportsbooks` ("
    "  `sportsbook_id` int(11) NOT NULL,"
    "  `system_id` int(11),"
    "  `name` text NOT NULL,"
    "  `alias` text"
    ") ENGINE=InnoDB"
)


cursor.execute(test_query)
cnx.close()