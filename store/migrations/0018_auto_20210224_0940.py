# Generated by Django 3.1.6 on 2021-02-24 02:40

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20210217_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fig',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Scale Figure'),
        ),
        migrations.AddField(
            model_name='product',
            name='nen',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Nendoroid'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Phim hành động', 'Phim hành động'), ('Phim hài hước', 'Phim hài hước'), ('Phim viễn tưởng', 'Phim viễn tưởng'), ('Phim kinh dị', 'Phim kinh dị'), ('Phim tâm lý', 'Phim tâm lý'), ('Phim gia đình', 'Phim gia đình'), ('Phim hoạt hình', 'Phim hoạt hình'), ('Scale Figure', 'Scale Figure'), ('Nendoroid', 'Nendoroid')], max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='type_text',
            field=models.CharField(blank=True, choices=[('Phim hành động', 'Phim hành động'), ('Phim hài hước', 'Phim hài hước'), ('Phim viễn tưởng', 'Phim viễn tưởng'), ('Phim kinh dị', 'Phim kinh dị'), ('Phim tâm lý', 'Phim tâm lý'), ('Phim gia đình', 'Phim gia đình'), ('Phim hoạt hình', 'Phim hoạt hình'), ('Scale Figure', 'Scale Figure'), ('Nendoroid', 'Nendoroid')], max_length=256, null=True),
        ),
    ]
