import unittest
from models.part import Part
from models.song import Song
from models.instrument import Instrument


class TestPart(unittest.TestCase):
    def setUp(self):
        self.song1 = ("The Jester", "The Purple Felts", "The Jester's Game")
        self.guitar1 = Part("Verse Chords", 5, self.song1)
        self.instrument = Instrument("guitar", "e92c", 2)
        self.guitar2 = Part("Chorus Shred", "3", 1, self.instrument)
        self.part3 = Part("Solo", 2)

    def test_has_name(self):
        actual = self.guitar1.name
        expected = "Verse Chords"
        self.assertEqual(actual, expected)

    def test_has_status(self):
        actual = self.guitar1.status
        expected = 5
        self.assertEqual(actual, expected)

    def test_has_song__none(self):
        actual = self.part3.song
        expected = None
        self.assertEqual(actual, expected)

    def test_has_song__song(self):
        actual = self.guitar1.song
        expected = self.song1
        self.assertEqual(actual, expected)

    def test_has_instrument(self):
        actual = self.guitar1.instrument
        expected = None
        self.assertEqual(actual, expected)

    def test_has_notes(self):
        actual = self.guitar1.notes
        expected = ""
        self.assertEqual(actual, expected)

    def test_has_id(self):
        actual = self.guitar1.id
        expected = None
        self.assertEqual(actual, expected)

    def test_get_status_string(self):
        actual = self.guitar1.get_status_str()
        expected = "Take!"
        self.assertEqual(actual, expected)

    def test_has_instrument__added(self):
        actual = self.guitar2.instrument
        expected = self.instrument
        self.assertEqual(actual, expected)
