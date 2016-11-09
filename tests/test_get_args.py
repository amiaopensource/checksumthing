from unittest import TestCase
from unittest.mock import patch
from scripts import args


class TestGet_args(TestCase):

    def test_get_args_help(self):
        testargs = ["-h"]
        with patch('sys.argv', testargs):
            arg = args.get_args()
            self.assertEqual(arg, arg)


    def test_get_args_nospace(self):
        testargs = ["-i ./Checksums/1", "-ie .md5", "-t md5", "-c lower", "-b 12345", "-a asdfdasf", "-ns"]
        with patch('sys.argv', testargs):
            arg = args.get_args()
            self.assertEqual(arg.noSpace, True)
