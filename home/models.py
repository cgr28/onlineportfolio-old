from django.db import models

# Create your models here.
class Skills(models.Model):
    name = models.CharField(default="skill", max_length=25)
    proficiency = models.PositiveSmallIntegerField(default=3)

