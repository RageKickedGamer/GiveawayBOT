import discord
import random
import time
import datetime
import asyncio

from discord.ext import commands
from discord.ext.commands import Bot
from random import randint

bot = commands.Bot(command_prefix = commands.when_mentioned_or("g+"))
'''bot.remove_command("help")'''
startup_extensions = ["cogs.create", "cogs.start"]
logs = discord.Object("403024766056792074")

for extension in startup_extensions:
    try:
        bot.load_extension(extension)
        print(f'{extension} Loaded')
    except Exception as e:
        print(f"Failed to load extention {extension}\n{type(e).__name__}: {e}")

@bot.event
async def on_ready():
    print("===================================")
    print("Logged in as: %s"%bot.user.name)
    print("ID: %s"%bot.user.id)
    print("Py Lib Version: %s"%discord.__version__)
    print("===================================")

@bot.command()
async def support():
    """Come Support Development!"""
    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    color = int(color, 16)
    embed=discord.Embed(title=":tada: Come Support Development! :tada:", colour = discord.Colour(value=color))
    embed.add_field(name = "Dev Server: ", value = 'https://discord.gg/X4CJdEM')
    embed.add_field(name = "Why Help?", value = "So you can help us suggest improvements, and give us some advise!")
    embed.set_footer(text = "Don't Forget to Upvote Us!")
    await bot.say(embed = embed)
    
@bot.command()
async def updates():
    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    color = int(color, 16)
    embed=discord.Embed(title=":tada: Updates :tada:", colour = discord.Colour(value=color))
    embed.add_field(name = "v0.1", value = "Multiple Winners are now added! Also if a giveaway stop and never finishes its because the bot auto turns off to refresh!\n"
                   "Also, we have added a new command named 'start'. type `+ghelp start` to see how it works!")
    embed.add_field(name = "Updates!: ", value = "Added a command +gstart to make giveaways faster!/n"
                   "Usage: +gstart <Time> <Winners> <Prize>), Ex. +gstart 1m 1 Nothing")
    await bot.say(embed = embed)
    
@bot.event
async def on_server_join(server):
    embed = discord.Embed(title="__Joined: {}__".format(server.name), color=0x00ff00, timestamp = datetime.datetime.utcnow())
    embed.add_field(name="Owned By", value=server.owner, inline=True)
    embed.add_field(name="Total Members", value="{0} members".format(server.member_count), inline=True)
    embed.add_field(name="Server Region", value=server.region, inline=True)
    await bot.send_message(logs, embed=embed)

@bot.event
async def on_server_remove(server):
    embed = discord.Embed(title="__Removed From: {}__".format(server.name), color=0xff0000, timestamp = datetime.datetime.utcnow())
    embed.add_field(name="Owned By", value=server.owner, inline=True)
    embed.add_field(name="Total Members", value="{0} members".format(server.member_count), inline=True)
    embed.add_field(name="Server Region", value=server.region, inline=True)
    await bot.send_message(logs, embed=embed)

if not os.environ.get('TOKEN'):
        print("No Token Found")
bot.run(os.environ.get('TOKEN').strip('\"'))
