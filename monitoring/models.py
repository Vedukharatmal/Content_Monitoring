from django.db import models

class Keyword(models.Model):
    name = models.CharField(max_length=255)

class ContentItem(models.Model):
    title = models.CharField(max_length=255)
    source = models.TextField()
    body = models.TextField()
    last_updated = models.DateTimeField()

class Flag(models.Model):
    keyword = Keyword
    content_item = ContentItem
    score = models.IntegerField
    status = models.TextChoices{

    }


