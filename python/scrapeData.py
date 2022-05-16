import requests
from bs4 import BeautifulSoup

#Make Functions for most steps


#http get request - httpsRequest()
URL = "https://www.basketball-reference.com/teams/MIA/2022.html"
homePage = requests.get(URL)
# def httpsRequest(url):
#     page = requests.get(url)
#     return page

#Parse HTML content from webpage
soup = BeautifulSoup(homePage.content, "html.parser")

# eastStandings = soup.find_all("tr", class_="full_table")

# team_name = eastStandings[0].find("th", class_="left")
# print(team_name.text)
# team_wins = eastStandings[0].find_all("td", class_="right")
# print(team_wins)

teamTotals = soup.find(id="totals")
# print(teamTotals)
playerTotals = teamTotals.find_all("tr")
# print(playerTotals)
print(len(playerTotals))