from django.db import models


# Create your models here.

class Goal(models.Model):
    title = models.CharField(max_length=140, blank=True)
    description = models.TextField(max_length=140)
    isDone = models.BooleanField()
    onDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return ("DONE-" if self.isDone else "") + (self.description if self.title == "" else self.title)
