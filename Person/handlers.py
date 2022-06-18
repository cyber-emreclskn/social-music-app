from .services import PersonModelService
from Person_proto import Person_pb2_grpc


def grpc_handlers(server):
    Person_pb2_grpc.add_PersonModelControllerServicer_to_server(
        PersonModelService.as_servicer(),
        server,
    )
