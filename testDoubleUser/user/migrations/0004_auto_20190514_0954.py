# Generated by Django 2.2 on 2019-05-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190514_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreprise',
            name='numero_departement',
            field=models.IntegerField(null=True),
        ),
    ]