import unittest
from models.instrument import Instrument


class TestInstrument(unittest.TestCase):
    def setUp(self):
        self.guitar = Instrument("Guitar", "fa-guitar")

    def test_has_name(self):
        actual = self.guitar.name
        expected = "Guitar"
        self.assertEqual(actual, expected)

    def test_has_icon(self):
        actual = self.guitar.icon
        expected = "fa-guitar"
        self.assertEqual(actual, expected)

    def test_has_id(self):
        actual = self.guitar.id
        expected = None
        self.assertEqual(actual, expected)
