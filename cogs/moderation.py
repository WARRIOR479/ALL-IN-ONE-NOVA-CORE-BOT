import discord
from discord.ext import commands
from discord import app_commands
from config import MAIN_COLOR


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="ban",
        description="Ban a member"
    )
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = "No reason provided"
    ):

        await member.ban(reason=reason)

        embed = discord.Embed(
            title="🔨 Member Banned",
            color=MAIN_COLOR
        )

        embed.add_field(
            name="Member",
            value=member.mention
        )

        embed.add_field(
            name="Reason",
            value=reason
        )

        await interaction.response.send_message(
            embed=embed
        )

    @app_commands.command(
        name="kick",
        description="Kick a member"
    )
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = "No reason provided"
    ):

        await member.kick(reason=reason)

        embed = discord.Embed(
            title="👢 Member Kicked",
            color=MAIN_COLOR
        )

        embed.add_field(
            name="Member",
            value=member.mention
        )

        embed.add_field(
            name="Reason",
            value=reason
        )

        await interaction.response.send_message(
            embed=embed
        )

    @app_commands.command(
        name="timeout",
        description="Timeout a member"
    )
    @app_commands.checks.has_permissions(moderate_members=True)
    async def timeout(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        minutes: int,
        reason: str = "No reason provided"
    ):

        from datetime import timedelta

        await member.timeout(
            timedelta(minutes=minutes),
            reason=reason
        )

        embed = discord.Embed(
            title="⏳ Member Timed Out",
            color=MAIN_COLOR
        )

        embed.add_field(
            name="Member",
            value=member.mention
        )

        embed.add_field(
            name="Minutes",
            value=minutes
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Moderation(bot))