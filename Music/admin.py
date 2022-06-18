from django.contrib import admin

from Music.models import AlbumModel, CommentModel, MusicModel

admin.site.register(MusicModel)
admin.site.register(AlbumModel)
admin.site.register(CommentModel)
