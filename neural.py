import asyncio
import os
import requests
from io import BytesIO
from PIL import Image
import discord

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
    "prompt": prompt,
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
    os.environ['neural']
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
    os.environ['neural']
  }
  count = 0
  while True:
    await asyncio.sleep(3)
    response2 = requests.get(url2, headers=headers2)

    count += 1

    data2 = response2.json()
    if data2["status"]["isReady"]:
      links = []
      for i in range(data2["input"]["amount"]):
        data3 = data2["output"][i]
        links.append(data3["full"])
      with BytesIO() as image_binary:
        create_image(links).save(image_binary, 'PNG')
        image_binary.seek(0)
        await channel.send(file=discord.File(fp=image_binary, filename='image.png'))
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