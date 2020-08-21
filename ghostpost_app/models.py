from django.db import models
from django.utils import timezone


class Post(models.Model):
  isBoast = models.BooleanField()
  body = models.CharField(max_length=280)
  upVotes = models.IntegerField()
  downVotes = models.IntegerField()
  postDate = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.content

# Matt Perry helped me with this
  @property
  def total(self):
    return self.upVotes - self.downVotes
