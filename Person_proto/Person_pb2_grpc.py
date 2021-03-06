# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from Person_proto import Person_pb2 as Person__proto_dot_Person__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class PersonModelControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/Person_proto.PersonModelController/List',
                request_serializer=Person__proto_dot_Person__pb2.PersonModelListRequest.SerializeToString,
                response_deserializer=Person__proto_dot_Person__pb2.PersonModel.FromString,
                )
        self.Create = channel.unary_unary(
                '/Person_proto.PersonModelController/Create',
                request_serializer=Person__proto_dot_Person__pb2.PersonModel.SerializeToString,
                response_deserializer=Person__proto_dot_Person__pb2.PersonModel.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/Person_proto.PersonModelController/Retrieve',
                request_serializer=Person__proto_dot_Person__pb2.PersonModelRetrieveRequest.SerializeToString,
                response_deserializer=Person__proto_dot_Person__pb2.PersonModel.FromString,
                )
        self.Update = channel.unary_unary(
                '/Person_proto.PersonModelController/Update',
                request_serializer=Person__proto_dot_Person__pb2.PersonModel.SerializeToString,
                response_deserializer=Person__proto_dot_Person__pb2.PersonModel.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/Person_proto.PersonModelController/Destroy',
                request_serializer=Person__proto_dot_Person__pb2.PersonModel.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class PersonModelControllerServicer(object):
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


def add_PersonModelControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=Person__proto_dot_Person__pb2.PersonModelListRequest.FromString,
                    response_serializer=Person__proto_dot_Person__pb2.PersonModel.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=Person__proto_dot_Person__pb2.PersonModel.FromString,
                    response_serializer=Person__proto_dot_Person__pb2.PersonModel.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=Person__proto_dot_Person__pb2.PersonModelRetrieveRequest.FromString,
                    response_serializer=Person__proto_dot_Person__pb2.PersonModel.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=Person__proto_dot_Person__pb2.PersonModel.FromString,
                    response_serializer=Person__proto_dot_Person__pb2.PersonModel.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=Person__proto_dot_Person__pb2.PersonModel.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Person_proto.PersonModelController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PersonModelController(object):
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
        return grpc.experimental.unary_stream(request, target, '/Person_proto.PersonModelController/List',
            Person__proto_dot_Person__pb2.PersonModelListRequest.SerializeToString,
            Person__proto_dot_Person__pb2.PersonModel.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/Person_proto.PersonModelController/Create',
            Person__proto_dot_Person__pb2.PersonModel.SerializeToString,
            Person__proto_dot_Person__pb2.PersonModel.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/Person_proto.PersonModelController/Retrieve',
            Person__proto_dot_Person__pb2.PersonModelRetrieveRequest.SerializeToString,
            Person__proto_dot_Person__pb2.PersonModel.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/Person_proto.PersonModelController/Update',
            Person__proto_dot_Person__pb2.PersonModel.SerializeToString,
            Person__proto_dot_Person__pb2.PersonModel.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/Person_proto.PersonModelController/Destroy',
            Person__proto_dot_Person__pb2.PersonModel.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
