import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Estou pronto para bagaçar! Estou conectado como {bot.user}")

# Token do Bot
bot.run(os.getenv("token"))  # Setar em variavel de ambiente
