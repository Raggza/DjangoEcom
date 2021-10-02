# Generated by Django 3.1.6 on 2021-02-14 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='types',
            field=models.CharField(blank=True, choices=[('Phim hành động', 'Phim hành động'), ('Phim hài hước', 'Phim hài hước'), ('Phim cổ trang', 'Phim cổ trang'), ('Phim viễn tưởng', 'Phim viễn tưởng'), ('Phim võ thuật', 'Phim võ thuật'), ('Phim kinh dị', 'Phim kinh dị'), ('Phim tâm lý', 'Phim tâm lý'), ('Phim gia đình', 'Phim gia đình'), ('Phim hoạt hình', 'Phim hoạt hình')], max_length=256, null=True),
        ),
    ]