import datetime
from django.test import TestCase
from ..models import Album, Artist, Song


class SongModelTest(TestCase):

    @staticmethod
    def create_song(title, duration, artist_name, album_name, album_release_date):
        artist = Artist.objects.create(name=artist_name)

        album = Album.objects.create(name=album_name,
                                     artist=artist,
                                     release_date=album_release_date)

        return Song.objects.create(title=title,
                                   duration=duration,
                                   artist=artist,
                                   album=album)

    def test_duration_to_string_with_positive_number(self):
        fav_song = self.create_song("Ghost Ship",
                                    299,
                                    "Blur",
                                    "The Magic Whip",
                                    datetime.date(2015, 4, 27))

        self.assertEqual(fav_song.duration_to_string(), "0:04:59")

    def test_duration_to_string_with_negative_number(self):
        self.create_song("Ghost Ship",
                         -1,
                         "Blur",
                         "The Magic Whip",
                         datetime.date(2015, 4, 27))

        self.assertRaises(ValueError)


