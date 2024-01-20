# APPLICATION_ID = 1195693423722762261
#PUBLIC_KEY=eea54beae82bb7f3b42b9b93eb6708a446ac5269e576289ea4434885b075f4c4

import discord
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
chat = ''

token = os.getenv("SECRET_KEY")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        try:
            chat += f"{message.author}: {message.content}\n"
            print(f'Message from {message.author}: {message.content}')
            if self.user != message.author:
                if self.user in message.mentions:
                    response = openai.Completion.create(
                        model="davinci-002",
                        prompt=f"{chat}\nUmairBot: ",
                        temperature=1,
                        max_tokens=256,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    channel = message.channel
                    messageToSend = response['choices'][0]['text']
                    await channel.send(messageToSend)
        except Exception as e:
            print(e)
            chat = ""

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)


