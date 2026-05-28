import discord
from discord.ext import commands
from discord import app_commands
from mcstatus import JavaServer
from config import MAIN_COLOR


class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="status",
        description="Minecraft server status"
    )
    async def status(
        self,
        interaction: discord.Interaction,
        ip: str
    ):

        try:
            server = JavaServer.lookup(ip)
            status = server.status()

            embed = discord.Embed(
                title="Minecraft Server Status",
                color=MAIN_COLOR
            )

            embed.add_field(
                name="IP",
                value=ip,
                inline=False
            )

            embed.add_field(
                name="Players",
                value=f"{status.players.online}/{status.players.max}"
            )

            embed.add_field(
                name="Ping",
                value=f"{round(status.latency)}ms"
            )

            embed.add_field(
                name="Version",
                value=status.version.name
            )

            await interaction.response.send_message(
                embed=embed
            )

        except Exception:
            await interaction.response.send_message(
                "Server offline"
            )


async def setup(bot):
    await bot.add_cog(Minecraft(bot))
