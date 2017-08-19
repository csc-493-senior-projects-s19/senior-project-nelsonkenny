from app.models.util import *
from app.models.User import *
from app.models.Preferences import*

class Form(Model):
    FID = PrimaryKeyField()
    user = ForeignKeyField(User)
    money = IntegerField()
    duration = IntegerField(null = True)
    preference = ForeignKeyField(Preferences)
    