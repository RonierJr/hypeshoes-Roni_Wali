# Generated by Django 4.2.3 on 2023-11-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0006_alter_tenis_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenis',
            name='valor',
            field=models.FloatField(),
        ),
    ]
