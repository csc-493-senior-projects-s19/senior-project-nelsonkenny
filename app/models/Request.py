from app.models.util import *
from app.models.Driver import *
from app.models.Rider import *
from app.models.Form import *

class Request(baseModel):
    REID   = PrimaryKeyField()
    driver = ForeignKeyField(Driver, null = True, related_name ='request_rider')
    rider  = ForeignKeyField(Rider, null = False, related_name = 'request_driver')
    form   = ForeignKeyField(Form, null = False)
    status = BooleanField()
    
    
    