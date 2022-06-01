from getPlayerData import *
from sqlFunctions import *

# Grabbing player data from getPlayerData.py
# Prepares it to be queried into sql database
urls = getURL_list(url, allNBAteams)
player3PTstats = getAllStats(urls)
# connect to database using sqlFunctoins
connection = create_db_connection("localhost", "root", "Connor01", "sys")

# Queries
sql = '''
    INSERT INTO players (player_id, player_name, player_team, 3PT_shots_made, 3PT_shots_attempted, 3PT_percentage) VALUES (%s %s %s %s %s %s)
    '''
for player in player3PTstats:
    
    