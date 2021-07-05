import os

def bot_pass():
    with open("bot1.txt") as f:
        return f.read()