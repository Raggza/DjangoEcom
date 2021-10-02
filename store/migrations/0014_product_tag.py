# Generated by Django 3.1.6 on 2021-02-16 02:27

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210214_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tag',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Phim hành động', 'Phim hành động'), ('Phim hài hước', 'Phim hài hước'), ('Phim viễn tưởng', 'Phim viễn tưởng'), ('Phim kinh dị', 'Phim kinh dị'), ('Phim tâm lý', 'Phim tâm lý'), ('Phim gia đình', 'Phim gia đình'), ('Phim hoạt hình', 'Phim hoạt hình')], max_length=256, null=True),
        ),
    ]
