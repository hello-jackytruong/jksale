from django.db import models
import os
import uuid
from django.utils.text import slugify 


# Create your models here.

class ImageMedia(models.Model):
    image = models.ImageField(upload_to='', null=True, blank=True)

    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if self.title != None:
            slug = slugify(self.title)

            has_slug = ImageMedia.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = ImageMedia.objects.filter(slug=slug).exists()
            self.slug = slug
        
        super().save(*args, **kwargs)


