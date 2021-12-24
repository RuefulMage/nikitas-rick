class Song:
    def __init__(self, Song = []):
        self.Song = Song

    def addSong(self, song):
        self.Song.append(song)

    def deleteSong(self, name):
        for i in range(len(self.Song)):
            if self.Song[i].name == name:
                self.Song.remove(self.Song[i])

    def isSongExists(self, name):
        for the_name in self.Song:
            if the_name.name == name:
                return the_name
            return False

    def printLibrary(self):
        if len(self.Song) == 0:
            print("No songs")
            return
        print("Song Library:")
        for song in self.Song:
            print(f"  Song name: {song.name}")
            print(f"  Author: {song.author}")
            print(f"  year: {song.year}")
            print(f"  album: {song.album}")
