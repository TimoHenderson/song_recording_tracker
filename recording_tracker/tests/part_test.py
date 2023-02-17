import unittest
from models.part import Part


class TestPart(unittest.TestCase):
    def setUp(self):
        self.guitar1 = Part("Verse Chords")

    def test_has_name(self):
        actual = self.guitar1.name
        expected = "Verse Chords"
        self.assertEqual(actual, expected)
