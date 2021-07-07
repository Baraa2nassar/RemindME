import discord
from key import *

import json as jason
import datetime
import asyncio
import logging
import re,os
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix , intents=intents)  # add the intents= part to your existing constructor call
#bot = commands.Bot(command_prefix , intents=intents,help_command=None)  # add the intents= part to your existing constructor call

''' #a testing command for debuging
@bot.command()
async def ping(ctx):
	await ctx.send("pong")
'''

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game(name = "!cmds for commands"))
    #guild = bot.get_guild(756582312208236695)
    #print (guild.members[1])
    print("We have logged in as {0.user}".format(bot))


bot.load_extension("cogs.remindercog")
bot.load_extension("cogs.helpCog")
bot.load_extension("cogs.funCommandsCogs")


BOT = os.getenv("BOT_SECRET", bot_pass())
token = BOT
bot.run(token)
