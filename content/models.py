from django.db import models
from datetime import datetime
# Create your models here.


class ImageContent(models.Model):
    url_image = models.URLField(null=True)

