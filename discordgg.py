import discord
import requests

client = discord.Client()
discordToken = "NjE4ODM2MDE0OTQ5MjAzOTg3.Xatd4Q.YlQgLlulO6zRgi7ehFFEA6wrxCU"
riotApiKey = "RGAPI-7c02fddb-2cf7-45d2-9e5c-58dd7cfd5704"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    """
    Checks to see if the bot is activated ! is going to be our key
    character. When the bot recognizes this it will execute code.
    """
    if message.content[0] == "!":
        summonerName = getSummonerName(message.content)
        summonerID = getSummonerID(summonerName)
        if summonerID == False:
            await message.channel.send("Summoner name: " + summonerName + " was not found")
        else:
            print(getSummonerRank(summonerID, summonerName))
            await message.channel.send(getSummonerRank(summonerID, summonerName))

def getSummonerName(commandMessage):
    return commandMessage[1:]


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

def getQueueType(data):
    if len(data) == 0:
        return False;
    if data[0]["queueType"] == "RANKED_SOLO_5x5":
        return 0
    elif data[1]["queueType"] == "RANKED_SOLO_5x5":
        return 1
    elif data[2]["queueType"] == "RANKED_SOLO_5x5":
        return 2

def getWinRatio(wins, losses):
    x = wins + losses
    y = wins * 100
    return round(y / x)

client.run(discordToken)
