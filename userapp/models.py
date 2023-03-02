from django.contrib.auth.models import User
from django.db import models
# from django_countries.fields import CountryField
# from cities.models import BaseCountry


# Create your models here.
class Profil(models.Model):
    T = [
        ("Erkak", "Erkak"),
        ("Ayol", "Ayol"),
    ]
    # davlat = CountryField(blank_label='(Country)', blank=True)
    shahar = models.CharField(max_length=50)
    tel = models.CharField(max_length=13)
    jins = models.CharField(max_length=5, choices=T)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self): return f"{self.user.first_name} {self.user.last_name}"