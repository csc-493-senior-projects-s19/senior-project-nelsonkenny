from app.models.util import *
from app.models.User import *

class Driver(baseModel):
    DID = PrimaryKeyField()
    user = ForeignKeyField(User, null = False) 