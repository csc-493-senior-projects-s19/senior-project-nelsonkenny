from app.models.util import *

class Groceries(Model):
    GID = PrimaryKeyField()
    name = CharField(max_length = 200)
    price = IntegerField()
    