from django.db import models
from django.contrib.auth.models import User
from utils import data


class HelpRequest(models.Model):
    paper_type = models.CharField(max_length=100, choices=data.PAPER_TYPE)
    study_level = models.CharField(max_length=100, choices=data.STUDY_LEVEL)
    pages = models.IntegerField()
    price = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    days = models.IntegerField()
    description = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="client")

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.client.username} ({self.date.strftime('%c')})"
