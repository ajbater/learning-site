from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=225)
    description = models.TextField()
