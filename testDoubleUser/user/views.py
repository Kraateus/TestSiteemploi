from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView

from .models import User, Candidat, Recruteur
from .forms import CandidatSignUpForm, RecruteurSignUpForm, EntrepriseCreationForm


def CandidatSignUpView(request):
    if request.method == 'POST':
        form = CandidatSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            mail = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(mail=mail, password=raw_password)
            login(request, user)
            return redirect('user:home')
    else:
        form = CandidatSignUpForm()
    return render(request, 'user/candidat/signup.html', {'form': form})


def RecruteurSignUpView(request):
    if request.method == 'POST':
        form = RecruteurSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            mail = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(mail=mail, password=raw_password)
            login(request, user)
            return redirect('user:home')
    else:
        form = RecruteurSignUpForm
    return render(request, 'user/recruteur/signup.html', {'form': form})


def EntrepriseCreationView(request):
    if request.method == 'POST':
        form = EntrepriseCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:home')
    else:
        form = EntrepriseCreationForm
    return render(request, 'user/entreprise/creation.html', {'form': form})


class IndexView(ListView):
    model = Recruteur
    template_name = 'user/index.html'


class SignUpView(TemplateView):
    template_name = 'user/signup.html'
