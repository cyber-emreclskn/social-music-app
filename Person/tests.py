from django.test import TestCase
import grpc
from Person_proto import Person_pb2, Person_pb2_grpc
from django.contrib.auth.models import User

with grpc.insecure_channel('localhost:50051') as channel:

    stub = Person_pb2_grpc.PersonModelControllerStub(channel)
    print("--------Create Model-------")

    user = User(username = "kkkkk", password = "kkkkkk")

    response2 = stub.Create(Person_pb2.PersonModel(
        userId = user.id,
        firstname="Kamil",
        lastName="Caliskan123",
        username="hakancaliskan01",
        password="yaladunya0101",
    ))
    print(response2, end=" ")

    print("***************************************")
    response = stub.Retrieve(
            Person_pb2.PersonModelRetrieveRequest(
                id = 3
            )
        )
    print(response, end=" ")

    print("***************************************")

    response = stub.Retrieve(
            Person_pb2.PersonModelRetrieveRequest(
                id = 3
            )
        )
    print(response, end=" ")

    print("***************************************")

