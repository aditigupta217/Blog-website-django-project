from django.db import models

# Create your models here.

class category(models.Model):
    category_name = models.CharField(max_length=50 , unique=True)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)