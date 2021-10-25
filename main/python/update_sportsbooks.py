from pysbr import *

import mysql.connector

cnx = mysql.connector.connect(user='ben', password='',
                              host='127.0.0.1',
                              database='odds')
cursor = cnx.cursor()

sb = Sportsbook()

# update table of sportsbooks
sportsbook_keys_json = sb.sportsbook_config()['sportsbooks']
inserts = []
for book in sportsbook_keys_json:
    write = True
    print(book)
    if book['sportsbook id']:
        check_sportsbook_query = "SELECT * FROM sportsbooks WHERE sportsbook_id = %s"
        cursor.execute(check_sportsbook_query, (book['sportsbook id'],))
        for (sportsbook_id, system_id, name, alias) in cursor:
            if sportsbook_id == book['sportsbook id'] and system_id == book['system sportsbook id']:
                write = False
        if write:
            print("WRITING: ", book['sportsbook id'])
            add_sportsbook_query = "INSERT INTO `sportsbooks` (`sportsbook_id`, `system_id`, `name`, `alias`) VALUES (%s,%s,%s,%s)"
            inserts += [(book['sportsbook id'], book['system sportsbook id'], book['name'], book['alias'])]

add_sportsbook_query = "INSERT INTO `sportsbooks` (`sportsbook_id`, `system_id`, `name`, `alias`) VALUES (%s,%s,%s,%s)"
cursor = cnx.cursor()
cursor.executemany(add_sportsbook_query, inserts)
cnx.commit()
cnx.close()