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

    if "bot" in message.content.lower():
        await message.channel.send("Halo, ada yag bisa saya bantu 😎")

    if message.content.lower().startswith("tolol"):
        await message.channel.send("Gak usah toxic gua ban juga lu ")

    if message.content.lower().strip() == "p":
    await message.channel.send("Waalaikumsallam")

    if "sepi" in message.content.lower():
    await message.channel.send("soalnya kalo rame lanjut part 2 xixixi")

    if message.content.lower().startswith("owner"):
        await message.channel.send("Owner sibuk geyzz")


client.run(os.environ['TOKEN'])











