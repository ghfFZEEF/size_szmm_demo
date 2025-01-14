from django.db import models


class GoodsType(models.Model):
    links: tuple[tuple[str, ...], ...] = (
        ("pulsators", "Доильные аппараты"),
        ("grain_crushers", "Зернодробилки"),
        ("grass_choppers", "Измельчители травы"),
        ("pulsators_accessories", "Комплектующие для доильных аппаратов"),
        ("grain_crushers_accessories", "Комплектующие/запчасти для зернодробилок"),
        ("grass_choppers_accessories", "Запчасти для измельчителей травы"),
        ("cultivators_accessories", "Комплектующие для мотоблоков и культиваторов"),
        ("Tooth_harrow_couplings", "Сцепки зубовых борон"),
    )
    
    name: models.CharField = models.CharField(max_length=30)
    image: models.ImageField = models.ImageField(null=True, blank=True, upload_to="goods_types_images/")
    link: models.CharField = models.CharField(max_length=50, choices=links)


class Pulsator(models.Model):
    name: models.CharField = models.CharField(max_length=30)
    description: models.CharField = models.CharField(max_length=1000)
    image_1: models.ImageField = models.ImageField(null=True, blank=True, upload_to="pulsator_images/")
    image_2: models.ImageField = models.ImageField(null=True, blank=True, upload_to="pulsator_images/")
    image_3: models.ImageField = models.ImageField(null=True, blank=True, upload_to="pulsator_images/")
    image_4: models.ImageField = models.ImageField(null=True, blank=True, upload_to="pulsator_images/")
    image_5: models.ImageField = models.ImageField(null=True, blank=True, upload_to="pulsator_images/")


class GrainCrushers(models.Model):
    name: models.CharField = models.CharField(max_length=30)
    description: models.CharField = models.CharField(max_length=1000)
    image_1: models.ImageField = models.ImageField(null=True, blank=True, upload_to="grain_crushers_images/")
    image_2: models.ImageField = models.ImageField(null=True, blank=True, upload_to="grain_crushers_images/")
    image_3: models.ImageField = models.ImageField(null=True, blank=True, upload_to="grain_crushers_images/")
    image_4: models.ImageField = models.ImageField(null=True, blank=True, upload_to="grain_crushers_images/")
    image_5: models.ImageField = models.ImageField(null=True, blank=True, upload_to="grain_crushers_images/")


class GrassChoppers(models.Model):
    name: models.CharField = models.CharField(max_length=30)
    description: models.CharField = models.CharField(max_length=1000)
    image_1: models.ImageField = models.ImageField(null=True, blank=True, upload_to="grass_choppers_images/")
    image_2: models.ImageField = models.ImageField(null=True, blank=True, upload_to="grass_choppers_images/")
    image_3: models.ImageField = models.ImageField(null=True, blank=True, upload_to="grass_choppers_images/")
    image_4: models.ImageField = models.ImageField(null=True, blank=True, upload_to="grass_choppers_images/")
    image_5: models.ImageField = models.ImageField(null=True, blank=True, upload_to="grass_choppers_images/")


class QrCode(models.Model):
    image: models.ImageField = models.ImageField(null=True, blank=True, upload_to="qr_code")
    