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
    return commandMessage.split(" ")[1]

"""
Param: Data (retrieved from the json in getSummonerRank()).
So data from the Riot Games API comes in randomly. Meaning that the 
queuetype is not static and is always changing. For it this method
checks in what position/index "Ranked Solo 5v5" is in and returns it.
Returns: (int) Position where "Ranked Solo 5v5" is in.
"""
def getQueueType(data):
    print('datalen: ' + str(len(data)))
    if data[0]["queueType"] == "RANKED_SOLO_5x5":
        return 0
    elif data[1]["queueType"] == "RANKED_SOLO_5x5":
        return 1
    elif data[2]["queueType"] == "RANKED_SOLO_5x5":
        return 2
    elif data[3]["queueType"] == "RANKED_SOLO_5x5":
        return 3
    else:
        return 4


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
    region = message.split(" ")[0][1:].lower()
    dictionary = {"ru" : "ru", "kr" : "kr", "br" : "br1", "oce" : "oc1", "jp" : "jp1", "na" : "na1", "eune" : "eun1",
                  "euw" : "euw1", "tr" : "tr1", "lan" : "la1", "las" : "la2", "help" : "help"}
    return dictionary[region]

def helpCommand():
    helpInstructions = "**Use: ![REGION] [SummonerName] [Command]** \n" \
            "**Commands:** \n" \
            "**' '** *(Summoner Information)* \n" \
            "**'-g'** *(Live Game Information)* \n"
    return helpInstructions

def test_getWinRatio():
    print("** TESTING getWinRatio(wins, loses) **")
    hundred = getWinRatio(100, 0)
    fifty = getWinRatio(100, 100)
    zero = getWinRatio(0, 100)
    print(hundred == 100)
    print(fifty == 50)
    print(zero == 0)

def test_getRegion():
    print("** TESTING getRegion(message) **")
    test1 = "!na pikachung"
    test2 = "!euw pikachung"
    test3 = "!lan pikachung"
    test4 = "!las pikachung"
    print(getRegion(test1) == "na1")
    print(getRegion(test2) == "euw1")
    print(getRegion(test3) == "la1")
    print(getRegion(test4) == "la2")


if __name__ == '__main__':
    print("*** TESTING ***")
    test_getRegion()
    test_getWinRatio()