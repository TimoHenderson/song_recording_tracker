import unittest
from models.song import Song
from models.part import Part


class TestSong(unittest.TestCase):
    def setUp(self):

        self.song3 = Song("SDKMN", "The Purple Felts", "The Jester's Game")
        self.parts_status = [3, 1]
        self.song1 = Song(
            "The Jester",
            "The Purple Felts",
            "The Jester's Game",
            "This needs more parts",
            self.parts_status,
        )

    def test_has_title(self):
        actual = self.song3.title
        expected = "SDKMN"
        self.assertEqual(actual, expected)

    def test_has_artist(self):
        actual = self.song3.artist
        expected = "The Purple Felts"
        self.assertEqual(actual, expected)

    def test_has_album(self):
        actual = self.song3.album
        expected = "The Jester's Game"
        self.assertEqual(actual, expected)

    def test_has_notes(self):
        actual = self.song3.notes
        expected = ""
        self.assertEqual(actual, expected)

    def test_has_parts(self):
        # breakpoint()
        actual = self.song3.parts_status
        expected = []
        self.assertEqual(actual, expected)

    def test_has_parts_local(self):
        actual = Song("ELP", "Tarkus", "Egg").parts_status
        expected = []
        self.assertEqual(actual, expected)

    def test_has_id(self):
        actual = self.song3.id
        expected = None
        self.assertEqual(actual, expected)

    def test_can_get_overall_completion__with_parts(self):
        actual = self.song1.get_completion()
        expected = 40
        self.assertEqual(actual, expected)

    def test_can_get_overall_completion__no_parts(self):
        actual = self.song3.get_completion()
        expected = 0
        self.assertEqual(actual, expected)

    def test_can_get_num_of_parts(self):
        actual = self.song1.get_num_parts()
        expected = 2
        self.assertEqual(actual, expected)
