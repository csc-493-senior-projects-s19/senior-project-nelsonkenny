from app.models.util import *
# from app.models.User import *
# from app.models.Form import *
# from app.models.Offer import *
# from app.models.OfferPassenger import *
# from app.models.Request import *
# from app.models.Rider import *
# from app.models. import *


DB = getDB()

class baseModel(Model):
  class Meta:
    database = DB

    
class Form(baseModel):
    FID         = PrimaryKeyField()
    destination = CharField(max_length = 200)
    origin      = CharField(max_length = 200)
    date        = CharField()
    time        = CharField()
    notes       = CharField(max_length = 1000)
    
class User(baseModel):
    UID      = PrimaryKeyField()
    username = CharField(max_length = 200)
    firstName = CharField(max_length=100)
    lastName = CharField(max_length=100)
    phone    = CharField(max_length=11)
    email    = CharField(max_length=100)
    password = CharField(max_length=100)

class Rider(baseModel):
    RID  = PrimaryKeyField()
    user = ForeignKeyField(User, null = False)

class Driver(baseModel):
    DID = PrimaryKeyField()
    user = ForeignKeyField(User, null = False)    


class Offer(baseModel):
    OID           = PrimaryKeyField()
    driver        = ForeignKeyField(Driver, null = False)
    form        = ForeignKeyField(Form, null = False)
    num_passenger = IntegerField(null = False)

class OfferPassenger(baseModel):
    OPID  = PrimaryKeyField()
    offer   = ForeignKeyField(Offer, null = False)
    passenger = ForeignKeyField(Rider, null = False)
    
class Request(baseModel):
    REID   = PrimaryKeyField()
    driver = ForeignKeyField(Driver, null = True, related_name ='request_rider')
    rider  = ForeignKeyField(Rider, null = False, related_name = 'request_driver')
    form   = ForeignKeyField(Form, null = False)
    status = BooleanField()

class Announcement(baseModel):
    AID     = PrimaryKeyField()
    author  = ForeignKeyField(User, null = True, related_name ='author')
    date    = CharField()
    time    = CharField()
    content = CharField()
    
class Message(baseModel):
    MID      = PrimaryKeyField()
    sender   = ForeignKeyField(User, null = False, related_name ='message_sender')
    receiver = ForeignKeyField(User, null = True, related_name = 'message_receiver')
    content  = CharField()
    date     = CharField()
    time     = CharField()    

DB.create_tables([Form, Offer, OfferPassenger, Request, User, Rider, Driver, Announcement, Message])

# migrate(
#     migrator.add_column("rooms", "lastModified", CharField(null = True))
#     )





