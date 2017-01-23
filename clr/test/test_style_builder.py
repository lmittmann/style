import unittest
import sys

import clr


class StyleBuilderTestCase(unittest.TestCase):
    def test_single_string(self):
        # test styling of single string
        self.assertTrue('test' in clr.red('test'))
        self.assertTrue('31' in clr.red('test'))

    def test_multiple_strings(self):
        # test styling of multiple strings
        self.assertTrue('test1 test2' in clr.red('test1', 'test2'))
        self.assertTrue('31' in clr.red('test1', 'test2'))

    def test_non_string_arguments(self):
        # test styling of multiple arguments that are not strings
        self.assertTrue('1 True 0.1' in clr.red(1, True, 0.1))
        self.assertTrue('31' in clr.red(1, True, 0.1))

    def test_seperator(self):
        # test custom seperator
        self.assertTrue('test1, test2' in clr.red('test1', 'test2', sep=', '))

    def test_style_chaining(self):
        # test that chaining style attributes works
        self.assertTrue('31;47;1' in clr.red.bg_white.bold('test'))
        self.assertTrue('47;31;1' in clr.bg_white.red.bold('test'))
        self.assertTrue('47;1;31' in clr.bg_white.bold.red('test'))

if __name__ == '__main__':
    unittest.main()
