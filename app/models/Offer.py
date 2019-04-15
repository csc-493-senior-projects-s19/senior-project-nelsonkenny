from app.models.util import *
from app.models.Driver import *
from app.models.Rider import *
from app.models.Form import *


class Offer(baseModel):
    OID           = PrimaryKeyField()
    driver_id        = ForeignKeyField(Driver, null = False)
    form_id          = ForeignKeyField(Form, null = False)
    num_passenger = IntegerField(null = False)

    