from django.views.generic import ListView
from .models import Card

class CardListView(ListView):
    model = Card
    template_name = 'card_list.html'
