from django.urls import path
from .views import MusicViews

app_name = "Music"

musicViews = MusicViews()

urlpatterns = [
    path("add-album/",musicViews.CreateAlbum,name="createAlbum"),
    path("update-album/<int:id>",musicViews.UpdateAlbum,name="updateAlbum"),
    path("delete-album/<int:id>",musicViews.DestroyAlbum,name="deleteAlbum"),
    path("album-dashboard/<int:id>",musicViews.AlbumDashboard,name="albumDashboard"),
    path("create-music/<int:album_id>",musicViews.CreateMusic,name="createMusic"),
    path("update-music/<int:id>",musicViews.UpdateMusic,name="updateMusic"),
    path("delete-music/<int:id>",musicViews.DeleteMusic,name="deleteMusic"),
    path("albums/",musicViews.allAlbums,name="albums"),
    path("album-detail/<int:album_id>",musicViews.albumDetail,name="albumDetail"),
    path("music-comment/<int:id>",musicViews.addComment,name="musicComment"),
    path("music-detail/<int:id>",musicViews.MusicDetail,name="musicDetail")

]