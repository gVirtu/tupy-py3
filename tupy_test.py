import unittest
import pytest
import subprocess
import json

class TestTupyProgram(unittest.TestCase):

    def test_entrypoint_file(self):
        output = subprocess.getoutput("python3 -m tupy code/helloWorld.uerj")
        self.assertEqual(output, "Olá mundo!")       

    def test_entrypoint_filedebug(self):
        output = subprocess.getoutput("python3 -m tupy code/helloWorld.uerj --debug")
        self.assertNotEqual(output, "Olá mundo!") 
        self.assertEqual(output[-10:], "Olá mundo!")

    def test_entrypoint_filenotfound(self):
        output = subprocess.getoutput("python3 -m tupy code/filethatdoesnotexist.uerj")
        self.assertEqual(output, "Arquivo code/filethatdoesnotexist.uerj não encontrado!")       

    def test_entrypoint_trace(self):
        output = subprocess.getoutput("python3 -m tupy code/tracecoverage.uerj -t")
        result = json.loads(output)
        self.assertTrue("code" in result.keys())            
        self.assertTrue("trace" in result.keys())            
        self.assertEqual(len(result["trace"]), 12)

    def test_entrypoint_tracebars(self):
        output = subprocess.getoutput("python3 -m tupy code/tracebars.uerj -t")
        result = json.loads(output)
        self.assertTrue("code" in result.keys())            
        self.assertTrue("trace" in result.keys())            
        self.assertEqual(len(result["trace"]), 1)

    def test_entrypoint_traceexception(self):
        output = subprocess.getoutput("python3 -m tupy code/exception.uerj -t")
        result = json.loads(output)
        self.assertTrue("code" in result.keys())            
        self.assertTrue("trace" in result.keys())            
        self.assertEqual(len(result["trace"]), 4)
        self.assertEqual(result["trace"][-1]["event"], "exception")

    def test_entrypoint_tokens(self):
        output = subprocess.getoutput("python3 -m tupy code/helloWorld.uerj --tokens")
        self.assertEqual(output, ("=> NAME                   escrever\n"
                                  "=> OPEN_PAREN                    (\n"
                                  "=> STRING_LITERAL              Olá\n"
                                  "=> COMMA                         ,\n"
                                  "=> STRING_LITERAL           mundo!\n"
                                  "=> CLOSE_PAREN                   )\n"
                                  "=> NEWLINE                      \\n\n"
                                  "Olá mundo!"))

    def test_entrypoint_stdin(self):
        p = subprocess.Popen(['python3', '-m', 'tupy'], stdout=subprocess.PIPE, 
                                stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output = p.communicate(input=b'escrever("Teste")\n')[0]
        outputlines = output.decode().split("\n")
        self.assertEqual(outputlines[-2], "Teste")
        p.terminate()

    def test_hidden_variables(self):
        output = subprocess.getoutput("python3 -m tupy code/invisible.uerj -t")
        result = json.loads(output)
        self.assertTrue("code" in result.keys())            
        self.assertTrue("trace" in result.keys())            
        self.assertTrue( all( 
                            len(result["trace"][i]["ordered_globals"]) == 0 
                            for i in range(len(result["trace"])-1)
                         )) 

if __name__ == '__main__':
    unittest.main()
