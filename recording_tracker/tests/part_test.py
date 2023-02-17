import unittest
from models.part import Part
from models.song import Song


class TestPart(unittest.TestCase):
    def setUp(self):
        self.song1 = ("The Jester", "The Purple Felts", "The Jester's Game")
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
        actual = self.guitar1.song
        expected = None
        self.assertEqual(actual, expected)

    def test_has_instrument(self):
        actual = self.guitar1.instrument
        expected = ""
        self.assertEqual(actual, expected)

    def test_has_notes(self):
        actual = self.guitar1.notes
        expected = ""
        self.assertEqual(actual, expected)

    def test_has_id(self):
        actual = self.guitar1.id
        expected = None
        self.assertEqual(actual, expected)
