import unittest
import pytest
import subprocess

class TestTupyProgram(unittest.TestCase):

    def test_entrypoint_file(self):
        output = subprocess.getoutput("python3 -m tupy code/helloWorld.uerj")
        self.assertEqual(output, "Olá mundo!")               

    def test_entrypoint_stdin(self):
        p = subprocess.Popen(['python3', '-m', 'tupy'], stdout=subprocess.PIPE, 
                                stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output = p.communicate(input=b'escrever("Teste")\n')[0]
        self.assertEqual(output.decode(), "Teste\n")

if __name__ == '__main__':
    unittest.main()
