from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
import requests

# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


def get_movies(request):
    headers = {}
    search_query = request.GET.get('search_query')
    url = 'https://api.themoviedb.org/3/search/movie?api_key=7a8e62877c1a69626e05867280207f00&language=en-US&page=1&include_adult=false&query=' + search_query
    response = requests.get(url)
    data = response.json()
    print(data)
    return render(request, 'search.html', data)

