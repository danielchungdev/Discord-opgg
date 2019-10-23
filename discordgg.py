"""
Project: Discordgg.py
File: discordgg.py
Author: Daniel Chung
Date: 9/02/19
Description: This file contains the main functions that are based
on the bot. This file is basically the MAIN. Run this file for bot
to work on the servers.
Installs: discord.py
"""

import discord
from riotGamesAPI import *
from functions import *

#CHANGE DISCORD TOKEN EVERYTIME
client = discord.Client()
discordToken = "NjE4ODM2MDE0OTQ5MjAzOTg3.Xa6qKg.F8wzyGOIrnAWvw2yCYDBDS2WY38"

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
        region = getRegion(message.content)
        summonerName = getSummonerName(message.content)
        summonerID = getSummonerID(summonerName, region)
        if summonerID == False:
            await message.channel.send("```diff\n - Summoner name: " + summonerName + " was not found\n```")
        else:
            #print(getSummonerRank(summonerID, summonerName, region))
            await message.channel.send(getSummonerRank(summonerID, summonerName, region))

client.run(discordToken)