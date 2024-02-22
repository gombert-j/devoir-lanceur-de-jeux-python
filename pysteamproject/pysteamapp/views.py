from django.template import loader
from django.http import HttpResponse
from .models import BibliothequeDeJeux, Jeux


# Create your views here.


def index(request):
    bibliotheques = BibliothequeDeJeux.objects.all()
    # template loader
    template = loader.get_template('liste_bibliotheques.html')
    context = {'bibliotheques': bibliotheques}
    return HttpResponse(template.render())



def liste_de_jeux(request):
    jeux = Jeux.objects.all()
    # template loader
    template = loader.get_template('liste_jeux.html')
    # context
    context = {'jeux': jeux}
    return HttpResponse(template.render(context, request))