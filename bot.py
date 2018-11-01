import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import time
from discord import Game

Client = discord.client
client = commands.Bot(command_prefix = "?")
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game = Game(name = "I'm Alive!"))
    print("Ready, Freddy!")

@client.event
async def on_message(message):
    if message.content == "$ping"
        await client.send_message(message.channel, "pong")
    if ("hello") in message.content:
        await client.delete_message(message)

client.run("NTAxNTIxODYwODI0MDA2NjY4.DqapaA.su1bMmowu0Q6Atiav19OmmSgflc")
