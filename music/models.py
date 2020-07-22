from django.db import models



class  Music(models.Model):
    TYPE = (
        ('SINGLE','SINGLE'),
        ('Featured','Featured')
    )
    title = models.CharField(max_length=500)
    music = models.FileField(upload_to='music', max_length=500)
    thumbnail = models.ImageField(upload_to='music_image', max_length=500)
    type = models.CharField(choices=TYPE, max_length=50)

    def __str__(self):
        return self.title