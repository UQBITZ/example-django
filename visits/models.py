from django.db import models


class Visit(models.Model):
    at = models.DateTimeField(auto_now_add=True)
