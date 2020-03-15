#!/usr/bin/env python
import argparse

from src.inputs.profile import ProfileCommands
from src.inputs.account import AccountCommands

COMMANDS = {
    "test": None,
    "profiles":  ProfileCommands,
    "accounts":  AccountCommands,
    "transactions": None,
}

# Setup argument parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')
subparsers.required = True

for name, Commands in COMMANDS.items():
    sub = subparsers.add_parser(name)
    if Commands is not None:
        Commands.setup_commands(sub)


if __name__ == "__main__":
    args = parser.parse_args()
    COMMANDS[args.command].run(args)


