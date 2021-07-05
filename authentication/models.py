from django.db import models
from mirage import fields


class User(models.Model):
    google_id = models.CharField(max_length=21, unique=True)
    avatar = models.CharField(max_length=254)
    email = fields.EncryptedEmailField(max_length=64, unique=True)
    name = models.CharField(max_length=254)
    first_name = models.CharField(max_length=254)
    family_name = models.CharField(max_length=254)
    created_on = models.DateTimeField(auto_now_add=True)
    xp = models.PositiveIntegerField(default=100)

    @property
    def add_xp(self, xp, *args, **kwargs):
        self.xp += int(xp)
        super(User, self).save(*args, **kwargs)

    @property
    def update_avatar(self, avatar, *args, **kwargs):
        self.avatar = avatar
        super(User, self).save(*args, **kwargs)
