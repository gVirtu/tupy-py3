import unittest
import pytest
import tupy
import sys
import io

class TestTupyProgram(unittest.TestCase):

    def setUp(self):
        self.saved_stdout = sys.stdout
        self.out = io.StringIO()
        sys.stdout = self.out

    def tearDown(self):
        sys.stdout = self.saved_stdout  
    def test_entrypoint_file(self):
        ret = tupy.main([None, "code/helloWorld.uerj"])
        output = self.out.getvalue()
        self.assertEqual(output, "Olá mundo!\n")               

    def test_entrypoint_stdin(self):
        sys.stdin = io.StringIO("escrever(\"Teste\")\n")
        ret = tupy.main([None])
        output = self.out.getvalue()
        self.assertEqual(output, "Teste\n")

if __name__ == '__main__':
    unittest.main()
