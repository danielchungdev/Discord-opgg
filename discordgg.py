import discord
from riotGamesAPI import *

#CHANGE DISCORD TOKEN EVERYTIME
client = discord.Client()


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

client.run(discordToken)
