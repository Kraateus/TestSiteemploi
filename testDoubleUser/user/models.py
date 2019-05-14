import os
from django.contrib.auth.models import AbstractUser
from django.db import models


class Entreprise(models.Model):
    nom_entreprise = models.CharField(max_length=250, default='none')
    numero = models.IntegerField(default=0)
    adresse = models.TextField(default='none')
    ville = models.CharField(max_length=100)
    departement = models.CharField(max_length=100)
    numero_departement = models.IntegerField(null=True)
    code_postal = models.CharField(max_length=12)


def get_image_path(instance, filename):
    return os.path.join('user', str(instance), filename)


class User(AbstractUser):
    is_candidat = models.BooleanField(default=False)
    is_recruteur = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    REQUIRED_FIELDS = ['username']
    accepted_cgu = models.BooleanField(default=False, null=True, blank=True)


class Recruteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recruteur', primary_key=True)

    entreprise = models.OneToOneField(Entreprise,
                                      on_delete=models.CASCADE,
                                      related_name='recruteur_entreprise',
                                      primary_key=False,
                                      blank=True,
                                      null=True)

    poste_entreprise = models.TextField(max_length=250, default='none')
    numero = models.CharField(max_length=200)
    pays = models.TextField(max_length=250, default='France')

    def __str__(self):
        return self.poste_entreprise


class Candidat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidat', primary_key=True)
    nom_metier = models.TextField(max_length=250)
    zone_recherche = models.IntegerField(default=0)

    def __str__(self):
        return self.nom_metier

    def __add__(self, other):
        self.nom_metier = self

