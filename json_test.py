import unittest
import pytest
import sys
import io
from antlr4 import InputStream
import tupy

class TestJSONPrinter(unittest.TestCase):

    def test_simple_code(self):
        ret = tupy.main([None, "code/simple.uerj", "--trace"])
        self.assertEqual(ret, "nadas\n")

if __name__ == '__main__':
    unittest.main()
