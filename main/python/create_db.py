import mysql.connector

cnx = mysql.connector.connect(user='ben', password='',
                              host='127.0.0.1',
                              database='odds')

drop_query = (
    "DROP TABLE `sportsbooks`;"
    "DROP TABLE `nfl_teams`;"
    "DROP TABLE `nfl_events`;"
    "DROP TABLE `nfl_odds`;"
)

dump = (
    "-- sportsbooks table"
    "CREATE TABLE `sportsbooks` ("
    "  `sportsbook_id` int(11) NOT NULL,"
    "  `system_id` int(11),"
    "  `name` text NOT NULL,"
    "  `alias` text"
    ") ENGINE=InnoDB;"
    "-- nfl_teams table"
    "CREATE TABLE `nfl_teams` ("
    "`sbr_abbreviation` VARCHAR(256),"
    "`abbreviation` VARCHAR(256),"
    "`team_id` INT,"
    "`name` VARCHAR(256),"
    "`nickname` VARCHAR(256),"
    "`location` VARCHAR(256)"
    ") ENGINE=InnoDB;"
    "-- nfl_events table" 
    "CREATE TABLE `nfl_events` ("
    "`recorded_at` DATETIME,"
    "`participant_id_1` INT,"
    "`participant_id_2` INT,"
    "`participant_name_1` VARCHAR(256),"
    "`participant_name_2` VARCHAR(256),"
    "`is_home_1` BOOLEAN,"
    "`is_home_2` BOOLEAN,"
    "`score_1` INT,"
    "`score_2` INT,"
    "`sport_id` INT,"
    "`league_id` INT,"
    "`season_id` INT,"
    "`event_id` INT,"
    "`description` VARCHAR(256),"
    "`location` VARCHAR(256),"
    "`event_status` VARCHAR(256),"
    "`event_date` DATETIME"
    ") ENGINE=InnoDB;"
    "-- nfl_odds table"
    "CREATE TABLE `nfl_odds` ("
    "`line_offered_at` DATETIME,"
    "`market_id` INT,"
    "`event_id` INT,"
    "`sportsbook_id` INT,"
    "`event_date` DATETIME,"
    "`participant_id` INT,"
    "`spread_total` DOUBLE,"
    "`decimal_odds` DOUBLE,"
    "`american_odds` INT"
    ") ENGINE=InnoDB;"
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

create_nfl_events = (
    "CREATE TABLE `nfl_events` ("
    "`recorded_at` DATETIME,"
    "`participant_id_1` INT,"
    "`participant_id_2` INT,"
    "`participant_name_1` VARCHAR(256),"
    "`participant_name_2` VARCHAR(256),"
    "`is_home_1` BOOLEAN,"
    "`is_home_2` BOOLEAN,"
    "`score_1` INT,"
    "`score_2` INT,"
    "`sport_id` INT,"
    "`league_id` INT,"
    "`season_id` INT,"
    "`event_id` INT,"
    "`description` VARCHAR(256),"
    "`location` VARCHAR(256),"
    "`event_status` VARCHAR(256),"
    "`event_date` DATETIME"
    ") ENGINE=InnoDB"
)

create_nfl_odds = (
    "CREATE TABLE `nfl_odds` ("
    "`line_offered_at` DATETIME,"
    "`market_id` INT,"
    "`event_id` INT,"
    "`sportsbook_id` INT,"
    "`event_date` DATETIME,"
    "`participant_id` INT,"
    "`spread_total` DOUBLE,"
    "`decimal_odds` DOUBLE,"
    "`american_odds` INT"
    ") ENGINE=InnoDB;"
)

cursor = cnx.cursor()
cursor.execute(dump, multi=True)
cnx.close()

# cursor = cnx.cursor()
# cursor.execute(create_sportsbooks)
# cursor = cnx.cursor()
# cursor.execute(create_nfl_teams)
# cursor = cnx.cursor()
# cursor.execute(create_nfl_events)
# cursor = cnx.cursor()
# cursor.execute(create_nfl_odds)
# cnx.close()