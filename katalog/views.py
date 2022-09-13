from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    catalog_items_data = CatalogItem.objects.all()
    context = {
        'catalog_list' : catalog_items_data,
        'name' : 'Ardhito Nurhadyansah',
        'NPM'  : "2106750206",
    }
    return render(request, "katalog.html", context)
