# bot.py
import os

import discord

TOKEN = 'NzYwMjA5MDQ1NDQwNjkyMjc3.X3It2A.d55a0tsoQ7PAjKIdmG-LOdQQWAU'
GUILD = 'projects'

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
