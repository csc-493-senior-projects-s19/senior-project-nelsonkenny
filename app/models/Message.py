from app.models.util import *
from app.models.Form import *
from app.models.Driver import *
from app.models.Rider import *

class Message(baseModel):
    MID      = PrimaryKeyField()
    sender   = ForeignKeyField(User, null = False, related_name ='message_sender')
    receiver = ForeignKeyField(User, null = True, related_name = 'message_receiver')
    content  = CharField()
    date     = CharField()
    time     = CharField()    
    