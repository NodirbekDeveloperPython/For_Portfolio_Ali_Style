from django.db.models import Sum
from django.shortcuts import render, redirect
from .models import *
from userapp.models import Profil
from asosiyapp.models import Mahsulot
# Create your views here.
from rest_framework.views import View

class TanlanganView(View):
    def get(self,request):
        context = {
            'tanlanganlar': Tanlangan.objects.filter(profil__user=request.user)
        }
        return render(request, 'page-profile-wishlist.html', context)

def tanlangan_ochirish(request,pk):
    Tanlangan.objects.get(id=pk).delete()
    return redirect('/buyurtma/tanlangan/')

class TanlanganQoshishView(View):
    def get(self,request,pk):
        pr = Profil.objects.get(user=request.user)
        m = Mahsulot.objects.get(id=pk)
        tanlangan = Tanlangan.objects.filter(profil=pr, mahsulot=m)
        if len(tanlangan) > 0:
            return redirect('/buyurtma/tanlangan/')
        Tanlangan.objects.create(
            profil = pr,
            mahsulot = m,
        )
        return redirect('/buyurtma/tanlangan/')


class SavatView(View):
    def get(self, request):
        sv = Savat.objects.filter(profil__user=request.user)
        umumiy = 0
        for i in sv:
            umumiy += i.umumiy

        chegirma = 0
        for s in sv:
            chegirma += s.mahsulot.narx*s.mahsulot.chegirma*0.01*s.miqdor

        total = umumiy - chegirma

        context = {
            'savatlar': sv,
            'umumiy': umumiy,
            'chegirma': chegirma,
            'total': total
        }
        return render(request, 'page-shopping-cart.html', context)




class BuyurtmaView(View):
    def get(self,request):
        context = {
            "buyurtmalar": Buyurtma.objects.filter(profil__user=request.user)
        }
        return render(request, 'page-profile-orders.html', context)


class BuyurtmaqoshishView(View):
    def get(self,request):
        savatlar = Savat.objects.filter(profil__user=request.user)
        buyurtma = Buyurtma.objects.create(
            profil = Profil.objects.get(user=request.user),
            umumiy = savatlar.aggregate(Sum('umumiy')).get('umumiy__sum'),
            yakuniy = int(savatlar.aggregate(Sum('umumiy')).get('umumiy__sum')) + 5
        )
        for s in savatlar:
            buyurtma.savat.add(s)
        buyurtma.save()
        return redirect('/buyurtma/')


def savat_qoshish(request,pk):
    savat = Savat.objects.get(id=pk)
    if savat.miqdor != 10:
        savat.miqdor = savat.miqdor + 1
        savat.umumiy = savat.miqdor * savat.mahsulot.narx
        savat.save()
        return redirect('/buyurtma/savat/')
    return redirect('/buyurtma/savat/')


def savat_kamaytirish(request,pk):
    savat = Savat.objects.get(id=pk)
    if savat.miqdor != 1:
        savat.miqdor = savat.miqdor - 1
        savat.umumiy = savat.miqdor * savat.mahsulot.narx
        savat.save()
        return redirect('/buyurtma/savat/')
    return redirect('/buyurtma/savat/')


class SavatQoshishView(View):
    def get(self,request, pk):
        pr = Profil.objects.get(user=request.user)
        m = Mahsulot.objects.get(id=pk)
        savat = Savat.objects.filter(profil=pr, mahsulot=m)
        if len(savat) > 0:
            return redirect('/buyurtma/savat/')
        Savat.objects.create(
            profil = pr,
            mahsulot = m,
            umumiy = m.narx
        )
        return redirect('/buyurtma/savat/')



def savat_ochirish(request,pk):
    Savat.objects.get(id=pk).delete()
    return redirect('/buyurtma/savat/')



class PageProfilMainView(View):
    def get(self,request):
        return render(request, 'page-profile-main.html')




class PageProfilAddressView(View):
    def get(self,request):
        return render(request, 'page-profile-address.html')


class PageProfilSettingView(View):
    def get(self,request):
        context = {
            "profil": Profil.objects.get(user=request.user)
        }
        return render(request, 'page-profile-setting.html', context)




class PageProfileSellerView(View):
    def get(self,request):
        return render(request, 'page-profile-seller.html')


