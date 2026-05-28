import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix="$",
    intents=intents,
    help_command=None
)

COGS = [
    "cogs.utility",
    "cogs.embeds",
    "cogs.minecraft",
    "cogs.welcome",
    "cogs.autoresponse",
    "cogs.tickets",
    "cogs.help",
    "cogs.moderation"
]


@bot.event
async def on_ready():

    print(f"Logged in as {bot.user}")

    activity = discord.Streaming(
        name="NOVACORE",
        url="https://twitch.tv/novamc"
    )

    await bot.change_presence(
        activity=activity
    )

    try:
        synced = await bot.tree.sync()

        print(f"Synced {len(synced)} commands")

    except Exception as e:
        print(e)


async def load_cogs():

    for cog in COGS:

        try:
            await bot.load_extension(cog)

            print(f"Loaded {cog}")

        except Exception as e:
            print(f"Failed to load {cog}")
            print(e)


async def main():

    async with bot:

        await load_cogs()

        await bot.start(TOKEN)


asyncio.run(main())