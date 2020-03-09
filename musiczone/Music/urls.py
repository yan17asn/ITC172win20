from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getArtist/', views.getArtist, name="artist"),
    path('getAlbum/', views.getAlbum, name="album"),
    path('getSong/', views.getSong, name="song"),
    path('getAlbumList/<int:id>', views.getAlbumList, name="albumlist"),
    path('getSongReview/<int:id>', views.getSongReview, name="songreview"),
    path('getArtistSong/<int:id>', views.getArtistSong, name="artistsong"),
    path('newGenre/',views.newGenre,name="newgenre"),
    path('newArtist/',views.newArtist,name="newartist"),
    path('newAlbum/',views.newAlbum,name="newalbum"),
    path('newSong/',views.newSong,name="newsong"),
    path('newSongReview/',views.newSongReview,name="newsongreview"),
    path('loginMessage/',views.loginMessage,name="loginmessage"),
    path('logoutMessage/',views.logoutMessage,name="logoutmessage")
]