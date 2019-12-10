"""
Project: Discordgg.py
File: riotGamesAPI.py
Author: @Daniel Chung
Date: 02/9/19
Description: This file contains all the functions that are
related to the Riot Games API mostly using GET requests.
Installs: request
"""
import API_Keys
import requests
from functions import *

riotApiKey = API_Keys.riot_games_api()

"""
Param: summonerName (from user input)
This function gets the summonerID (different from summoner name)
this is used for future use. Here also happens the check for error
404 meaning that the summoner doesn't exist and therefore doing 
error handling.
Return: (boolean) if Error, (str) summonerID 
"""
def getSummonerID(summonerName, region):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + riotApiKey
    print(URL)
    response = requests.get(url=URL)
    data = response.json()
    if len(data) == 1:
        if data["status"]["status_code"] == "404":
            return False
        return False
    else:
        summonerID = data['id']
        return summonerID

"""
Param: summonerID (getSummonerID), summoner (summonerName from user input).
This function is the one that is responsible for the main 
method of the application. It will format and return the 
rank information of the summoner name to be displayed. 
Returns: (str) User's ranked information or No ranked games.  
"""
def getSummonerRank(summonerID, summoner, region):
    URL = "https://" + region +".api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerID + "?api_key=" + riotApiKey
    print(URL)
    response = requests.get(url=URL)
    data = response.json()
    index = getQueueType(data)
    print("index: " + str(index))
    if index != 4:
        tier = data[index]['tier']
        print(tier)
        rank = data[index]['rank']
        print(rank)
        wins = data[index]['wins']
        losses = data[index]['losses']
        lp = str(data[index]['leaguePoints'])
        winRatio = getWinRatio(wins, losses)

        fullRank = "```fix\n" + summoner.capitalize() + "\n" +tier + " " + rank + " " + lp + "lp\n" + str(wins) +"/"+ str(losses) + "\n" + str(winRatio) + "% \n```"
        return fullRank
    else:
        print("im in else")
        return "Summoner has no Ranked games"