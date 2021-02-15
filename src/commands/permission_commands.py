# Permissions commands

# Imports

import discord
from discord.ext import commands
import sys, json, os

try:
    # The insertion index should be 1 because index 0 is this file
    sys.path.insert(1, "../")  # the type of path is string
    # Import commands here
    import globals, logger
except (ModuleNotFoundError, ImportError) as e:
    print("{} failure".format(type(e)))
else:
    print("Imports succeeded")

with open(globals.config_path, "rb") as config_file:
    config = json.load(config_file)

output_folder = config["database_folder_path"]

if not os.path.exists(output_folder + "/permissions.json"):
    with open(output_folder + "/permissions.json", 'w'): pass
    pass

if globals.permissions_default_type == "Whitelist":
    perms = "Whitelist"
    pass
elif globals.permissions_default_type == "Blacklist":
    perms = "Blacklist"
    print("blacklist is currently unsupported")
    exit()
    pass
else:
    print("Permissions not properly specified, check globals.py")
    exit()

async def perms_set(role_id, command, allow_or_deny):
    with open(output_folder + "/permissions.json", "rb") as perms_file:
        data = json.load(perms_file)
    
    data[str(role_id)][str(command)] = str(allow_or_deny)

    with open(output_folder + "/permissions.json", "wb") as perms_file:
        json.dump(data, perms_file)


async def perms_get(role_id):
    with open(output_folder + "/permissions.json", "rb") as perms_file:
        data = json.load(perms_file)
    return data[str(role_id)]

async def perms_isAllowed(ctx):
    guild_roles = []
    author = ctx.author
    command = ctx.command
    for role in ctx.guild.roles:
        for member in role.members:
            if member.id == author.id:
                guild_roles.append(role)
    for role in guild_roles:
        commands_for_role = await perms_get(role.id)
        for command_name, command_value in commands_for_role.items():
            if command_name == command.name:
                if command_value == "True":
                    return True
    return False
    

async def perms_canExec(ctx):
    if perms == "Whilelist":
        if ctx.author.id == ctx.guild.owner.id or await perms_isAllowed(ctx):
            return True
    elif perms == "Blacklist":
        print("blacklist is currently unsupported")
        exit()


@commands.command()
async def permissions(ctx, action, role_id, command, allow_or_deny):
    if await perms_canExec(ctx):
        if action == "set":
            perms_set(role_id, command, allow_or_deny)
        elif action == "get":
            ctx.send(perms_get(role_id))





