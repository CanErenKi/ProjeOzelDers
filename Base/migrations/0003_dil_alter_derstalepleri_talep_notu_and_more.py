# Generated by Django 5.0.3 on 2024-05-04 15:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_derstalepleri_isim'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dil', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='derstalepleri',
            name='talep_notu',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='VerilebilecekDersler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ucret', models.IntegerField()),
                ('ders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.ders')),
                ('ders_dili', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.dil')),
                ('egitmen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]