class Record:

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        self.songs = []
        
    def get_title(self):
        return self.title.title()
    
    def get_year(self):
        return self.year
    
    def get_artist(self):
        return self.artist
    
    def get_songs(self):
        return self.songs
    
    def total_runtime(self):
        total_runtime = 0

        for song in self.songs:
            total_runtime += song.runtime
        
        return total_runtime
    
    def has_song(self, song):
        return song in self.songs

    def get_longest_song(self):
        longest_runtime = self.songs[0]
        for song in self.songs:
            if song.runtime > longest_runtime.runtime:
                longest_runtime = song

        return longest_runtime