import os

command_prefix='!'
#filename = "reminders_list.txt"
#filename = ctx.message.guild.name

def bot_pass():
    with open("SeTe.txt") as f:
        return f.read()