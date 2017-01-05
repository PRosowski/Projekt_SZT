from __future__ import unicode_literals

from django.db import models
import os
from tagging.fields import TagField
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce import models as tinymce_models


# def get_image_path(instance, filename):
#     return os.path.join('post', str(instance.id), filename)


class Category(models.Model):
    title = models.CharField(max_length=250, help_text='Maksymalnie 100 znakow')
    slug = models.SlugField(unique=True, help_text="Wartocd generowana z tytulu. Musi byc unikalna")
    description = models.TextField(help_text="Opis kategorii.")

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/kategorie/%s/" % self.slug


class Post(models.Model):
    STATUS_CHOICES = (
        (1, 'Live'),
        (2, 'Szkic'),
        (3, 'Ukryty'),
    )
    author = models.ForeignKey(User)
    title = models.CharField(max_length=250, help_text='Maksymalnie 250 znakow')
    excerpt = models.TextField(blank=True,
                               help_text='Krotkie podsumowanie. Opcjonalne')
    content = tinymce_models.HTMLField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    categories = models.ManyToManyField(Category)
    tags = TagField()
    #post_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.ForeignKey(User)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
