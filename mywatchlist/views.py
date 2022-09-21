from django.shortcuts import render
from .models import MyWatchList

from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_html(request):
    watchlist_objects = MyWatchList.objects.all()
    film_watched_counter = len(MyWatchList.objects.filter(is_watched=True))
    context  = {
        'watchlist_list': watchlist_objects,
        'name' : "Ardhito Nurhadyansah",
        'NPM' : "2106750206",
        'film_watched_amount': film_watched_counter,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


