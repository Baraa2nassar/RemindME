import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
command_prefix='!'
bot = commands.Bot(command_prefix , intents=intents)  # add the intents= part to your existing constructor call
#bot = commands.Bot(command_prefix , intents=intents,help_command=None)  # add the intents= part to your existing constructor call


#filename = "reminders_list.txt"
#filename = ctx.message.guild.name
def yaya_sql():
	with open("timertable.txt")as f:
		return f.read()

def bot_pass():
    with open("SeTe.txt") as f:
        return f.read()