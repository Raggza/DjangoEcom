# Generated by Django 3.1.6 on 2021-02-14 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210208_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='types',
            field=models.CharField(blank=True, choices=[('green', 'green'), ('red', 'red')], max_length=256, null=True),
        ),
    ]