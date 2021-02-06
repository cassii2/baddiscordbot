# main.py
import os
import logging
from commands import parse
import random

import discord

fp = open("token.txt", "r")
TOKEN = fp.read()

COMMAND_KEY = '$'

client = discord.Client()
random.seed()

logging.basicConfig(level=logging.INFO)

@client.event
async def on_ready():
    print('Logged on as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(COMMAND_KEY):
        command = message.content[1:]
        await parse(command, message)


client.run(TOKEN)

