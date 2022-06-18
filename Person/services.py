import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from .models import PersonModel
from .serializers import PersonModelSerializer


class PersonModelService(Service):

    def List(self,request,context):
        persons = PersonModel.objects.all()
        serializer = PersonModelSerializer(
            persons,
            many = True,
        )
        for msg in serializer.message:
            yield msg
        
    
    def Create(self,request,context):
        serializer = PersonModelSerializer(message = request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    
    def get_object(self,pk):
        try:
            return PersonModel.objects.get(pk=pk)
        except PersonModel.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND,'PERSON:%s not found!' % pk)


    def Retrieve(self,request,context):
        person = self.get_object(request.id)
        serializer = PersonModelSerializer(person)
        return serializer.message

    
    def Update(self,request,context):
        person = self.get_object(request.id)
        serializer = PersonModelSerializer(
            person,
            message = request,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    
    def Destroy(self,request,context):
        person = self.get_object(request.id)
        person.delete()
        return empty_pb2.Empty()