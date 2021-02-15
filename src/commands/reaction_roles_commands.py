# Reaction Roles related commands

# Imports

import discord
from discord.ext import commands
import sys, json, os

try:
    # The insertion index should be 1 because index 0 is this file
    sys.path.insert(1, "../")  # the type of path is string
    # Import commands here
    import globals
except (ModuleNotFoundError, ImportError) as e:
    print("{} failure".format(type(e)))
else:
    print("Import succeeded")

with open(globals.config_path, "rb") as config_file:
    config = json.load(config_file)

output_folder = config["database_folder_path"]

if not os.path.exists(output_folder + "/reaction_roles.json"):
    with open(output_folder + "/reaction_roles.json", 'w'): pass