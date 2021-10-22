import discord
import os
import datetime
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Estou pronto para bagaçar! Estou conectado como {bot.user}")
    current_time.start()

@bot.event
async def on_message(message):  # Evita loop
    if message.author == bot.user:
        return

    if "Bot lixo" in message.content:
        await message.channel.send(f"Por favor, {message.author.name}, eu não sou ruim.")

    await bot.process_commands(message)


@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name
    response = "Olá, " + name

    await ctx.send(response)


@tasks.loop(hours=1)
async def current_time():
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y às %H:%M:%S")

    channel = bot.get_channel(856956765216047124)  # ID canal abbot

    await channel.send("Data atual: " + now)


# Token do Bot
bot.run(os.getenv("token"))  # Setar em variavel de ambiente
