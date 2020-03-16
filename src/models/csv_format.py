import datetime
from peewee import *

from src.models.base import *
from src.models.profile import *

class CSVFormat(BaseModel):
    description_field_name = TextField()
    value_field_name = TextField()
    type_field_name = TextField()
    account_id_field = TextField(null=True, default=None)

    
db.create_tables([CsvFormat])

    
