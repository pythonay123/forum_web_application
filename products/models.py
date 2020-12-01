from django.db import models
from PIL import Image
from django.shortcuts import reverse
import os


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=30, default=0.00)
    sale_price = models.DecimalField(decimal_places=2, max_digits=30, blank=True, null=True)
    # image = models.ImageField(upload_to='products/images/', null=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('title', 'slug')

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price

    def get_absolute_url(self):
        return reverse('single_product', args=[self.slug, ])
        # return '/product/{}/'.format(self.slug)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/', null=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        img_dir, img_name = os.path.split(self.image.path)
        return "{}=>{}".format(self.product.title, img_name)

    # Override the save method
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.width != 250 and img.height != 350:
            output_size = (250, 350)
            img.resize(output_size, Image.ANTIALIAS).save(self.image.path)


VAR_CATEGORIES = (
    ('size', 'size'),
    ('color', 'color'),
    ('package', 'package'),
)


class VariationManager(models.Manager):
    def all(self):
        return super(VariationManager, self).filter(active=True)

    def sizes(self):
        return self.all().filter(category='size')

    def colors(self):
        return self.all().filter(category='color')

    def packages(self):
        return self.all().filter(category='package')


class Variation(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
    image = models.ForeignKey(ProductImage, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    objects = VariationManager()

    def __str__(self):
        return self.title
