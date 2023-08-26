from django.db import models
from django.contrib.auth.models import User

from utils.data import TOPICS


class Paper(models.Model):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to="blogs/")
    thumbnail = models.FileField(upload_to="thumbnails/")
    topic = models.CharField(max_length=100, choices=TOPICS)
    # price = modelsP.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    pages = models.IntegerField(default=1)
    slug = models.SlugField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author")
    subscribers = models.ManyToManyField(
        User, blank=True, related_name="subscribers")

    @property
    def get_price(self):
        return self.pages * 5

    def __str__(self):
        return self.title
