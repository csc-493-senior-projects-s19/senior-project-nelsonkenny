from app.models.util import *

class User(baseModel):
    UID      = PrimaryKeyField()
    username = CharField(max_length = 200)
    firstName = CharField(max_length=100)
    lastName = CharField(max_length=100)
    phone    = CharField(max_length=11)
    email    = CharField(max_length=100)
    password = CharField(max_length=100)
    