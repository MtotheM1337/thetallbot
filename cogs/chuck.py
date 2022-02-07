from discord.ext import commands
import requests
import json

class Chuck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # Chuck Norris qoute command
    @commands.command()
    async def chuck(self, ctx):
        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = json.loads(response.text)
        
        await ctx.send(data["value"])
