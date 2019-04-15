from app.models.util import *

class Form(baseModel):
    FID         = PrimaryKeyField()
    destination = CharField(max_length = 200)
    origin      = CharField(max_length = 200)
    date        = CharField()
    time        = CharField()
    notes       = CharField(max_length = 1000)