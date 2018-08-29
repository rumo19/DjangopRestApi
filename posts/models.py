from django.db import models

# Create your models here.
# posts/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    upload = models.FileField(upload_to='uploads/')
    date = models.DateField()


    def __str__(self):
        return self.title
