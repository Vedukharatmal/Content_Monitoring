from django.db import models

class Keyword(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class ContentItem(models.Model):
    title = models.CharField(max_length=255)
    source = models.CharField(max_length=100)
    body = models.TextField()
    last_updated = models.DateTimeField()
    def __str__(self):
        return self.title

class Flag(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    content_item = models.ForeignKey(ContentItem, on_delete=models.CASCADE)
    score = models.IntegerField()
    
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        RELEVANT = 'relevant', 'Relevant'
        IRRELEVANT ='irrelevant', 'Irrelevant'

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    ) 

    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.keyword.name} - {self.content_item.title} ({self.status})"


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['keyword', 'content_item'],
                name='unique_keyword_content'
            )
        ]