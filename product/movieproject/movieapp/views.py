from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie})


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('Name', )
        desc = request.POST.get('Dis', )
        year = request.POST.get('Year', )
        imges = request.FILES['img']
        movie = Movie(Name=name, Dis=desc, Year=year, img=imges)
        movie.save()

    return render(request, "add.html")


def update(request, id):
    movie = Movie.objects.get(id=id)
    forms = MovieForm(request.POST or None, request.FILES, instance=movie)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request, "edit.html", {'forms': forms, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
