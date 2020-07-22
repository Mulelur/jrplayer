from django.db import models
from django.utils.safestring import mark_safe

class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='image-gallery')

    def __str__(self):
        return self.title

    def image_tag(self):
        img = Gallery.objects.get(image=self.image)
        if img.id is not None:
                return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))  
        else:     
            return ""   
