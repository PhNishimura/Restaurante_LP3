# Generated by Django 4.2.7 on 2023-11-25 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_regiao_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='regiao',
            name='macro_regiao',
            field=models.CharField(choices=[('América do Sul', 'AMERICA_SUL'), ('América do Norte', 'AMERICA_NORTE'), ('América Central', 'AMERICA_CENTRAL'), ('Ásia', 'ASIA'), ('África', 'AFRICA'), ('Arábia ', 'ARABIA'), ('Outros', 'OUTROS')], default='OUTROS', max_length=30),
        ),
    ]