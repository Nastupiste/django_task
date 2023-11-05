from django.db import models

# Create your models here.


class task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)
