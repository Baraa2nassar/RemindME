import discord
import json as jason
import datetime
import asyncio
import pytz
#from bot import *
from discord.ext import tasks, commands
import re,os
import sys
import random
sys.path.append('C:\\Users\\baraa\\Documents\\GitHub\\RemindME') #goes back one direcrtory to import key
                                                                 # mainly to use f"{command_prefix}
from key import *
from pytz import timezone

eastern = timezone('US/Eastern')
class MyCog(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
        self.printer.start()

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

    @commands.command(pass_context=True) 

    async def reminders_list(self,ctx):
          with open(f"{ctx.message.guild.name}_reminders_list") as f: 
            cmds = f.read()
          #embed = discord.Embed(color = discord.Color.red())
          #await ctx.send(embed=embed)
          await ctx.send("```CS\n #These are the current runnning reminders#\n" + cmds + "```")

    @commands.command(pass_context=True) 
    async def timer(self,ctx, *args):# a timer/countdown command that works as long as the bot is alive
       is_a_num = re.search(r"^(\d{2,4})$", ''.join(args)) #the r"string" treats things literly + re is a regular expression + 
       #the \d is just for it to work in its equivilant charachters like the arabic numerals ٠١٢٣٤٥٦٧٨٩
       #print (f"is_a_num is {is_a_num}")
       #print (f"args[0] is: "  +args[0] + "\n" + "args[1]:" + args[1] )

    # or ()
    #solve to check that the input is int 
    #solve to accept it whether the user puts a promt or not
# or
       #is_a_num = (isinstance(args[0],int))
       #print (is_a_num)

       try:
           if ((len(args) >= 2)):
                val = int(args[0])
                bal = int (args [1])
           else:
                pass

       except ValueError:
           print("That's not an int!")
           await ctx.send(f"***Invalid Command! Must include hours followed by minutes!***\n (ex: `{command_prefix}timer 0 30 'Do HW'`)")
           #embed = discord.Embed(color = discord.Color.red())

           #await ctx.send(embed=embed)
           embed = discord.Embed(color=0xFFD700 )
           embed.set_image(url ="https://cdn.discordapp.com/attachments/841054606413791283/861802458686816277/unknown.png")
           #file = discord.File("https://cdn.discordapp.com/attachments/841054606413791283/861802458686816277/unknown.png", filename="...")
           await ctx.send(embed=embed)
           return

       if ((len(args) < 2)) : # Make sure 2 arguments were passed
          await ctx.send(f"***Invalid Command! Must include hours followed by minutes!***\n (ex: `{command_prefix}timer 0 30 'Do HW'`)")
          embed = discord.Embed(color = discord.Color.red())
          #embed = discord.Embed(title = "",desctiption = "this is desctiption",color=0x461111)
          embed.set_image(url ="https://cdn.discordapp.com/attachments/841054606413791283/861802458686816277/unknown.png")
          #file = discord.File("https://cdn.discordapp.com/attachments/841054606413791283/861802458686816277/unknown.png", filename="...")
          await ctx.send(embed=embed)

          #await ctx.send(file=discord.File(''))
       else:
          eta = ((int(args[0]) * 60) * 60) + (int(args[1]) * 60) #coverts the hours to seconds (args[0]*3600) and minutes to seconds args[1]*60
          sentence = ''
          if (len(args)==3):
            sentence = ("`"+ '"' +args[2]+'"'+"`")

          now=datetime.datetime.now().astimezone(eastern)
          secondsAdd= datetime.timedelta(seconds = eta) #how long is the timer is for
          NewREminder = now + secondsAdd
          #await ctx.send(f"**I will remind you in **" + args[0] + f"** hour(s) & {args[1]} minute(s) **" + sentence )
          await ctx.send(f"**I will remind you on **" + 
            str(NewREminder.strftime("%h/%d/%Y")) + 
            " at " +str(NewREminder.strftime("%I:%M%p"))+sentence )

          #whatYouSay = (input("enter a text to be saved in the file \n"))
          #filename = ctx.message.guild.name

          with open(f"{ctx.message.guild.name}_reminders_list", "a+") as f: #the a+ will append the data and it will create a file if there is no existing file already
            #each server have their own guild docs with their own reminders
            my_timer = re.sub(r"!timer", '', str(NewREminder.strftime("%h/%d/%Y")) +
             " at " +str(NewREminder.strftime("%I:%M%p"))+sentence)

            des = (str(my_timer) +" by: "+ (ctx.author.name) +'\n')

            f.write(des)
            #print (f"des is: {des}")
          await asyncio.sleep(eta)

          with open(f"{ctx.message.guild.name}_reminders_list", "r+") as f:
              
              lines = f.readlines()
              f.seek(0)
              for i in lines:
                if i!=des:
                    f.write(i)
              f.truncate()
          pending = asyncio.all_tasks()
          print (pending)

          #await ctx.send("**REMINDER** " + ctx.author.mention +  f" {sentence} \n{ctx.message.jump_url} ")
          embed = discord.Embed(  
                       color=0xFFD700 )
          CoolTitle=["Your time has come","You ready?",
          "Reminder","Remember","Remember the 5th of November","Ur timer is up", "ACT NOW", 
          "Stop procrastinating", "Get up there", "Timer","Reminding you"]
          embed.add_field(name=random.choice(CoolTitle), value=f"{ctx.author.mention} {sentence}\n [Jump to message]({ctx.message.jump_url})" , inline=False)
          await ctx.send(ctx.author.mention)
          await ctx.send (embed=embed) 
          #await ctx.send()
          #here mebed

          #deleting this previous reminder
    #https://i.ytimg.com/vi/C49pbTDHgog/hqdefault.jpg
    @tasks.loop(seconds=60.0)
    async def printer(self):

        now=datetime.datetime.now().astimezone(eastern)#has to be in the loop to renew the time
        now = now.replace(tzinfo=None)
        remindMeAT =datetime.datetime(2021,7,5,17,16)  #year,month,day,hour,min,sec

        channel = self.bot.get_channel(841054606413791283)

        if (remindMeAT.day==now.day and remindMeAT.hour==now.hour and remindMeAT.minute==now.minute):#same day and?
                print(f"I sent a message on {channel}")
                #remindMeAT = (remindMeAT+tdelta) # it should send a message every two minutes
                #response = ("it is", now)
                await channel.send(now)
                #print ("time is", now)
                await asyncio.sleep (31)
        print(self.everyFriday())
        print(now)
        if (self.everyFriday().day==now.day and self.everyFriday().hour==now.hour):
                await channel.send("*Salam! \n")
                await channel.send("```cs\n jumaa mubarakah :) \n Do not forget to:\n 1:read #surat alkahf\n 2:make #dua```")
                print("jumaa mubarakah :) \ndon't foget to:\n 1:read surat alkahf\n 2:make dua")
                await asyncio.sleep (3600) #sleeps for one hour once it is executed

    @printer.before_loop
    async def before_printer(self):
        print('waiting...')
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(MyCog(bot))