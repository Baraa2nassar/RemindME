import discord
#from bot import *
from discord.ext import tasks, commands
import re,os
import sys
import random

intents = discord.Intents.all()
intents.members = True

#class helpingCog(commands.Cog):
class FunCommandsCog(commands.Cog):
	"""some fun commands that available for users"""
	def __init__(self, bot):
		#self.arg = arg
		self.bot=bot
	print ("- Fun commands cog is up")

	@commands.Cog.listener()
	async def on_message(self,message):
		#if message.author == self.user:
	    if message.author == self.bot.user:
	        return -1;

	    userMessage = message.content.lower() 
	    #if message.content.startswith("heyo"):
	    #	await message.channel.send("heyo")

	    #if str("flip a coin") in userMessage: #might want to customize it more
	    if (userMessage.startswith("flip a coin")) or (userMessage.startswith("flip coin")):
	    	faceCoin = ["heads","tails"]
	    	await message.reply(random.choice(faceCoin))

	    dice=["dice",'die','di','dic']
	    if userMessage.startswith(f"role a di"):
	    	await message.reply("🎲"+str(random.randint(1,6)))

def setup(bot):
	bot.add_cog(FunCommandsCog(bot))

