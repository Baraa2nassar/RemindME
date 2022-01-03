#import discord
from key import *
#import json as jason
import datetime
import asyncio
import logging
import re,os
#from discord.ext import commands
from pytz import timezone
import asyncpg

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

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.TooManyArguments):
    await ctx.send('too many arguments')
  if isinstance(error, commands.MissingRequiredArgument):
      #if error.param.name == 'when':
      await ctx.send("You forgot to give me input! Try `!remind me tomorrow at 2:59pm to send email to prof. Baraa`")

@bot.command()
@commands.has_permissions(manage_channels=True, manage_messages=True)
async def poll(ctx: commands.Context, channel: discord.TextChannel, *, message=""):
    """Send message to a specific channel. then adds emojis underneath it"""       
    print("hey")
    print ("msg is: ",message)
    custom_emojis = re.findall(r'[^\w\s()\"#/[@;:<>{}`+=~|.!?,-]', message)      
    print (custom_emojis)
    x = await ctx.guild.get_channel(channel.id).send(message)
    for index, mystr in enumerate(custom_emojis):
       # x = await message.channel.send(mystr)
       try:
        await x.add_reaction(str(mystr))
       except:
        pass
        
    await ctx.message.add_reaction ("✅")
    # return await ctx.tick()

    # if message.content.startswith("/poll"):
      # print (message.content)
      # messageContent=message.content.replace ("/poll","")

      # custom_emojis = re.findall(r'[^\w\s()\"#/[@;:<>{}`+=~|.!?,-]', message.content)
      # print (custom_emojis)
      

bot.load_extension("cogs.remindercog")
bot.load_extension("cogs.helpCog")
bot.load_extension("cogs.funCommandsCogs")

numnum = os.getenv("BOT_SECRET", yaya_sql())

async def create_db_pool():
    bot.pg_con = await asyncpg.create_pool(
      host="localhost",
      database="reminders",
      user="postgres",
      password=numnum)
      #,max_inactive_connection_lifetime=3)

bot.loop.run_until_complete(create_db_pool())

BOT = os.getenv("BOT_SECRET", bot_pass())
token = BOT
bot.run(token)

