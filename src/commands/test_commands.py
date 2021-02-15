# testing purposes commands

# Imports

import discord
from discord.ext import commands
import sys

try:
    # The insertion index should be 1 because index 0 is this file
    sys.path.insert(1, "../")  # the type of path is string
    # Import commands here
    import globals, logger
except (ModuleNotFoundError, ImportError) as e:
    print("{} failure".format(type(e)))
else:
    print("Import succeeded")

@commands.command()
async def nou(ctx):
    await ctx.send("no u")
    if globals.logging_enabled:
        await logger.log(ctx)
    pass

@commands.command()
async def ping(ctx):
    await ctx.send("pong!")
    if globals.logging_enabled:
        await logger.log(ctx)
    pass

@commands.command()
async def create_channel(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel("test1")
    if globals.logging_enabled:
        await logger.log(ctx)
    pass

