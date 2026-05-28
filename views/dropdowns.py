import discord
from views.buttons import TicketButtons


class TicketDropdown(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(
                label="General Support",
                description="General help ticket",
                emoji="🎫"
            ),

            discord.SelectOption(
                label="Bug Report",
                description="Report bugs",
                emoji="🐛"
            ),

            discord.SelectOption(
                label="Purchase Support",
                description="Store support",
                emoji="💎"
            )
        ]

        super().__init__(
            placeholder="Select ticket type...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        category = discord.utils.get(
            interaction.guild.categories,
            name="TICKETS"
        )

        if category is None:
            category = await interaction.guild.create_category(
                "TICKETS"
            )

        channel = await interaction.guild.create_text_channel(
            name=f"ticket-{interaction.user.name}",
            category=category
        )

        await channel.set_permissions(
            interaction.guild.default_role,
            read_messages=False
        )

        await channel.set_permissions(
            interaction.user,
            read_messages=True,
            send_messages=True
        )

        embed = discord.Embed(
            title="🎫 Ticket Created",
            description=f"""
Type: {self.values[0]}

Support will help you soon.
""",
            color=0x8b5cf6
        )

        view = TicketButtons()

        await channel.send(
            interaction.user.mention,
            embed=embed,
            view=view
        )

        await interaction.response.send_message(
            f"Created {channel.mention}",
            ephemeral=True
        )


class TicketDropdownView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(TicketDropdown())