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
                         "0 -- 1 []; 0 -- 3 [color=\"red\"; ]; 1 -- 2 []; 2 -- 3 []; 0 [label = \"ABC\"]; }]]"])
        desired_digraph = "".join(["[[DOT digraph {", _graph_opts, extra, "0; 1; 2; 3; 2 ", _graph_highlight,
                         "0 -> 1 []; 1 -> 2 []; 2 -> 3 []; 3 -> 0 [color=\"red\"; ]; ", extra, "}]]"])

        ret = Interpreter.interpret(("inteiro grafo[4,4]\n"
                                     "grafo[0,1] <- grafo[1,0] <- 1\n"
                                     "grafo[2,1] <- grafo[1,2] <- 2\n"
                                     "grafo[2,3] <- grafo[3,2] <- 100\n"
                                     "grafo[0,3] <- grafo[3,0] <- 4\n"
                                     "grafo_MA(grafo, [1], [[3,0]], \"0 [label = \\\"ABC\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_graph)

        ret = Interpreter.interpret(("inteiro digrafo[4,4]\n"
                                     "digrafo[0,1] <- 1\n"
                                     "digrafo[1,2] <- 7\n"
                                     "digrafo[2,3] <- 3\n"
                                     "digrafo[3,0] <- 44\n"
                                     "digrafo_MA(digrafo, [2], [[3,0]], \"0 [label = \\\"ABC\\\"]; \")\n"))

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
                                     "grafo_LA(grafo, [1], [[3,0]], \"0 [label = \\\"ABC\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_graph)

        ret = Interpreter.interpret(("inteiro digrafo[4,*]\n"
                                     "digrafo[0] <- inserir(digrafo[0], 1)\n"
                                     "digrafo[1] <- inserir(digrafo[1], 2)\n"
                                     "digrafo[2] <- inserir(digrafo[2], 3)\n"
                                     "digrafo[3] <- inserir(digrafo[3], 0)\n"
                                     "digrafo_LA(digrafo, [2], [[3,0]], \"0 [label = \\\"ABC\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_digraph)

    def test_graphviz_weighted_prints(self):
        extra = "0 [label = \"ABC\"]; "
        desired_graph = "".join(["[[DOT strict graph {", _graph_opts, extra, "0; 1; 2; 3; 1 ", _graph_highlight,
                         "0 -- 1 [label=\"1\"; ]; 0 -- 3 [color=\"red\"; label=\"4\"; ]; ",
                         "1 -- 2 [label=\"2\"; ]; 2 -- 3 [label=\"100\"; ]; 0 [label = \"ABC\"]; }]]"])
        desired_digraph = "".join(["[[DOT digraph {", _graph_opts, extra, "0; 1; 2; 3; 2 ", _graph_highlight,
                         "0 -> 1 [label=\"1\"; ]; 1 -> 2 [label=\"7\"; ]; 2 -> 3 [label=\"3\"; ]; ",
                         "3 -> 0 [color=\"red\"; label=\"44\"; ]; ", extra, "}]]"])

        ret = Interpreter.interpret(("inteiro grafo[4,4]\n"
                                     "grafo[0,1] <- grafo[1,0] <- 1\n"
                                     "grafo[2,1] <- grafo[1,2] <- 2\n"
                                     "grafo[2,3] <- grafo[3,2] <- 100\n"
                                     "grafo[0,3] <- grafo[3,0] <- 4\n"
                                     "grafo_valorado_MA(grafo, [1], [[3,0]], \"0 [label = \\\"ABC\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_graph)

        ret = Interpreter.interpret(("inteiro digrafo[4,4]\n"
                                     "digrafo[0,1] <- 1\n"
                                     "digrafo[1,2] <- 7\n"
                                     "digrafo[2,3] <- 3\n"
                                     "digrafo[3,0] <- 44\n"
                                     "digrafo_valorado_MA(digrafo, [2], [[3,0]], \"0 [label = \\\"ABC\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_digraph)

        ret = Interpreter.interpret(("inteiro grafo[4,*,2]\n"
                                     "grafo[0] <- inserir(grafo[0], [1, 1])\n"
                                     "grafo[0] <- inserir(grafo[0], [3, 4])\n"
                                     "grafo[1] <- inserir(grafo[1], [0, 1])\n"
                                     "grafo[1] <- inserir(grafo[1], [2, 2])\n"
                                     "grafo[2] <- inserir(grafo[2], [1, 2])\n"
                                     "grafo[2] <- inserir(grafo[2], [3, 100])\n"
                                     "grafo[3] <- inserir(grafo[3], [2, 100])\n"
                                     "grafo[3] <- inserir(grafo[3], [0, 4])\n"
                                     "grafo_valorado_LA(grafo, [1], [[3,0]], \"0 [label = \\\"ABC\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_graph)

        ret = Interpreter.interpret(("inteiro digrafo[4,*,2]\n"
                                     "digrafo[0] <- inserir(digrafo[0], [1, 1])\n"
                                     "digrafo[1] <- inserir(digrafo[1], [2, 7])\n"
                                     "digrafo[2] <- inserir(digrafo[2], [3, 3])\n"
                                     "digrafo[3] <- inserir(digrafo[3], [0, 44])\n"
                                     "digrafo_valorado_LA(digrafo, [2], [[3,0]], \"0 [label = \\\"ABC\\\"]; \")\n"))

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
                           ("inteiro grafo[2,2]\n"
                            "grafo_MA(grafo, [], [[1, 2, 3]])\n"))

        self.assertRaises(TupyValueError, Interpreter.interpret, 
                           ("inteiro digrafo[1,2]\n"
                            "digrafo_MA(digrafo)\n"))
        self.assertRaises(TupyValueError, Interpreter.interpret, 
                           ("inteiro digrafo[2,2]\n"
                            "digrafo_MA(digrafo, [1, 3])\n"))
        self.assertRaises(TupyValueError, Interpreter.interpret, 
                           ("inteiro digrafo[2,2]\n"
                            "digrafo_MA(digrafo, [], [[1, 2, 3]])\n"))

        self.assertRaises(TupyIndexError, Interpreter.interpret, 
                           ("inteiro grafo[2,*] <- [ [3], [] ]\n"
                            "grafo_LA(grafo)\n"))
        self.assertRaises(TupyValueError, Interpreter.interpret, 
                           ("inteiro grafo[2,*]\n"
                            "grafo_LA(grafo, [0, 3])\n"))
        self.assertRaises(TupyValueError, Interpreter.interpret, 
                           ("inteiro grafo[2,*]\n"
                            "grafo_LA(grafo, [], [[1, 2, 3]])\n"))

        self.assertRaises(TupyIndexError, Interpreter.interpret, 
                           ("inteiro digrafo[2,*] <- [ [], [3] ]\n"
                            "digrafo_LA(digrafo)\n"))
        self.assertRaises(TupyValueError, Interpreter.interpret, 
                           ("inteiro digrafo[2,*]\n"
                            "digrafo_LA(digrafo, [1, 3])\n"))
        self.assertRaises(TupyValueError, Interpreter.interpret, 
                           ("inteiro digrafo[2,*]\n"
                            "digrafo_LA(digrafo, [], [[1, 2, 3]])\n"))

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

        desired_empty_tree = ("[[DOT digraph G { 1 [label = \"📥 vazio!\" fontsize=\"25\" shape = \"plaintext\"] }]]")

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
                                     "raiz.prox[0], raiz.prox[1] <- n1, n2\n"
                                     "n1.prox[1] <- n3\n"
                                     "n2.prox[0] <- n4\n"
                                     "arvore(raiz, \"c\", \"prox\", [n2]), \\\n"
                                     "arvore(nulo, \"c\", \"prox\", [n2])\n"))

        self.assertEqual(ret[0].type, Type.STRING)
        self.assertEqual(ret[0].value, desired_tree)
        self.assertEqual(ret[1].type, Type.STRING)
        self.assertEqual(ret[1].value, desired_empty_tree)

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

    def test_graphviz_matrix(self):
        desired_matrix = ("[[DOT digraph G {node [shape=plaintext]; 1 [label = <<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\">"
                        "<TR><TD PORT=\"rc\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\"> </FONT></TD>"
                        "<TD PORT=\"c0\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">0</FONT></TD>"
                        "<TD PORT=\"c1\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">1</FONT></TD>"
                        "<TD PORT=\"c2\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">2</FONT></TD></TR>"
                        "<TR><TD PORT=\"r0\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">0</FONT></TD>"
                        "<TD PORT=\"v0_0\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">1</FONT></TD>"
                        "<TD PORT=\"v0_1\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"23\">20</FONT></TD>"
                        "<TD PORT=\"v0_2\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"20\">300</FONT></TD></TR>"
                        "<TR><TD PORT=\"r1\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">1</FONT></TD>"
                        "<TD PORT=\"v1_0\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"15\">4000</FONT></TD>"
                        "<TD PORT=\"v1_1\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"12\">50000</FONT></TD>"
                        "<TD PORT=\"v1_2\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"10\">600000</FONT></TD></TR>"
                        "<TR><TD PORT=\"r2\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">2</FONT></TD>"
                        "<TD PORT=\"v2_0\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"9\">7000000</FONT></TD>"
                        "<TD PORT=\"v2_1\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"8\">80000000</FONT></TD>"
                        "<TD PORT=\"v2_2\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"6\">99999999999</FONT></TD></TR></TABLE>>]; }]]")
        ret = Interpreter.interpret("matriz([ [1, 20, 300], [4000, 50000, 600000], [7000000, 80000000, 99999999999] ], [[0,0], [2,2], [1,1], [2,2]])\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_matrix)      

        self.maxDiff = 93593
        desired_offset_matrix = ("[[DOT digraph G {node [shape=plaintext];"
                                " 1 [label = <<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
                                "<TD PORT=\"rc\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\"> </FONT></TD>"
                                "<TD PORT=\"c7\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">7</FONT></TD>"
                                "<TD PORT=\"c8\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">8</FONT></TD></TR><TR>"
                                "<TD PORT=\"r4\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">4</FONT></TD>"
                                "<TD PORT=\"v4_7\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">1</FONT></TD>"
                                "<TD PORT=\"v4_8\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">2</FONT></TD></TR><TR>"
                                "<TD PORT=\"r5\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">5</FONT></TD>"
                                "<TD PORT=\"v5_7\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">3</FONT></TD>"
                                "<TD PORT=\"v5_8\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">4</FONT></TD></TR></TABLE>>];"
                                " }]]")

        ret = Interpreter.interpret("matriz([ [1, 2], [3, 4] ], [], 4, 7)\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_offset_matrix)      

        self.assertRaises(TupyValueError, Interpreter.interpret, 
            "matriz([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ], [[0,0], [2], [1,1,1]])\n")      

    def test_graphviz_vector(self):        
        desired_vector = ("[[DOT digraph G {node [shape=plaintext]; 1 [label = <<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\">"
                            "<TR><TD PORT=\"c0\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">0</FONT></TD>"
                            "<TD PORT=\"c1\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">1</FONT></TD>"
                            "<TD PORT=\"c2\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">2</FONT></TD>"
                            "<TD PORT=\"c3\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">3</FONT></TD>"
                            "<TD PORT=\"c4\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">4</FONT></TD>"
                            "<TD PORT=\"c5\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">5</FONT></TD>"
                            "<TD PORT=\"c6\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">6</FONT></TD>"
                            "<TD PORT=\"c7\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">7</FONT></TD>"
                            "<TD PORT=\"c8\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">8</FONT></TD></TR>"
                            "<TR><TD PORT=\"v0\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">1</FONT></TD>"
                            "<TD PORT=\"v1\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"23\">20</FONT></TD>"
                            "<TD PORT=\"v2\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"20\">300</FONT></TD>"
                            "<TD PORT=\"v3\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"15\">4000</FONT></TD>"
                            "<TD PORT=\"v4\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"12\">50000</FONT></TD>"
                            "<TD PORT=\"v5\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"10\">600000</FONT></TD>"
                            "<TD PORT=\"v6\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"9\">7000000</FONT></TD>"
                            "<TD PORT=\"v7\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"8\">80000000</FONT></TD>"
                            "<TD PORT=\"v8\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                            "<FONT FACE=\"COURIER\" POINT-SIZE=\"6\">99999999999</FONT></TD></TR></TABLE>>]; 3 -> 1}]]")
        ret = Interpreter.interpret("vetor([1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 99999999999], [4, 1, 8], \"3 -> 1\")\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_vector)

        self.maxDiff = 93593
        desired_offset_vector = ("[[DOT digraph G {node [shape=plaintext];"
                                " 1 [label = <<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
                                "<TD PORT=\"c8\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">8</FONT></TD>"
                                "<TD PORT=\"c9\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">9</FONT></TD>"
                                "<TD PORT=\"c10\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">10</FONT></TD>"
                                "<TD PORT=\"c11\" BGCOLOR=\"WHITE\" BORDER=\"0\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">11</FONT></TD></TR><TR>"
                                "<TD PORT=\"v8\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">1</FONT></TD>"
                                "<TD PORT=\"v9\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">2</FONT></TD>"
                                "<TD PORT=\"v10\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">3</FONT></TD>"
                                "<TD PORT=\"v11\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                                "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">4</FONT></TD></TR></TABLE>>];"
                                " }]]")

        ret = Interpreter.interpret("vetor([1, 2, 3, 4], [], 8)\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_offset_vector)   

    def test_graphviz_stack(self):
        desired_stack=("[[DOT digraph G {node [shape=plaintext]; edge [arrowsize = 0.5]; 0 [label = \" \"]; 0 -> 1; 1 -> 0; "
                        "1 [label = <<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\">"
                        "<TR><TD PORT=\"v8\" SIDES=\"LBR\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"6\">99999999999</FONT></TD></TR>"
                        "<TR><TD PORT=\"v7\" SIDES=\"LBRT\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"8\">80000000</FONT></TD></TR>"
                        "<TR><TD PORT=\"v6\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"9\">7000000</FONT></TD></TR>"
                        "<TR><TD PORT=\"v5\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"10\">600000</FONT></TD></TR>"
                        "<TR><TD PORT=\"v4\" SIDES=\"LBRT\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"12\">50000</FONT></TD></TR>"
                        "<TR><TD PORT=\"v3\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"15\">4000</FONT></TD></TR>"
                        "<TR><TD PORT=\"v2\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"20\">300</FONT></TD></TR>"
                        "<TR><TD PORT=\"v1\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"23\">20</FONT></TD></TR>"
                        "<TR><TD PORT=\"v0\" SIDES=\"LBRT\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">1</FONT></TD></TR></TABLE>>]; 3 -> 1}]]")
        ret = Interpreter.interpret("pilha([1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 99999999999], [4, 1, 8], \"3 -> 1\")\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_stack)

    def test_graphviz_queue(self):
        desired_queue=("[[DOT digraph G {node [shape=plaintext]; edge [arrowsize = 0.5]; C [label = \" \"]; "
                        "F [label = \" \"]; F -> 1; 1 -> C; {rank = same; F; 1; C;} "
                        "1 [label = <<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\">"
                        "<TR><TD PORT=\"v8\" SIDES=\"BRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"6\">99999999999</FONT></TD>"
                        "<TD PORT=\"v7\" SIDES=\"LBRT\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"8\">80000000</FONT></TD>"
                        "<TD PORT=\"v6\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"9\">7000000</FONT></TD>"
                        "<TD PORT=\"v5\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"10\">600000</FONT></TD>"
                        "<TD PORT=\"v4\" SIDES=\"LBRT\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"12\">50000</FONT></TD>"
                        "<TD PORT=\"v3\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"15\">4000</FONT></TD>"
                        "<TD PORT=\"v2\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"20\">300</FONT></TD>"
                        "<TD PORT=\"v1\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"23\">20</FONT></TD>"
                        "<TD PORT=\"v0\" SIDES=\"LBT\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">1</FONT></TD></TR></TABLE>>]; 3 -> 1}]]")
        ret = Interpreter.interpret("fila([1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 99999999999], [4, 1, 8], \"3 -> 1\")\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_queue)

    def test_graphviz_linked_list(self):
        desired_linked_list=("[[DOT digraph {node [shape=none];"
                            " splines=true; null [shape=point];"
                            " s0 [label=<<TABLE CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
                            "<TD WIDTH=\"42\" HEIGHT=\"36\" SIDES=\"R\" BGCOLOR=\"white\" PORT=\"c\">5</TD>"
                            "<TD BORDER=\"0\" PORT=\"r\"> </TD></TR></TABLE>>];"
                            " s1 [label=<<TABLE CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
                            "<TD WIDTH=\"42\" HEIGHT=\"36\" SIDES=\"R\" BGCOLOR=\"white\" PORT=\"c\">10</TD>"
                            "<TD BORDER=\"0\" PORT=\"r\"> </TD></TR></TABLE>>];"
                            " s2 [label=<<TABLE CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
                            "<TD WIDTH=\"42\" HEIGHT=\"36\" SIDES=\"R\" BGCOLOR=\"white\" PORT=\"c\">3</TD>"
                            "<TD BORDER=\"0\" PORT=\"r\"> </TD></TR></TABLE>>];"
                            " s3 [label=<<TABLE CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
                            "<TD WIDTH=\"42\" HEIGHT=\"36\" SIDES=\"R\" BGCOLOR=\"yellow\" PORT=\"c\">15</TD>"
                            "<TD BORDER=\"0\" PORT=\"r\"> </TD></TR></TABLE>>];"
                            " s4 [label=<<TABLE CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
                            "<TD WIDTH=\"42\" HEIGHT=\"36\" SIDES=\"R\" BGCOLOR=\"white\" PORT=\"c\">20</TD>"
                            "<TD BORDER=\"0\" PORT=\"r\"> </TD></TR></TABLE>>];"
                            " s4:r -> null; s3:r -> s4:c; s2:r -> s3:c; s1:r -> s2:c; s0:r -> s1:c;"
                            " {rank = same; null; s0; s1; s2; s3; s4; }; }]]")

        desired_double_linked_list=("[[DOT digraph {node [shape=none];"
                                    " splines=true; null [shape=point];"
                                    " s0 [label=<<TABLE CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
                                    "<TD BORDER=\"0\" PORT=\"l\"> </TD>"
                                    "<TD WIDTH=\"42\" HEIGHT=\"36\" SIDES=\"LR\" BGCOLOR=\"white\" PORT=\"c\">5</TD>"
                                    "<TD BORDER=\"0\" PORT=\"r\"> </TD></TR></TABLE>>];"
                                    " s1 [label=<<TABLE CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
                                    "<TD BORDER=\"0\" PORT=\"l\"> </TD>"
                                    "<TD WIDTH=\"42\" HEIGHT=\"36\" SIDES=\"LR\" BGCOLOR=\"white\" PORT=\"c\">10</TD>"
                                    "<TD BORDER=\"0\" PORT=\"r\"> </TD></TR></TABLE>>];"
                                    " s2 [label=<<TABLE CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
                                    "<TD BORDER=\"0\" PORT=\"l\"> </TD>"
                                    "<TD WIDTH=\"42\" HEIGHT=\"36\" SIDES=\"LR\" BGCOLOR=\"white\" PORT=\"c\">3</TD>"
                                    "<TD BORDER=\"0\" PORT=\"r\"> </TD></TR></TABLE>>];"
                                    " s3 [label=<<TABLE CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
                                    "<TD BORDER=\"0\" PORT=\"l\"> </TD>"
                                    "<TD WIDTH=\"42\" HEIGHT=\"36\" SIDES=\"LR\" BGCOLOR=\"yellow\" PORT=\"c\">15</TD>"
                                    "<TD BORDER=\"0\" PORT=\"r\"> </TD></TR></TABLE>>];"
                                    " s4 [label=<<TABLE CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
                                    "<TD BORDER=\"0\" PORT=\"l\"> </TD>"
                                    "<TD WIDTH=\"42\" HEIGHT=\"36\" SIDES=\"LR\" BGCOLOR=\"white\" PORT=\"c\">20</TD>"
                                    "<TD BORDER=\"0\" PORT=\"r\"> </TD></TR></TABLE>>];"
                                    " s4:r -> null; s3:r -> s4:l; s3:r -> s4:l [dir=back];"
                                    " s2:r -> s3:l; s2:r -> s3:l [dir=back]; s1:r -> s2:l;"
                                    " s1:r -> s2:l [dir=back]; s0:r -> s1:l; s0:r -> s1:l [dir=back];"
                                    " {rank = same; null; s0; s1; s2; s3; s4; }; }]]")

        desired_empty_linked_list=("[[DOT digraph G { 1 [label = \"📥 vazio!\" fontsize=\"25\" shape = \"plaintext\"] }]]")

        ret = Interpreter.interpret(("tipo Nó:\n"
                                     "\tinteiro c\n"
                                     "\tNó prox\n"
                                     "\tNó(inteiro chave):\n"
                                     "\t\tc <- chave\n"
                                     "Nó cab <- Nó(5)\n"
                                     "Nó n1 <- Nó(10)\n"
                                     "Nó n2 <- Nó(3)\n"
                                     "Nó n3 <- Nó(15)\n"
                                     "Nó n4 <- Nó(20)\n"
                                     "cab.prox <- n1\n"
                                     "n1.prox <- n2\n"
                                     "n2.prox <- n3\n"
                                     "n3.prox <- n4\n"
                                     "lista_encadeada(cab, \"c\", \"prox\", falso, [n3]), \\\n"
                                     "lista_encadeada(cab, \"c\", \"prox\", verdadeiro, [n3]), \\\n"
                                     "lista_encadeada(nulo, \"c\", \"prox\", falso, [n3])\n"))

        self.assertEqual(ret[0].type, Type.STRING)
        self.assertEqual(ret[0].value, desired_linked_list)
        self.assertEqual(ret[1].type, Type.STRING)
        self.assertEqual(ret[1].value, desired_double_linked_list)
        self.assertEqual(ret[2].type, Type.STRING)
        self.assertEqual(ret[2].value, desired_empty_linked_list)

    def test_graphviz_circular_linked_list(self):
        desired_linked_list=('[[DOT digraph {node [shape=none]; splines=true; null [shape=point]; s0 '
                            '[label=<<TABLE CELLPADDING="0" CELLSPACING="0"><TR><TD WIDTH="42" '
                            'HEIGHT="36" SIDES="R" BGCOLOR="white" PORT="c">5</TD><TD BORDER="0" '
                            'PORT="r"> </TD></TR></TABLE>>]; s1 [label=<<TABLE CELLPADDING="0" '
                            'CELLSPACING="0"><TR><TD WIDTH="42" HEIGHT="36" SIDES="R" BGCOLOR="yellow" '
                            'PORT="c">10</TD><TD BORDER="0" PORT="r"> </TD></TR></TABLE>>]; null '
                            '[style=invis]; s0:c:s -> s1:r:s [dir=back];s0:r -> s1:c; {rank = same; null; '
                            's0; s1; }; }]]')

        desired_double_linked_list=('[[DOT digraph {node [shape=none]; splines=true; null [shape=point]; s0 '
                                    '[label=<<TABLE CELLPADDING="0" CELLSPACING="0"><TR><TD BORDER="0" PORT="l"> '
                                    '</TD><TD WIDTH="42" HEIGHT="36" SIDES="LR" BGCOLOR="white" '
                                    'PORT="c">5</TD><TD BORDER="0" PORT="r"> </TD></TR></TABLE>>]; s1 '
                                    '[label=<<TABLE CELLPADDING="0" CELLSPACING="0"><TR><TD BORDER="0" PORT="l"> '
                                    '</TD><TD WIDTH="42" HEIGHT="36" SIDES="LR" BGCOLOR="yellow" '
                                    'PORT="c">10</TD><TD BORDER="0" PORT="r"> </TD></TR></TABLE>>]; null '
                                    '[style=invis]; s0:l:s -> s1:r:s [dir=both];s0:r -> s1:l; s0:r -> s1:l '
                                    '[dir=back]; {rank = same; null; s0; s1; }; }]]')

        self.maxDiff = 99999
        ret = Interpreter.interpret(("tipo Nó:\n"
                                     "\tinteiro c\n"
                                     "\tNó prox\n"
                                     "\tNó(inteiro chave):\n"
                                     "\t\tc <- chave\n"
                                     "Nó cab <- Nó(5)\n"
                                     "Nó n1 <- Nó(10)\n"
                                     "cab.prox <- n1\n"
                                     "n1.prox <- cab\n"
                                     "lista_encadeada(cab, \"c\", \"prox\", falso, [n1]), \\\n"
                                     "lista_encadeada(cab, \"c\", \"prox\", verdadeiro, [n1])\n"))
        self.assertEqual(ret[0].type, Type.STRING)
        self.assertEqual((ret[0].value, ret[1].value), (desired_linked_list, desired_double_linked_list))
        self.assertEqual(ret[1].type, Type.STRING)
        self.assertEqual(ret[1].value, desired_double_linked_list)
        
    def test_graphviz_linked_list_errors(self):
        typedef = "tipo Nó:\n\tinteiro c\n\tNó prox\n\tNó(inteiro chave):\n\t\tc <- chave\n"

        self.assertRaises(TupyTypeError, Interpreter.interpret, "lista_encadeada(1)") # too few args
        self.assertRaises(TupyTypeError, Interpreter.interpret, "lista_encadeada(1, 2, 3, 4, 5, 6, 7)") # too many args
        self.assertRaises(TupyTypeError, Interpreter.interpret, "lista_encadeada(1, 2, 3)") # not struct
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
            "{0}Nó cab <- Nó(0); lista_encadeada(cab, 2, 3)".format(typedef)) #not string
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
            "{0}Nó cab <- Nó(0); lista_encadeada(cab, \"c\", 3)".format(typedef)) #not string 2
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
            "{0}Nó cab <- Nó(0); lista_encadeada(cab, \"c\", \"prox\", \"duplo\")".format(typedef)) #not bool
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
            "{0}Nó cab <- Nó(0); lista_encadeada(cab, \"c\", \"prox\", falso, 4)".format(typedef)) #not list
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
            ("{0}tipo Outro:\n"
             "\tinteiro c\n"
             "Nó cab <- Nó(0); Outro outro <- Outro()\n"
             "lista_encadeada(cab, \"c\", \"prox\", [outro])").format(typedef)) #not right class
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
            "{0}Nó cab <- Nó(0); lista_encadeada(cab, \"c\", \"prox\", falso, [cab], 0)".format(typedef)) #not string
        self.assertRaises(TupyNameError, Interpreter.interpret, 
            "{0}Nó cab <- Nó(0); lista_encadeada(cab, \"d\", \"prox\")".format(typedef)) #wrong attr
        self.assertRaises(TupyNameError, Interpreter.interpret, 
            "{0}Nó cab <- Nó(0); lista_encadeada(cab, \"c\", \"prod\")".format(typedef)) #wrong attr 2
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
            ("tipo Nó:\n"
            "\tinteiro c\n"
            "\tinteiro prox\n"
            "Nó cab <- Nó();\n"
            "lista_encadeada(cab, \"c\", \"prox\")").format(typedef)) #wrong edge type

if __name__ == '__main__':
    unittest.main()
