import aiohttp
import os
import requests
import discord

from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = commands.when_mentioned_or("+g"))

class api():
    
    dbltoken = os.environ.get('DBLT')
    url = "https://discordbots.org/api/bots/" + bot.user.id + "/stats"
    headers = {"Authorization" : dbltoken}

    async def on_ready():
        payload = {"server_count"  : len(bot.servers)}
        requests.post(url, data=payload, headers=headers)

    async def on_server_join(server):
        payload = {"server_count"  : len(bot.servers)}
        requests.post(url, data=payload, headers=headers)

    async def on_server_remove(server):
        payload = {"server_count"  : len(bot.servers)}
        requests.post(url, data=payload, headers=headers)
      
def setup(bot):
    bot.add_cog(api)
