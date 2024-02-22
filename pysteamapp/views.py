from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Index of shared list')

# new_game()
def new_game(request):
    shopping_list = ShopList.objects.all()
    # template loader
    template = loader.get_template('shoplist.html')
    # context
    context = { 'shoplists': shopping_list}
    return HttpResponse(template.render(context, request))