# Generated by Django 4.2.7 on 2023-11-22 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regiao',
            name='thumb',
            field=models.ImageField(upload_to='thumb_regioes'),
        ),
    ]