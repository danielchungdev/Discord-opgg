import discord
import requests
#CHANGE DISCORD TOKEN EVERYTIME
client = discord.Client()
discordToken = "NjE4ODM2MDE0OTQ5MjAzOTg3.Xatd4Q.YlQgLlulO6zRgi7ehFFEA6wrxCU"
riotApiKey = "RGAPI-7c02fddb-2cf7-45d2-9e5c-58dd7cfd5704"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


"""
Main method checks if the user's message has the keyletter "!"
if it has then it proceeds to check for the summonername and 
retrieve information.
"""

@client.event
async def on_message(message):
    if message.content[0] == "!":
        summonerName = getSummonerName(message.content)
        summonerID = getSummonerID(summonerName)
        if summonerID == False:
            await message.channel.send("Summoner name: " + summonerName + " was not found")
        else:
            print(getSummonerRank(summonerID, summonerName))
            await message.channel.send(getSummonerRank(summonerID, summonerName))

"""
Param: userInput. 
This functions gets the summonerName from
the message input. 
Return: (str) summonerName. (Basically a strip.)
"""
def getSummonerName(commandMessage):
    return commandMessage[1:]

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

client.run(discordToken)
