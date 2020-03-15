import datetime
import re

from peewee import *

# TODO: fix the path
db = SqliteDatabase('data/moneyz.db')


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = db

