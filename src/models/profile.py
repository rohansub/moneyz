import datetime
from peewee import *

from src.models.base import *

class Profile(BaseModel):
    name = TextField(unique=True)


db.create_tables([Profile])

    
    

