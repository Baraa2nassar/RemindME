import discord
from key import *

import json as jason
import datetime
import asyncio
import logging
import re,os

from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game(name = "(HAHA I am Alive, JUST WAIT UNTIL BARAA SETS ME FREE)"))
    print("We have logged in as {0.user}".format(bot))

bot.load_extension("cogs.remindercog")

BOT = os.getenv("BOT_SECRET", bot_pass())
token = BOT
bot.run(token)


