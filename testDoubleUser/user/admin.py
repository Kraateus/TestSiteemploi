from django.contrib import admin
from .models import User, Candidat, Recruteur, Entreprise
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


class CandidatInLine(admin.StackedInline):
    model = Candidat
    can_delete = False
    verbose_name_plural = 'Candidats'


class RecruteurInLine(admin.StackedInline):
    model = Recruteur
    can_delete = False
    verbose_name_plural = 'Recruteurs'


class UserAdmin(BaseUserAdmin):
    if User.is_recruteur:
        inlines = RecruteurInLine,
    elif User.is_candidat:
        inlines = CandidatInLine,
    else:
        inlines = ()
    list_display = ('username', 'email', 'is_candidat', 'is_recruteur', 'is_staff')


admin.site.register(Entreprise)
admin.site.register(User, UserAdmin)
