# Generated by Django 3.1.6 on 2021-02-16 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_product_hd'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ani',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Phim hoạt hình'),
        ),
        migrations.AddField(
            model_name='product',
            name='gd',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Phim gia đình'),
        ),
        migrations.AddField(
            model_name='product',
            name='hh',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Phim hài hước'),
        ),
        migrations.AddField(
            model_name='product',
            name='kd',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Phim kinh dị'),
        ),
        migrations.AddField(
            model_name='product',
            name='tl',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Phim tâm lý'),
        ),
        migrations.AddField(
            model_name='product',
            name='vt',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Phim viễn tưởng'),
        ),
        migrations.AlterField(
            model_name='product',
            name='hd',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Phim hành động'),
        ),
    ]
