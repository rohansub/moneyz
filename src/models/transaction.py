import datetime
from peewee import *

from src.models.base import *
from src.models.account import *


class Transaction(BaseModel):
    transaction_id = TextField(unique=True, null=True, default=None)
    account_transaction_id = TextField(unique=True, null=True, default=None)
    transaction_date = DateTimeField(default=datetime.datetime.now)
    value = DoubleField()
    category = TextField()
    description = TextField()
    account = ForeignKeyField(Account, backref='transactions')


db.create_tables([Transaction])
