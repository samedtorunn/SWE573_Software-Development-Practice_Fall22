from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(default="", null=False, blank=True, db_index=True)


    def get_absolute_url(self):
        return reverse("postDetailUrl", args=[self.slug])

    def __str__(self):
        return f"{self.title}  {self.author}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)