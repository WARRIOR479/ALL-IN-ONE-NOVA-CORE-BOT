id="utility1"
import discord
from discord.ext import commands
from discord import app_commands
from config import MAIN_COLOR

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="user", description="Check user info")
    async def user(self, interaction: discord.Interaction, member: discord.Member = None):

        member = member or interaction.user

        embed = discord.Embed(
            title=f"{member.name} Info",
            color=MAIN_COLOR
        )

        embed.set_thumbnail(url=member.display_avatar.url)

        embed.add_field(name="Username", value=member.name)
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Joined", value=member.joined_at.strftime('%d/%m/%Y'))
        embed.add_field(name="Created", value=member.created_at.strftime('%d/%m/%Y'))

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="server", description="Server info")
    async def server(self, interaction: discord.Interaction):

        guild = interaction.guild

        embed = discord.Embed(
            title=f"{guild.name}",
            color=MAIN_COLOR
        )

        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        embed.add_field(name="Members", value=guild.member_count)
        embed.add_field(name="Owner", value=guild.owner)
        embed.add_field(name="Created", value=guild.created_at.strftime('%d/%m/%Y'))

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))
    