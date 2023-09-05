import asyncio
import os
import requests
from io import BytesIO
from PIL import Image
import discord
import re

class ViewWithButton(discord.ui.View):
  channel = 0
  prompt = "test"
  def __init__(self, *, timeout=180, parameter, p2):
    super().__init__(timeout=timeout)
    self.channel = parameter
    self.prompt = p2
  @discord.ui.button(label="Regenerate!",style=discord.ButtonStyle.green)
  async def blurple_button(self,button:discord.ui.Button,interaction:discord.Interaction):
    embedVar = discord.Embed(title=f'Regeneration Started', description=f"Prompt: '{self.prompt}'", color=0xff0000)
    #await interaction.response.send_message(embed=embedVar)
    await Generate(self.prompt,self.channel)

def create_image(links):
  
  images=[]
  for index in links:
    response = requests.get(index)
    images.append(Image.open(BytesIO(response.content)))
  image = Image.new("RGB", (images[0].width*len(images), images[0].height))
  i=0
  for img in images:
    image.paste(images[i], (images[i].width*i, 0))
    i+=1
  return image

async def Generate(prompt, channel, count=2, negativePrompt = "",size="square"):
  url = "https://api.neural.love/v1/ai-art/generate"
  payload = {
    "amount": count,
    "isPublic": True,
    "isPriority": False,
    "isHd": False,
    "steps": 25,
    "cfgScale": 7.5,
    "prompt": re.sub(r'\W+', '', prompt),
    "style": "anything",
    "layout": size,
    "negativePrompt": negativePrompt
  }
  headers = {
    "accept":
    "application/json",
    "content-type":
    "application/json",
    "authorization":
    os.environ['NEURAL']
  }
  response = requests.post(url, json=payload, headers=headers)
  data = response.json()

  if not "orderId" in data.keys():
    await channel.send("**Error while generating, try again?**")
    return
  orderId = data["orderId"]
  print(orderId)
  url2 = "https://api.neural.love/v1/ai-art/orders/" + orderId
  print(url2)
  headers2 = {
    "accept":
    "application/json",
    "authorization":
    os.environ['NEURAL']
  }
  count = 0
  while True:
    await asyncio.sleep(3)
    response2 = requests.get(url2, headers=headers2)

    count += 1

    data2 = response2.json()
    if data2["status"]["isReady"]:
      print("Awesome! Debugging!")
      links = []
      view = ViewWithButton(parameter=channel,p2=prompt) # Establish an instance of the discord.ui.View class

      #e = discord.Embed(title="Results are in!")
      for i in range(data2["input"]["amount"]):
        data3 = data2["output"][i]
        links.append(data3["full"])
        style = discord.ButtonStyle.gray  # The button will be gray in color
        item = discord.ui.Button(style=style, label="Full #"+str(i+1), url=data3["full"])  # Create an item to pass into the view class.
        view.add_item(item=item)  # Add that item into the view class
      with BytesIO() as image_binary:
        create_image(links).save(image_binary, 'PNG')
        image_binary.seek(0)
        
        #await message.channel.send(embed=HelpEmbed, components=[action_row])
        await channel.send(file=discord.File(fp=image_binary, filename='image.png'),view=view)
      break
    elif data2["status"]["code"] == 998:
      await channel.send("All results were NSFW, aborting!")
      break
    elif count > 10:
      await channel.send("Taking too long, aborting!")
      break
    else:
      #await message.channel.send("Not done, waiting 10 seconds to retry..."
                                 
      await asyncio.sleep(7)
