# Generated by Django 5.0 on 2024-04-20 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumo', '0002_alter_resumo_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumo',
            name='sexo',
            field=models.CharField(choices=[('FEMININO', 'Feminino'), ('MASCULINO', 'Masculino'), ('OUTRO', 'Outro')], default=' ', max_length=100),
        ),
    ]
