import discord
import json as jason
import datetime
import asyncio
import pytz
#from bot import *
from discord.ext import tasks, commands
import re,os
import sys

#from funCommandsCogs import *

sys.path.append('C:\\Users\\baraa\\Documents\\GitHub\\RemindME') #goes back one direcrtory to import key
                                                                 # mainly to use f"{command_prefix}
from key import *
import random

quotes = ["Time waits for no one","Time is like a sword if you don't cut it it will cut you",
"the prophet PBUH said: Take advantage of five before five, 1) your youth before your old age ...  ", 
"“There are two blessings which many people lose: (They are) health and free time for doing good.” (Bukhari 8/421)", 
"“Yesterday is history, tomorrow is a mystery, but today is a gift. That is why it is called the present.”",
 "The key is in not spending time, but in investing it","plan for the worst hope for the best"
 ,"https://youtu.be/JObb2BYmp2w?t=45","https://www.youtube.com/watch?v=0xe5twFK1SI","oh Allah we ask you for good endings"]

class helpingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    print ("- helpCog is up")
    @commands.command(pass_context=True)
    async def quote(self,ctx):
      embed = discord.Embed(  
                    color=0xFFD700 )
      embed.add_field(name="**Quote**", value=random.choice(quotes) , inline=False)
        #await ctx.send(random.choice(quotes))
      await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def cmds(self,ctx):

        with open("cmds.md") as f: 
              cmds = f.read()

              embed = discord.Embed(  
                    color=0xFFD700 ) #changes the color to golden 
              quote=random.choice(quotes)
              embed.add_field(name="**Quote**", value=quote , inline=False)
              #embed.add_field(name="**Commands**", value="```fix\n"+cmds+"\n```", inline=False) 
              embed.add_field(name="**Commands**", value=cmds, inline=False) 
              embed.set_author(name = "RemindME Bot Commands:",icon_url="https://image.flaticon.com/icons/png/512/1792/1792929.png")

              embed.set_thumbnail(
                url=
                "https://cdn.discordapp.com/attachments/841054606413791283/862398120880242718/d9nds2y-e961d4ec-b733-4163-a3a6-68c08d9dde4e.png")
              await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(helpingCog(bot))
