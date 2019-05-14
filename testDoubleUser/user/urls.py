from django.urls import path
from . import views


app_name = 'user'
urlpatterns = [
    path('home/', views.IndexView.as_view(), name='home'),
    path('entreprise/', views.EntrepriseCreationView, name='entrepriseCreation'),
    path('signup/', views.SignUpView.as_view(), name='SignUp'),
    path('signup/candidat', views.CandidatSignUpView, name='candidatSignUp'),
    path('signup/recruteur', views.RecruteurSignUpView, name='recruteurSignUp'),
]
