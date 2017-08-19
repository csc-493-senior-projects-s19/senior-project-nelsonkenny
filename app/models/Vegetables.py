from app.models.util import *

class Vegtables(Model):
    VID = PrimaryKeyField()
    name = CharField(max_length = 200)
    price = IntegerField()
    