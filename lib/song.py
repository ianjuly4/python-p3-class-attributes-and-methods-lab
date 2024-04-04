class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name
    @property
    def artist(self):
        return self._artist
    @artist.setter
    def artist(self, artist):
        self._artist = artist
    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self, genre):
        self._genre = genre

    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment    

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in Song.genres:
            Song.genres.append(genre)
            print(Song.genres)
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in Song.artists:
            Song.artists.append(artist)
            print(Song.artists)
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
        print(Song.genre_count)
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

hot_in_here = Song("hot in here", "Nelly", "Rap")
thriller = Song("Thriller", "Michael Jackson", "Hip hop")
