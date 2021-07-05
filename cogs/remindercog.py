import discord
import json as jason
import datetime
import asyncio
import pytz
from discord.ext import tasks, commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()


    def everyFriday(self): #switches to this week's Friday
        now=datetime.datetime.now()
        week= datetime.timedelta(days = 7)
        thisWeeksFriday=datetime.datetime(2021,1,1,9,0)#do NOT change these numbers! this is one friday

        while (thisWeeksFriday < now):
            try:
                thisWeeksFriday += week 
                #print (thisWeeksFriday, "1")
                if (thisWeeksFriday >= now):
                        return thisWeeksFriday
            except:
                print ("everyFriday broke")
                pass

    print ("remindercog is up")
    @tasks.loop(seconds=60.0)
    async def printer(self):
        now=datetime.datetime.now()#has to be in the loop to renew the time
        remindMeAT =datetime.datetime(2021,7,5,17,16)  #year,month,day,hour,min,sec

        channel = self.bot.get_channel(841054606413791283)
        #await channel.send(now)

        #print ("Now is: " , now)
        #print ("My reminder is set to: ",remindMeAT, "\n")
        
        #try:
            #(1) going to take the server's ID'
            #(2) look it up in the docs 
            #(3) if available see the selected channel and use it
            #(4) if not make a new document and store in it the guild ID for the server

         # channel ID goes here dev MSU id - I need to make it a variable

        if (remindMeAT.day==now.day and remindMeAT.hour==now.hour and remindMeAT.minute==now.minute):#same day and?
                print(f"I sent a message on {channel}")
                #remindMeAT = (remindMeAT+tdelta) # it should send a message every two minutes
                #response = ("it is", now)
                await channel.send(now)
                #print ("time is", now)
                await asyncio.sleep (31)
        
        if (self.everyFriday().day==now.day and self.everyFriday().hour==now.hour):
                await channel.send("*this is just a test for future juma'a* \n")
                await channel.send("```cs\n jumaa mubarakah :) \n Do not forget to:\n 1:read #surat alkahf\n 2:make #dua```")
                print("jumaa mubarakah :) \ndon't foget to:\n 1:read surat alkahf\n 2:make dua")
                await asyncio.sleep (3600) #sleeps for one hour once it is executed


    @printer.before_loop
    async def before_printer(self):
        print('waiting...')
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(MyCog(bot))


#@bot.event

#---------------------------------------------------

#bot = commands.Bot(command_prefix='!',self_bot = True)
#bot = commands.Bot(command_prefix='>')

#client = MyClient()

#client.run('ODM4MjQ2MDgxNTA5NzIwMTc0.YI4Tfw.KpJvsosp-F9pvJlfcBKGUvWHTt4')


'''
    @bot.command()
    async def timer(ctx, *args):
       is_a_num = re.search(r"^(\d{2,4})$", ''.join(args))
       if is_a_num and len(args) != 2: # Make sure 2 arguments were passed
          await ctx.send("***Invalid Command! Must include hours followed by minutes!***\n (ex: `/time 0 30`)")
       else:
          eta = ((int(args[0]) * 60) * 60) + (int(args[1]) * 60)
          await ctx.send(f"You will be notified in **" + args[0] + "** hour(s) & **" + args[1] + "** minute(s)!")
          await asyncio.sleep(eta)
          await ctx.send(ctx.author.mention + " **ALERT! YOUR TIMER HAS RUN OUT! DO WHAT YOU MUST!**")
'''
