import datetime
from aiohttp import request
import twitchio
from twitchio.ext import commands

import requests
from discord import Webhook, RequestsWebhookAdapter

import os

import dotenv

import json

with open("config.json") as config_file:
    config = json.load(config_file)

dotenv.load_dotenv()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            irc_token=os.environ.get("TwitchTOKEN"),
            client_id=os.environ.get("client_id"),
            nick=config["nickname"],
            prefix=config["prefix"],
            initial_channels=config["channels"],
        )

    async def event_ready(self):
        print(f"Twitch Bot Ready | {self.nick}")

    async def event_message(self, message):
        print(
            f"[MESSAGE LOGS] ({message.channel.name}) "
            + message.author.name
            + " - "
            + message.content
        )

        if message.author.name != "doobme":
            webhook = Webhook.from_url(os.environ.get("webhook_url"), adapter=RequestsWebhookAdapter())

            webhook.send(message.author.name + " - " + message.content)
            
            print("Sent: " + message.content + "\nTo Discord.")

        await self.handle_commands(message)

    @commands.command(name="ping", aliases=["ding"])    
    async def test_command(self, ctx):
        await ctx.send(f"FeelsDankMan 🔔 ding @{ctx.author.name}")

    async def discord_relay_thing_command(self, msg, username):
        for channel in self.initial_channels:
            xd = self.get_channel(channel)
            await xd.send(f"{username} - {msg}")

