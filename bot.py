# import discord.py
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os

# set a discord client
Client = discord.Client()
client = command.Bot(command_prefix = "?")

@client.event
async def on_ready():
    print("I'm in!")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        await client.send_message(message.channel, message.content[::-1])

client.run("NTAxNTIxODYwODI0MDA2NjY4.DqapaA.su1bMmowu0Q6Atiav19OmmSgflc")
