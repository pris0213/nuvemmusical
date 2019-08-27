from django.urls import path
from nuvemmusicalapp import views

app_name = 'nuvemmusicalapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('songs', views.SongView.as_view(), name='songs'),
    path('artists', views.ArtistView.as_view(), name='artists'),
    path('albums', views.AlbumView.as_view(), name='albums')
]