# Generated by Django 3.1.6 on 2021-02-16 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_product_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hd',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]