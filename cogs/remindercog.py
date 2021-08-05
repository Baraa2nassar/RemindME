import discord
#import json as jason
import datetime
import asyncio
import pytz
#from bot import *
from discord.ext import tasks, commands
import re,os
import sys
import random
sys.path.append('C:\\Users\\baraa\\Documents\\GitHub\\RemindME') #goes back one direcrtory to import key
#print(sys.path)                                                                 # mainly to use f"{command_prefix}
import asyncpg
from key import *
from pytz import timezone
import textwrap
import time
import traceback
from dateparser.search import search_dates

#have a bug that I need to reaearch sometime soon, where if you put "!remind me hello" it will set hello two days from now
#which is annoying I wait it to raise an error for that

#raise toomanyarguments issue for non ignore commands

#import time
eastern = timezone('US/Eastern')

class ParsedTime:
  def __init__(self, dt, arg):
      self.dt = dt
      self.arg = arg

class TimeConverter(commands.Converter):
  async def convert(self, ctx, argument) -> ParsedTime:
      parsed = search_dates(
          argument, settings={
              'TIMEZONE': 'US/Eastern',
              'PREFER_DATES_FROM': 'future',
              'FUZZY': True
          }
      )
      if parsed is None:
          return None
      elif(parsed [0][0] == "me"):
          return None
      else:
          pass
          #return parsed 

      if not parsed:
      #if ((when is None) ) : # Make sure 2 arguments were passed - #Error handler to show the correct input
          await ctx.send(f"***Invalid Command! see following example***\n (ex: `{command_prefix}remind me in 10 minutes to 'Do HW'\n !remind me next thursday at 3pm to attend MSA event`)")
          embed = discord.Embed(color = discord.Color.red())
          #embed = discord.Embed(title = "",desctiption = "this is desctiption",color=0x461111)
          embed.set_image(url ="https://cdn.discordapp.com/attachments/841054606413791283/871492062665658398/unknown.png")
          #file = discord.File("https://cdn.discordapp.com/attachments/841054606413791283/861802458686816277/unknown.png", filename="...")
          return await ctx.send(embed=embed,delete_after=25)
          raise self.InvalidTimeProvided()
          #raise commands.BadArgument('Invalid time provided. Try again with a different time.') # Time can't be parsed from the argument

      string_date = parsed[0][0]
      date_obj = parsed[0][1]

      now=datetime.datetime.now().astimezone(eastern)
      now = now.replace(tzinfo=None)
      #print ("now: ",now)
      #print ("date_obj: ",date_obj)
      if date_obj <= now: # Check if the argument parsed time is in the past.
          await ctx.send("Time is in the past.")
          raise commands.BadArgument('Time can not be in the past.') # Raise an error.
      
      to_be_passed = f"in {argument}"
      

      if (to_be_passed == "in me"):
        raise commands.BadArgument('Provided time is invalid')

      reason = argument.replace(string_date, "")
      if reason[0:2] == 'me' and reason[0:6] in ('me to ', 'me in ', 'me at '): # Checking if reason startswith me to/in/at
          reason = reason[6:] # Strip it.

      if reason[0:2] == 'me' and reason[0:9] == 'me after ': # Checking if the reason starts with me after
          reason = reason[9:] # Strip it.

      if reason[0:3] == 'me ': # Checking if the reason starts with "me "
          reason = reason[3:] # Strip it.

      if reason[0:2] == 'me': # Checking if the reason starts with me
          reason = reason[2:] # Strip it.

      if reason[0:6] == 'after ': # Checking if the argument starts with "after "
          reason = reason[6:] # Strip it.

      if reason[0:5] == 'after': # Checking if the argument starts with after
          reason = reason[5:] # Strip it.


      return ParsedTime(date_obj.replace(tzinfo=None), reason.strip())



#----------------------------------------------

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot

        self.printer.start()
        self.yourtask.start()
        
    async def run(self, *args, **kwargs):
      numnum = os.getenv("BOT_SECRET", yaya_sql())
      self.pg_con = await asyncpg.connect(host="localhost",database="reminders",user="postgres",password=numnum)      
      self.yourtask.start()

        #self._task = bot.loop.create_task(self.dispatch_timers())


    def cog_unload(self):
        self.printer.cancel()

    print ("- remindercog is up")
    def everyFriday(self): #switches to this week's Friday
        now=datetime.datetime.now().astimezone(eastern)
        now = now.replace(tzinfo=None)
        week= datetime.timedelta(days = 7)
        thisWeeksFriday=datetime.datetime(2021,1,1,9,0)#do NOT change these numbers! this is one friday
        #thisWeeksFriday=datetime.datetime(2021,1,1,9,0)#do NOT change these numbers! this is one friday

        while (thisWeeksFriday < now):
            try:
                thisWeeksFriday += week 
                #print (thisWeeksFriday)
                #print (thisWeeksFriday, "1")
                if (thisWeeksFriday > now):
                        thisWeeksFriday = thisWeeksFriday - week
                        return thisWeeksFriday 
            except:
                print ("everyFriday broke")
                pass


    @tasks.loop()
    async def yourtask(self):
      # if you don't care about keeping records of old tasks, remove this WHERE and change the UPDATE to DELETE
      #con = connection or self.bot.pool
      next_task = await self.bot.pg_con.fetchrow('SELECT * FROM za_time WHERE NOT completed ORDER BY expired LIMIT 1')
      
      # if no remaining tasks, stop the loop
      if next_task is None:
        self.yourtask.stop()
      # sleep until the task should be done
      
      #print (next_task['row_id'])

      now=datetime.datetime.now().astimezone(eastern)
      now = now.replace(tzinfo=None)

      if next_task['expired'] is not None:
        guild_id = next_task['guild_id']
        channel_id = next_task['channel_id']
        user_id = next_task['user_id']
        content =next_task['content']
        url = next_task['url']
        created=next_task['created']
        expired=next_task ['expired']
        completed=next_task ['completed']
        
        embed = discord.Embed(  
                     color=0xFFD700 )

        CoolTitle=["Your time has come","You ready?",
        "Reminder","Remember","Remember the 5th of November","Ur timer is up", "ACT NOW", 
        "Stop procrastinating", "Get up there", "Timer","Reminding you"]

        if next_task['expired'] >= now:
          to_sleep = (next_task['expired'] - now).total_seconds()
          #print (to_sleep)
          channel = self.bot.get_channel(int(channel_id))
          await asyncio.sleep(to_sleep)
          await channel.send(f"<@{user_id}>")
          embed.add_field(name=random.choice(CoolTitle), value=f"<@{user_id}> {content}\n [Jump to message]({url})" , inline=False)
          await channel.send (embed=embed) 
          #await channel.send(msg)
          await self.bot.pg_con.execute('UPDATE za_time SET completed = true WHERE row_id = $1', next_task['row_id'])
        else:
          x=next_task['row_id']
          channel = self.bot.get_channel(int(channel_id))
          
          embed.add_field(name=random.choice(CoolTitle), value=f"<@{user_id}> {content}\n [Jump to message]({url})" , inline=False)
          channel_id = int(channel_id)
          await channel.send(f"<@{user_id}>")
          await channel.send (embed=embed) 
          #channel = self.bot.get_channel(841054606413791283)
          #await channel.send("your task have expired some time ago:")
          await self.bot.pg_con.execute('UPDATE za_time SET completed = true WHERE row_id = $1', next_task['row_id'])
          
      #await discord.utils.sleep_until(next_task['expired']) #will change this to seconds cacluation 
      #do your task stuff here with `next_task`
      

    # add a `before_loop` and `wait_until_ready` if you need the bot to be logged in
    
#--------------------------------------------------------------------------    
    #@commands.command(pass_context=True) 
    @commands.group(name='reminder', aliases=['remindme', 'remind', "timer"], usage='<when>', invoke_without_command=True)
    async def reminder(self,ctx, *, when: TimeConverter):

      if ((when is None or when.dt is None ) ) : # Make sure 2 arguments were passed - #Error handler to show the correct input
          await ctx.send(f"***Invalid Command! see following example***\n (ex: `{command_prefix}remind me in 10 minutes to 'Do HW'\n !remind me next thursday at 3pm to attend MSA event`)")
          embed = discord.Embed(color = discord.Color.red())
          #embed = discord.Embed(title = "",desctiption = "this is desctiption",color=0x461111)
          embed.set_image(url ="https://cdn.discordapp.com/attachments/841054606413791283/871492062665658398/unknown.png")
          #file = discord.File("https://cdn.discordapp.com/attachments/841054606413791283/861802458686816277/unknown.png", filename="...")
          return await ctx.send(embed=embed,delete_after=25)
          raise self.InvalidTimeProvided()

      #print(f"when is {when.dt}") 
      #print(f"TimeConverter is {TimeConverter.arg}") 
      #print ("here is the time: ")
      now=datetime.datetime.now().astimezone(eastern)

      #sentence = ''
      sentence = ("`"+ '"' +when.arg+'"'+"`")

      await ctx.send(f"**I will remind you  **" + f'<t:{int(when.dt.timestamp())}:R>' +sentence )
      #e.add_field(name= f'<t:{int(expired.timestamp())}:R>', value=f" [{_id}]({url}) {shorten} ...", inline=False)

      user_ID=str(ctx.message.author.id)
      guild_id=str(ctx.message.guild.id)
      channel_id=str(ctx.message.channel.id)
      URL = ctx.message.jump_url

      ClockIn = await self.bot.pg_con.fetch("SELECT * FROM za_time WHERE url = $1 "
        ,URL)
      
      if not ClockIn:
        now=datetime.datetime.now().astimezone(eastern)
        now = now.replace(tzinfo=None)
        #when.dt = when.dt.replace(tzinfo=None)
        #print(when.dt)
        await self.bot.pg_con.execute('''
            INSERT INTO za_time(user_id,guild_id, created, expired,content,url,channel_id) VALUES($1, $2,$3,$4,$5,$6,$7)
        ''', user_ID,guild_id,now,when.dt,sentence,URL,channel_id)

      #it sleeps
      if self.yourtask.is_running():
        self.yourtask.restart()
      else:
        self.yourtask.start()
          
          #await asyncio.sleep(eta)
          #reminder message after it slept
          #deleting this previous reminder
    @reminder.error
    async def remind_error(self,ctx, error): # Add self as the first param if this is in a cog/class.
        #if isinstance(error, TimeInPast):
        #    await ctx.send("Time is in the past.")
        if isinstance(error, commands.BadArgument):
            await ctx.send("Invalid time. Try `!remind me to say salam to my friend in 5 min`")
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'when':
                await ctx.send("You forgot to give me input! Try `!remind me tomorrow at 2:59pm to send email to prof. Baraa`")
        if isinstance(error, commands.TooManyArguments):
                await ctx.send(f'Too many arguments.')
              
    @reminder.command(name='list', ignore_extra=False)
    async def reminder_list(self, ctx):
        """Shows the 10 latest currently running reminders."""
        #if not self.ignore_extra:
            #if not view.eof:
                 #raise TooManyArguments('Too many arguments passed to ' + self.qualified_name)
        
        query = """SELECT row_id, expired, content, url 
                   FROM za_time
                   WHERE completed = false
                   AND user_id = $1
                   ORDER BY expired
                   LIMIT 10;
                """

        records = await self.bot.pg_con.fetch(query, str(ctx.author.id))

       # ClockIn = await self.bot.pg_con.fetch("SELECT * FROM za_time WHERE url = $1 ",URL)
        if len(records) == 0:
            return await ctx.send('No currently running reminders.')

        e = discord.Embed(color=0xFFD700, title='Reminders')

        if len(records) == 10:
            e.set_footer(text='Only showing up to 10 reminders.')
        else:
            e.set_footer(text=f'{len(records)} reminder{"s" if len(records) > 1 else ""}')

        for _id, expired, message,url in records:
            shorten = textwrap.shorten(message, width=512)
            #print(records['expired'])
            #deadLine=records['expired']
            #expired = expired.strftime("%A at %I:%M%p -- %h/%d/%Y")

            e.add_field(name= f'<t:{int(expired.timestamp())}:R>', value=f" [{_id}]({url}) {shorten} ...", inline=False)


        await ctx.send(embed=e) 

    @reminder.command(name='delete', aliases=['remove', 'cancel'], ignore_extra=False)
    async def reminder_delete(self, ctx, *, id: int):
        """Deletes a reminder by its ID.
        To get a reminder ID, use the reminder list command.
        You must own the reminder to delete it, obviously.
        """

        query = '''DELETE FROM za_time WHERE row_id =$1 AND user_id =$2 '''

        status = await self.bot.pg_con.execute(query, id,str(ctx.author.id))

        #status = await ctx.db.execute(query, id, str(ctx.author.id))

        if status == 'DELETE 0':
            return await ctx.send('Could not delete any reminders with that ID.')
        else:
          if self.yourtask.is_running():
            self.yourtask.restart()
          else:
            self.yourtask.start()

        await ctx.send('Successfully deleted reminder.')

 


    @tasks.loop(seconds=60.0) #this will be merged with the other function soon when I apply#reocuring command           
    async def printer(self):

        now=datetime.datetime.now().astimezone(eastern)#has to be in the loop to renew the time
        now = now.replace(tzinfo=None)
        remindMeAT =datetime.datetime(2021,7,5,17,16)  #year,month,day,hour,min,sec

        channel = self.bot.get_channel(772590741124808714)

        if (remindMeAT.day==now.day and remindMeAT.hour==now.hour and remindMeAT.minute==now.minute):#same day and?
                print(f"I sent a message on {channel}")
                #remindMeAT = (remindMeAT+tdelta) # it should send a message every two minutes
                #response = ("it is", now)
                await channel.send(now)
                #print ("time is", now)
                await asyncio.sleep (31)
        if (self.everyFriday().day==now.day and self.everyFriday().hour==now.hour):
                await channel.send("*Salam! \n")
                await channel.send("```cs\n jumaa mubarakah :) \n Do not forget to:\n 1:read #surat alkahf\n 2:make #dua```")
                print("jumaa mubarakah :) \ndon't foget to:\n 1:read surat alkahf\n 2:make dua")
                await asyncio.sleep (3600) #sleeps for one hour once it is executed

    @printer.before_loop
    async def before_printer(self):
        print('waiting...')
        await self.bot.wait_until_ready()

    @yourtask.before_loop
    async def before_yourtask(self):
      print ('loading tasks...')
      await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(MyCog(bot))