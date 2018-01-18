import discord
import aiohttp
import asyncio
import os
import requests

from discord.ext import commands

bot = commands.Bot(command_prefix = commands.when_mentioned_or ("+g"))
BOT_ID = "396464677032427530"
AUTH = os.environ.get('DBLT')
token = DBLT
url = "https://discordbots.org/api/bots/{}/stats".format(BOT_ID)
headers = {"Authorization" : AUTH}

class api():
    
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
