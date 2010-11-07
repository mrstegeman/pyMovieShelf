from django.conf.urls.defaults import *
from pymovieshelf.models import Movie

info_dict = {
        'queryset': Movie.objects.all().order_by('title'),
        }
urlpatterns = patterns(
    '',
    (r'^$', 'django.views.generic.list_detail.object_list', dict(info_dict, paginate_by=50)),
    (r'^add_imdb/', 'pymovieshelf.views.add_imdb'),
    (r'^search/', 'pymovieshelf.views.search'),
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
)
