from django.urls import path
from .views import *



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bolimlar/', BolimlarView.as_view(), name='bolimlar'),
    path('bolim/<str:nom>/', BolimView.as_view(), name='bolim'),

    path('ichki/<int:pk>/', IchkiView.as_view(), name='ichki-mahsulotlar'),

    path('mahsulot/<int:pk>/', MahsulotView.as_view(), name='mahsulot'),

    path('terms/', PageStarterView.as_view()),

    path('page-components/', PageComponents.as_view()),

    path('page-content/', PageContentView.as_view()),

    path('page-listing-large/', PageListingLargeView.as_view()),

    path('page-offers/', PageOffersView.as_view()),

    path('page-payment/', PagePaymentView.as_view()),





    path('page-rtl-page-product/', rtlPageDetailView.as_view()),



    path('page-search/<str:soz>/', SearchingView.as_view()),

]
