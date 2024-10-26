from django.db import models

class GoodsTypes(models.Model):
    name: models.CharField = models.CharField(max_length=30)
    image: models.IntegerField = models.ImageField()
    link: models.CharField = models.CharField(max_length=200)
