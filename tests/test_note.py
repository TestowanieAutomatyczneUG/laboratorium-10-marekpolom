import unittest
from assertpy import *
from parameterized import parameterized

import sample.note as note

class TestNote(unittest.TestCase):

    def setUp(self):
        self.note = note.Note

    @parameterized.expand([
        (None, 2.3),
        ("  ", 2.3),
        ("Name", 1.0),
        ("Name", 7.0),
        ("Name", 'To nie pangram'),
    ])
    def test_note_class_exception(self, name, n):
        assert_that(self.note).raises(Exception).when_called_with(name, n)

    @parameterized.expand([
        ('Name', 2.3),
    ])
    def test_note_get_name(self, name, n):
        x = self.note(name, n)

        assert_that(x.getName()).is_equal_to(name)

    @parameterized.expand([
        ("Name", 2.3),
    ])
    def test_note_get_note(self, name, n):
        x = self.note(name, n)

        assert_that(x.getNote()).is_equal_to(n)

    @parameterized.expand([
        ("Name", 2.3, float),
    ])
    def test_note_get_note_instance(self, name, n, exp):
        x = self.note(name, n)

        assert_that(x.getNote()).is_instance_of(exp)

    @parameterized.expand([
        ("Name", 2.3, str),
    ])
    def test_note_get_name_instance(self, name, n, exp):
        x = self.note(name, n)

        assert_that(x.getName()).is_instance_of(str)

if __name__ == '__main__':
    unittest.main()
