import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
from random import randint
import os

bot=commands.Bot(command_prefix = '+g')

@bot.event
async def on_ready():
    print("===================================")
    print("Logged in as")
    print("Username: %s"%bot.user.name)
    print("ID: %s"%bot.user.id)
    print('Server count:', str(len(bot.servers)))
    print('User Count:',len(set(bot.get_all_members())))
    print("Py Lib Version: %s"%discord.__version__)
    print("===================================")
    await bot.change_presence(game = discord.Game(name='Giveaways'))

@bot.command(pass_context = True)
async def create(ctx):
    """Create a Giveaway!"""
    await bot.say(" :tada: Lets create your Giveaway")
    await asyncio.sleep(1)
    await bot.say("What channel will the :tada: Giveaway :tada: be held in?\n"
                  "\n"
                  "`Ex. Channel Named #giveaways, Just Say giveaways`")
    channel_name = await bot.wait_for_message(author = ctx.message.author)
    g_channel = discord.utils.get(ctx.message.server.channels, name = channel_name.content)

    #check if the channel exists
    if not g_channel:
        await bot.say(":x: | Channel Not Found | Start Over")
    if g_channel:
        await bot.say(":white_check_mark: | Channel Selected!")
        await asyncio.sleep(1)
        await bot.say("How long will the Giveaway Be?\n"
                      "\n"
                      "`Ex. 5 Minutes, You Say 5`")
        g_end = await bot.wait_for_message(author = ctx.message.author)
        await asyncio.sleep(1)
        await bot.say(":tada: Giveaway set to end {} Minutes after the start".format(g_end.content))
        await asyncio.sleep(1)
        await bot.say("How many winner will be selected?\n"
                      "\n"
                      "`Pick a Number 1 (More Winners Coming Soon!)`")
        g_winners = await bot.wait_for_message(author = ctx.message.author)
        await asyncio.sleep(1)
        await bot.say(":tada: {} Winner(s) will be Chosen".format(g_winners.content))
        await asyncio.sleep(1)
        await bot.say("What are you giving away?\n"
                      "\n"
                      "`This Will Become The Title Of The Giveaway`\n"
                      "`Ex. If I'm Giving away Free Steam Keys I Would say Free Steam Keys`")
        g_prize = await bot.wait_for_message(author = ctx.message.author)
        await asyncio.sleep(1)
        await bot.say("Giving away  {}".format(g_prize.content))
        await asyncio.sleep(1)
        await bot.say(":tada: Almost Done Please Confirm Below")
        await asyncio.sleep(1)
        await bot.say("You are Giving away `{}` with `{}` Winners, that will Last `{}` Minutes?\n"
                      "\n"
                      "`If This Is Correct Say Yes. If Not Say No (You Will Have To Start Over)`".format(g_prize.content, g_winners.content, g_end.content))
        response = await bot.wait_for_message(author = ctx.message.author, channel = ctx.message.channel)
        response = response.content.lower()

        yesres = 'yes'
        nores = 'no'
        if response.lower() == nores.lower():
            await asyncio.sleep(1)
            await bot.say(":x: | Giveaway Canceled, Please Restart The Setup")
        if response.lower() == yesres.lower():
            await bot.say(":tada: Giveaway Started! :tada:")
            #For The Countdown
            g_end.content = int(g_end.content)
            c_time = g_end.content * 60
            mue = c_time            
            color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
            color = int(color, 16)
            embed=discord.Embed(title=":tada: __**{} Giveaway!**__ :tada:".format(g_prize.content), colour = discord.Colour(value=color))
            embed.add_field(name = "How long is it?", value = "{} Minutes".format(g_end.content))
            embed.add_field(name = "Winners: ", value = "{} Winner(s)".format(g_winners.content))
            embed.add_field(name = "Time Left: ", value = "{} Seconds".format(mue), inline = True)
            embed.set_footer(text = "Add The Reaction to join!")
            give_away = await bot.send_message(g_channel, embed = embed)
            ga_message = await bot.add_reaction(give_away, "\U0001f389")
            for loop in range (c_time):
                await asyncio.sleep(1)
                c_time -= 1

                mue = c_time
            

                embed=discord.Embed(title=":tada: __**{} Giveaway!**__ :tada:".format(g_prize.content), colour = discord.Colour(value=color))
                embed.add_field(name = "How long is it?", value = "{} Minutes".format(g_end.content))
                embed.add_field(name = "Winners: ", value = "{} Winner(s)".format(g_winners.content))
                embed.add_field(name = "Time Left: ", value = "{} Seconds".format(mue), inline = True)
                embed.set_footer(text = "Add The Reaction to join!")

                await bot.edit_message(give_away, embed = embed)
            ga_message = await bot.get_message(give_away.channel, give_away.id)
            ga_users=[]
            for user in await bot.get_reaction_users(ga_message.reactions[0]):
                ga_users.append(user.mention)
            ga_bot = ctx.message.server.get_member('396464677032427530')
            ga_users.remove(ga_bot.mention)
            winner = random.choice(ga_users)
        #Winning Embed
        color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        embed=discord.Embed(title=":tada: __**Giveaway Ended!**__ :tada:", colour = discord.Colour(value=color))
        embed.add_field(name = "Winners: ", value = "{} Winner(s)".format(g_winners.content))
        embed.add_field(name = "Winner: ", value = "{}".format(winner))
        embed.add_field(name = "Prize: ", value = "{}".format(g_prize.content))
        embed.set_footer(text = "Better Luck Next Time!")
        await bot.edit_message(give_away, embed = embed)
        await bot.send_message(g_channel, ":tada: {} Has Won {}! Come Claim Your Prize! :tada:".format(winner, g_prize.content))

@bot.command()
async def support():
    """Come Support Development!"""
    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    color = int(color, 16)
    embed=discord.Embed(title=":tada: Come Support Development! :tada:", colour = discord.Colour(value=color))
    embed.add_field(name = "Dev Server: ", value = 'https://discord.gg/aXZMuCN')
    embed.add_field(name = "Why Help?", value = "So you can help us suggest improvements, and give us some advise!")
    embed.set_footer(text = "Don't Forget to Upvote Us!")
    await bot.say(embed = embed)
    
@bot.command()
async def updates():
    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    color = int(color, 16)
    embed=discord.Embed(title=":tada: Updates :tada:", colour = discord.Colour(value=color))
    embed.add_field(name = "v0.1", value = "We are now VERY close to let the bot select Multiple winners. Stay Tuned!!")
    await bot.say(embed = embed)
    
@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandNotFound):
        await bot.send_message(ctx.message.channel, ":x: | Command Not Found!")

if not os.environ.get('TOKEN'):
        print("No Token Found")
bot.run(os.environ.get('TOKEN').strip('\"'))
