import directory


import unittest
from unittest import mock

# nosetests3 -v --with-coverage   --cover-package=directory test_directory.py


class DirectoryTest(unittest.TestCase):
    @mock.patch("pathlib.Path")
    @mock.patch("directory.check_directory", return_value=True)
    def test_create_exist_directory_with_test_should_return_path(
        self, check_directory_mock, path_mock
    ):
        dir_name = "test"

        path_mock_result = path_mock()

        result = directory.create_directory(dir_name)

        self.assertIs(result, path_mock_result)
        path_mock.assert_called()
        # path_mock_result.mkdir.assert_called()
        # path_mock_result.mkdir.assert_called_once()
        # path_mock_result.mkdir.assert_called_with(parents=True)

    @mock.patch("pathlib.Path")
    @mock.patch("directory.check_directory", return_value=False)
    def test_create_none_directory_with_test_should_return_path(
        self, check_directory_mock, path_mock
    ):
        dir_name = "test"

        result = directory.create_directory(dir_name)

        path_mock_result = path_mock()
        self.assertEqual(result, path_mock_result)

        path_mock_result.mkdir.assert_called()
        path_mock_result.mkdir.assert_called_once()
        path_mock_result.mkdir.assert_called_with(parents=True)

    def test_check_directory_with_test_should_true(self):
        path = mock.MagicMock()
        path.exists.return_value = True

        result = directory.check_directory(path)

        self.assertTrue(result)
