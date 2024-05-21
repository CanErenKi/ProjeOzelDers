# Generated by Django 5.0.3 on 2024-05-15 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='kullanici_tipi',
            field=models.CharField(choices=[('ogretmen', 'Öğretmen'), ('ogrenci', 'Öğrenci')], default=False, max_length=50),
            preserve_default=False,
        ),
    ]
