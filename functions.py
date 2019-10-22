"""
Project: Discordgg.py
File: functions.py
Author: Daniel Chung
Date: 9/02/19
Description: This file contains all the functions that are
general to only python code.
Installs: ---
"""


"""
Param: userInput.
This functions gets the summonerName from
the message input.
Return: (str) summonerName. (Basically a strip.)
"""
def getSummonerName(commandMessage):
    return commandMessage[1:]

"""
Param: Data (retrieved from the json in getSummonerRank()).
So data from the Riot Games API comes in randomly. Meaning that the 
queuetype is not static and is always changing. For it this method
checks in what position/index "Ranked Solo 5v5" is in and returns it.
Returns: (int) Position where "Ranked Solo 5v5" is in.
"""
def getQueueType(data):
    if len(data) == 0:
        return False
    if data[0]["queueType"] == "RANKED_SOLO_5x5":
        return 0
    elif data[1]["queueType"] == "RANKED_SOLO_5x5":
        return 1
    elif data[2]["queueType"] == "RANKED_SOLO_5x5":
        return 2

"""
Params: Users Wins, Users Losses.
This function is a basic rule of thirds to get the users Win Ratio.
Returns: (int) Win Ratio.
"""
def getWinRatio(wins, losses):
    x = wins + losses
    y = wins * 100
    return round(y / x)

"""
Params: message.content
This functions returns the server in which the search is going to be 
looked at.
"""
def getRegion(message):
    return message.split(" ")[0][1:].lower()

def test_getRegion():
    print("** TESTING getRegion(message) **")
    test1 = "!na pikachung"
    test2 = "!euw pikachung"
    test3 = "!lan pikachung"
    test4 = "!kr pikachung"
    print(getRegion(test1) == "na")
    print(getRegion(test2) == "euw")
    print(getRegion(test3) == "lan")
    print(getRegion(test4) == "kr")

def main():
    print("*** TESTING ***")
    test_getRegion()

main()