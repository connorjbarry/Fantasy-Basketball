import requests
from bs4 import BeautifulSoup

#Make Functions for most steps

playerList = []

url = "https://www.basketball-reference.com/teams/MIA/2022.html"

#http get request - httpsRequest()
def httpsRequest(url):
    page = requests.get(url)
    return page

# Parse HTML content from webpage - getPLayerTotalStats()
def getPlayerTotalStats(page):
    parsedPage = BeautifulSoup(page.content, "html.parser")
    teamTotalStats = parsedPage.find(id="totals")
    tempFind = teamTotalStats.find("tbody")
    playerTotalStats = tempFind.find_all("tr")
    return playerTotalStats


def makePlayerDict(playerStats, playerList):
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
        playerDict = {
            'name' : player_name.text,
            '3PM'  : threesMade,
            '3PA'  : threesAttempted,
            '3P%'  : threesPct
        }
        makeListPlayers(playerList, playerDict)

def makeListPlayers(playerList, playerDict):
    playerList.append(playerDict)

# page = httpsRequest(url)
# playerStats = getPlayerTotalStats(page)
# makePlayerDict(playerStats, playerList)
# print(playerList)


# Parse HTML content from webpage - getPLayerTotalStats()
# soup = BeautifulSoup(page.content, "html.parser")
# teamTotals = soup.find(id="totals")
# playerTotals = teamTotals.find_all("tr")
# for i in range(1,len(playerTotals)-1):
    # player_name = playerTotals[i].find('td', class_="left")
    # print(player_name.text)
    # player_stats = playerTotals[i].find_all('td', class_="right")
    # print(player_stats)
    # print(player_stats[0].attrs)
    # for idx, data in enumerate(player_stats):
        # if player_stats[idx].attrs['data-stat'] == 'fg3':
            # threesMade = player_stats[idx].text
        # elif player_stats[idx].attrs['data-stat'] == 'fg3a':
            # threesAttempted = player_stats[idx].text
        # elif player_stats[idx].attrs['data-stat'] == 'fg3_pct':
            # if player_stats[idx].text == '':
                # player_stats[idx].text = 0
            # threesPct = player_stats[idx].text
    # playerDict = {
        # 'name' : player_name.text,
        # '3PM'  : threesMade,
        # '3PA'  : threesAttempted,
        # '3P%'  : threesPct
    # }
    # playerList.append(playerDict)    