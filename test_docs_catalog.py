import unittest
from unittest.mock import Mock, patch

import docs_catalog
from docs_catalog import lists, documents, directories, people, shelf, add


class TestDocsCatalog(unittest.TestCase):

    def test_lists(self):
        self.assertEqual(lists(documents), [['passport', '2207 876234', 'Василий Гупкин'],
                                            ['invoice', '11-2', 'Геннадий Покемонов'],
                                            ['insurance', '10006', 'Аристарх Павлов']])

    def test_people_true(self):
        self.assertEqual(people(documents, '11-2'), 'Геннадий Покемонов')

    def test_people_false(self):
        self.assertEqual(people(documents, '111'), 'Человека с таким номером документа нет в нашей базе!')

    def test_shelf_true(self):
        self.assertEqual(shelf(directories, '11-2'), '1')

    def test_shelf_false(self):
        self.assertEqual(shelf(directories, '111'), 'Документа с таким номером нет на наших полках!')

    @patch('builtins.input')
    def test_add_true(self, mock_input):
        mock_input.add_type.return_value = 'passport'
        mock_input.add_number.return_value = '4835 765432'
        mock_input.add_name.return_value = 'Ivan'
        mock_input.add__number_shelf.return_value = '3'
        self.assertTrue(add(documents, directories))

    @patch('builtins.input')
    def test_add_false(self, mock_input):
        mock_input.add_type.return_value = 'passport'
        mock_input.add_number.return_value = '4835 765432'
        mock_input.add_name.return_value = 'Ivan'
        mock_input.add__number_shelf.return_value = '4'
        self.assertEqual(add(documents, directories), 'Данной полки в нашем архиве не существует.\nПопробуйте снова!')
