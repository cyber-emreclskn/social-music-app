from django_grpc_framework import proto_serializers
from Person.models import PersonModel
from Person_proto import Person_pb2


class PersonModelSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = PersonModel
        proto_class = Person_pb2.PersonModel
        fields = '__all__'