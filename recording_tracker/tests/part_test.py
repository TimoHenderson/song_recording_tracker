import unittest
from models.part import Part
from models.song import Song


class TestPart(unittest.TestCase):
    def setUp(self):
        # self.song1 =
        self.guitar1 = Part("Verse Chords", 5)

    def test_has_name(self):
        actual = self.guitar1.name
        expected = "Verse Chords"
        self.assertEqual(actual, expected)

    def test_has_status(self):
        actual = self.guitar1.status
        expected = 5
        self.assertEqual(actual, expected)

    def test_has_song(self):
        actual = self.guitar1.status
        expected = 5
        self.assertEqual(actual, expected)
