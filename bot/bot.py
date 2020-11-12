import discord
import requests
from src.services.scheduleService import *
import json

client = discord.Client()

with open("config.json") as f:
    CONFIG = json.load(f)


@client.event
async def on_ready():
    print("Efetuamos o login como {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith(CONFIG["PREFIX"] + "horarios"):
        msg = message.content
        embed = horarios(msg, _getArgs(msg))
        await message.channel.send(embed=embed)


client.run(CONFIG["TOKEN"])


def _getArgs(mensagem):
    return mensagem.split(" ")[1:]
