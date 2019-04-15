from app.models.util import *
from app.models.Offer import *
from app.models.User import *

class OfferPassenger(baseModel):
    OPID  = PrimaryKeyField()
    offer  = ForeignKeyField(Offer, null = False)
    passenger = ForeignKeyField(Rider, null = False)