# Generated by Django 4.1.2 on 2022-12-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_comment_author_post_bookmarkers_post_likers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
