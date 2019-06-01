import discord
from discord.ext import commands
import PartyParrotConstants
import os
import random

client = discord.Client()
client = commands.Bot(command_prefix=commands.when_mentioned, help_command=None)

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

    await client.process_commands(message)


async def exclamation_message(message):
    result = await recursive_walk(PATH, message)
    if not result:
        await message.channel.send('Sorry, I don\'t know that bird.')


async def recursive_walk(folder, message):
    found = False
    for root, directories, files in os.walk(folder):
        gif = '{}.gif'.format(message.content[1:])
        if directories:
            for directory in directories:
                found = await recursive_walk(os.path.join(root,directory), message)
            if found:
                return found
        if gif in files:
            found = True
            await message.channel.send(file=discord.File(os.path.join(folder, gif)))
            return found

@client.command()
async def help(ctx):
    embed = discord.Embed(title='Party Parrot Bot', description='It uploads party parrot gifs for you. List of commands as follows:')
    for root, directories, files in os.walk(PATH):
        for file in files:
            embed.add_field(name="!"+file[:-4], value=file[:-4])
            if len(embed.fields) == 25:
                await ctx.author.send(embed=embed)
                embed = discord.Embed(title='Party Parrot Bot', description='It uploads party parrot gifs for you. List of commands as follows:')
    await ctx.author.send(embed=embed)

client.run(PartyParrotConstants.token)
