import os
import discord
import requests
import json
import random
from replit import db

client = discord.Client()

sad_wrods = ["sad", "depressed", "unhappy", "angry", "annoyed", "frustrated", "unloved"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there!",
  "You are a greate person/bot."
]

encourage_db_key = "encouragements"

def get_quotes():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouragement_message):
  if encourage_db_key in db.keys():
    encouragements = db[encourage_db_key]
    encouragements.append(encouragement_message)
    db[encourage_db_key] = encouragements
  else:
    db[encourage_db_key] = [encouragement_message]

  return("[" + encouragement_message + "] added sucessfully!")

def delete_encouragements(index):
  encouragements = db[encourage_db_key]
  if len(encouragements) > index:
    del encouragements[index]
    db[encouragements]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  if msg.startswith('!hi'):
    await message.channel.send('''
Hello!
I am a personal assistant bot of Mr. Prasanna.
Please follow the below link for his profile.
https://www.linkedin.com/in/prasanna-srinivasan2905/
    ''')

  if any(word in msg for word in sad_wrods):
    await message.channel.send(random.choice(starter_encouragements))

  options = []
  if encourage_db_key in db.keys():
   options = options.append(db[encourage_db_key])

  # TODO: -------------------------

  if msg.startswith('!inspire'):
    if options.size() > 0
      await message.channel.send(options)
    else
      await message.channel.send("")

  # TODO: -------------------------
  
  if msg.startswith('!add'):
    encourage_message = msg.split("!add ", 1)[1]
    update_encouragements(encourage_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith('!delete'):
    encouragements = []
    if encourage_db_key in  db.keys():
      index = int(msg.split("!delete", 1)[1])
      delete_encouragements(index)
      encouragements = db[encourage_db_key]
    await message.channel.send(encouragements)

  if msg.startswith(":laughing:"):
    await message.channel.send("I know why it is funny. :rofl: :yum:")

client.run(os.getenv('TOKEN'))