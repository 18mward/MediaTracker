from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Card
from django.urls import reverse_lazy

class CardListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = 'card_list.html'
    login_url = 'login'

class MovieListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = 'movie_list.html'
    login_url = 'login'

class SeriesListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = 'series_list.html'
    login_url = 'login'
    
class WatchedListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = 'watched_list.html'
    login_url = 'login'

class CardDetailView(LoginRequiredMixin, DetailView):
    model = Card
    template_name = 'card_detial.html'
    login_url = 'login'
