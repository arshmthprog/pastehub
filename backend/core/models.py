from django.db import models

class Paste(models.Model):
    name = models.CharField(max_length=255)
    paste = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)