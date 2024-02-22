from django.contrib import admin

# Register your models here.
from .models import Bibliotheque, Jeu

admin.site.register(Bibliotheque)
admin.site.register(Jeu)