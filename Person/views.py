import django
from django.shortcuts import get_object_or_404, redirect, render
import grpc
from Person.forms import PersonCreateModelForm, PersonLoginForm
from Person.models import PersonModel
from Person_proto import Person_pb2, Person_pb2_grpc
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction
from django.contrib.auth import login,authenticate,logout
from Music.models import AlbumModel, MusicModel

def index(request):
    context = dict()
    return render(request,"index.html",context)

class PersonWievs:

    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = Person_pb2_grpc.PersonModelControllerStub(self.channel)

    def CreatePersonModel(self, request):
        person_form = PersonCreateModelForm(
            request.POST or None
        )
        context = dict()
        context['form'] = person_form

        if person_form.is_valid():
            person = person_form.save(commit=False)
            newUser = User(
                username=person.username,
            )
            newUser.set_password(person.password)
            newUser.save()

            person.userModel = newUser
            person.save()

            self.stub.Update(
                Person_pb2.PersonModel(
                    id = person.id,
                    firstname=person.firstname,
                    lastName=person.lastName,
                    username=person.username,
                    password=person.password,
                    email=person.email,
                ) 
            )
            
            

            messages.success(request,"Başarılı Kayıt")
            return redirect("index")
            
        return render(request,"register.html",context)


    def RetrievePersonModel(self, id):        
        response = self.stub.Retrieve(
            Person_pb2.PersonModelRetrieveRequest(
                id = id
            )
        )
        return response

    def UpdatePersonModel(self,request, id):
        context = dict()
        person = get_object_or_404(Person_pb2.PersonModel,pk = id)
        person_update_form = PersonCreateModelForm(
            request.POST or None,
            initial = person 
        )
        context['update_form'] = person_update_form
        if person_update_form.is_valid():
            person = person_update_form.save(commit = False)
            self.stub.Update(
                Person_pb2.PersonModel(
                    firstName = person.firstName,
                    lastName = person.lastName,
                    username = person.username,
                    password = person.password,
                    email = person.email,
                )
            )
            person.userModel = request.user
            person.save()
        return render(request,"update-user.html",context)


    def DestroyPersonModel(self,request, id):
        context = dict()
        person_model = self.stub.Retrieve(
            Person_pb2.PersonModel,
            id = id,
        )
        context['person_model'] = person_model
        return render(request)


    def DashboardPerson(self,request):
        context = dict()
        userModel = get_object_or_404(User,pk = request.user.id)
        personModel = PersonModel.objects.get(userModel = userModel)
        context['user'] = personModel

        albums = AlbumModel.objects.filter(publisher = personModel)
        context['albums'] = albums

        return render(request,"dashboard.html",context)


    def loginPerson(self,request):
        context = dict()
        loginForm = PersonLoginForm(
            request.POST or None
        )
        context['loginForm'] = loginForm

        if loginForm.is_valid():
            username = loginForm.cleaned_data.get('username')
            password = loginForm.cleaned_data.get('password')

            user = authenticate(username = username,password = password)
            if user is None:
                messages.info(request,"Kullanıcı Bulunamadı")
                return render(request,"login.html",context)

            messages.success(request,"Giriş Başarılı")
            login(request,user)
            return redirect("index")    

        return render(request,"login.html",context)


    def logoutPerson(self,request):
        logout(request)
        messages.info(request,"Çıkış Yapıldı")
        return redirect("index")


