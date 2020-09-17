from django.db import models
from PIL import Image
from django.utils.safestring import mark_safe


class Shop(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(max_length=1000, upload_to='shop-images')
    category = models.CharField(max_length=150, default='')
    price = models.IntegerField()
    descirption = models.TextField()
    slug = models.SlugField(blank=True)
    invetory = models.IntegerField(default=0)
    # sku = models.CharField(max_length=15, blank=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 912 or img.width > 926:
            output_size = (912, 926)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def image_tag(self):
        img = Shop.objects.get(image=self.image)
        if img.id is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))  
        else:     
            return ""        

class ColorVarient(models.Model):
    product = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='color')
    color = models.CharField(max_length=8)

    def get_color(self):
        c = ColorVarient.objects.get(color=self.color)
        if c.id is not None:
            return mark_safe('<div class="{}"></div>'.format(c.color))
        else:
            return ""

    def __str__(self):
        return self.color

class SizeVarient(models.Model):
    SIZE = (
        ('xxs','xxs'),
        ('xs','xs'),
        ('s','s'),
        ('m','m'),
        ('l','l'),
        ('xl','xl'),
        ('xxl','xxl'),
        ('all', 'all')
    )
    product = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='size')
    size = models.CharField(max_length=120, choices=SIZE)

    def __str__(self):
        return ('size: {} - product: {}'.format(self.size, self.product.title))

