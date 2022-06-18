from django.contrib.auth.models import User
from django.db import models



class PersonModel(models.Model):
    
    userModel = models.ForeignKey(
        User,
        null=True,
        blank=True,
        verbose_name="Kullanıcı Modeli",
        on_delete=models.CASCADE,
    )
    firstname = models.CharField(
        null=True,
        blank=True,
        max_length=65,
    )
    lastName = models.CharField(
        null=True,
        blank=True,
        max_length=65,
    )
    username = models.CharField(
        null=True,
        blank=True,
        max_length=75,
    )
    password = models.CharField(
        null=True,
        blank=True,
        max_length=75,
    )
    email = models.EmailField(
        null=True,
        blank=True,
        max_length=85,
    )

    def __str__(self):
        return "{} {}".format(self.firstname,self.lastName)


