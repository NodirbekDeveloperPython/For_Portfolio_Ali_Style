from django.db import models
from userapp.models import Profil




# Create your models here.
class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to='bolimlar')
    def __str__(self):return self.nom

class Ichki(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to='ichki_bolimlar')
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE, related_name='ichkilar')
    def __str__(self): return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=70)
    brend = models.CharField(max_length=70)
    batafsil = models.CharField(max_length=700)
    kafolat = models.CharField(max_length=70)
    yetkazish = models.CharField(max_length=70)
    narx = models.PositiveSmallIntegerField()
    chegirma = models.PositiveSmallIntegerField(default=0)
    mavjud = models.BooleanField(default=True)
    min_order = models.CharField(max_length=30, default="1 dona")
    ichki = models.ForeignKey(Ichki, on_delete=models.CASCADE)
    def __str__(self): return self.nom


class Rasm(models.Model):
    rasm = models.FileField(upload_to="mahsulotlar")
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE, related_name='rasmlari')


