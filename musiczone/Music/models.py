from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    genrename = models.CharField(max_length=255)
    
    def __str__(self):
        return self.genrename
    
    class Meta:
        db_table='genre'
        verbose_name_plural='genre'

class Artist(models.Model):
    name = models.CharField(max_length=255)
    born = models.DateField()
    url = models.URLField(null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='artist'
        verbose_name_plural='artist'


class Album(models.Model):
    albumtitle = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist,on_delete=models.DO_NOTHING)
    releasedate = models.DateField()
    

    def __str__(self):
        return self.albumtitle
    
    class Meta:
        db_table='album'
        verbose_name_plural='album'


class Song(models.Model):
    songtitle = models.CharField(max_length=255)
    album = models.ForeignKey(Album,on_delete=models.DO_NOTHING)
    artist = models.ForeignKey(Artist,on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(Genre,on_delete=models.DO_NOTHING)
    track = models.SmallIntegerField(null=True, blank=True)
    length = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.songtitle
    
    class Meta:
        db_table='song'
        verbose_name_plural='song'

class SongReview(models.Model):
    song = models.ForeignKey(Song,on_delete=models.DO_NOTHING)
    postby = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    rating = models.PositiveSmallIntegerField(default=10,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    reviews = models.TextField()

    def __str__(self):
        return self.reviews

    class Meta:
        db_table='songreview'
        verbose_name_plural='songreview'







