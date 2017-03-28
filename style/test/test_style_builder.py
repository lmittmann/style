import unittest
import sys

import style


class StyleBuilderTestCase(unittest.TestCase):
    def test_single_string(self):
        # test styling of single string
        self.assertTrue('test' in style.red('test'))
        self.assertTrue('31' in style.red('test'))

    def test_multiple_strings(self):
        # test styling of multiple strings
        self.assertTrue('test1 test2' in style.red('test1', 'test2'))
        self.assertTrue('31' in style.red('test1', 'test2'))

    def test_non_string_arguments(self):
        # test styling of multiple arguments that are not strings
        self.assertTrue('1 True 0.1' in style.red(1, True, 0.1))
        self.assertTrue('31' in style.red(1, True, 0.1))

    def test_seperator(self):
        # test custom seperator
        self.assertTrue('test1, test2' in style.red('test1', 'test2', sep=', '))

    def test_non_string_seperator(self):
        # test if a non string seperator raises a TypeError
        with self.assertRaises(TypeError):
            style.red('test1', 'test2', sep=0)

    def test_style_chaining(self):
        # test that chaining style attributes works
        self.assertTrue('31;47;1' in style.red.on_white.bold('test'))
        self.assertTrue('47;31;1' in style.on_white.red.bold('test'))
        self.assertTrue('47;1;31' in style.on_white.bold.red('test'))

if __name__ == '__main__':
    unittest.main()