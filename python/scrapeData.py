import requests
from bs4 import BeautifulSoup
from playerClass import *

# ///TODO - Make Functions for most steps

playerList = []
url = "https://www.basketball-reference.com/teams/MIA/2022.html"

# http get request - httpsRequest()
def httpsRequest(url):
    page = requests.get(url)
    return page

# Parse HTML content from webpage - getPLayerTotalStats()
def getPlayerTotalStats(page):
    parsedPage = BeautifulSoup(page.content, "html.parser")
    teamTotalStats = parsedPage.find(id="totals")
    findTable = teamTotalStats.find("tbody")
    playerTotalStats = findTable.find_all("tr")
    return playerTotalStats


def makePlayer(playerStats, playerList, team):
    for i in range(0,len(playerStats)):
        player_name = playerStats[i].find('td', class_="left")
        player_stats = playerStats[i].find_all('td', class_="right")
        for idx, data in enumerate(player_stats):
            if player_stats[idx].attrs['data-stat'] == 'fg3':
                threesMade = data.text
            elif player_stats[idx].attrs['data-stat'] == 'fg3a':
                threesAttempted = data.text
            elif player_stats[idx].attrs['data-stat'] == 'fg3_pct':
                threesPct = data.text

        player = Player(None, player_name.text, team, threesMade, threesAttempted, threesPct)

        makeListPlayers(playerList, player)

def makeListPlayers(playerList, player):
    playerList.append(player.getPlayer())

# page = httpsRequest(url)
# playerStats = getPlayerTotalStats(page)
# makePlayer(playerStats, playerList, "Mia") 
# print(playerList)  