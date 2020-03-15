from src.inputs.base import BaseCommands, Command

class ProfileCommands(BaseCommands):
    @classmethod
    def commands(cls, key=None):
        return {
            "list": ListProfiles
        }

class ListProfiles(Command):
    @classmethod
    def setup(cls, parser):
        pass

    @classmethod
    def run(cls, options):
        print(options)