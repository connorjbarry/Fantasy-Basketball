from scrapeData import *
import time

allNBAteams = ["ATL", "BRK", "BOS", "CHO", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]

allPlayers3PTstats = []

url = "https://www.basketball-reference.com/"

allURLs = [url + "teams/" + i + "/2022.html" for i in allNBAteams]

for url in allURLs:
    page = httpsRequest(url)
    playerStats = getPlayerTotalStats(page)
    makePlayerDict(playerStats, allPlayers3PTstats)
    time.sleep(5)
print(allPlayers3PTstats)
