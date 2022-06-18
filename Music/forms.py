from django import forms
from .models import MusicModel, AlbumModel
from django.utils.translation import gettext_lazy as _


class MusicModelForm(forms.ModelForm):
    class Meta:
        model = MusicModel
        fields = [
            "musicName",
            "the_music",
        ]
        labels = {
            "musicName" : _("Music Name"),
            "the_music" : _("Music File"),
        }
        

class AlbumModelForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = [
            "artist",
            "album_title",
            "genre",
            "album_logo",
        ]
        labels = {
            "artist" : _("Artist"),
            "album_title" : _("Album Title"),
            "genre" : _("Genre"),
            "album_logo" : _("Album Logo"),
        }