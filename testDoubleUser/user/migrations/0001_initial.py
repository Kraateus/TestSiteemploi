# Generated by Django 2.2 on 2019-05-14 08:24

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_candidat', models.BooleanField(default=False)),
                ('is_recruteur', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('accepted_cgu', models.BooleanField(blank=True, default=False, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdresseEntreprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='candidat', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nom_metier', models.TextField(max_length=250)),
                ('zone_recherche', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.TextField()),
                ('departement', models.TextField()),
                ('numero_departement', models.IntegerField()),
                ('code_postal', models.TextField()),
                ('adresse', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='adresse', to='user.AdresseEntreprise')),
            ],
        ),
        migrations.CreateModel(
            name='Recruteur',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='recruteur', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nom_entreprise', models.TextField(default='none', max_length=250)),
                ('poste_entreprise', models.TextField(default='none', max_length=250)),
                ('numero', models.IntegerField(default=0)),
                ('pays', models.TextField(default='France', max_length=250)),
                ('entreprise', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recruteur_entreprise', to='user.Entreprise')),
            ],
        ),
    ]
