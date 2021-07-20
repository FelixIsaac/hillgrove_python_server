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


# class SeenSolutions(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     solution = models.ForeignKey(session.Solution, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('user', 'solution')

class SolutionProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    solution = models.ForeignKey(session.Solution, on_delete=models.CASCADE)
    attempts = models.IntegerField(default=0)
    shown_hint = models.BooleanField(default=False)
    shown_solution = models.BooleanField(default=False)
    solution_code = models.TextField()
    draft_code = models.TextField()

    class Meta:
        unique_together = ('user', 'solution')
