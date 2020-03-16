from src.inputs.base import BaseCommands, Command

class AccountCommands(BaseCommands):

    @classmethod
    def commands(cls, key=None):
        return {
            "list": ListAccounts
        }


class ListAccounts(Command):
    @classmethod
    def setup(cls, parser):
        parser.add_argument(
            "--profile_name", 
            "--profile-name",
            "--profile", 
            "-p",
            help="name of the profile to list accounts for",
            required=True,
        )
    
    @classmethod
    def run(cls, options):
        print(options)
    
    