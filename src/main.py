# Nightly fluffy manager main file
# File purpose:
#   - Load the config specified in the config_path variable
#   - Run the bot
# Details:
#   - Try to keep code to a minimum in this file

# Imports
import discord
from discord.ext import commands
import random, json, sys


try:
    # The insertion index should be 1 because index 0 is this file
    sys.path.insert(1, "./commands/")  # the type of path is string
    # Import commands here
    import test_commands
except (ModuleNotFoundError, ImportError) as e:
    print("{} failure".format(type(e)))
else:
    print("Import succeeded")


# Variables

# Config must be a json file
config_path = ""


# Exec
with open(config_path, "rb") as config_file:
    config = json.load(config_file)

nightly_fluffy_manager = commands.Bot(command_prefix=config["command_prefix"], description=config["description"], intents=config["intents"])

nightly_fluffy_manager.add_command(test_commands.nou)
nightly_fluffy_manager.add_command(test_commands.ping)

nightly_fluffy_manager.run(config["token"])