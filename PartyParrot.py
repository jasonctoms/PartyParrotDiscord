import discord
from discord.ext import commands
import PartyParrotConstants
import os

client = discord.Client()
bot = commands.Bot(command_prefix='!')

PATH = PartyParrotConstants.path
TOKEN = PartyParrotConstants.token


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    try:
        if message.content.startswith('!') and filter(lambda x: message.content[1:] in x, os.listdir(PATH)):
            await message.channel.send(file=discord.File(PATH + '{}.gif'.format(message.content[1:])))
    except:
        await message.channel.send('Sorry, I don\'t know that bird.')


client.run(PartyParrotConstants.token)
