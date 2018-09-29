from django.db import models
from apps.topics.models import Topics

# Create your models here.
class News(models.Model):
    STATUS_NEWS = (
        ('draft', 'Draft'),
        ('publish', 'Publish'),
        ('deleted', 'Deleted')
    )

    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_NEWS, default='draft')
    topics = models.ManyToManyField(Topics)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title