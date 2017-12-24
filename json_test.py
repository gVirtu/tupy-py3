import unittest
import pytest
import subprocess

class TestJSONPrinter(unittest.TestCase):

    def test_simple_code(self):
        output = subprocess.getoutput("python3 -m tupy code/simple.uerj -t")
        self.assertEqual(output, "nadas")   

if __name__ == '__main__':
    unittest.main()
