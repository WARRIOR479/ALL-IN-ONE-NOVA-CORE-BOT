id="welcome1"
import discord
from discord.ext import commands
from discord import app_commands
import sqlite3
from config import MAIN_COLOR

conn = sqlite3.connect("database/welcome.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS welcome (
 guild_id INTEGER,
 channel_id INTEGER
)
''')

conn.commit()

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="welcome", description="Set welcome channel")
    @app_commands.checks.has_permissions(administrator=True)
    async def welcome(self, interaction: discord.Interaction, channel: discord.TextChannel):

        cursor.execute("DELETE FROM welcome WHERE guild_id = ?", (interaction.guild.id,))
        cursor.execute(
            "INSERT INTO welcome VALUES (?, ?)",
            (interaction.guild.id, channel.id)
        )

        conn.commit()

        await interaction.response.send_message(f"Welcome channel set to {channel.mention}")

    @commands.Cog.listener()
    async def on_member_join(self, member):

        cursor.execute(
            "SELECT channel_id FROM welcome WHERE guild_id = ?",
            (member.guild.id,)
        )

        data = cursor.fetchone()

        if data:
            channel = member.guild.get_channel(data[0])

            embed = discord.Embed(
                title="Welcome to NOVA MC",
                description=f"Welcome {member.mention}",
                color=MAIN_COLOR
            )

            embed.set_thumbnail(url=member.display_avatar.url)

            await channel.send(embed=embed)

async def setup(bot):
  await bot.add_cog(Welcome(bot))
