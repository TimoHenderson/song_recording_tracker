import unittest
from models.album import Album
from models.artist import Artist


class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.artist1 = Artist("The Purple Felts", 1)
        self.album1 = Album("The Jester's Game", self.artist1)
        self.album2 = Album("The Jester's Game", self.artist1, [75, 50], 1)

    def test_has_name(self):
        actual = self.album1.name
        expected = "The Jester's Game"
        self.assertEqual(actual, expected)

    def test_has_artist(self):
        actual = self.album1.artist
        expected = self.artist1
        self.assertEqual(actual, expected)

    def test_has_id__no_id(self):
        actual = self.album1.id
        expected = None
        self.assertEqual(actual, expected)

    def test_has_id__has_id(self):
        actual = self.album2.id
        expected = 1
        self.assertEqual(actual, expected)

    def test_has_songs_completion__none_given(self):
        actual = self.album1.songs_completion
        expected = []
        self.assertEqual(actual, expected)

    def test_has_songs_completion__has(self):
        actual = self.album2.songs_completion
        expected = [75, 50]
        self.assertEqual(actual, expected)
