"""
Project: Discordgg.py
File: riotGamesAPI.py
Author: Daniel Chung
Date: 9/02/19
Description: This file contains all the functions that are
related to the Riot Games API mostly using GET requests.
Installs: request
"""

import requests
from functions import *

riotApiKey = "RGAPI-a2df110b-81c3-49cc-85fb-80553838885d"

"""
Param: summonerName (from user input)
This function gets the summonerID (different from summoner name)
this is used for future use. Here also happens the check for error
404 meaning that the summoner doesn't exist and therefore doing 
error handling.
Return: (boolean) if Error, (str) summonerID 
"""
def getSummonerID(summonerName):
    URL = "https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + riotApiKey
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
def getSummonerRank(summonerID, summoner):
    URL = "https://la1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerID + "?api_key=" + riotApiKey
    response = requests.get(url=URL)
    data = response.json()
    index = getQueueType(data)
    if index != False:
        tier = data[index]['tier']
        rank = data[index]['rank']
        wins = data[index]['wins']
        losses = data[index]['losses']
        lp = str(data[index]['leaguePoints'])
        winRatio = getWinRatio(wins, losses)
        fullRank = summoner.capitalize() + "\n" +tier + " " + rank + " " + lp + "lp\nW/L: " + str(wins) +"/"+ str(losses) + " WR:" + str(winRatio) + "%"
        return fullRank
    else:
        return "Summoner has no Ranked games"