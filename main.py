import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot login sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "hai":
        await message.channel.send("Halo juga 👋")

    if "kamu siapa" in message.content.lower():
        await message.channel.send("Aku bot auto respond dari Railway 😎")

    if message.content.lower().startswith("!ping"):
        await message.channel.send("🏓 Pong!")

client.run(os.environ['TOKEN'])
