import os

import discord
import generate
import neural
import itemname
import random
import re
from discord import app_commands
from discord.ext import tasks
import keep_alive
from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

queue = []

guildID = 1081397933276155977
botID = 1144041248303366314
magicForum = 1144040531240964256
raceForum = 1144075835217825868
subclassForum = 1144075898870579290
locationForum = 1144075950749925457
monsterForum = 1144081512724176947
npcForum = 1144425240018034878
otherForum = 1144426051720724602
logChannel = 1144064721922834582
autogen = True

@client.event
async def on_message(message):
    if message.author != client.user:
        pass

@client.event
async def on_thread_create(thread):
    # await thread.send("## Sample Concept Art Being Generated")
    await neural.Generate(f"art of the '{thread.name}', a form of {thread.parent.name}",thread)

@tree.command(name = "magicitem", description = "Generate a new magic item!", guild=discord.Object(id=guildID))
async def magicitem(interaction, name:str, desc: str = ""):
  queue.append(["magic item", name,desc + ", and Give detailed rules for item effects and flavor accordingly. Keep non-artifact, non-legendary magic items simple.", magicForum, interaction.user.id])
  embedVar = discord.Embed(title=f'Queue position: {len(queue)}', description=f"It won't be long until we get around to the '{name}'!", color=0xffff00)
  await interaction.response.send_message(embed=embedVar)

@tree.command(name = "race", description = "Generate a new race!", guild=discord.Object(id=guildID))
async def race(interaction, name:str, desc: str = ""):
  queue.append(["race", name,desc, raceForum, interaction.user.id])
  embedVar = discord.Embed(title=f'Queue position: {len(queue)}', description=f"It won't be long until we get around to the '{name}'!", color=0xffff00)
  await interaction.response.send_message(embed=embedVar)
  
@tree.command(name = "subclass", description = "Generate a new subclass!", guild=discord.Object(id=guildID))
async def subclass(interaction, name:str, desc: str = ""):
  queue.append(["subclass", name,desc, subclassForum, interaction.user.id])
  embedVar = discord.Embed(title=f'Queue position: {len(queue)}', description=f"It won't be long until we get around to the '{name}'!", color=0xffff00)
  await interaction.response.send_message(embed=embedVar)
  
@tree.command(name = "location", description = "Generate a new location!", guild=discord.Object(id=guildID))
async def location(interaction, name:str, desc: str = ""):
  queue.append(["location", name,desc+", and Describe the location in detail. Provide key locations and any necessary information on NPCs.", locationForum, interaction.user.id])
  embedVar = discord.Embed(title=f'Queue position: {len(queue)}', description=f"It won't be long until we get around to the '{name}'!", color=0xffff00)
  await interaction.response.send_message(embed=embedVar)

@tree.command(name = "monster", description = "Generate a new monster!", guild=discord.Object(id=guildID))
async def monster(interaction, name:str, desc: str = ""):
  queue.append(["living being", name,desc + ", and Give adequate description to both the flavoring of the monster AND the stat block.", monsterForum, interaction.user.id])
  embedVar = discord.Embed(title=f'Queue position: {len(queue)}', description=f"It won't be long until we get around to the '{name}'!", color=0xffff00)
  await interaction.response.send_message(embed=embedVar)

@tree.command(name = "npc", description = "Generate a new npc!", guild=discord.Object(id=guildID))
async def npc(interaction, name:str, desc: str = ""):
  queue.append(["NPC", name,desc + ". Provide a stat block for the NPC, but also include a bond, ideal, personality trait, and flaw. Offer a potential quest involving the NPC.", npcForum, interaction.user.id])
  embedVar = discord.Embed(title=f'Queue position: {len(queue)}', description=f"It won't be long until we get around to the '{name}'!", color=0xffff00)
  await interaction.response.send_message(embed=embedVar)

@tree.command(name = "other", description = "Generate a new npc!", guild=discord.Object(id=guildID))
async def other(interaction, name:str, type:str = "spell", desc: str = ""):
  queue.append([type, name,f"Be sure to follow all rules surrounding the {type}.", 1144426051720724602, interaction.user.id])
  embedVar = discord.Embed(title=f'Queue position: {len(queue)}', description=f"It won't be long until we get around to the '{name}'!", color=0xffff00)
  await interaction.response.send_message(embed=embedVar)

@tree.command(name = "ask", description = "Use in a thread to get more details!", guild=discord.Object(id=guildID))
async def ask(interaction, question:str):
  if interaction.channel.type == discord.ChannelType.public_thread or interaction.channel.type == discord.ChannelType.forum:
    embedVar = discord.Embed(title=f'Reply inbound', description=f"Question: {question}", color=0xffffff)
    await interaction.response.send_message(embed=embedVar)
    #The important code
    ctx = ""
    async for message in interaction.channel.history(limit=100,oldest_first=True):
      if str(message.author.id) == str(botID):
        ctx += message.content
    await interaction.channel.send(await generate.GetText(f"You are being asked a question about a piece of DND 5E content. The piece of content is: \n{ctx} \n\nThe question is: {question}. Answer the question thoroughly, but keep it less than 200 words. You do not need to restate any of the content's material nor that this is for DND 5E."))
  else :
    embedVar = discord.Embed(title=f'Invalid location', description=f"Do this inside of a forum post for context-specific results!", color=0xff0000)
    await interaction.response.send_message(embed=embedVar)

@tree.command(name = "conceptart", description = "Generate concept art!", guild=discord.Object(id=guildID))
async def conceptart(interaction, prompt:str):
  embedVar = discord.Embed(title=f'Art inbound!', description=f"Prompt: '{prompt}'", color=0xffffff)
  await interaction.response.send_message(embed=embedVar)
  await neural.Generate(f"{prompt}", interaction.channel)
    
intervals = 0
alreadyGenerating = False

async def AddAutoGen(amount):
  if amount > 10 or !autogen:
    return
  for i in range(amount):
    v = random.choice([0,1,2,3 ])
    if v == 0:
      queue.append(["magic item", itemname.makeItem().title(),"Give detailed rules for item effects and mechanics.", magicForum, -1])
    elif v == 1:
      queue.append(["living being", itemname.makeItem(itemname.creatures).title(),"Give adequate description to both the flavoring of the monster AND the stat block.", monsterForum, -1])
    elif v == 2:
      queue.append(["location", itemname.makeItem(itemname.locations).title(),"Describe the location in detail. Provide key locations and any necessary information on NPCs.", locationForum, -1])
    elif v == 3:
      queue.append(["spell", itemname.makeItem(itemname.spells).title(),"Be sure to follow all rules surrounding the spell.", otherForum, -1])

@tasks.loop(minutes=0.4)
async def FlushQueue():
  global alreadyGenerating
  global intervals
  try:
    if alreadyGenerating:
      return
    alreadyGenerating = True

    if len(queue) == 0:
      intervals = (intervals+1)%6
      if intervals == 0:
        await AddAutoGen(1)
    
    if len(queue) > 0:
      obj = queue.pop(0)
      keep_alive.header = obj[1]
      obj[1] = re.sub('[^A-Za-z0-9 ]+', '', obj[1])
      log = client.get_channel(logChannel)
      await log.send(f"**Now generating the {obj[0]} '{obj[1]}'**")
      channel = client.get_channel(obj[3])
      st = f"Create a DND 5e {obj[0]} named the '{obj[1]}'. {obj[2]} Keep the final text under 300 words. Use markdown text formatting."
      c = await generate.GetText(st)
      keep_alive.body = c
      if len(c) > 1900:
        c2 = c[1899:(len(c)-1)]
        c = c[0:1899]
        thread = await channel.create_thread(name = obj[1], content = c + " (Truncated)")
        await thread.thread.send(c2)
        if (obj[4]!=-1):
          await thread.thread.send("<@" + str(obj[4]) + ">")
        else:
          await thread.thread.send("Autogenerated by the bot")
      else:
        thread = await channel.create_thread(name = obj[1], content = c)
        if (obj[4]!=-1):
          await thread.thread.send("<@" + str(obj[4]) + ">")
        else:
          await thread.thread.send("Autogenerated by the bot")
      
    alreadyGenerating = False
  except Exception as e:
    
    log = client.get_channel(logChannel)
    await log.send("I'm just as confused as you are, there was an error somehow! The next time it should work though.")
    await log.send("Error message: " + str(e))
    alreadyGenerating = False

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    await tree.sync(guild=discord.Object(id=guildID))
    log = client.get_channel(logChannel)
    await log.send("Bot now online")
    FlushQueue.start()

keep_alive()

my_secret = os.environ['discordbot']
client.run(my_secret)