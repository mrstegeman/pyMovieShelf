from django.conf.urls import url
from django.views.generic.list import ListView

from pymovieshelf.models import Movie
from pymovieshelf import views

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=Movie.objects.all().order_by('title'),
        paginate_by=50)),
    url(r'^add_imdb/', views.add_imdb),
    url(r'^search/', views.search),
    url(r'^(?P<pk>\d+)/$', views.MovieDetailView.as_view()),
]
