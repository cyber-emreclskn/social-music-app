from django.test import TestCase
import grpc
from Music_proto import Music_pb2, Music_pb2_grpc
from django.test import Client

with grpc.insecure_channel('localhost:50051') as channel:

        stub = Music_pb2_grpc.MusicModelControllerStub(channel)
        print("---Create Model----")
        response = stub.Create(
            Music_pb2.MusicModel(
              musicName="Nothing Else Matters",
            )
        )
        print(response, end=" ")
