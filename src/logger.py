# Command logging utility


# Imports

import discord
from discord.ext import commands
import random, json, sys, os
from datetime import datetime

try:
    import globals
except (ModuleNotFoundError, ImportError) as e:
    print("{} failure".format(type(e)))
else:
    print("Import succeeded")


with open(globals.config_path, "rb") as config_file:
    config = json.load(config_file)

output_folder = config["database_folder_path"]

if not os.path.exists(output_folder + "/command_logs.txt"):
    with open(output_folder + "/command_logs.txt", 'w'): pass
    pass

async def log(ctx, *args):
    with open(output_folder + "/command_logs.txt", 'a') as log_file:
        log_file.write("[" + datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + "] - " + str(ctx.author.name) + " (" + str(ctx.author.id) + ") executed command: {" + str(ctx.command.name) + "} with the following arguments:{0} | Raw message content:{1}".format(locals()["args"], str(ctx.message.content)))
    pass

