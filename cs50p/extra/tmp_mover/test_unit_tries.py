import os
import unittest
from unittest.mock import patch

# testing the module mover
from mover import sort_by_extension


class TestSortByExtension(unittest.TestCase):

    @patch('mover.os.makedirs')
    @patch('mover.shutil.move')
    @patch('mover.os.walk')
    def test_sort_by_extension(self, mock_walk, mock_move, mock_makedirs):
        # test data - extension dictionary
        ext_dict = {".doc": "documents", ".jpg": "images", ".mp3": "music", ".unknown": "unknown"}
        # test_data = source folder
        source = os.path.join("/test_dir")
        # test data - return value for os.walk mock
        return_value = [
            ('/test_dir', ('subdir',), ('file1.doc', 'file2.jpg', 'file3.mp3', 'file4.unknown'))
        ]

        # mock the return value of os.walk in module mover
        mock_walk.return_value = return_value

        # code under test
        sort_by_extension(source, ext_dict)

        # assert calls to os.makedirs in module mover
        for key, value in ext_dict.items():
            os.path.join("test_dir")
            mock_makedirs.assert_any_call(os.path.join(source, value), exist_ok=True)

        # assert calls to shutil.move in module mover
        for file in return_value[0][2]:
            _, file_extension = os.path.splitext(file)
            mock_move.assert_any_call(os.path.join(source, file), os.path.join(
                source, ext_dict.get(file_extension), file))


if __name__ == '__main__':
    unittest.main()
