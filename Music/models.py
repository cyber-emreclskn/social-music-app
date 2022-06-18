from django.db import models
from Person.models import PersonModel


class AlbumModel(models.Model):
    artist = models.CharField(
        max_length=200,
        null=True,
    )
    album_title = models.CharField(
        max_length=300,
        null=True,
        blank=True,
    )
    genre = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    album_logo = models.ImageField(
        upload_to = "album_logos/",
        null=True,
        blank=True,
    )
    publisher = models.ForeignKey(
        PersonModel,
        null=True,
        blank=True,
        verbose_name="Yayınlayıcı",
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(
        null=True,
        blank=True,
        auto_now_add=True,
        verbose_name="Oluşturma Tarihi",
    )

    def __str__(self):
        return self.album_title + '-' + self.artist

class MusicModel(models.Model):

    albums = models.ForeignKey(
        AlbumModel,
        null=True,
        blank=True,
        verbose_name="Albüm",
        on_delete=models.CASCADE,
    )
    musicName = models.CharField(
        null=True,
        blank=True,
        verbose_name="Muzik İsmi",
        max_length=80,
    )
    the_music = models.FileField(
        null=True,
        blank=True,
        upload_to="musics/",
    )
    music_person = models.ForeignKey(
        PersonModel,
        null=True,
        blank=True,
        verbose_name="Müzik Sahibi",
        on_delete=models.CASCADE,
    )
    

    def __str__(self):
        return self.musicName


class CommentModel(models.Model):
    
    comment_person = models.ForeignKey(
        PersonModel,
        on_delete=models.CASCADE,
        verbose_name="Yorum Kullanıcısı",
        null=True,
        blank=True,
    )
    comment_text = models.TextField(
        null=True,
        blank=True,
        verbose_name="Yorum"
    )
    comment_music = models.ForeignKey(
        MusicModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
