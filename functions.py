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
        return False;
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