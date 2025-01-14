# Generated by Django 5.1.2 on 2024-11-02 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szmm', '0006_rename_image_link_goodstype_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrainCrushers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='grain_crushers_images/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='grain_crushers_images/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='grain_crushers_images/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='grain_crushers_images/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='grain_crushers_images/')),
            ],
        ),
        migrations.CreateModel(
            name='GrassChoppers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='grass_choppers_images/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='grass_choppers_images/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='grass_choppers_images/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='grass_choppers_images/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='grass_choppers_images/')),
            ],
        ),
        migrations.AlterField(
            model_name='goodstype',
            name='link',
            field=models.CharField(choices=[('pulsators', 'Доильные аппараты'), ('grain_crushers', 'Зернодробилки'), ('grass_choppers', 'Измельчители травы'), ('pulsators_accessories', 'Комплектующие для доильных аппаратов'), ('grain_crushers_accessories', 'Комплектующие/запчасти для зернодробилок'), ('grass_choppers_accessories', 'Запчасти для измельчителей травы'), ('cultivators_accessories', 'Комплектующие для мотоблоков и культиваторов'), ('Tooth_harrow_couplings', 'Сцепки зубовых борон')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pulsator',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
