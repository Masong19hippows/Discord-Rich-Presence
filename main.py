#!/usr/bin/env python3

import os
import sys

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():

   guild = discord.utils.get(client.guilds, name=GUILD)
   member = discord.utils.get(guild.members, name="Masong19hippows")

   if member.activities == ():
      print('none')
   else:
      for activity in member.activities:
         if isinstance(activity, discord.activity.Game):
            name = activity.name
            Type = "Playing"
            Activity = f"{name}"
            Final = Type + ' ' + Activity
            print(Final)
         elif isinstance(activity, discord.activity.Streaming):
            name2 = activity.name
            name3 = activity.platform
            Type = "Streaming"
            Activity = f"{name2} on {name3}"
            Final = Type + ' ' + Activity
            print(Final)
         elif isinstance(activity, discord.activity.Spotify):
            name4 = activity.title
            name5 = ', '.join(activity.artists)
            Type = "Listening to Spotify:"
            Activity = f"Song Name: {name4}\nSong Artists: {name5}"
            Final = Type + '\n' + Activity
            print(Final)
client.run(TOKEN)
