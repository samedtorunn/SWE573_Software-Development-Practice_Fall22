# Generated by Django 4.1.2 on 2022-12-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_auto_20221227_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
