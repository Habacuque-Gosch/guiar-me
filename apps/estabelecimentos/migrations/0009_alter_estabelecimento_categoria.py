# Generated by Django 5.0 on 2024-06-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimentos', '0008_alter_estabelecimento_cep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='categoria',
            field=models.CharField(choices=[('Árabe', 'TESTE'), ('Brasileira', 'TESTE1'), ('Chinesa', 'TESTE2'), ('Italiana', 'TESTE2'), ('Fast Food', 'TESTE2'), ('Gourmet', 'TESTE2'), ('Japonesa', 'TESTE2'), ('Mexicana', 'TESTE2'), ('Vegetariana', 'TESTE2'), ('Vegana', 'TESTE2'), ('Pizza', 'TESTE2'), ('Sushi', 'TESTE2'), ('Frutos do mar', 'TESTE2'), ('Hambúrguer', 'TESTE2'), ('Massa', 'TESTE2'), ('Carne', 'TESTE2'), ('Peixe', 'TESTE2'), ('Sopa', 'TESTE2'), ('Salada', 'TESTE2'), ('Sobremesa', 'TESTE2')], default='', max_length=100),
        ),
    ]
