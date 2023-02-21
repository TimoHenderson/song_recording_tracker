import unittest
from models.song import Song
from models.part import Part
from models.album import Album
from models.artist import Artist


class TestSong(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("The Purple Felts", 1)
        self.album = Album("The Jesters Game", self.artist, 1)
        self.parts_status = [3, 1]
        self.song3 = Song("SDKMN", self.album)

        self.song1 = Song(
            "The Jester",
            self.artist,
            [3, 5, 3],
            "This needs more parts",
            3,
        )

    def test_has_title(self):
        actual = self.song3.title
        expected = "SDKMN"
        self.assertEqual(actual, expected)

    def test_has_artist(self):
        actual = self.song3.album.artist.name
        expected = "The Purple Felts"
        self.assertEqual(actual, expected)

    def test_has_album(self):
        actual = self.song3.album.name
        expected = "The Jesters Game"
        self.assertEqual(actual, expected)

    def test_has_notes(self):
        actual = self.song3.notes
        expected = ""
        self.assertEqual(actual, expected)

    def test_has_parts(self):
        # breakpoint()
        actual = self.song3.parts_status
        expected = []
        self.assertEqual(actual, expected)

    def test_has_parts_local(self):
        actual = Song("Egg", self.album).parts_status
        expected = []
        self.assertEqual(actual, expected)

    def test_has_id(self):
        actual = self.song3.id
        expected = None
        self.assertEqual(actual, expected)

    def test_can_get_overall_completion__with_parts(self):
        actual = self.song1.get_completion()
        expected = 73
        self.assertEqual(actual, expected)

    def test_can_get_overall_completion__no_parts(self):
        actual = self.song3.get_completion()
        expected = 0
        self.assertEqual(actual, expected)

    def test_can_get_num_of_parts(self):
        actual = self.song1.get_num_parts()
        expected = 3
        self.assertEqual(actual, expected)
