from django.db import models


class LikeCounter(models.Model):
    likes = models.IntegerField(default=0)
