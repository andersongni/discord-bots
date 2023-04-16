import discord
# from discord import Client
import re
import os

# Create an Intents object
intents = discord.Intents.default()

# Specify the intents you want to enable for your bot
intents.messages = True
intents.message_content = True
intents.guilds = True

# print(dir(intents))

# Create a bot instance with the intents
client = discord.Client(intents=intents)

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print('------')

# Event handler for when a message is received
@client.event
async def on_message(message):
    # Check if the message is from the bot itself to avoid infinite loop
    if message.author == client.user:
        return
    
    print ("-------------------------------------")
    print ("Received message on channel: " + str(message.channel.id))
    print ("Author: " + str(message.author))
    print ("Content: \n" + message.content)
    # print(dir(message))

    # Check if the message starts with a specific command
    if message.content.startswith('!mplay'):
        # Get the content of the message
        content = message.content

        # Define the custom delimiter as "!play " followed by optional newline character
        delimiter = r"!mplay |\n"

        # Convert message.content to an array of strings, ignoring newline characters after "!play "
        words = re.split(delimiter, content)
        
        # Filter out empty strings from the list
        for word in words:
            if word != '':
                await message.channel.send("!play " + word)
        

# Run the bot with the bot token
discord_token = os.environ['GOUVEAS_BOT_TOKEN']
client.run(discord_token)
