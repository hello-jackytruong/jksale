from django.db import models
from mptt.managers import TreeManager
from mptt.models import MPTTModel
from django.utils.text import slugify

# Create your models here.

class Category(MPTTModel):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    objects = models.Manager()
    tree = TreeManager()


class ProductAttribute(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=100)

class ProductType(models.Model):
    name = models.CharField(max_length=128)
    has_variants = models.BooleanField(default=True)

class Product(models.Model):
    product_type = models.ForeignKey(ProductType, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='product/', null=True, blank=True, default="/user.png")
    description = models.TextField()
    post_excerpt = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.FloatField()
    available_on = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    # attributes = HStoreField(default={})
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(
        unique=True,
        db_index=True,
        blank=True,
        default=None,
        max_length=255,
        null=True,
    )

    # objects = ProductQuerySet.as_manager()
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == None:

            slug = slugify(self.name)

            has_slug = Product.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.name) + '-' + str(count)
                has_slug = Product.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)
    
    
    

    # def save(self, *args, **kwargs):

	# 	if self.slug==None:
	# 		slug = slugify(self.name)

	# 		has_slug = Product.objects.filter(slug=slug).exists()
	# 		count = 1
	# 		while has_slug:
	# 			count += 1
	# 			slug = slugify(self.name) + '-' + str(count) 
	# 			has_slug = Product.objects.filter(slug=slug).exists()

	# 		self.slug = slug

	# 	super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    # ppoi = PPOIField()
    alt = models.CharField(max_length=128, blank=True)
    # order = models.PositiveIntegerField(editable=False)