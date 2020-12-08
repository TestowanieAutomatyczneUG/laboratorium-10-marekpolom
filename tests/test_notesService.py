import unittest
from unittest.mock import *
from assertpy import *
from parameterized import parameterized

import sample.note as note
import sample.notesStorage as serv

class TestNote(unittest.TestCase):

    def setUp(self):
        self.note = note.Note

    @parameterized.expand([
        ("Jan", 4.0),
    ])
    def test_notes_service_add(self, name, n):
        test_obj = serv.NotesService()
        test_obj.store.add = Mock(name='add')
        test_obj.store.add.return_value = True

        assert_that(test_obj.add(self.note(name, n))).is_true()

    def test_notes_service_clear(self):
        test_obj = serv.NotesService()
        test_obj.store.clear = Mock(name='clear')
        test_obj.store.clear.return_value = True

        assert_that(test_obj.clear()).is_true()

    @parameterized.expand([
        ("Jan", 4.0, 5.0, 3.0, 4.0),
    ])
    def test_notes_service_clear(self, name, n1, n2, n3, exp):
        test_obj = serv.NotesService()
        test_obj.store.getAllNotesOf = Mock(name='getAllNotesOf')
        test_obj.store.getAllNotesOf.return_value = [self.note(name, n1), self.note(name, n2), self.note(name, n3)]

        assert_that(test_obj.averageOf(name)).is_equal_to(exp)

if __name__ == '__main__':
    unittest.main()
