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
  guild = discord.utils.get(client.guilds, name=GUILD)
  member = discord.utils.get(guild.members, name="Masong19hippows")
  for activity in member.activities:
    if isinstance(activity, Game):
       name = activity.name
       Type = "Playing"
       Activity = f"{name}"
       print(Activity)
    elif isinstance(activity, Streaming):
       name2 = activity.name
       name3 = activity.platform
       Type = "Streaming"
       Activity = f"{name2} on {name3}"
       print(Activity)
    elif isinstance(activity, Spotify):
       name4 = activity.title
       name5 = activity.artists
       Type = "Listening to Spotify"
       Activity = f"**Song Name**:{name4}\n**Song Artists:**{name5}"
       print(Activity)
    else:
       print('none')

client.run(TOKEN)
