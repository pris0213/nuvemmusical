from django.db import models
import datetime


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=500)
    genre = models.CharField(max_length=150, default='Alternative Rock')


class Album(models.Model):
    name = models.CharField(max_length=1000)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateTimeField('date of release')


class Song(models.Model):
    title = models.CharField(max_length=1000)
    duration = models.FloatField(default=0)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def duration_to_string(self):

        duration = self.floatfield_to_float(self.duration)

        try:
            if duration < 0:
                raise ValueError
            if duration >= 0:
                return str(datetime.timedelta(seconds=duration))
        except ValueError:
            print("The duration of the song can\'t be negative.")
    duration_to_string.short_description = 'Duration'

    @staticmethod
    def floatfield_to_float(a_floatfield_var):
        var_as_string = str(a_floatfield_var)
        return float(var_as_string)
