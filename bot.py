import asyncio
import discord

from discord.ext import commands
from discord.ext.commands import bot

from twitchbot import Bot

loop = asyncio.get_event_loop()

import dotenv
import os
dotenv.load_dotenv()

bot = commands.Bot(command_prefix="xd")
Bot = Bot()

TOKEN = os.environ.get("TOKEN")


@bot.event
async def on_message(message):

    if message.channel.id == 853517503913132033:
        if not message.author.bot:
            await Bot.discord_relay_thing_command(msg=message.content, username=message.author.name)
            print("Sent: " + message.content + "\nTo Twitch.")

loop.create_task(bot.start(TOKEN))
loop.create_task(Bot.run())
loop.run_forever()
