from poe_api_wrapper import PoeApi
import os
client = PoeApi(os.environ['PB'])
import asyncio

#from revChatGPT.V1 import AsyncChatbot
#chatbot = AsyncChatbot(config={
#  "email": os.environ['email'],
#  "password": os.environ['pass']
#})


#Auth
async def GetText(prompt,bot = "chinchilla"):
  prev_text = ""
  #code = ""
  for chunk in client.send_message(bot, prompt, suggest_replies=True):
    await asyncio.sleep(0.05)
  prev_text = chunk["text"]
  client.delete_chat(bot, del_all=True)
  #client.chat_break(bot, chatCode = code)
  #async for data in chatbot.ask(prompt):
  #    message = data["message"][len(prev_text) :]
  #    #print(message, end="", flush=True)
  #    prev_text = data["message"]
  return prev_text
