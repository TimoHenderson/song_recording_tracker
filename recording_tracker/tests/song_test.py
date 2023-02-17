import unittest
from models.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song3 = Song("SDKMN")

    def test_has_title(self):
        actual = self.song3.title
        expected = "SDKMN"
        self.assertEqual(actual, expected)
