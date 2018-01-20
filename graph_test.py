import unittest
import pytest
import sys
import io
import random
import math
import builtins
from antlr4 import InputStream
from tupy.Instance import Instance
from tupy.Type import Type
from tupy.Interpreter import Interpreter, memRead
from tupy.Builtins import _graph_opts, _graph_highlight
from tupy.errorHelper import TupyNameError, TupyRuntimeError, TupySyntaxError, \
                             TupyTypeError, TupyValueError, TupyParseError, \
                             TupyIndexError

class TestGraphs(unittest.TestCase):
    def setUp(self):
        Interpreter.isDebug = False

    def test_graphviz_prints(self):
        extra = "0 [label = \"ABC\"]; "
        desired_graph = "".join(["[[DOT strict graph {", _graph_opts, extra, "0; 1; 2; 3; 1 ", _graph_highlight,
                         "0 -- 1; 0 -- 3; 1 -- 2; 2 -- 3; 0 [label = \"ABC\"]; }]]"])
        desired_digraph = "".join(["[[DOT digraph {", _graph_opts, extra, "0; 1; 2; 3; 2 ", _graph_highlight,
                         "0 -> 1; 1 -> 2; 2 -> 3; 3 -> 0; ", extra, "}]]"])

        ret = Interpreter.interpret(("inteiro grafo[4,4]\n"
                                     "grafo[0,1] <- grafo[1,0] <- 1\n"
                                     "grafo[2,1] <- grafo[1,2] <- 2\n"
                                     "grafo[2,3] <- grafo[3,2] <- 100\n"
                                     "grafo[0,3] <- grafo[3,0] <- 4\n"
                                     "grafo_MA(grafo, [1], \"0 [label = \\\"ABC\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_graph)

        ret = Interpreter.interpret(("inteiro digrafo[4,4]\n"
                                     "digrafo[0,1] <- 1\n"
                                     "digrafo[1,2] <- 7\n"
                                     "digrafo[2,3] <- 3\n"
                                     "digrafo[3,0] <- 44\n"
                                     "digrafo_MA(digrafo, [2], \"0 [label = \\\"ABC\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_digraph)

        ret = Interpreter.interpret(("inteiro grafo[4,*]\n"
                                     "grafo[0] <- inserir(grafo[0], 1)\n"
                                     "grafo[0] <- inserir(grafo[0], 3)\n"
                                     "grafo[1] <- inserir(grafo[1], 0)\n"
                                     "grafo[1] <- inserir(grafo[1], 2)\n"
                                     "grafo[2] <- inserir(grafo[2], 1)\n"
                                     "grafo[2] <- inserir(grafo[2], 3)\n"
                                     "grafo[3] <- inserir(grafo[3], 2)\n"
                                     "grafo[3] <- inserir(grafo[3], 0)\n"
                                     "grafo_LA(grafo, [1], \"0 [label = \\\"ABC\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_graph)

    def test_graphviz_prints2(self):
        extra = "0 [label = \"ABC\"]; "
        desired_digraph = "".join(["[[DOT digraph {", _graph_opts, extra, "0; 1; 2; 3; 2 ", _graph_highlight,
                         "0 -> 1; 1 -> 2; 2 -> 3; 3 -> 0; ", extra, "}]]"])

        ret = Interpreter.interpret(("inteiro digrafo[4,*]\n"
                                     "digrafo[0] <- inserir(digrafo[0], 1)\n"
                                     "digrafo[1] <- inserir(digrafo[1], 2)\n"
                                     "digrafo[2] <- inserir(digrafo[2], 3)\n"
                                     "digrafo[3] <- inserir(digrafo[3], 0)\n"
                                     "digrafo_LA(digrafo, [2], \"0 [label = \\\"ABC\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_digraph)

    def test_graphviz_errors(self):
        self.assertRaises(TupyValueError, Interpreter.interpret, 
                           ("inteiro grafo[2,1]\n"
                            "grafo_MA(grafo)\n"))
        self.assertRaises(TupyValueError, Interpreter.interpret, 
                           ("inteiro grafo[2,2]\n"
                            "grafo_MA(grafo, [0, 3])\n"))

        self.assertRaises(TupyValueError, Interpreter.interpret, 
                           ("inteiro digrafo[1,2]\n"
                            "digrafo_MA(digrafo)\n"))
        self.assertRaises(TupyValueError, Interpreter.interpret, 
                           ("inteiro digrafo[2,2]\n"
                            "digrafo_MA(digrafo, [1, 3])\n"))

        self.assertRaises(TupyIndexError, Interpreter.interpret, 
                           ("inteiro grafo[2,*] <- [ [3], [] ]\n"
                            "grafo_LA(grafo)\n"))
        self.assertRaises(TupyValueError, Interpreter.interpret, 
                           ("inteiro grafo[2,*]\n"
                            "grafo_LA(grafo, [0, 3])\n"))

        self.assertRaises(TupyIndexError, Interpreter.interpret, 
                           ("inteiro digrafo[2,*] <- [ [], [3] ]\n"
                            "digrafo_LA(digrafo)\n"))
        self.assertRaises(TupyValueError, Interpreter.interpret, 
                           ("inteiro digrafo[2,*]\n"
                            "digrafo_LA(digrafo, [1, 3])\n"))
    def test_graphviz_trees(self):
        tree_data = ("1 -> 2 [style = invis]; " 
                     "2 [style = invis]; "
                     "1 -> 3; " 
                     "3 [label = \"15\"]; "
                     "0 -> 1; "
                     "1 [label = \"10\"]; "
                     "4 -> 5; "
                     "5 [label = \"20\"]; " 
                     "4 -> 6 [style = invis]; "
                     "6 [style = invis]; "
                     "0 -> 4; "
                     "4 {0}"
                     "4 [label = \"3\"]; "
                     "0 [label = \"5\"]; "
                     "{{rank = same; 0; }}; "
                     "{{rank = same; 1; 4; }}; "
                     "{{rank = same; 2; 3; 5; 6; }}; ").format(_graph_highlight)
        desired_tree = "".join(["[[DOT digraph {", _graph_opts, tree_data, "}]]"])

        ret = Interpreter.interpret(("tipo Nó:\n"
                                     "\tinteiro c\n"
                                     "\tNó prox[2]\n"
                                     "\tNó(inteiro chave):\n"
                                     "\t\tc <- chave\n"
                                     "Nó raiz <- Nó(5)\n"
                                     "Nó n1 <- Nó(10)\n"
                                     "Nó n2 <- Nó(3)\n"
                                     "Nó n3 <- Nó(15)\n"
                                     "Nó n4 <- Nó(20)\n"
                                     "raiz.prox[0], raiz.prox[1] <- ref n1, n2\n"
                                     "n1.prox[1] <- ref n3\n"
                                     "n2.prox[0] <- ref n4\n"
                                     "arvore(raiz, \"c\", \"prox\", [n2])\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_tree)

    def test_graphviz_tree_errors(self):
        typedef = "tipo Nó:\n\tinteiro c\n\tNó prox[2]\n\tNó(inteiro chave):\n\t\tc <- chave\n"
        treebuild = (("Nó raiz <- Nó(5)\n"
                      "Nó n1 <- Nó(10)\n"
                      "Nó n2 <- Nó(3)\n"
                      "Nó n3 <- Nó(15)\n"
                      "Nó n4 <- Nó(20)\n"
                      "raiz.prox[0], raiz.prox[1] <- ref n1, n2\n"
                      "n1.prox[1] <- ref n3\n"
                      "n2.prox[0] <- ref n4\n"))

        self.assertRaises(TupyTypeError, Interpreter.interpret, "arvore(1)") # too few args
        self.assertRaises(TupyTypeError, Interpreter.interpret, "arvore(1, 2, 3, 4, 5, 6)") # too many args
        self.assertRaises(TupyTypeError, Interpreter.interpret, "arvore(1, 2, 3)") # not struct
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
            "{0}Nó raiz <- Nó(0); arvore(raiz, 2, 3)".format(typedef)) #not string
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
            "{0}Nó raiz <- Nó(0); arvore(raiz, \"c\", 3)".format(typedef)) #not string 2
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
            "{0}Nó raiz <- Nó(0); arvore(raiz, \"c\", \"prox\", 4)".format(typedef)) #not list
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
            ("{0}tipo Outro:\n"
             "\tinteiro c\n"
             "Nó raiz <- Nó(0); Outro outro <- Outro()\n"
             "arvore(raiz, \"c\", \"prox\", [outro])").format(typedef)) #not right class
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
            "{0}Nó raiz <- Nó(0); arvore(raiz, \"c\", \"prox\", [raiz], 0)".format(typedef)) #not string
        self.assertRaises(TupyNameError, Interpreter.interpret, 
            "{0}Nó raiz <- Nó(0); arvore(raiz, \"d\", \"prox\")".format(typedef)) #wrong attr
        self.assertRaises(TupyNameError, Interpreter.interpret, 
            "{0}Nó raiz <- Nó(0); arvore(raiz, \"c\", \"prod\")".format(typedef)) #wrong attr 2
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
            ("tipo Nó:\n"
            "\tinteiro c\n"
            "\tinteiro prox[2]\n"
            "Nó raiz <- Nó();\n"
            "arvore(raiz, \"c\", \"prox\")").format(typedef)) #wrong edge type
        self.assertRaises(TupyRuntimeError, Interpreter.interpret, 
            ("{0}{1}"
            "n4.prox[0] <- ref n2\n"
            "arvore(raiz, \"c\", \"prox\")").format(typedef, treebuild)) #tree has cycles

if __name__ == '__main__':
    unittest.main()
