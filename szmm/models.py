from django.db import models


class GoodsType(models.Model):
    name: models.CharField = models.CharField(max_length=30)
    image_link: models.ImageField = models.ImageField(null=True, blank=True, upload_to="goods_types_images/")
    link: models.CharField = models.CharField(max_length=200)


class Pulsator(models.Model):
    name: models.CharField = models.CharField(max_length=30)
    image_link: models.ImageField = models.ImageField(null=True, blank=True, upload_to="pulsator_images/")
    description: models.CharField = models.CharField(max_length=200)
