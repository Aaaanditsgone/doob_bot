"""
 ____                    __          ____            __      
/\  _`\                 /\ \        /\  _`\         /\ \__   
\ \ \/\ \    ___     ___\ \ \____   \ \ \L\ \    ___\ \ ,_\  
 \ \ \ \ \  / __`\  / __`\ \ '__`\   \ \  _ <'  / __`\ \ \/  
  \ \ \_\ \/\ \L\ \/\ \L\ \ \ \L\ \   \ \ \L\ \/\ \L\ \ \ \_ 
   \ \____/\ \____/\ \____/\ \_,__/    \ \____/\ \____/\ \__\
    \/___/  \/___/  \/___/  \/___/      \/___/  \/___/  \/__/

 
 Doob Bot, A simple discord bot for Raider.io

 Github: https://github.com/onnenon/doob_bot 

"""

import asyncio
import datetime
import time

from secrets import BOT_TOKEN

import discord
from discord.ext import commands
from discord.ext.commands import Bot

from raiderio_api import char_api_request

CHAR_PREFIX = ['#info', '#ioscore', '#best', '#highest']
MYTHIC_PLUS_PREFIX = []

BOT = commands.Bot(command_prefix="#")


@BOT.event
async def on_ready():
    """Function that will print to console when bot is running successfully. """
    print(f"{BOT.user.name} Is Running")
    print(f"With the ID: {BOT.user.id}")


@BOT.event
async def on_message(message):
    """Function that scans messages in text channels of a server and calls the
    Raider.io API when a defined prefix is used.
    """
    # Split the message into a list
    args = message.content.split(" ")

    # If first index of that list is in the defined prefixes prep the message
    if args[0] in CHAR_PREFIX or args[0] in MYTHIC_PLUS_PREFIX:
        prefix = args.pop(0)
        arg_fix = [arg.replace("_", "-") for arg in args]

        if prefix in CHAR_PREFIX:
            embed = discord.Embed(
                title="Doob Bot",
                colour=discord.Colour(0x52472b),
                url="https://discordapp.com",
                description="A simple Discord bot for getting Raider.io Data\n",
                timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            embed.set_footer(text=("-" * 115))
            try:
                message_embed = char_api_request(arg_fix, prefix, embed)
                return await BOT.send_message(
                    message.channel, embed=message_embed)
            except:
                return await BOT.send_message(
                    message.channel,
                    "No data was returned from Raider.io, check your spelling!!"
                )

        if prefix in MYTHIC_PLUS_PREFIX:
            # TODO Create commands that get non-character info from API
            pass


BOT.run(BOT_TOKEN)
