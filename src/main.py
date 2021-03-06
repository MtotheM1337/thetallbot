#!/usr/bin/env python3
import os
import discord
from discord.ext import commands
from cogs import Dice, Chuck

def main():
    # Exits early if the API key were not provided, as it's mandatory.
    api_token = os.getenv('TTB_TOKEN')
    if not api_token:
        print("[FATAL]: TTB_TOKEN is missing.")
        exit(1)

    about = '''
    Small bot for learning Python.
    '''

    # Creates the bot
    bot = commands.Bot(command_prefix='!', description=about)

    # Startup hook on successful Discord API connection.
    @bot.event
    async def on_ready():
        print(f'---\nLogged in as {bot.user} (ID: {bot.user.id})\n---')

    # Loads the cogs.
    bot.add_cog(Dice(bot))
    bot.add_cog(Chuck(bot))

    # Starts the bot.
    bot.run(api_token)

# Only run main function if called and not imported.
if __name__ == "__main__":
    main()
