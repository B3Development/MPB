import os
import discord

from discord import client
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv() # Loading token from .env file

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = "-", intents = intents) # Setting the bot's prefix.(character before each command)

@client.event
async def on_ready():

    activity = discord.Game(name = "-help", type = 3) # Setting the bot's presence in Discord.
    await client.change_presence(status = discord.Status.online, activity = activity) # Sending presence to Discord to display.

    print(f'+----------------------+\n'
          f'|        MPB Bot       |\n'
          f'|         v1.1         |\n'
          f'+----------------------+\n'
          f'|       By Fwayne      |\n'
          f'+----------------------+\n') # Letting us know the bot is ready for action.

@client.event 
async def on_member_join(member):
  role = discord.utils.get(member.guild.roles, id = 919468792139091989)
  await member.add_roles(role)

@client.command()
async def load(extension):
    client.load_extension(f'cog.{extension}')

@client.command()
async def unload(extension):
    client.unload_extension(f'cog.{extension}')

for filename in os.listdir('./cog'):
    if filename.endswith('.py'):
        client.load_extension(f'cog.{filename[0:-3]}')

client.run(os.getenv('TOKEN'))