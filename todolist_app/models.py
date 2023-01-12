from django.db import models
from django.contrib.auth.models import User


class TaskList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task + " - " + str(self.done)
