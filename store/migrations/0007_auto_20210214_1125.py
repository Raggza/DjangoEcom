# Generated by Django 3.1.6 on 2021-02-14 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20210214_1123'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Types',
            new_name='Type',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='types',
            new_name='type',
        ),
    ]