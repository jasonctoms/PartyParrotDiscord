import discord
import PartyParrotConstants

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    try:
        if message.content.startswith('!') and 'parrot' in message.content:
            await message.channel.send(file=discord.File(PartyParrotConstants.path + '{}.gif'.format(message.content[1:])))
    except:
        await message.channel.send('Sorry, I don\'t know that bird.')


client.run(PartyParrotConstants.token)
