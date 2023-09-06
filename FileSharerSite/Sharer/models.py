from django.db import models

class SharedFile(models.Model):
    title = models.TextField(default='without title')
    date = models.DateField(auto_created=True, auto_now=True)
    text = models.TextField(default='without text')
    shared_file = models.FileField(upload_to='files/', blank=True)