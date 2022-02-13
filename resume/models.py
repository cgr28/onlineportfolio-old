from django.db import models

# Create your models here.
class Resume(models.Model):
    resume = models.FileField(upload_to="resume", default=None)
    link = models.CharField(max_length = 150, default=None)