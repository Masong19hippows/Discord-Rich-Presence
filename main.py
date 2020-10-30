#!/usr/bin/env python3

import os
import sys
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import discord
from dotenv import load_dotenv
from Docs import update

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

DOCUMENT_ID = '1JBy1rmy3HQ6Dx9Ab9ERlxDSXT3O854RKhv6kVwmAf4s'
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():

   guild = discord.utils.get(client.guilds, name=GUILD)
   member = discord.utils.get(guild.members, name="Masong19hippows")

   if member.activities == ():
      act = 'none'
   else:
      for activity in member.activities:
         if isinstance(activity, discord.activity.Game):
            name = activity.name
            Type = "Playing"
            act = Type + ' ' + name
            update(docId=DOCUMENT_ID).delEvry()
            update(docId=DOCUMENT_ID).insertText(index='1', words=act)
         elif isinstance(activity, discord.activity.Streaming):
            name = activity.name
            plat = activity.platform
            Type = "Streaming"
            Activity = f"{name} on {plat}"
            act = Type + ' ' + Activity
            update(docId=DOCUMENT_ID).delEvry()
            update(docId=DOCUMENT_ID).insertText(index='1', words=act)
         elif isinstance(activity, discord.activity.Spotify):
            name = activity.title
            artist = ', '.join(activity.artists)
            imageURL = activity.album_cover_url
            Type = "Listening to Spotify:"
            Activity = f"Song Name: {name}     Song Artists: {artist}"
            act = Type + '      ' + Activity
            update(docId=DOCUMENT_ID).delEvry()
            update(docId=DOCUMENT_ID).insertText(index='1', words=act)
            update(docId=DOCUMENT_ID).insertImage(index='1', URL=imageURL)

client.run(TOKEN)
