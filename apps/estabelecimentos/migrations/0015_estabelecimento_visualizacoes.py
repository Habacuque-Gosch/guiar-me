# Generated by Django 5.0 on 2024-08-28 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimentos', '0014_produto_usuario_business_prod'),
    ]

    operations = [
        migrations.AddField(
            model_name='estabelecimento',
            name='visualizacoes',
            field=models.IntegerField(blank=True, default=0.0, null=True),
        ),
    ]
