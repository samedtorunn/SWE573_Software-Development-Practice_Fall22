# Generated by Django 4.1.2 on 2022-12-26 15:20
from django.contrib.auth.hashers import make_password
from django.db import migrations, models

def populate_data(apps, schema_editor):
    UserProfile = apps.get_model('application', 'UserProfile')
    Post = apps.get_model('application', 'Post')
    Space = apps.get_model('application', 'Space')
    User = apps.get_model('auth', 'User')

    alice_profile = UserProfile.objects.create(
        user=User.objects.create(
            username = "alice",
            first_name= "alice",
            last_name= "barker",
            email= "alice@gmail.com",
            password= make_password("123456"),
        )
    )
    samed_profile = UserProfile.objects.create(
        user=User.objects.create(
            username = "samed",
            first_name= "samed",
            last_name= "torun",
            email= "samed@gmail.com",
            password= make_password("123456"),
        )
    )
    john_profile = UserProfile.objects.create(
        user=User.objects.create(
            username = "johndoe",
            first_name= "John",
            last_name= "Doe",
            email= "johndoe@gmail.com",
            password= make_password("123456"),
        )
    )

    Post.objects.create(
        title="What is the best use of ai",
        content="Artificial intelligence (AI) can be used in a variety of ways and has the potential to be very useful in many different fields. Some of the best uses of AI include: Automating tasks and processes: AI can be used to automate repetitive tasks, freeing up time for people to focus on more important work.",
        link="https://lorem.ipsum",
        author=alice_profile,
        slug="this-is-a-post",

    )

    Post.objects.create(
        title="Freelancer Platforms",
        content="Freelance platforms are online marketplaces that connect clients with freelancers for a variety of projects. These platforms typically allow clients to post job listings, and freelancers can browse and apply for jobs that match their skills and expertise. Some common types of projects that are",
        link="https://lorem.ipsum",
        author=samed_profile,
        slug="samed-evleniyor",
    )

    tech_space = Space.objects.create(
        admin=samed_profile,
        title="Technology",
        slug="technology"
    )
    tech_space.members.add(samed_profile)
    tech_space.members.add(alice_profile)

    Post.objects.create(
        title="Samed founds Othersapp",
        content="this is a tech company",
        link="https://lorem.ipsum",
        author=samed_profile,
        slug="samed-ffounds-othersapp",
        space=tech_space
    )

class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_space_slug'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(populate_data),
    ]