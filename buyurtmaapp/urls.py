from django.urls import path
from .views import *
urlpatterns = [
    path('', BuyurtmaView.as_view()),
    path('buyurtma-qoshish/', BuyurtmaqoshishView.as_view()),
    path('tanlangan/', TanlanganView.as_view()),
    path('tanlangan-qoshish/<int:pk>/', TanlanganQoshishView.as_view()),
    path('tanlangan-ochirish/<int:pk>/', tanlangan_ochirish),
    path('savat/', SavatView.as_view()),
    path('savat_q/<int:pk>/', savat_qoshish),
    path('savat_k/<int:pk>/', savat_kamaytirish),
    path('savat-qoshish/<int:pk>/', SavatQoshishView.as_view()),
    path('savat-ochirish/<int:pk>/', savat_ochirish),

    path('page-profil-main/', PageProfilMainView.as_view()),

    path('page-profil-address/', PageProfilAddressView.as_view()),

    path('page-profil-settings/', PageProfilSettingView.as_view()),

    path('page-profil-seller/', PageProfileSellerView.as_view()),



]