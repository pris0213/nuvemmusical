from django.contrib import admin
from django import forms

# Register your models here.
from nuvemmusicalapp.models import Album, Artist, Song


class SongAdmin(admin.ModelAdmin):
    model = Song
    fieldsets = [
        (None, {
            'fields': ['title', 'duration', 'artist', 'album']
        })
    ]
    list_display = ['title', 'duration_to_string', 'get_artist', 'get_album']

    def get_artist(self, obj):
        return obj.artist.name
    get_artist.order_field = 'artist'
    get_artist.short_description = 'Artist'

    def get_album(self, obj):
        return obj.album.name
    get_album.order_field = 'album'
    get_album.short_description = 'Album'

#     def formfield_for_manytomany(self, db_field, request, **kwargs):
#         if db_field.name == "artist":
#             kwargs["queryset"] = ArtisArtist.objects.all()
#         return super(SongAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
#
#
# class ArtistChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         return obj.name


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name', 'artist', 'release_date']
        })
    ]
    list_display = ('name', 'get_artist', 'get_release_date')
    release_date = forms.DateField(
        widget=forms.DateInput(format='%d/%b/%Y'),
        input_formats=('%d/%b/%Y', )
    )

    def get_artist(self, obj):
        return obj.artist.name
    get_artist.order_field = 'artist'
    get_artist.short_description = 'Artist'

    def get_release_date(self, obj):
        return obj.release_date.strftime("%d %B %Y")
    get_release_date.admin_order_field = 'timefield'
    get_release_date.short_description = 'Date of Release'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "artist":
            kwargs["queryset"] = Artist.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name', 'genre']
        })
    ]
    list_display = ('name', 'genre')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song, SongAdmin)
