from django.template import loader
from django.http import HttpResponse
from .models import Bibliotheque, Jeu


# Create your views here.


def index(request):
    bibliotheques = Bibliotheque.objects.all()
    # template loader
    template = loader.get_template('liste_bibliotheques.html')
    context = {'bibliotheques': bibliotheques}
    return HttpResponse(template.render())



def liste_de_jeux(request):
    jeux = Jeu.objects.all()
    # template loader
    template = loader.get_template('liste_jeux.html')
    # context
    context = {'jeux': jeux}
    return HttpResponse(template.render(context, request))