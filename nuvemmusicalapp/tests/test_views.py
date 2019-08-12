from django.test import TestCase
from django.urls import reverse


class SongViewTest(TestCase):
    def test_song_view_loads(self):
        response = self.client.get(reverse('nuvemmusicalapp:songs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'songs.html')


class ArtistViewTest(TestCase):
    def test_artist_view_loads(self):
        response = self.client.get(reverse('nuvemmusicalapp:artists'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'artists.html')


class AlbumViewTest(TestCase):
    def test_album_view_loads(self):
        response = self.client.get(reverse('nuvemmusicalapp:albums'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'albums.html')

