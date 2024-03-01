from django.db import models
from datetime import datetime
# Create your models here.


class ImageContent(models.Model):
    image_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    url_image = models.URLField(null=True)

    def __str__(self):
        return self.title
    
class Article(models.Model):
    image = models.ForeignKey(ImageContent, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    article_shapo = models.TextField()
    content = models.TextField()
    data_plush = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title