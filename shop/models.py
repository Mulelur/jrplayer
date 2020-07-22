from django.db import models
from PIL import Image
from django.utils.safestring import mark_safe


class Shop(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(max_length=1000, upload_to='shop-images')
    price = models.IntegerField()
    descirption = models.TextField()
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    def save(self):
        super().save()

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
