from getPlayerData import *
from sqlFunctions import *

# Grabbing player data from getPlayerData.py
# Prepares it to be queried into sql database
urls = getURL_list(url, allNBAteams)
player3PTstats = getAllStats(urls)
players = playerListsOfLists(player3PTstats)
# connect to database using sqlFunctoins
create_db_connection("localhost", "root", "Connor01", "sys")

# Queries
