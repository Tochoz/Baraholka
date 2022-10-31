from django.conf import settings
from django.db.models import ForeignKey, Model, CharField, CASCADE

User = settings.AUTH_USER_MODEL

class Item(Model):
    user = ForeignKey(User, on_delete=CASCADE)
