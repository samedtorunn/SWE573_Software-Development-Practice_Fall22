# Generated by Django 4.1.2 on 2022-12-27 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_alter_userprofile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
