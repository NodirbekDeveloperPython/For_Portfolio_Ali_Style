from django.db import models
from asosiyapp.models import *
from django.core.exceptions import ValidationError
from userapp.models import *

def validate_miqdor(qiymat):
    if qiymat >= 1 and qiymat <= 10:
        return qiymat
    else:
        raise ValidationError("Minimum 1, Maksimum 10 dona bo'lishi mumkin xalos!")


class Savat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField(default=1, validators=[validate_miqdor,])
    umumiy = models.PositiveIntegerField()
    def __str__(self): return self.mahsulot.nom


class Tanlangan(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE, null=True)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.profil.user.first_name} {self.profil.user.last_name}, {self.mahsulot.nom}"


class Buyurtma(models.Model):
    savat = models.ManyToManyField(Savat, related_name='savatlari')
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    umumiy = models.PositiveIntegerField()
    yetkazish = models.PositiveIntegerField(default=5)
    yakuniy = models.PositiveIntegerField()
    # def __str__(self): return self.savat.mahsulot.nom