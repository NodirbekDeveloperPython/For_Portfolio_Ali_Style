from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.core.mail import send_mail
from django.conf import settings



class RegisterView(View):
    def get(self,request):
        return render(request, 'page-user-register.html')


    def post(self, request):
        if request.POST.get('p1') != request.POST.get('p2'):
            return redirect('/user/register/')
        else:
            user = User.objects.create_user(
                username=request.POST.get('email'),
                password=request.POST.get('p1'),
                first_name = request.POST.get('f_name'),
                last_name=request.POST.get('l_name'),
                email=request.POST.get('email')
            )

            profil = Profil.objects.create(
                shahar = request.POST.get("sh"),
                tel = request.POST.get("tel"),
                jins = request.POST.get("jins"),
                user = user
            )

            send_mail(
                subject='Assalomu Alaykum',
                message="Alistyle onlayn do'koniga xush kelibsiz !"
                        "Maroqli xarid tilaymiz.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=True
            )

            return redirect("/user/login/")


class LoginView(View):
    def get(self,request):
        return render(request, 'page-user-login.html')

    def post(self,request):
        user = authenticate(username=request.POST.get('l'), password=request.POST.get('p'))
        if user is None or request.POST.get('remember') != "on":
            return redirect('/user/login/')
        login(request, user)
        return redirect('/asosiy/')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/user/login/')