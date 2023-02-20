import unittest
from models.artist import Artist


class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist1 = Artist("The Purple Felts")

    def test_has_name(self):
        actual = self.artist1.name
        expected = "The Purple Felts"
        self.assertEqual(actual, expected)
