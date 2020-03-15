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
        sub = parser.add_subparsers(dest='sub_command', required=True)
        for name, command in cls.commands().items():
            sub.add_parser(name)
            command.setup(parser)

    @classmethod
    def run(cls, options):
        cls.commands()[options.sub_command].run(options)

class Command:
    @classmethod
    def run(self, options):
        pass
    @classmethod
    def setup(self, parser):
        pass