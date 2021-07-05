import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)

-------
        #self.bot.remove_command('help')
        @commands.command(pass_context=True)
        async def ping(self, ctx):
            """No context."""
            await ctx.send("this is a test")

        async def on_message(self, message):
                print(message.content)
------------
    async def on_ready(self):
        #print(f'Logged in as {self.user} (ID: {self.user.id})')
        channel = self.get_channel(841054606413791283) # channel ID goes here
        await channel.send ("*I will send you what time is it at 5:20PM insAllah* ")
        print("alive")