from django.urls import path
from .views import PersonWievs

app_name = "Person"

personViews = PersonWievs()

urlpatterns = [
    path("create-person",personViews.CreatePersonModel,name="personCreate"),
    path("delete-person/<int:id>",personViews.DestroyPersonModel,name="personDelete"),
    path("update-person/<int:id>",personViews.UpdatePersonModel,name="personUpdate"),
    path("retrieve-person/<int:id>",personViews.RetrievePersonModel,name="personRetrieve"),
    path("dashboard-person/",personViews.DashboardPerson,name="dashboardPerson"),
    path("login-person/",personViews.loginPerson,name="loginPerson"),
    path("logout-person/",personViews.logoutPerson,name="logoutPerson"),
]