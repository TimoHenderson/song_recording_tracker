import unittest
from models.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song3 = Song("SDKMN", "The Purple Felts", "The Jester's Game")

    def test_has_title(self):
        actual = self.song3.title
        expected = "SDKMN"
        self.assertEqual(actual, expected)

    def test_has_artist(self):
        actual = self.song3.artist
        expected = "The Purple Felts"
        self.assertEqual(actual, expected)

    def test_has_album(self):
        actual = self.song3.album
        expected = "The Jester's Game"
        self.assertEqual(actual, expected)

    def test_has_notes(self):
        actual = self.song3.notes
        expected = ""
        self.assertEqual(actual, expected)

    def test_has_parts(self):
        actual = self.song3.parts
        expected = []
        self.assertEqual(actual, expected)

    def test_has_id(self):
        actual = self.song3.id
        expected = None
        self.assertEqual(actual, expected)
