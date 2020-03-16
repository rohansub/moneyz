from abc import ABC, abstractmethod

class BaseCommands:
    def __init__(self, parser):
        self.parser = parser
        self.setup_commands()
    
    @classmethod
    def commands(cls, key=None):
        pass

    @classmethod
    def setup_commands(cls, parser):
        subparsers = parser.add_subparsers(dest='sub_command', required=True)
        for name, command in cls.commands().items():
            sub = subparsers.add_parser(name)
            command.setup(sub)

    @classmethod
    def run(cls, options):
        cls.commands()[options.sub_command].run(options)

class Command:
    @classmethod
    def run(cls, options):
        pass
    @classmethod
    def setup(cls, parser):
        pass