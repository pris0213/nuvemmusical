from django.shortcuts import render
from django.views import generic

from nuvemmusicalapp.models import Song, Artist, Album


class IndexView(generic.ListView):
    template_name = 'nuvemmusicalapp/index.html'
    model = Song
    context_object_name = 'song_list'

    def get_queryset(self):
        return Song.objects


class SongView(generic.ListView):
    template_name = 'nuvemmusicalapp/songs.html'
    model = Song
    context_object_name = 'song_list'

    def get_queryset(self):
        return Song.objects.all()


class ArtistView(generic.ListView):
    template_name = 'nuvemmusicalapp/artists.html'
    model = Artist
    context_object_name = 'artist_list'

    def get_queryset(self):
        return Artist.objects.all()


class AlbumView(generic.ListView):
    template_name = 'nuvemmusicalapp/albums.html'
    model = Album
    context_object_name = 'album_list'

    def get_queryset(self):
        return Album.objects.all()

