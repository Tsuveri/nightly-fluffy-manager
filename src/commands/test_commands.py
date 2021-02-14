# testing purposes commands

# Imports

import discord
from discord.ext import commands


@commands.command()
async def nou(ctx):
    await ctx.send("no u")
    pass

@commands.command()
async def ping(ctx):
    await ctx.send("pong!")
    pass

@commands.command()
async def create_channel(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel("test1")
