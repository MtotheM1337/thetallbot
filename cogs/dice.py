from discord.ext import commands
import random

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # Simple dice rolling command.
    @commands.command()
    async def roll(self, ctx, sides: int):
        """Rolls a X sided dice."""
        try:
            result = random.randint(1, sides)
        except:
            await ctx.send(f"The amount of sides have to be >=1")
            return

        await ctx.send(f"🎲 You rolled a D{sides}: {result}")
    