import unittest
from models.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song3 = Song("SDKMN", "The Purple Felts")

    def test_has_title(self):
        actual = self.song3.title
        expected = "SDKMN"
        self.assertEqual(actual, expected)

    def test_has_artist(self):
        actual = self.song3.artist
        expected = "The Purple Felts"
        self.assertEqual(actual, expected)
