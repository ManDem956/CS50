# testing the module main2.py
import unittest
from unittest.mock import patch
from main2 import sort_by_extension


class TestSortByExtension(unittest.TestCase):

    @patch('main2.os.makedirs')
    @patch('main2.shutil.move')
    @patch('main2.os.walk')
    def test_sort_by_extension(self, mock_walk, mock_move, mock_makedirs):
        mock_walk.return_value = [
            ('/test_dir', ('subdir',), ('file1.doc', 'file2.jpg', 'file3.mp3', 'file4.unknown'))
        ]

        sort_by_extension('/test_dir')

        mock_makedirs.assert_any_call('/test_dir/Document_Files', exist_ok=True)
        mock_makedirs.assert_any_call('/test_dir/Image_Files', exist_ok=True)
        mock_makedirs.assert_any_call('/test_dir/Audio_Files', exist_ok=True)
        mock_makedirs.assert_any_call('/test_dir/Unknown', exist_ok=True)

        mock_move.assert_any_call('/test_dir/file1.doc', '/test_dir/Document_Files/file1.doc')
        mock_move.assert_any_call('/test_dir/file2.jpg', '/test_dir/Image_Files/file2.jpg')
        mock_move.assert_any_call('/test_dir/file3.mp3', '/test_dir/Audio_Files/file3.mp3')
        mock_move.assert_any_call('/test_dir/file4.unknown', '/test_dir/Unknown/file4.unknown')


if __name__ == '__main__':
    unittest.main()
