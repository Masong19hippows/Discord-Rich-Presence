# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  for member in client.get_all_members():
      print(member)
#      if member.game == None:
#          continue
#  else:
#      print(member.name, member, member.game)


client.run(TOKEN)
