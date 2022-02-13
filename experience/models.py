from django.db import models

# Create your models here.
class Experience(models.Model):

    CHOICES = (
        ('pro', 'proffesional'),
        ('club', 'club'),
        ('education', 'education'),
    )

    title = models.CharField(default="No title", max_length=50, null=True)
    period = models.CharField(default="current", max_length=50, null=True)
    role = models.CharField(default=None, max_length=25, null=True)
    descr = models.TextField(default="No description", null=True)
    type = models.CharField(default="current", choices=CHOICES, max_length=25, null=True)
    img = models.FileField(upload_to="experience", default=None, null=True)