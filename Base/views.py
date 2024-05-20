from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .formlar import RegisterForm, DersTalepleriForm, ProfileForm, OgrenciForm, EgitmenForm
from .models import DersTalepleri, EgitmenProfile, OgrenciProfile


def login_page(request):
  sayfa = 'login'
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, 'Böyle bi kullanıcı ismi bulunmuyor')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request,user)
      return redirect('Home')
    else:
      messages.error(request, 'Yanlış Şifre')
  context = {'sayfa': sayfa}
  return render(request, 'Log-Sign.html',context)



def logout_user(request):
  logout(request)
  return redirect('Home')


def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save() 
            if profile.kullanici_tipi == 'egitmen':
                d = {'profile':profile}
                egitmen = EgitmenProfile.objects.create(**d) 
                egitmen.save()
            elif profile.kullanici_tipi == 'ogrenci':
                d = {'profile':profile}
                ogrenci = OgrenciProfile.objects.create(**d)
                ogrenci.save()          
            login(request, user)
            return redirect('Home')  
    else:
        form = RegisterForm()
        profile_form = ProfileForm()
    context = {
       'form': form , 
       'profile_form': profile_form, 
       }
    return render(request, 'Log-Sign.html', context)


def MainPage(request):
  return render(request,'MainPage.html')


def OzelDers(request):
   return render(request,'OzelDers.html')


def biz_kimiz(request):
   return render(request,'hakkımızda.html')  


def derstalepleri(request):
   derstalepleri = DersTalepleri.objects.all()
   context = {'derstalepleri': derstalepleri}
   return render(request, 'DersTalepleri.html',context)



def TalepOlustur(request):
    user = request.user
    if request.method == 'POST':
        min=request.POST.get('min_butce')
        max=request.POST.get('max_butce')
        if max >= min:
           form = DersTalepleriForm(request.POST)
           if form.is_valid():
             ders_talebi = form.save(commit=False)
             ders_talebi.kullanici = user
             ders_talebi.save()
             return redirect('DersTalepleri')
        else:
            messages.error(request,'Minimum bütçe aralığı maksimum bütçe aralığından büyük olamaz')
            form = DersTalepleriForm()
    else:
        form = DersTalepleriForm()
    return render(request, 'TalepOluştur.html', {'form': form})



def talep_detay(request, pk):
    ders_talebi = DersTalepleri.objects.get(id=pk)
    return render(request, 'TalepDetay.html', {'ders_talebi': ders_talebi})


def talep_sil(request, pk):
   ders_talebi = DersTalepleri.objects.get(id=pk)
   ders_talebi.delete()
   return redirect('DersTalepleri')



def talep_duzenle(request, pk):
   ders_talebi = DersTalepleri.objects.get(id=pk)
   if request.method == 'POST':
        min=request.POST.get('min_butce')
        max=request.POST.get('max_butce')
        if max >= min:
           form = DersTalepleriForm(request.POST, instance=ders_talebi)
           if form.is_valid():
             form.save()
             return redirect('DersTalepleri')
        else:
            messages.error(request,'Minimum bütçe aralığı maksimum bütçe aralığından büyük olamaz')
            form = DersTalepleriForm()
   else:
      form = DersTalepleriForm(instance=ders_talebi)
    
   return render(request, 'TalepOluştur.html', {'form': form})



def talep_kabul(request,pk):
   ders_talebi = DersTalepleri.objects.get(id=pk)
   ders_talebi.talep_durumu = True
   ders_talebi.save()
   return redirect('DersTalepleri')


def Matematik(request):
    return render(request, 'OzelDers.html')


def Python(request):
    return render(request, 'OzelDers.html')


def Fizik(request):
    return render(request, 'OzelDers.html')


def Gitar(request):
    return render(request, 'OzelDers.html')




   

