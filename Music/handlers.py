from .services import AlbumServices, MusicModelService
from Music_proto import Music_pb2_grpc
from Album_proto import Album_pb2_grpc


def grpc_handlers(server):
    Music_pb2_grpc.add_MusicModelControllerServicer_to_server(
        MusicModelService.as_servicer(),
        server,
    )
    Album_pb2_grpc.add_AlbumModelControllerServicer_to_server(
        AlbumServices.as_servicer(),
        server
    )