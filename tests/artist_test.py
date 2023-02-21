import unittest
from models.artist import Artist


class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist1 = Artist("The Purple Felts")
        self.artist2 = Artist("U2", [50, 75], 1)

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

    def test_has_albums_completion__none_given(self):
        actual = self.artist1.albums_completion
        expected = []
        self.assertEqual(actual, expected)

    def test_has_albums_completion__has(self):
        actual = self.artist2.albums_completion
        expected = [50, 75]
        self.assertEqual(actual, expected)

    def test_can_get_completion(self):
        actual = self.artist2.get_completion()
        expected = 62
        self.assertEqual(actual, expected)

    def test_can_get_num_albums(self):
        actual = self.artist2.get_num_albums()
        expected = 2
        self.assertEqual(actual, expected)
