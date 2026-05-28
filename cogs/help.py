import discord
from discord.ext import commands
from discord import app_commands
from config import MAIN_COLOR


class HelpDropdown(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(
                label="Utility",
                description="User & server commands",
                emoji="🛠️"
            ),
            discord.SelectOption(
                label="Minecraft",
                description="Minecraft related commands",
                emoji="⛏️"
            ),
            discord.SelectOption(
                label="Tickets",
                description="Support system commands",
                emoji="🎫"
            ),
            discord.SelectOption(
                label="Setup",
                description="Setup & configuration",
                emoji="⚙️"
            )
        ]

        super().__init__(
            placeholder="Select command category...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        if self.values[0] == "Utility":

            embed = discord.Embed(
                title="🛠️ Utility Commands",
                color=MAIN_COLOR
            )

            embed.description = """
`/user`
Check user information

`/server`
Check server information

`/embed`
Create custom embeds
"""

        elif self.values[0] == "Minecraft":

            embed = discord.Embed(
                title="⛏️ Minecraft Commands",
                color=MAIN_COLOR
            )

            embed.description = """
`/status`
Check Minecraft server status
"""

        elif self.values[0] == "Tickets":

            embed = discord.Embed(
                title="🎫 Ticket Commands",
                color=MAIN_COLOR
            )

            embed.description = """
`/panel`
Create ticket panel

Ticket Buttons:
• Claim
• Close
• Delete
"""

        elif self.values[0] == "Setup":

            embed = discord.Embed(
                title="⚙️ Setup Commands",
                color=MAIN_COLOR
            )

            embed.description = """
`/welcome`
Setup welcome system

`/autoresponse`
Create automatic responses
"""

        embed.set_footer(text="NOVA MC • Premium Discord Bot")

        await interaction.response.edit_message(
            embed=embed,
            view=self.view
        )


class HelpView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(HelpDropdown())


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="help",
        description="Show all bot commands"
    )
    async def help(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="🌌 NOVA MC HELP MENU",
            description="""
Welcome to **NOVA MC**

Use the dropdown menu below
to explore all command categories.
""",
            color=MAIN_COLOR
        )

        embed.add_field(
            name="Categories",
            value="""
🛠️ Utility
⛏️ Minecraft
🎫 Tickets
⚙️ Setup
""",
            inline=False
        )

        if interaction.guild.icon:
            embed.set_thumbnail(
                url=interaction.guild.icon.url
            )

        embed.set_footer(
            text="NOVA MC • Modern Minecraft Utility Bot"
        )

        view = HelpView()

        await interaction.response.send_message(
            embed=embed,
            view=view
        )


async def setup(bot):
    await bot.add_cog(Help(bot))