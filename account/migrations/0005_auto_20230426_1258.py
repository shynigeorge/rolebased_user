# Generated by Django 3.2.18 on 2023-04-26 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_doctor',
            field=models.BooleanField(default=False, verbose_name='Is doctor'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_patient',
            field=models.BooleanField(default=False, verbose_name='Is patient'),
        ),
    ]
