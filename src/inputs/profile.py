from src.inputs.base import BaseCommands, Command
from src.models.profile import Profile

class ProfileCommands(BaseCommands):
    @classmethod
    def commands(cls, key=None):
        return {
            "list": ListProfiles,
            "create": CreateProfile,
        }

class ListProfiles(Command):
    @classmethod
    def setup(cls, parser):
        pass

    @classmethod
    def run(cls, options):
        print([p.name for p in Profile.select()])


class CreateProfile(Command):
    @classmethod
    def setup(cls, parser):
        parser.add_argument(
            "--name", 
            action="store",
            help="name of profile",
            required=True,
        )

    @classmethod
    def run(cls, options):
        pass