from django.db import models

class GoodsTypes(models.Model):
    name: models.CharField = models.CharField(max_length=30)
    image_link: models.CharField = models.CharField(max_length=200)
    link: models.CharField = models.CharField(max_length=200)
