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

    if "p" in massage.content.lower():
        await massage.channel.sed("Wa'alaikumsallam")

    if message.content.lower() == "host":
        # Ganti 'host' dengan nama channel kamu
        channel = discord.utils.get(message.guild.text_channels, name="support")
        if channel:
            await message.channel.send(f"Host-nya ada di {channel.mention}")
        else:
            await message.channel.send("Channel #host tidak ditemukan 😢")

client.run(os.environ['TOKEN'])


