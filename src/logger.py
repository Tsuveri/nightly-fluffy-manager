# Command logging utility


# Imports

import discord
from discord.ext import commands
import random, json, sys, os

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