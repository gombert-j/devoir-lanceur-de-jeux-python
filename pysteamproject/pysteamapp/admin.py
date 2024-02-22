from django.contrib import admin

# Register your models here.
from .models import BibliothequeDeJeux, Jeux

admin.site.register(BibliothequeDeJeux)
admin.site.register(Jeux)