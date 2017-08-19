from app.models.util import *

class Fruits(Model):
    FRID = PrimaryKeyField()
    name = CharField(max_length = 200)
    price = IntegerField()
    