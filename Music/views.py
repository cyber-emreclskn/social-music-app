from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
import grpc
from django.contrib import messages
from Music.models import AlbumModel, CommentModel, MusicModel
from Music_proto import Music_pb2_grpc,Music_pb2
from Album_proto import Album_pb2, Album_pb2_grpc
from Person.models import PersonModel
from .forms import AlbumModelForm, MusicModelForm

class MusicViews:
    
    def __init__(self):

        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = Music_pb2_grpc.MusicModelControllerStub(self.channel)
        self.albumStub = Album_pb2_grpc.AlbumModelControllerStub(self.channel)


    def CreateMusic(self,request,album_id):
        context = dict()
        album = get_object_or_404(AlbumModel,pk = album_id)
        music_forms = MusicModelForm(
            request.POST or None,
            request.FILES or None,
        )
        context['musicAddForm'] = music_forms
        if music_forms.is_valid():
            music = music_forms.save(commit=False)
            music_user = request.user
            music.albums = album
            music.save()

            self.stub.Update(
                Music_pb2.MusicModel(
                    id = music.id,
                    musicName = music.musicName,
                )
            )
            messages.success(request,"Müzik Albüme Eklendi")
            return redirect(reverse('Music:albumDashboard',args=[album_id]))
        return render(request,"music-add.html",context)
    

    def UpdateMusic(self,request,id):
        context = dict()
        music = get_object_or_404(MusicModel,pk = id)
        person = PersonModel.objects.get(userModel = request.user)
        album = AlbumModel.objects.filter(publisher = person).first()
        music_update_form = MusicModelForm(
            request.POST or None,
            request.FILES or None,
            instance=music
        )
        context['musicUpdateForm'] = music_update_form
        if music_update_form.is_valid():
            music = music_update_form.save(commit=False)
            music.music_person = person
            music.save()

            self.stub.Update(
                Music_pb2.MusicModel(
                    id = id,
                    musicName = music.musicName,
                )
            )
            messages.success(request,"Müzik Güncellendi")
            return redirect(reverse("Music:albumDashboard",args=[album.id]))
        return render(request,"music-update.html",context)


    def RetrieveMusic(self,request,id):
        self.stub.Retrieve(
            Music_pb2.MusicModelRetrieveRequest(
                id = id
            )
        )
        return render(request)



    def DeleteMusic(self,request,id):
        music = get_object_or_404(MusicModel,pk = id)
        person = PersonModel.objects.get(userModel = request.user)
        album = AlbumModel.objects.filter(publisher = person).first()
        self.stub.Destroy(
            Music_pb2.MusicModel(
                id = id
            )
        )
        return redirect(reverse("Music:albumDashboard",args=[album.id]))
        
    
    def CreateAlbum(self,request):
        context = dict()
        albumForm = AlbumModelForm(
            request.POST or None,
            request.FILES,
        )
        personModel = PersonModel.objects.get(userModel = request.user)
        context['albumForm'] = albumForm
        if albumForm.is_valid():
            album = albumForm.save(commit=False)
            album.publisher = personModel
            album.save()

            self.albumStub.Update(
                Album_pb2.AlbumModel(
                    id = album.id,
                    artist = album.artist,
                    album_title = album.album_title,
                    genre = album.genre,
                )
            )
           
            messages.success(request,"Başarılı Album Kayıtı")
            return redirect("Person:dashboardPerson")
        
        return render(request,"album-add.html",context)

    def UpdateAlbum(self,request,id):
        context = dict()
        album = get_object_or_404(AlbumModel,pk=id)
        album_updated_form = AlbumModelForm(
            request.POST or None,
            request.FILES or None,
            instance=album,
        )
        personModel = PersonModel.objects.get(userModel = request.user)
        context['albumUpdatedForm'] = album_updated_form
        if album_updated_form.is_valid():
            album = album_updated_form.save(commit=False)
            album.publisher = personModel
            album.save()

            self.albumStub.Update(
                Album_pb2.AlbumModel(
                    id = album.id,
                    artist = album.artist,
                    album_title = album.album_title,
                    genre = album.genre,
                    
                )
            )
            messages.success(request,"Başarılı Album Güncellemesi")
            return redirect("Person:dashboardPerson")
        return render(request,"album-update.html",context)


    def RetrieveAlbum(self,request):
        pass


    def DestroyAlbum(self,request,id):
        album = get_object_or_404(AlbumModel,pk=id)
        self.albumStub.Destroy(
            Album_pb2.AlbumModel(
                id = id
            )
        )
        return redirect("Person:dashboardPerson")

        
    def AlbumDashboard(self,request,id):
        context = dict()

        album = get_object_or_404(AlbumModel,pk = id)
        musics = MusicModel.objects.filter(albums = album)
        context['musics'] = musics
        context['album'] = album

        return render(request,"album-dashboard.html",context)
    

    def allAlbums(self,request):
        context = dict()
        albums = AlbumModel.objects.all()
        context['albums'] = albums
        return render(request,"album.html",context)

    
    def albumDetail(self,request,album_id):
        context = dict()
        album = get_object_or_404(AlbumModel,pk=album_id)
        musics = MusicModel.objects.filter(albums=album)
        context['album'] = album
        context['musics'] = musics
        return render(request,"album-detail.html",context)

    
    def addComment(self,request,id):
        music = get_object_or_404(MusicModel,id=id)
        person = PersonModel.objects.filter(userModel = request.user).first()
        if request.method == "POST":
            comment_text = request.POST.get("comment_text")
            newComment = CommentModel(comment_text = comment_text)
            newComment.comment_music = music
            newComment.comment_person = person
            newComment.save()
        return redirect(reverse("Music:musicDetail",args=[music.id]))


    def MusicDetail(self,request,id):
        context = dict()
        music = get_object_or_404(MusicModel,pk = id)
        comments = CommentModel.objects.filter(comment_music = music)
        context['music'] = music
        context['comments'] = comments
        return render(request,"music-detail.html",context)