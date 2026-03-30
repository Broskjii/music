from django.shortcuts import redirect, render
from .models import Genre, Track
from .forms import GenreForm



def index(request):
    return render(request, 'main/index.html')


def genres(request):
    genres_list = Genre.objects.all()
    return render(request, "main/genres.html", {"genres": genres_list})


def tracks(request):
    tracks_list = Track.objects.prefetch_related("genres").all()
    return render(request, "main/tracks.html", {"tracks": tracks_list})

def add_genre(request):
    if request.method == "POST":
        genre = GenreForm(request.POST)
        if genre.is_valid():
            genre.save()
        return redirect('/genres')
    else:
        genreform = GenreForm()
        return render(request, "add_genre.html", {'form': genreform})
    
def edit_genre(request, id_genre):
    g = Genre.objects.get(id=id_genre)

    if request.method == "POST":

        genre = GenreForm(request.POST, instance=g)

        if genre.is_valid():
            genre.save()

        return redirect('/genres')

    else:
        genreform = GenreForm(instance=g)
        return render(request, "add_genre.html", {'form': genreform})
    


