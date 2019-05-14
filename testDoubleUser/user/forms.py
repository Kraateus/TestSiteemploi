from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import formset_factory
from .models import User, Candidat, Recruteur, Entreprise


class EntrepriseCreationForm(forms.Form):
    nom_entreprise = forms.CharField(max_length=250)
    numero = forms.IntegerField()
    adresse = forms.CharField()
    ville = forms.CharField()
    departement = forms.CharField()
    numero_departement = forms.CharField()
    code_postal = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = Entreprise

    @transaction.atomic
    def save(self):
        entreprise = Entreprise.objects.create()
        entreprise.nom_entreprise = self.cleaned_data.get('nom_entreprise')
        entreprise.numero = self.cleaned_data.get('numero')
        entreprise.adresse = self.cleaned_data.get('adresse')
        entreprise.ville = self.cleaned_data.get('ville')
        entreprise.departement = self.cleaned_data.get('departement')
        entreprise.numero_departement = self.cleaned_data.get('numero_departement')
        entreprise.code_postal = self.cleaned_data.get('code_postal')
        entreprise.save()
        return entreprise


class CandidatSignUpForm(UserCreationForm):
    nom_metier = forms.CharField(max_length=150)
    zone_recherche = forms.IntegerField(max_value=500, min_value=0)
    email = forms.EmailField(max_length=50)
    accepted_cgu = forms.BooleanField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_candidat = True
        user.email = self.cleaned_data.get('email')
        user.accepted_cgu = self.cleaned_data.get('accepted_cgu')
        user.save()
        candidat = Candidat.objects.create(user=user)
        candidat.nom_metier = self.cleaned_data.get('nom_metier')
        candidat.zone_recherche = self.cleaned_data.get('zone_recherche')
        candidat.save()
        return user


class RecruteurSignUpForm(UserCreationForm):
    Entreprises = formset_factory(EntrepriseCreationForm, extra=1, max_num=1)

    entreprise = forms.ModelChoiceField(queryset=Entreprise.objects, empty_label='Create yours')

    poste_entreprise = forms.CharField(max_length=150)
    numero = forms.CharField(max_length=200)
    pays = forms.CharField(max_length=250)
    accepted_cgu = forms.BooleanField()
    email = forms.EmailField(max_length=50)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_recruteur = True
        user.email = self.cleaned_data.get('email')
        user.accepted_cgu = self.cleaned_data.get('accepted_cgu')
        user.save()
        recruteur = Recruteur.objects.create(user=user)
        recruteur.entreprise = self.cleaned_data.get('entreprise')
        recruteur.poste_entreprise = self.cleaned_data.get('poste_entreprise')
        recruteur.numero = self.cleaned_data.get('numero')
        recruteur.pays = self.cleaned_data.get('pays')
        recruteur.save()
        return user




