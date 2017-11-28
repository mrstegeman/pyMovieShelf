# Description

pyMovieShelf is a Python/Django based DVD and Blu-ray collection manager. It allows a user to search for and select a movie from IMDb's database. When selected, info from IMDb will be imported into the database. The user is presented with a full movie list, as well as a details page for each movie. Details shown for each movie include title, year, genres, length, a plot summary, format (DVD/Blu-ray/digital), and a movie poster.

# Requirements

Besides Django (tested with 1.11), pyMovieShelf requires IMDbPY (http://imdbpy.sourceforge.net/).

# Usage

## Populate Database

```
$ python3 manage.py sqlmigrate pymovieshelf 0001
$ python3 manage.py migrate
```

## Run Server

`$ python3 manage.py runserver`
