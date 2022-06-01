from scrapeData import *
import time

allNBAteams = ["ATL", "BRK", "BOS", "CHO", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]

allPlayers3PTstats = []

url = "https://www.basketball-reference.com/"

def getURL_list(url, allNBAteams):
    return [url + "teams/" + i + "/2022.html" for i in allNBAteams]

def getAllStats(allURLs):
    for idx, url in enumerate(allURLs):
        page = httpsRequest(url)
        playerStats = getPlayerTotalStats(page)
        makePlayer(playerStats, allPlayers3PTstats, allNBAteams[idx])
        # time.sleep(5)
    return allPlayers3PTstats

# ///TODO - separate list of dictionaries into individual list of each stat to expedite database entry.

# def getPlayerNames(dct):
#     return [d['name'] for d in dct]

# def getPlayer3PTM(dct):
#     return [d['3PM'] for d in dct]

# def getPlayer3PTA(dct):
#     return [d['3PA'] for d in dct]

# def getPlayer3PT_pct(dct):
#     return [d['3P%'] for d in dct]

# print(getAllStats(getURL_list(url, allNBAteams)))

