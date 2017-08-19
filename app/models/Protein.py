from app.models.util import *

class Protein(Model):
    PID = PrimaryKeyField()
    name = CharField(max_length = 200)
    price = IntegerField()
    