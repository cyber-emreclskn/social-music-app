import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from Person.serializers import PersonModelSerializer
from .models import AlbumModel, MusicModel
from .serializers import AlbumModelSerializer, MusicModelSerializer


class MusicModelService(Service):

    def List(self,request,context):
        musics = MusicModel.objects.all()
        serializer = MusicModelSerializer(
            musics,
            many = True
        )
        for msg in serializer.message:
            yield msg


    def Create(self,request,context):
        serializer = MusicModelSerializer(message = request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    
    def get_object(self,pk):
        try:
            return MusicModel.objects.get(pk=pk)
        except MusicModel.DoesNotExist:
            self.context.abort(
                grpc.StatusCode.NOT_FOUND,
                'Music:%s not found!' %pk
            )

    
    def Retrieve(self,request,context):
        music = self.get_object(request.id)
        serializer = PersonModelSerializer(music)
        return serializer.message

    
    def Update(self,request,context):
        music = self.get_object(request.id)
        serializer = MusicModelSerializer(
            music,
            message = request,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    
    def Destroy(self,request,context):
        music = self.get_object(request.id)
        music.delete()
        return empty_pb2.Empty()



class AlbumServices(Service):
    
    def List(self,request,context):
        albums = AlbumModel.objects.all()
        serializer = AlbumModelSerializer(
            albums,
            many = True,
        )
        for msg in serializer.message:
            yield msg

    
    def Create(self,request,context):
        serializer = AlbumModelSerializer(message = request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message


    def get_object(self,pk):
        try:
            return AlbumModel.objects.get(pk=pk)
        except AlbumModel.DoesNotExist:
            self.context.abort(
                grpc.StatusCode.NOT_FOUND,
                'Album:%s not found!' %pk
            )

    def Update(self,request,context):
        album = self.get_object(request.id)
        serializer = AlbumModelSerializer(
            album,
            message = request
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message


    def Destroy(self,request,context):
        album = self.get_object(request.id)
        album.delete()
        return empty_pb2.Empty()


    def Retrieve(self,request,context):
        album = self.get_object(request.id)
        serializer = AlbumModelSerializer(album)
        return serializer.message




