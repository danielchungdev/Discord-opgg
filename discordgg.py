import discord
import requests

client = discord.Client()
discordToken = "NjE4ODM2MDE0OTQ5MjAzOTg3.Xaqzyw.osNryIZLPM6PSxp96yYu_fpa_4w"
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
        print(getSummonerID(summonerName))


def getSummonerName(commandMessage):
    return commandMessage[1:]


def getSummonerID(summonerName):
    URL = "https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + riotApiKey
    response = requests.get(url=URL)
    data = response.json()
    summonerID = data['id']
    return summonerID


client.run(discordToken)
