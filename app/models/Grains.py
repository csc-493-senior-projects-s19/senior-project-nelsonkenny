from app.models.util import *

class Grains(Model):
    GRID = PrimaryKeyField()
    name = CharField(max_length = 200)
    price = IntegerField()
    