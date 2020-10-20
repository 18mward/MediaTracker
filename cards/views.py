from django.views.generic import ListView, DetailView
from .models import Card

class CardListView(ListView):
    model = Card
    template_name = 'card_list.html'

class MovieListView(ListView):
    model = Card
    template_name = 'movie_list.html'

class SeriesListView(ListView):
    model = Card
    template_name = 'series_list.html'

class CardDetailView(DetailView):
    model = Card
    template_name = 'card_detial.html'
