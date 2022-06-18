from turtle import mode
from django.db import models
from Person.models import PersonModel


class BandModel(models.Model):

    bandName = models.CharField(
        null=True,
        blank=True,
        max_length=90,
        verbose_name="Grup İsmi"
    )
    
    bandLogo = models.ImageField(
        null=True,
        blank=True,
        upload_to="bandLogos/",
        verbose_name="Grup Logosu",
    )
class BandMembers(models.Model):

    band = models.ForeignKey(
        BandModel,
        on_delete=models.CASCADE,
        verbose_name="Grup",
        null=True,
        blank=True,
    )
    bandUser = models.ForeignKey(
        PersonModel,
        on_delete=models.CASCADE,
        verbose_name="Grup Üyesi",
        null=True,
        blank=True,
    )

    

    