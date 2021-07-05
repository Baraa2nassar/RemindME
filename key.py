import os

def bot_pass():
    with open("bot.txt") as f:
        return f.read()