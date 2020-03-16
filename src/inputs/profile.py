from src.inputs.base import BaseCommands, Command
import src.controllers.profile as profile

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
    def run(cls, args):
        profiles = [p.name for p in profile.get_all()]
        if len(profiles) == 0:
            print("No profiles are currently stored on this machine")
        else:
            print("There are {} profiles in this machine".format(len(profiles)))
            for p in profiles:
                print("-".format(p.name))


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
    def run(cls, args):
        """
        Create a new profile
            - args.name - name of the profile
        Return 
        """