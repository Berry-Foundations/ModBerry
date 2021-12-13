# ModBerry

import discord
import os
import server

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} is ready!')
	activity = discord.Activity(type=discord.ActivityType.watching, name="Suspicious Users!")
	await client.change_presence(activity=activity)
	server.super_run()

try:
	token = os.getenv('TOKEN')
	client.run(token)
except Exception as e:
	print(e)

