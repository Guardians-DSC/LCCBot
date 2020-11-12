import discord
import requests
from src.services.scheduleService import *
import json

client = discord.Client()


def _getArgs(mensagem):
    return mensagem.split(" ")[1:]


@client.event
async def on_ready():
    print("Efetuamos o login como {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith("!" + "horarios"):
        msg = message.content
        embed = horarios(msg, _getArgs(msg))
        await message.channel.send(embed=embed)


client.run("NzU0ODQ3ODI4Mjk5NDgxMDg4.X16s0g.BvA6vtgT03JosE42hwX2B0wNCT" + "8")
