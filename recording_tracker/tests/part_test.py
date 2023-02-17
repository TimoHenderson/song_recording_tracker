import unittest
from models.part import Part


class TestPart(unittest.TestCase):
    def setUp(self):
        self.guitar1 = Part("Verse Chords", 5)

    def test_has_name(self):
        actual = self.guitar1.name
        expected = "Verse Chords"
        self.assertEqual(actual, expected)

    def test_has_status(self):
        actual = self.guitar1.status
        expected = 5
        self.assertEqual(actual, expected)
