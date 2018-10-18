# import discord.py
import dbl
import discord
from discord.ext import commands

import aiohttp
import asyncio
import logging

Client = discord.client()
client = commands.Bot(command_prefix = "!")

class DiscordBotsOrgAPI:
    """Handles interactions with the discordbots.org API"""


    def __init__(self, bot):
        self.bot = bot
        self.token = 'NTAxNTIxODYwODI0MDA2NjY4.DqapaA.su1bMmowu0Q6Atiav19OmmSgflc'  #  set this to your DBL token
        self.dblpy = dbl.Client(self.bot, self.token)
        self.bot.loop.create_task(self.update_stats())

    async def update_stats(self):
        """This function runs every 30 minutes to automatically update your server count"""

        while True:
            logger.info('attempting to post server count')
            try:
                await self.dblpy.post_server_count()
                logger.info('posted server count ({})'.format(len(self.bot.guilds)))
            except Exception as e:
                logger.exception('Failed to post server count\n{}: {}'.format(type(e).__name__, e))
            await asyncio.sleep(1800)


def setup(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(DiscordBotsOrgAPI(bot))
# set a discord client

@client.event
async def on_ready():
    print("I'm in!")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        await client.send_message(message.channel, message.content[::-1])

client.run("NTAxNTIxODYwODI0MDA2NjY4.DqapaA.su1bMmowu0Q6Atiav19OmmSgflc")
