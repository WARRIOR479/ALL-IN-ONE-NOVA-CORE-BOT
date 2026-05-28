id="embed1"
import discord
from discord.ext import commands
from discord import app_commands

class Embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="embed", description="Create custom embed")
    @app_commands.checks.has_permissions(administrator=True)
    async def embed(
        self,
        interaction: discord.Interaction,
        title: str,
        description: str,
        color: str = "8b5cf6",
        image: str = None
    ):

        embed = discord.Embed(
            title=title,
            description=description,
            color=int(color, 16)
        )

        if image:
            embed.set_image(url=image)

        embed.set_footer(text="NOVA MC")

        await interaction.channel.send(embed=embed)
        await interaction.response.send_message("Embed sent", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Embeds(bot))