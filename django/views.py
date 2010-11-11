from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
import imdb
from pymovieshelf.models import Movie
from django.contrib.auth.decorators import user_passes_test
import re

def staff_required(login_url=None):
        return user_passes_test(lambda u: u.is_staff, login_url=login_url)

@staff_required(login_url='/admin/')
def add_imdb(request):
    if request.POST and 'select' in request.POST:
        i = imdb.IMDb()
        try:
            m = i.get_movie(request.POST['movie_id'])
        except imdb.IMDbError:
            return render_to_response('pymovieshelf/add_imdb.html',
                    {'error': 'Failed to fetch movie info.',},
                    context_instance=RequestContext(request))

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
            r = re.sub(r'(USA\:)?(?P<runtime>\d+).*', r'\g<runtime>', m['runtime'][0])
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
        return render_to_response('pymovieshelf/add_imdb.html',
                {'movie_list': movie_list, },
                context_instance=RequestContext(request))
    else:
        return render_to_response('pymovieshelf/add_imdb.html',
                {},
                context_instance=RequestContext(request))

def search(request):
    if request.POST and 'title' in request.POST:
        movie_list = Movie.objects.filter(title__icontains=request.POST['title'])
        return render_to_response('pymovieshelf/movie_list.html',
                {'object_list': movie_list,},
                context_instance=RequestContext(request))
    else:
        return redirect('/pymovieshelf/')
