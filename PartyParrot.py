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
    if message.content.startswith('!'):
        await exclamation_message(message)


async def exclamation_message(message):
    result = await recursive_walk(PATH, message)
    if not result:
        await message.channel.send('Sorry, I don\'t know that bird.')


async def recursive_walk(folder, message):
    for root, directories, files in os.walk(folder):
        gif = '{}.gif'.format(message.content[1:])
        if gif in files:
            await message.channel.send(file=discord.File(os.path.join(folder, gif)))
            return True
        if directories:
            for directory in directories:
                await recursive_walk(os.path.join(root, directory), message)


client.run(PartyParrotConstants.token)
