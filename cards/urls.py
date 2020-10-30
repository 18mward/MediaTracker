from django.urls import path
from .views import (
    CardListView,
    CardDetailView,
    MovieListView,
    SeriesListView,
    WatchedListView,
)

urlpatterns = [
    path('', CardListView.as_view(), name='card_list'),
    path('<int:pk>/', CardDetailView.as_view(), name='card_detail'),
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('series/', SeriesListView.as_view(), name='series_list'),
    path('watched_list/', WatchedListView.as_view(), name='watched_list'),
]
