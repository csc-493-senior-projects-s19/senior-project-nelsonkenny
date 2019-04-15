from app.models.util import *
from app.models.User import *

class Announcement(baseModel):
    AID     = PrimaryKeyField()
    author  = ForeignKeyField(User, null = True, related_name ='author')
    date    = CharField()
    time    = CharField()
    content = CharField()
    