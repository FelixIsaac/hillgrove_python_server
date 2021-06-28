from django.db import models

# Create your models here.


class User(models.Model):
    google_id = models.CharField(max_length=21, unique=True)
    avatar = models.CharField(max_length=43)
    email = models.EmailField(max_length=64, unique=True)
    name = models.CharField(max_length=254)
    first_name = models.CharField(max_length=254)
    family_name = models.CharField(max_length=254)
    created_on = models.DateTimeField()
    xp = models.PositiveIntegerField(default=100)

    def avatar_urL(self):
        return 'https://lh3.googleusercontent.com/a/{}=s96-'.format(self.avatar)

    def add_xp(self, xp, *args, **kwargs):
        self.xp += int(xp)
        super(User, self).save(*args, **kwargs)

    def update_avatar(self, avatar, *args, **kwargs):
        self.avatar = avatar
        super(User, self).save(*args, **kwargs)


# class Session(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=300)
