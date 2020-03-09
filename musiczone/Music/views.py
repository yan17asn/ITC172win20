from django.shortcuts import render,get_object_or_404
from .models import Artist, Album, Song, SongReview
from django.contrib.auth.decorators import login_required
from .forms import GenreForm, ArtistForm, AlbumForm, SongForm, SongReviewForm


# Create your views here.

#Index view
def index(request):
    return render(request,'Music/index.html')

#Artist list view
def getArtist(request):
    artist_list = Artist.objects.all()
    context={'artist_list':artist_list}
    return render(request, 'Music/artist.html', context=context)

#Album list view
def getAlbum(request):
    album_list = Album.objects.all()
    context={'album_list':album_list}
    return render(request, 'Music/album.html', context=context)

#Song list view
def getSong(request):
    song_list = Song.objects.all()
    context={'song_list':song_list}
    return render(request, 'Music/song.html', context=context)

#Album song list view
def getAlbumList(request,id):
    
    album_list = Song.objects.filter(album=id)
    context={
        'album_list': album_list
    }
    return render(request, 'Music/albumlist.html', context=context)

#Review list view
def getSongReview(request,id):
    s = get_object_or_404(Song, pk=id)
    title = s.songtitle
    artist = s.artist
    a = Artist.objects.get(name=artist)
    aid = a.id
    review_list = SongReview.objects.filter(song=id)
    context={
        'aid':aid,
        'title':title,
        'artist':artist,
        'review_list': review_list
    }
    return render(request, 'Music/songreview.html', context=context)

#Artist all song view
def getArtistSong(request,id):
    artist_song_list = Song.objects.filter(artist=id)
    context={
        'artist_song_list':artist_song_list,
    }
    return render(request, 'Music/artistsong.html', context=context)


#form view
@login_required
def newGenre(request):
    form=GenreForm
    if request.method=='POST':
        form=GenreForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=GenreForm()
    else:
        form=GenreForm()
    return render(request,'Music/newGenre.html',{'form':form})

@login_required
def newArtist(request):
    form=ArtistForm
    if request.method=='POST':
        form=ArtistForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ArtistForm()
    else:
        form=ArtistForm()
    return render(request,'Music/newArtist.html',{'form':form})

@login_required
def newAlbum(request):
    form=AlbumForm
    if request.method=='POST':
        form=AlbumForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=AlbumForm()
    else:
        form=AlbumForm()
    return render(request,'Music/newAlbum.html',{'form':form})

@login_required
def newSong(request):
    form=SongForm
    if request.method=='POST':
        form=SongForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=SongForm()
    else:
        form=SongForm()
    return render(request,'Music/newSong.html',{'form':form})

@login_required
def newSongReview(request):
    form=SongReviewForm
    if request.method=='POST':
        form=SongReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=SongReviewForm()
    else:
        form=SongReviewForm()
    return render(request,'Music/newSongReview.html',{'form':form})

def loginMessage(request):
    return render(request,'Music/loginMessage.html')

def logoutMessage(request):
    return render(request,'Music/logoutMessage.html')