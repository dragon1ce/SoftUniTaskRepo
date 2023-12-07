from typing import List
from project.song import Song


class Album:

    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.songs: List[Song] = [*songs]
        self.published: bool = False

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song in self.songs:
            return f"Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."
        for s in self.songs:
            if s.name == song_name:
                self.songs.remove(s)
                return f"Removed song {song_name} from album {self.name}."
        return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        elif not self.published:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        return_str = [f"Album {self.name}"]
        for s in self.songs:
            return_str.append(f"== {s.get_info()}")
        return '\n'.join(return_str)


