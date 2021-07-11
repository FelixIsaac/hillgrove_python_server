from django.db import models
import re


class Topic(models.Model):
    name = models.CharField(max_length=64, unique=True)
    session = models.ForeignKey('session.Session', on_delete=models.CASCADE)

    @property
    def url(self):
        return re.sub(r'[\W_]+', '-', self.name).lower()


class Session(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=254, unique=True)
    topics = models.ManyToManyField('session.Topic', related_name='session_topics')
    enabled = models.BooleanField(default=False)

    @property
    def url(self):
        return re.sub(r'[\W_]+', '-', self.name).lower()

class Solution(models.Model):
    name = models.CharField(max_length=64, unique=True)
    topic = models.ForeignKey('session.Topic', on_delete=models.CASCADE)
    solution = models.TextField()
