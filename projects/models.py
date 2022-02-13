from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(default="No title", max_length=25, null=True)
    short_descr = models.TextField(default="No description", null=True)
    long_descr = models.TextField(default="No description", null=True)
    link = models.CharField(max_length = 100, null=True)
    link_name = models.CharField(max_length = 50, null=True)
    img = models.FileField(upload_to="projects", default=None, null=True)
    langs_used = models.TextField(default="None", null=True)
