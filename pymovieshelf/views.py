from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
import imdb
import re

from pymovieshelf.models import Movie


class MovieDetailView(DetailView):

    model = Movie


def staff_required(login_url=None):
    return user_passes_test(lambda u: u.is_staff, login_url=login_url)


@staff_required(login_url='/admin/')
def add_imdb(request):
    if request.POST and 'select' in request.POST:
        i = imdb.IMDb()
        try:
            m = i.get_movie(request.POST['movie_id'])
        except imdb.IMDbError:
            return render(request,
                          'pymovieshelf/add_imdb.html',
                          {'error': 'Failed to fetch movie info.'})

        try:
            t = m['canonical title'].strip()
        except KeyError:
            t = ''

        try:
            g = ', '.join(m['genres'])
        except KeyError:
            g = ''

        try:
            y = m['year']
        except KeyError:
            y = ''

        try:
            c = m['full-size cover url'].strip()
        except KeyError:
            c = ''

        try:
            s = m['plot summary'][0][:m['plot summary'][0].rfind('::')]
        except KeyError:
            s = ''

        try:
            r = re.sub(r'(USA\:)?(?P<runtime>\d+).*',
                       r'\g<runtime>',
                       m['runtime'][0])
        except KeyError:
            r = ''

        newmovie = Movie(title=t, fmt=request.POST['format'], genres=g, year=y,
                         summary=s, length=r, img=c,
                         url='http://www.imdb.com/title/tt%s/' %
                         (request.POST['movie_id'], ))
        newmovie.save()
        return redirect('/admin/pymovieshelf/movie/')
    elif request.POST and 'title' in request.POST:
        i = imdb.IMDb()
        movie_list = i.search_movie(request.POST['title'])
        return render(request,
                      'pymovieshelf/add_imdb.html',
                      {'movie_list': movie_list})
    else:
        return render(request,
                      'pymovieshelf/add_imdb.html',
                      {})


def search(request):
    if request.POST and 'title' in request.POST:
        movie_list = \
            Movie.objects.filter(title__icontains=request.POST['title'])
        return render(request,
                      'pymovieshelf/movie_list.html',
                      {'object_list': movie_list})
    else:
        return redirect('/pymovieshelf/')
