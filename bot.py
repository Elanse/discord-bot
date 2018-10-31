import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
from discord import Game

Client = discord.client
client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
    await client.change_presence(game = Game(name = "I'm alive!")))
    print("Ready!")

@client.event
async def on_message(message):
    if message.content.upper() == "RAINDROP":
        await client.send_message(message.channel, "DROPTOP")
    if message.content.upper().startswith("HELLO"):
        await client.send_message(message.channel, "Hi there!")
