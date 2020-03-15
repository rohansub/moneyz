from peewee import *

from src.models.base import *
from src.models.profile import *

class Account(BaseModel):
    name = TextField(unique=True)
    description = TextField(default="")
    profile = ForeignKeyField(Profile, backref='accounts')
    
db.create_tables([Account])

