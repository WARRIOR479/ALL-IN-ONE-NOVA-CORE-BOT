import discord
from discord.ext import commands
from discord import app_commands

from views.dropdowns import TicketDropdownView
from config import MAIN_COLOR


class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="panel",
        description="Create ticket panel"
    )
    @app_commands.checks.has_permissions(
        administrator=True
    )
    async def panel(
        self,
        interaction: discord.Interaction
    ):

        embed = discord.Embed(
            title="🎫 NOVA CORE SUPPORT",
            description="""
Need help?

Select a ticket category
from the dropdown below.
""",
            color=MAIN_COLOR
        )

        embed.set_footer(
            text="NOVA CORE • Premium Support System"
        )

        embed.set_thumbnail(
            url=interaction.guild.icon.url
            if interaction.guild.icon
            else None
        )

        file = discord.File(
            "assets/ticket_bg.png",
            filename="ticket_bg.png"
        )

        embed.set_image(
            url="attachment://ticket_bg.png"
        )

        view = TicketDropdownView()

        await interaction.channel.send(
            embed=embed,
            view=view,
            file=file
        )

        await interaction.response.send_message(
            "✅ Ticket panel created.",
            ephemeral=True
        )

    @app_commands.command(
        name="add",
        description="Add user to ticket"
    )
    @app_commands.checks.has_permissions(
        manage_channels=True
    )
    async def add(
        self,
        interaction: discord.Interaction,
        member: discord.Member
    ):

        if "ticket" not in interaction.channel.name.lower():

            await interaction.response.send_message(
                "❌ This is not a ticket channel.",
                ephemeral=True
            )

            return

        await interaction.channel.set_permissions(
            member,
            read_messages=True,
            send_messages=True
        )

        embed = discord.Embed(
            title="✅ User Added",
            description=f"{member.mention} was added to the ticket.",
            color=0x00ff88
        )

        await interaction.response.send_message(
            embed=embed
        )

    @app_commands.command(
        name="remove",
        description="Remove user from ticket"
    )
    @app_commands.checks.has_permissions(
        manage_channels=True
    )
    async def remove(
        self,
        interaction: discord.Interaction,
        member: discord.Member
    ):

        if "ticket" not in interaction.channel.name.lower():

            await interaction.response.send_message(
                "❌ This is not a ticket channel.",
                ephemeral=True
            )

            return

        await interaction.channel.set_permissions(
            member,
            overwrite=None
        )

        embed = discord.Embed(
            title="❌ User Removed",
            description=f"{member.mention} was removed from the ticket.",
            color=0xff0000
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Tickets(bot))