from django.db import models
from django.utils import timezone


class dumb_santa(models.Model):
    address = models.CharField(max_length=50)
    extends = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now
	)

    def register(self):
        self.save()

    def __str__(self):
        return self.address