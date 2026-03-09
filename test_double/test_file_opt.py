import unittest
import unittest.mock as mock
import file_opt


class TestFileOpt(unittest.TestCase):
    @mock.patch("os.path.isfile", return_value=True)
    @mock.patch("os.remove")
    def test_filename_is_lower(self, os_remove, os_path_isfile):
        filename = mock.MagicMock()
        filename.isupper.return_value = False
        file_opt.rm_when_lower(filename)

        os_path_isfile.assert_called()
        os_remove.assert_called()
        filename.isupper.assert_called()

    @mock.patch("os.path.isfile", return_value=True)
    @mock.patch("os.remove")
    def test_filename_is_upper(self, os_remove, os_path_isfile):
        filename = mock.MagicMock()
        filename.isupper.return_value = True
        file_opt.rm_when_lower(filename)

        os_path_isfile.assert_not_called()
        os_remove.assert_not_called()
        filename.isupper.assert_called()
