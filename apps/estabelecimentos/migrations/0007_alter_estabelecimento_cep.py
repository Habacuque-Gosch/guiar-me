# Generated by Django 5.0 on 2024-05-29 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimentos', '0006_estabelecimento_cep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='cep',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
