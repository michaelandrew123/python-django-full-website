from django.db import models
from django.conf import settings
# Create your models here.

CATEGORY = [
    ("Inspirational", "Inspirational"),
    ("Motivational", "Motivational"),
    ("Life", "Life"),
    ("Friendship", "Friendship"),
    ("Funny", "Funny"),
    ("Happiness", "Happiness"),
    ("Love", "Love"),
    ("Success", "Success"),
    ("Thoughtful", "Thoughtful"),
    ("Wisdom", "Wisdom")   
]

class Qoutes(models.Model):
    title               = models.CharField(max_length=100, null=False, blank=False)
    description         = models.TextField(max_length=5000, null=False, blank=False)
    category            = models.CharField(max_length=30, choices=CATEGORY)
    author              = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Quotes"
        verbose_name_plural = "People Quotes"
