from django.db import models
from django.utils.safestring import mark_safe

from ckeditor_uploader.fields import RichTextUploadingField

class Event(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField()
    theme = models.CharField(max_length=500)
    venue = models.CharField(max_length=500)
    image = models.ImageField(max_length=1000, upload_to='event-images')
    artists = models.TextField()
    about_event = models.TextField()
    slug = models.SlugField(blank=True)


    def __str__(self):
        return self.title
class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()        

    def __str__(self):
        return self.title

class Album(models.Model):
    artist = models.CharField(max_length=1000)
    image = models.ImageField(max_length=1000, upload_to='album-images')
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=1000)
    released_date = models.DateField()
    label = models.CharField(max_length=100, blank=True)
    links = models.ForeignKey(Link, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=1000)
    song = models.FileField(upload_to='songs')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    artist = models.CharField(max_length=100, blank=True, default='Unknown')

    def __str__(self):
        return self.title

class Reply(models.Model):
    name = models.CharField(max_length=100)
    tetx = RichTextUploadingField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    text = models.TextField()
    date = models.DateField(blank=True, auto_now=True)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class New(models.Model):
    title = models.CharField(max_length=1000)
    image = models.ImageField(max_length=1000, upload_to='news-images')
    text = RichTextUploadingField()  
    date =  models.DateField(blank=True) 
    slug = models.SlugField(blank=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    website = models.URLField(blank=True)
    message = models.TextField()    

    def __str__(self):
        return self.name

class About(models.Model):
    icon = models.ImageField(upload_to='icons')
    url = models.URLField()

    def image_tag(self):
        img = About.objects.get(icon=self.icon)
        if img.id is not None:
                return mark_safe('<img src="{}" height="50"/>'.format(img.icon.url))  
        else:     
            return ""            

class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners')

    def __str__(self):
        return self.title            