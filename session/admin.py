from django.contrib import admin

# Register your models here.
from .models import Session, Topic

admin.site.register(Session)
admin.site.register(Topic)
