from django.db import models

class Comments(models.Model):
    post_id=models.IntegerField()
    text=models.TextField(max_length=1000)
