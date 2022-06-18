from django_grpc_framework import proto_serializers
from Music.models import MusicModel, AlbumModel
from Music_proto import Music_pb2
from Album_proto import Album_pb2


class MusicModelSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = MusicModel
        proto_class = Music_pb2.MusicModel
        fields = [
            "id",
            "musicName",
        ]


class AlbumModelSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = AlbumModel
        proto_class = Album_pb2.AlbumModel
        fields = [
            "id",
            "artist",
            "album_title",
            "genre",

        ]