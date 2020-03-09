from django.test import TestCase
from django.urls import reverse
from .models import Genre, Artist, Album, Song, SongReview
from django.contrib.auth.models import User
from .forms import GenreForm, ArtistForm, AlbumForm, SongForm, SongReviewForm

# Create your tests here.

# ==================  Genre Model ========================
class GenreTest(TestCase):
    def setUp(self):
       genre = Genre(genrename='Pop')
       return genre
    
    #test string
    def test_string(self):
       gen = self.setUp()
       self.assertEqual(str(gen), gen.genrename)

   # test Genre table.
    def test_table(self):
       self.assertEqual(str(Genre._meta.db_table), 'genre')

# ==================  Artist Model ========================
class ArtistTest(TestCase):
    def setUp(self):
        artist = Artist(name='Taylor Swift',born='1989-12-31',url='https://en.wikipedia.org/wiki/Taylor_Swift',
        description='Taylor Alison Swift is an American singer-songwriter.')
        return artist
    
    #test string
    def test_string(self):
        art = self.setUp()
        self.assertEqual(str(art), art.name)

    def test_born(self):
        art = self.setUp()
        self.assertEqual(str(art.born),'1989-12-31')

    def test_url(self):
        art = self.setUp()
        self.assertEqual(str(art.url),'https://en.wikipedia.org/wiki/Taylor_Swift')

    def test_description(self):
        art = self.setUp()
        self.assertEqual(str(art.description),'Taylor Alison Swift is an American singer-songwriter.')

    # test Artist table.
    def test_table(self):
       self.assertEqual(str(Artist._meta.db_table), 'artist')

# ==================  Album Model ========================
class AlbumTest(TestCase):
    def setUp(self):
        artist = Artist(name='Taylor Swift')
        album = Album(albumtitle='Fearless',artist=artist,releasedate='2008-11-11')
        return album
    
    #test string
    def test_string(self):
        alb = self.setUp()
        self.assertEqual(str(alb), alb.albumtitle)

    def test_artist(self):
        alb = self.setUp()
        self.assertEqual(str(alb.artist),'Taylor Swift')

    def test_releasedate(self):
        alb = self.setUp()
        self.assertEqual(str(alb.releasedate),'2008-11-11')

    # test Album table.
    def test_table(self):
       self.assertEqual(str(Album._meta.db_table), 'album')

# ==================  Song Model ========================
class SongTest(TestCase):
    def setUp(self):
        album = Album(albumtitle='Fearless')
        artist = Artist(name='Taylor Swift')
        genre = Genre(genrename='Pop')
        song = Song(songtitle='Love Stroy',album=album,artist=artist,genre=genre,track='3',length='3:55')
        return song
    
    #test string
    def test_string(self):
        son = self.setUp()
        self.assertEqual(str(son), son.songtitle)

    def test_album(self):
        son = self.setUp()
        self.assertEqual(str(son.album),'Fearless')

    def test_artist(self):
        son = self.setUp()
        self.assertEqual(str(son.artist),'Taylor Swift')

    def test_genre(self):
        son = self.setUp()
        self.assertEqual(str(son.genre),'Pop')

    def test_track(self):
        son = self.setUp()
        self.assertEqual(str(son.track),'3')

    def test_length(self):
        son = self.setUp()
        self.assertEqual(str(son.length),'3:55')

    # test Song table.
    def test_table(self):
       self.assertEqual(str(Song._meta.db_table), 'song')

    # ==================  SongReview Model ========================
class SongReviewTest(TestCase):
    def setUp(self):
        song = Song(songtitle='Love Stroy')
        sr = SongReview(song=song, rating='10', reviews='Good song!')
        return sr
    
    #test string
    def test_string(self):
        sr = self.setUp()
        self.assertEqual(str(sr), sr.reviews)

    def test_song(self):
        sr = self.setUp()
        self.assertEqual(str(sr.song),'Love Stroy')

    def test_postby(self):
        song = Song(songtitle='Love Stroy')
        user = User.objects.create(username='User001')
        sr = SongReview(song=song, postby=user,rating='10', reviews='Good song!')
        self.assertEqual(str(sr.postby),'User001')

    def test_reviews(self):
        sr = self.setUp()
        self.assertEqual(str(sr.reviews),'Good song!')

    # test SongReview table.
    def test_table(self):
       self.assertEqual(str(SongReview._meta.db_table), 'songreview')

# ==================  View_url Test ========================
        
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
       response=self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)

class ArtistViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
       response=self.client.get(reverse('artist'))
       self.assertEqual(response.status_code, 200)

class AlbumViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
       response=self.client.get(reverse('album'))
       self.assertEqual(response.status_code, 200)

class SongViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
       response=self.client.get(reverse('song'))
       self.assertEqual(response.status_code, 200)

class SongList_SongReview_ViewTest(TestCase):
    def setUp(self):
       self.u = User.objects.create(username='User001')
       self.genre = Genre.objects.create(genrename='Pop')
       self.artist = Artist.objects.create(name='Taylor Swift',born='1989-12-31',url='https://en.wikipedia.org/wiki/Taylor_Swift',
        description='Taylor Alison Swift is an American singer-songwriter.')
       self.album = Album.objects.create(albumtitle='Fearless',artist=self.artist,releasedate='2008-11-11')
       self.song = Song.objects.create(songtitle='Love Stroy',album=self.album,artist=self.artist,genre=self.genre,track='3',length='5:20')
       self.songreview = SongReview.objects.create(song=self.song, postby=self.u,rating='10', reviews='Good song!')
       
        
    def test_album_list_success(self):
        response = self.client.get(reverse('albumlist', args=(self.album.id,)))
        self.assertEqual(response.status_code, 200)

    def test_review_list_success(self):
        response = self.client.get(reverse('songreview', args=(self.song.id,)))
        self.assertEqual(response.status_code, 200)
    
    def test_artist_song_list_success(self):
        response = self.client.get(reverse('artistsong', args=(self.artist.id,)))
        self.assertEqual(response.status_code, 200)

class New_Genre_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.gen = Genre(genrename='Pop')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newgenre'))
        self.assertRedirects(response, '/accounts/login/?next=/Music/newGenre/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newgenre'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Music/newGenre.html')

class New_Artist_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.artist = Artist(name='Taylor Swift',born='1989-12-31',url='https://en.wikipedia.org/wiki/Taylor_Swift',
        description='Taylor Alison Swift is an American singer-songwriter.')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newartist'))
        self.assertRedirects(response, '/accounts/login/?next=/Music/newArtist/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newartist'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Music/newArtist.html')

class New_Album_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.artist = Artist(name='Taylor Swift')
        self.album = Album(albumtitle='Fearless',artist=self.artist,releasedate='2008-11-11')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newalbum'))
        self.assertRedirects(response, '/accounts/login/?next=/Music/newAlbum/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newalbum'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Music/newAlbum.html')

class New_Song_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.album = Album(albumtitle='Fearless')
        self.artist = Artist(name='Taylor Swift')
        self.genre = Genre(genrename='Pop')
        self.song = Song(songtitle='Love Stroy',album=self.album,artist=self.artist,genre=self.genre,track='3',length='5:20')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newsong'))
        self.assertRedirects(response, '/accounts/login/?next=/Music/newSong/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newsong'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Music/newSong.html')

class New_SongReview_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.song = Song(songtitle='Love Stroy')
        self.songreview = SongReview(song=self.song, postby=self.test_user,rating='10', reviews='Good song!')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newsongreview'))
        self.assertRedirects(response, '/accounts/login/?next=/Music/newSongReview/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newsongreview'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Music/newSongReview.html')

# ==================  Form Test ========================

class Genre_Form_Test(TestCase):
    def test_genre_form_is_valid(self):
      form = GenreForm(data={'genrename':"Pop"})
      self.assertTrue(form.is_valid())

    def test_genre_form_empty(self):
      form = GenreForm(data={'genrename':""})
      self.assertFalse(form.is_valid())

class Artist_Form_Test(TestCase):
    def test_artist_form_is_valid(self):
      form = ArtistForm(data={'name':"Taylor Swift",'born':"1989-12-31",'url':"https://en.wikipedia.org/wiki/Taylor_Swift",
      'description':"Taylor Alison Swift is an American singer-songwriter."})
      self.assertTrue(form.is_valid())

    def test_artist_form_minus_url(self):
      form = ArtistForm(data={'name':"Taylor Swift",'born':"1989-12-31",'description':"Taylor Alison Swift is an American singer-songwriter."})
      self.assertTrue(form.is_valid())

    def test_artist_form_minus_description(self):
      form = ArtistForm(data={'name':"Taylor Swift",'born':"1989-12-31",'url':"https://en.wikipedia.org/wiki/Taylor_Swift"})
      self.assertTrue(form.is_valid())
      
    def test_artist_form_empty(self):
      form = ArtistForm(data={'name':""})
      self.assertFalse(form.is_valid())

class Album_Form_Test(TestCase):
    def test_album_form_is_valid(self):
      self.artist = Artist.objects.create(name='Taylor Swift',born='1989-12-31',url='https://en.wikipedia.org/wiki/Taylor_Swift',
        description='Taylor Alison Swift is an American singer-songwriter.')
      form = AlbumForm(data={'albumtitle':"Fearless",'artist':self.artist,'releasedate':"2008-11-11"})
      self.assertTrue(form.is_valid())

    def test_album_form_empty(self):
      form = AlbumForm(data={'albumtitle':""})
      self.assertFalse(form.is_valid())

class Song_Form_Test(TestCase):
    def test_song_form_is_valid(self):
      self.genre = Genre.objects.create(genrename='Pop')
      self.artist = Artist.objects.create(name='Taylor Swift',born='1989-12-31',url='https://en.wikipedia.org/wiki/Taylor_Swift',
        description='Taylor Alison Swift is an American singer-songwriter.')
      self.album = Album.objects.create(albumtitle='Fearless',artist=self.artist,releasedate='2008-11-11')
      form = SongForm(data={'songtitle':"Love Story",'album':self.album,'artist':self.artist,'genre':self.genre,'track':"3",'length':"5:20"})
      self.assertTrue(form.is_valid())

    def test_song_form_minus_track(self):
      self.genre = Genre.objects.create(genrename='Pop')
      self.artist = Artist.objects.create(name='Taylor Swift',born='1989-12-31',url='https://en.wikipedia.org/wiki/Taylor_Swift',
        description='Taylor Alison Swift is an American singer-songwriter.')
      self.album = Album.objects.create(albumtitle='Fearless',artist=self.artist,releasedate='2008-11-11')
      form = SongForm(data={'songtitle':"Love Story",'album':self.album,'artist':self.artist,'genre':self.genre,'length':"5:20"})
      self.assertTrue(form.is_valid())

    def test_song_form_minus_length(self):
      self.genre = Genre.objects.create(genrename='Pop')
      self.artist = Artist.objects.create(name='Taylor Swift',born='1989-12-31',url='https://en.wikipedia.org/wiki/Taylor_Swift',
        description='Taylor Alison Swift is an American singer-songwriter.')
      self.album = Album.objects.create(albumtitle='Fearless',artist=self.artist,releasedate='2008-11-11')
      form = SongForm(data={'songtitle':"Love Story",'album':self.album,'artist':self.artist,'genre':self.genre,'track':"3"})
      self.assertTrue(form.is_valid())

    def test_song_form_empty(self):
      form = SongForm(data={'songtitle':""})
      self.assertFalse(form.is_valid())

class SongReview_Form_Test(TestCase):
    def test_song_review_form_is_valid(self):
      self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
      self.genre = Genre.objects.create(genrename='Pop')
      self.artist = Artist.objects.create(name='Taylor Swift',born='1989-12-31',url='https://en.wikipedia.org/wiki/Taylor_Swift',
        description='Taylor Alison Swift is an American singer-songwriter.')
      self.album = Album.objects.create(albumtitle='Fearless',artist=self.artist,releasedate='2008-11-11')
      self.song = Song.objects.create(songtitle='Love Stroy',album=self.album,artist=self.artist,genre=self.genre,track='3',length='5:20')
      form = SongReviewForm(data={'song':self.song,'postby':self.test_user,'rating':"10",'reviews':"Good song!"})
      self.assertTrue(form.is_valid())

    def test_song_review_form_empty(self):
      form = SongReviewForm(data={'reviews':""})
      self.assertFalse(form.is_valid())





    
        



    