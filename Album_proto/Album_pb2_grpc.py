# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from Album_proto import Album_pb2 as Album__proto_dot_Album__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AlbumModelControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/Music_proto.AlbumModelController/List',
                request_serializer=Album__proto_dot_Album__pb2.AlbumModelListRequest.SerializeToString,
                response_deserializer=Album__proto_dot_Album__pb2.AlbumModel.FromString,
                )
        self.Create = channel.unary_unary(
                '/Music_proto.AlbumModelController/Create',
                request_serializer=Album__proto_dot_Album__pb2.AlbumModel.SerializeToString,
                response_deserializer=Album__proto_dot_Album__pb2.AlbumModel.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/Music_proto.AlbumModelController/Retrieve',
                request_serializer=Album__proto_dot_Album__pb2.AlbumModelRetrieveRequest.SerializeToString,
                response_deserializer=Album__proto_dot_Album__pb2.AlbumModel.FromString,
                )
        self.Update = channel.unary_unary(
                '/Music_proto.AlbumModelController/Update',
                request_serializer=Album__proto_dot_Album__pb2.AlbumModel.SerializeToString,
                response_deserializer=Album__proto_dot_Album__pb2.AlbumModel.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/Music_proto.AlbumModelController/Destroy',
                request_serializer=Album__proto_dot_Album__pb2.AlbumModel.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class AlbumModelControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AlbumModelControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=Album__proto_dot_Album__pb2.AlbumModelListRequest.FromString,
                    response_serializer=Album__proto_dot_Album__pb2.AlbumModel.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=Album__proto_dot_Album__pb2.AlbumModel.FromString,
                    response_serializer=Album__proto_dot_Album__pb2.AlbumModel.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=Album__proto_dot_Album__pb2.AlbumModelRetrieveRequest.FromString,
                    response_serializer=Album__proto_dot_Album__pb2.AlbumModel.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=Album__proto_dot_Album__pb2.AlbumModel.FromString,
                    response_serializer=Album__proto_dot_Album__pb2.AlbumModel.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=Album__proto_dot_Album__pb2.AlbumModel.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Music_proto.AlbumModelController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AlbumModelController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Music_proto.AlbumModelController/List',
            Album__proto_dot_Album__pb2.AlbumModelListRequest.SerializeToString,
            Album__proto_dot_Album__pb2.AlbumModel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Music_proto.AlbumModelController/Create',
            Album__proto_dot_Album__pb2.AlbumModel.SerializeToString,
            Album__proto_dot_Album__pb2.AlbumModel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Music_proto.AlbumModelController/Retrieve',
            Album__proto_dot_Album__pb2.AlbumModelRetrieveRequest.SerializeToString,
            Album__proto_dot_Album__pb2.AlbumModel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Music_proto.AlbumModelController/Update',
            Album__proto_dot_Album__pb2.AlbumModel.SerializeToString,
            Album__proto_dot_Album__pb2.AlbumModel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Music_proto.AlbumModelController/Destroy',
            Album__proto_dot_Album__pb2.AlbumModel.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
