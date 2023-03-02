from django.shortcuts import render, redirect
from rest_framework.views import View
from .models import *
from buyurtmaapp.models import Savat
import random

# Create your views here.


class Home2View(View):
    def get(self, request):
        mahsulotlar = (Mahsulot.objects.all())
        context = {
            'bolimlar': Bolim.objects.all()[:4],
            'davomi': Bolim.objects.all()[4:],
            'mahsulotlar': mahsulotlar[:16],
            'mahsulotdavomi': mahsulotlar[16:]
        }
        return render(request, 'page-index-2.html', context)



class HomeView(View):
    def get(self, request):
        context = {
            'bolimlar': Bolim.objects.all()[:6],
             'davomi': Bolim.objects.all()[6:],
            "categorylar":  random.sample(list(Savat.objects.all()), 3), #Savat.objects.filter('mahsulot', distinct=True).order_by("-mahsulot")[:3]
            "karusellar": random.sample(list(Bolim.objects.all()), 3),
            "mahsulotlar": random.sample(list(Mahsulot.objects.all()), 12)
        }
        return render(request, 'page-index.html', context)




class BolimlarView(View):
    def get(self,request):
        context = {
            'bolimlar': Bolim.objects.all(),
        }
        return render(request, 'page-category.html', context)




class BolimView(View):
    def get(self,request, nom):
        context = {
            'bolimchalar': Ichki.objects.filter(bolim__nom=nom).order_by("-id")
        }
        return render(request, 'ichki.html', context)



class IchkiView(View):
    def get(self,request, pk):
        context = {
            'mahsulotlar': Mahsulot.objects.filter(ichki__id=pk)
        }
        return render(request, 'page-listing-grid.html', context)



class MahsulotView(View):
    def get(self, request,pk):
        context = {
            "mahsulot": Mahsulot.objects.get(id=pk),
        }
        return render(request,'page-detail-product.html', context)





class PageStarterView(View):
    def get(self,request):
        return render(request, 'page-blank-starter.html')




class PageComponents(View):
    def get(self, request):
        return render(request, 'page-components.html')





class PageContentView(View):
    def get(self,request):
        return render(request, 'page-content.html')




class PageListingLargeView(View):
    def get(self,request):
        return render(request, 'page-listing-large.html')




class PageOffersView(View):
    def get(self,request):
        return render(request, 'page-offers.html')




class PagePaymentView(View):
    def get(self, request):
        return render(request, 'page-payment.html')






class rtlPageDetailView(View):
    def get(self,request):
        return render(request, 'rtl-page-detail-product.html')



class SearchingView(View):
    def get(self,request, soz):
        mahsulotlar = Mahsulot.objects.filter(nom__contains=soz)
        if mahsulotlar is None or len(mahsulotlar) < 0:
            return redirect('/asosiy/page-search/<str:soz>/')

        else:
            context = {
                "mahsulotlar": mahsulotlar,

            }
            return render(request, 'page-searched.html', context)