from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150, blank=True)
    score = models.IntegerField(blank=True)
    approval = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score', 'date_added']

    def __str__(self):
        return self.name

    def get_score(self):
        if self.score:
            return self.score
        else:
            return None

    def get_location(self):
        if self.location:
            return self.location
        else:
            return None
