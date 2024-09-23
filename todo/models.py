from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
   
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10)
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False)
    def __str__(self):
        return self.title
