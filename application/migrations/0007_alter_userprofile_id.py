# Generated by Django 4.1.2 on 2022-12-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_populate_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]