import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logado como {bot.user} - PAPEL SCAN ONLINE!")
    await bot.tree.sync()

@bot.tree.command(name="ping", description="Testa se o bot esta online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong! Papel Scan online!")

@bot.tree.command(name="scan", description="Simula o scan de um papel")
async def scan(interaction: discord.Interaction, texto: str):
    await interaction.response.send_message(f"📄 **Papel escaneado:**\n```{texto}```")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.lower().startswith("!scan"):
        await message.channel.send("📄 Manda o texto do papel que eu escaneio pra tu!")
    await bot.process_commands(message)

token = os.getenv("DISCORD_TOKEN") or os.getenv("TOKEN")
bot.run(token)
