id="auto1"
import discord
from discord.ext import commands
from discord import app_commands
import sqlite3

conn = sqlite3.connect("database/autoresponse.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS autoresponse (
 guild_id INTEGER,
 trigger TEXT,
 title TEXT,
 description TEXT,
 image TEXT,
 color TEXT
)
''')

conn.commit()

class AutoResponse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="autoresponse", description="Create auto response")
    @app_commands.checks.has_permissions(administrator=True)
    async def autoresponse(
        self,
         interaction: discord.Interaction,
        trigger: str,
        title: str,
        description: str,
        color: str = "8b5cf6",
        image: str = None
    ):

        cursor.execute(
            "INSERT INTO autoresponse VALUES (?, ?, ?, ?, ?, ?)",
            (
                interaction.guild.id,
                trigger,
                title,
                description,
                image,
                color
            )
        )

        conn.commit()

        await interaction.response.send_message("Auto response created")

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        cursor.execute(
             "SELECT * FROM autoresponse WHERE guild_id = ?",
            (message.guild.id,)
        )

        data = cursor.fetchall()

        for row in data:
            trigger = row[1]

            if trigger.lower() in message.content.lower():

                embed = discord.Embed(
                    title=row[2],
                    description=row[3],
                    color=int(row[5], 16)
                )

                if row[4]:
                    embed.set_image(url=row[4])

                await message.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(AutoResponse(bot))