import discord


class TicketButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Claim",
        style=discord.ButtonStyle.green,
        emoji="✅"
    )
    async def claim(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        embed = discord.Embed(
            title="Ticket Claimed",
            description=f"{interaction.user.mention} claimed this ticket",
            color=0x00ff88
        )

        await interaction.response.send_message(
            embed=embed
        )

    @discord.ui.button(
        label="Close",
        style=discord.ButtonStyle.red,
        emoji="🔒"
    )
    async def close(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.channel.edit(
            name=f"closed-{interaction.channel.name}"
        )

        embed = discord.Embed(
            title="Ticket Closed",
            description="This ticket has been closed",
            color=0xff0000
        )

        await interaction.response.send_message(
            embed=embed
        )

    @discord.ui.button(
        label="Delete",
        style=discord.ButtonStyle.gray,
        emoji="🗑️"
    )
    async def delete(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.response.send_message(
            "Deleting ticket...",
            ephemeral=True
        )

        await interaction.channel.delete()