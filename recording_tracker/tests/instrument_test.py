import unittest
from models.instrument import Instrument


class TestInstrument(unittest.TestCase):
    def setUp(self):
        self.guitar = Instrument("Guitar")

    def test_has_name(self):
        actual = self.guitar.name
        expected = "Guitar"
        self.assertEqual(actual, expected)
