from django.db import models
from authentication.models import User
import session.models as session

# Create your models here.
class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_session = models.ForeignKey(session.Session, on_delete=models.CASCADE)
    last_topic = models.ForeignKey(session.Topic, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'last_session')