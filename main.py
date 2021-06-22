import os
import discord
import requests
import json

client = discord.Client()

def get_quotes():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('hi'):
    await message.channel.send('''
Hello!
I am a personal assistant of Mr. Prasanna.
Please follow the below link for his profile.
https://www.linkedin.com/in/prasanna-srinivasan2905/
    ''')

  if message.content.startswith('[inspiration]'):
    await message.channel.send(get_quotes())

client.run(os.getenv('TOKEN'))
