from django import forms
from .models import Genre, Artist, Album, Song, SongReview

class GenreForm(forms.ModelForm):
    class Meta:
        model=Genre
        fields='__all__'

class ArtistForm(forms.ModelForm):
    class Meta:
        model=Artist
        fields='__all__'

class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        fields='__all__'

class SongForm(forms.ModelForm):
    class Meta:
        model=Song
        fields='__all__'

class SongReviewForm(forms.ModelForm):
    class Meta:
        model=SongReview
        fields='__all__'