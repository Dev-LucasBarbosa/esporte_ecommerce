# Generated by Django 5.1.5 on 2025-02-15 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, help_text='Indica se o email do usuário foi verificado.'),
        ),
    ]
