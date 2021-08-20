from django.db import models
import uuid
from django.urls import reverse
from django.utils.text import slugify 
# Create your models here.

TYPE_POST_STATUS_CHOICES = [
    ('publish', 'Publish'),
    ('trash', 'Trash'),
    ('inherit', 'Inherit'),
    ('auto-draft', 'Auto Draft'),
]

class Posts(models.Model):
    post_title =  models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='post/',
        null=True, blank=True, default="default.jpg")
    post_name = models.CharField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)
    post_content = models.TextField(null=True, blank=True)
    post_excerpt = models.TextField(null=True, blank=True)
    post_status = models.CharField(max_length=20,
        choices=TYPE_POST_STATUS_CHOICES)
    slug = models.SlugField(
        unique=True,
        db_index=True,
        blank=True,
        default=None,
        max_length=255,
        null=True,
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk })
    
    def save(self, *args, **kwargs):
        if self.slug == None:

            slug = slugify(self.post_title)

            has_slug = Posts.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.post_title) + '-' + str(count)
                has_slug = Posts.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)

class CategoryPost(models.Model):
    name = models.CharField(max_length=200)
    slug= models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='post/category/', null=True, blank=True)
    category_parent = models.CharField(max_length=200, default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

class Tags(models.Model):
    name = models.CharField(max_length=200)
    slug= models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

class Comments(models.Model):
    name = models.CharField(max_length=200)
    slug= models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)