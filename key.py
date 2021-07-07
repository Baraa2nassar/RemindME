import os

command_prefix='!'


def bot_pass():
    with open("SeTe.txt") as f:
        return f.read()