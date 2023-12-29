# Generated by Django 4.2.3 on 2023-12-06 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_pedido_itempedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('em_processamento', 'Em Processamento'), ('concluido', 'Concluído')], default='pendente', max_length=20),
        ),
    ]