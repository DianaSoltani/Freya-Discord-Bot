import random
import asyncio
import aiohttp
import json
import discord
#import requests
#import youtube_dl

#from features import *
#from settings import *

TOKEN = 'NDY2MzY1OTQzOTEyNzI2NTQ5.DibA2w.Ym2fW6Pyolw0MguTcY07CJbCJ1M'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!who-sucks'):
        msg = 'GI0 SUCKS! HAHAHA!'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!cool'):
        await client.send_message(message.channel, 'Who is cool? Type !name name here')
        def check(msg):
            return msg.content.startswith('!name')

        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('!name'):].strip()
        await client.send_message(message.channel, '{} is cool indeed'.format(name))

@client.event
async def on_voice_state_update(before, after):
    if client.is_voice_connected(before.server) == True:
        global player
        previousChannel = before.voice_channel
        newChanner = after.voice_channel
        #Bot only talks when user's channel changes, not on mutes/deafens


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
