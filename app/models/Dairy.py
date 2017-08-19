from app.models.util import *

class Dairy(Model):
    DID = PrimaryKeyField()
    name = CharField(max_length = 200)
    price = IntegerField()
    
    