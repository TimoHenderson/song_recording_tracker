import unittest
from models.artist import Artist


class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist1 = Artist("The Purple Felts")
        self.artist2 = Artist("U2", 1)

    def test_has_name(self):
        actual = self.artist1.name
        expected = "The Purple Felts"
        self.assertEqual(actual, expected)

    def test_has_id__no_id(self):
        actual = self.artist1.id
        expected = None
        self.assertEqual(actual, expected)

    def test_has_id__has_id(self):
        actual = self.artist2.id
        expected = 1
        self.assertEqual(actual, expected)
