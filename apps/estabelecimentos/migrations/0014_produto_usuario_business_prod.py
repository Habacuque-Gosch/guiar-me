# Generated by Django 5.0 on 2024-08-28 00:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimentos', '0013_rename_produtos_produto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='usuario_business_prod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_business_prod', to=settings.AUTH_USER_MODEL),
        ),
    ]
