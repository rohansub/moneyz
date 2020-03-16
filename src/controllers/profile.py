from src.models.profile import Profile



def get_all():
    """
    Retrieve all profile objects
    """
    return [p for p in Profile.select()]


def create(name: str):
    """
    Create a new profile
    """
    return Profile.create(
        name=name
    )