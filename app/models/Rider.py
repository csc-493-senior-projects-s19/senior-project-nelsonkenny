from app.models.util import *
from app.models.User import *


class Rider(baseModel):
    RID  = PrimaryKeyField()
    user = ForeignKeyField(User, null = False)