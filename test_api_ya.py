import unittest
from api_ya import ApiYandexDisk, token
from unittest.mock import patch, MagicMock


class TestApiYa(unittest.TestCase):

    def setUp(self):
        self.api_ya_disk = ApiYandexDisk(token, 'new_folder')

    @patch('api_ya.requests')
    def test_create_new_folder_201(self, requests_mock):
        response_requests_mock = MagicMock()
        response_requests_mock.status_code = 201
        requests_mock.put.return_value = response_requests_mock
        self.assertEqual(self.api_ya_disk.create_new_folder(), 'Folder created')

    @patch('api_ya.requests')
    def test_create_new_folder_409(self, requests_mock):
        response_requests_mock = MagicMock()
        response_requests_mock.status_code = 409
        requests_mock.put.return_value = response_requests_mock
        self.assertEqual(self.api_ya_disk.create_new_folder(), 'A folder with the same name exists')

    @patch('api_ya.requests')
    def test_create_new_folder_400(self, requests_mock):
        response_requests_mock = MagicMock()
        response_requests_mock.status_code = 400
        requests_mock.put.return_value = response_requests_mock
        self.assertEqual(self.api_ya_disk.create_new_folder(), 'Incorrect data')

    @patch('api_ya.requests')
    def test_create_new_folder_401(self, requests_mock):
        response_requests_mock = MagicMock()
        response_requests_mock.status_code = 401
        requests_mock.put.return_value = response_requests_mock
        self.assertEqual(self.api_ya_disk.create_new_folder(), 'Not authorized')

    @patch('api_ya.requests')
    def test_create_new_folder_another_code(self, requests_mock):
        response_requests_mock = MagicMock()
        response_requests_mock.status_code = 404
        requests_mock.put.return_value = response_requests_mock
        self.assertEqual(self.api_ya_disk.create_new_folder(), 'Another mistake')
