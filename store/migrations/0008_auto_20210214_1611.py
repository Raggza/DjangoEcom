# Generated by Django 3.1.6 on 2021-02-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210214_1125'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, choices=[('Phim hành động', 'Phim hành động'), ('Phim hài hước', 'Phim hài hước'), ('Phim võ thuật', 'Phim võ thuật'), ('Phim kinh dị', 'Phim kinh dị'), ('Phim tâm lý', 'Phim tâm lý'), ('Phim gia đình', 'Phim gia đình'), ('Phim hoạt hình', 'Phim hoạt hình')], max_length=256, null=True),
        ),
    ]
