from datetime import timezone

from django.db import models

# Create your models here.
# menu/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Menu.Status.PUBLISHED)

class Menu(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    author = models.ForeignKey(User, models.CASCADE, 'menu_posts', null=True)
    price = models.FloatField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=Status.choices, default=Status.DRAFT, max_length=2)

    object = models.Manager()
    published_all = PublishedManager()
    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published'])
        ]

    def __str__(self):
        return self.name