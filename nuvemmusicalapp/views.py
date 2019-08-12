from django.shortcuts import render
from django.views import generic

from nuvemmusicalapp.models import Song, Artist, Album


class SongView(generic.ListView):
    template_name = 'nuvemmusicalapp/songs.html'
    model = Song

    def get_queryset(self):
        return Song.objects


class ArtistView(generic.ListView):
    template_name = 'nuvemmusicalapp/artists.html'
    model = Artist

    def get_queryset(self):
        return Artist.objects


class AlbumView(generic.ListView):
    template_name = 'nuvemmusicalapp/albums.html'
    model = Album

    def get_queryset(self):
        return Album.objects

