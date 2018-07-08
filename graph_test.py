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
from tupy.Builtins import _graph_opts, _graph_highlight, _empty_graphviz_return
from tupy.errorHelper import TupyNameError, TupyRuntimeError, TupySyntaxError, \
                             TupyTypeError, TupyValueError, TupyParseError, \
                             TupyIndexError

class TestGraphs(unittest.TestCase):
    def setUp(self):
        Interpreter.isDebug = False
        self.maxDiff = 49249323

    def test_graphviz_prints(self):
        extraHeader = "0 [label = \"ABC\"]; "
        extraFooter = "1 [label = \"DEF\"]; "
        desired_graph = "".join(["[[DOT strict graph {", _graph_opts, extraHeader, " 0; 1; 2; 3; 1 ", _graph_highlight,
                         "0 -- 1 []; 0 -- 3 [color=\"red\"; ]; 1 -- 2 []; 2 -- 3 []; ", extraFooter, " }]]"])
        desired_digraph = "".join(["[[DOT digraph {", _graph_opts, extraHeader, " 0; 1; 2; 3; 2 ", _graph_highlight,
                         "0 -> 1 []; 1 -> 2 []; 2 -> 3 []; 3 -> 0 [color=\"red\"; ]; ", extraFooter, " }]]"])

        ret = Interpreter.interpret(("inteiro grafo[4,4]\n"
                                     "grafo[0,1] <- grafo[1,0] <- 1\n"
                                     "grafo[2,1] <- grafo[1,2] <- 2\n"
                                     "grafo[2,3] <- grafo[3,2] <- 100\n"
                                     "grafo[0,3] <- grafo[3,0] <- 4\n"
                                     "grafo_MA(grafo, [1], [[3,0]], \"0 [label = \\\"ABC\\\"]; \",\n"
                                     "                              \"1 [label = \\\"DEF\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_graph)

        ret = Interpreter.interpret(("inteiro digrafo[4,4]\n"
                                     "digrafo[0,1] <- 1\n"
                                     "digrafo[1,2] <- 7\n"
                                     "digrafo[2,3] <- 3\n"
                                     "digrafo[3,0] <- 44\n"
                                     "digrafo_MA(digrafo, [2], [[3,0]], \"0 [label = \\\"ABC\\\"]; \",\n"
                                     "                              \"1 [label = \\\"DEF\\\"]; \")\n"))

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
                                     "grafo_LA(grafo, [1], [[3,0]], \"0 [label = \\\"ABC\\\"]; \",\n"
                                     "                              \"1 [label = \\\"DEF\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_graph)

        ret = Interpreter.interpret(("inteiro digrafo[4,*]\n"
                                     "digrafo[0] <- inserir(digrafo[0], 1)\n"
                                     "digrafo[1] <- inserir(digrafo[1], 2)\n"
                                     "digrafo[2] <- inserir(digrafo[2], 3)\n"
                                     "digrafo[3] <- inserir(digrafo[3], 0)\n"
                                     "digrafo_LA(digrafo, [2], [[3,0]], \"0 [label = \\\"ABC\\\"]; \",\n"
                                     "                              \"1 [label = \\\"DEF\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_digraph)

    def test_graphviz_weighted_prints(self):
        extraHeader = "0 [label = \"ABC\"]; "
        extraFooter = "1 [label = \"DEF\"]; "
        desired_graph = "".join(["[[DOT strict graph {", _graph_opts, extraHeader, " 0; 1; 2; 3; 1 ", _graph_highlight,
                         "0 -- 1 [label=\"1\"; ]; 0 -- 3 [color=\"red\"; label=\"4\"; ]; ",
                         "1 -- 2 [label=\"2\"; ]; 2 -- 3 [label=\"100\"; ]; ", extraFooter, " }]]"])
        desired_digraph = "".join(["[[DOT digraph {", _graph_opts, extraHeader, " 0; 1; 2; 3; 2 ", _graph_highlight,
                         "0 -> 1 [label=\"1\"; ]; 1 -> 2 [label=\"7\"; ]; 2 -> 3 [label=\"3\"; ]; ",
                         "3 -> 0 [color=\"red\"; label=\"44\"; ]; ", extraFooter, " }]]"])

        ret = Interpreter.interpret(("inteiro grafo[4,4]\n"
                                     "grafo[0,1] <- grafo[1,0] <- 1\n"
                                     "grafo[2,1] <- grafo[1,2] <- 2\n"
                                     "grafo[2,3] <- grafo[3,2] <- 100\n"
                                     "grafo[0,3] <- grafo[3,0] <- 4\n"
                                     "grafo_valorado_MA(grafo, [1], [[3,0]], \"0 [label = \\\"ABC\\\"]; \",\n"
                                     "                                       \"1 [label = \\\"DEF\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_graph)

        ret = Interpreter.interpret(("inteiro digrafo[4,4]\n"
                                     "digrafo[0,1] <- 1\n"
                                     "digrafo[1,2] <- 7\n"
                                     "digrafo[2,3] <- 3\n"
                                     "digrafo[3,0] <- 44\n"
                                     "digrafo_valorado_MA(digrafo, [2], [[3,0]], \"0 [label = \\\"ABC\\\"]; \",\n"
                                     "                                           \"1 [label = \\\"DEF\\\"]; \")\n"))

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
                                     "grafo_valorado_LA(grafo, [1], [[3,0]], \"0 [label = \\\"ABC\\\"]; \",\n"
                                     "                                       \"1 [label = \\\"DEF\\\"]; \")\n"))

        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_graph)

        ret = Interpreter.interpret(("inteiro digrafo[4,*,2]\n"
                                     "digrafo[0] <- inserir(digrafo[0], [1, 1])\n"
                                     "digrafo[1] <- inserir(digrafo[1], [2, 7])\n"
                                     "digrafo[2] <- inserir(digrafo[2], [3, 3])\n"
                                     "digrafo[3] <- inserir(digrafo[3], [0, 44])\n"
                                     "digrafo_valorado_LA(digrafo, [2], [[3,0]], \"0 [label = \\\"ABC\\\"]; \",\n"
                                     "                                           \"1 [label = \\\"DEF\\\"]; \")\n"))

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
        desired_tree = "".join(["[[DOT digraph {", _graph_opts, "99 -> 100; ", tree_data, "100 -> 99; }]]"])

        desired_empty_tree = _empty_graphviz_return

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
                                     "arvore(raiz, \"c\", \"prox\", [n2], \"99 -> 100;\", \"100 -> 99;\"), \\\n"
                                     "arvore(nulo, \"c\", \"prox\", [n2], \"99 -> 100;\", \"100 -> 99;\")\n"))

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
        self.assertRaises(TupyTypeError, Interpreter.interpret, "arvore(1, 2, 3, 4, 5, 6, 7)") # too many args
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
        self.assertRaises(TupyTypeError, Interpreter.interpret,
            "{0}Nó raiz <- Nó(0); arvore(raiz, \"c\", \"prox\", [raiz], \"\", 4)".format(typedef)) #not string
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
        desired_matrix = ("[[DOT digraph G {node [shape=plaintext];  1 [label = <<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\">"
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

        desired_offset_matrix = ("[[DOT digraph G {node [shape=plaintext];"
                                "  1 [label = <<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
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
        desired_vector = ("[[DOT digraph G { node [shape=plaintext]; 1 -> 3; 1 [label = <<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\">"
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
        ret = Interpreter.interpret("vetor([1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 99999999999], [4, 1, 8], \"1 -> 3;\", \"3 -> 1\")\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_vector)

        desired_offset_vector = ("[[DOT digraph G { node [shape=plaintext];"
                                "  1 [label = <<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
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
        desired_stack=("[[DOT digraph G { node [shape=plaintext]; edge [arrowsize = 0.5]; 1 -> 3; 0 [label = \" \"]; "
                        "0 -> 1; 1 -> 0; 1 [label = <<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
                        "<TD PORT=\"v8\" SIDES=\"LBR\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"6\">99999999999</FONT></TD></TR><TR>"
                        "<TD PORT=\"v7\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"8\">80000000</FONT></TD></TR><TR>"
                        "<TD PORT=\"v6\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"9\">7000000</FONT></TD></TR><TR>"
                        "<TD PORT=\"v5\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"10\">600000</FONT></TD></TR><TR>"
                        "<TD PORT=\"v4\" SIDES=\"LBRT\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"12\">50000</FONT></TD></TR><TR>"
                        "<TD PORT=\"v3\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"15\">4000</FONT></TD></TR><TR>"
                        "<TD PORT=\"v2\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"20\">300</FONT></TD></TR><TR>"
                        "<TD PORT=\"v1\" SIDES=\"LBRT\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"23\">20</FONT></TD></TR><TR>"
                        "<TD PORT=\"v0\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">1</FONT></TD></TR></TABLE>>]; {rank=min; 0}; 3 -> 1}]]")
        ret = Interpreter.interpret("pilha([1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 99999999999], [4, 1, 8], \"1 -> 3;\", \"3 -> 1\")\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_stack)

    def test_graphviz_queue(self):
        desired_queue=("[[DOT digraph G { node [shape=plaintext]; edge [arrowsize = 0.5]; 1 -> 3; "
                        "C [label = \" \"]; F [label = \" \"]; C -> 1 [dir=back]; 1 -> F [dir=back]; {rank = same; F; 1; C;} "
                        "1 [label = <<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\"><TR>"
                        "<TD PORT=\"v0\" SIDES=\"BRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"27\">1</FONT></TD>"
                        "<TD PORT=\"v1\" SIDES=\"LBRT\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"23\">20</FONT></TD>"
                        "<TD PORT=\"v2\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"20\">300</FONT></TD>"
                        "<TD PORT=\"v3\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"15\">4000</FONT></TD>"
                        "<TD PORT=\"v4\" SIDES=\"LBRT\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"12\">50000</FONT></TD>"
                        "<TD PORT=\"v5\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"10\">600000</FONT></TD>"
                        "<TD PORT=\"v6\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"9\">7000000</FONT></TD>"
                        "<TD PORT=\"v7\" SIDES=\"LBRT\" BGCOLOR=\"WHITE\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"8\">80000000</FONT></TD>"
                        "<TD PORT=\"v8\" SIDES=\"LBT\" BGCOLOR=\"YELLOW\" BORDER=\"1\" FIXEDSIZE=\"TRUE\" WIDTH=\"42\" HEIGHT=\"42\">"
                        "<FONT FACE=\"COURIER\" POINT-SIZE=\"6\">99999999999</FONT></TD></TR></TABLE>>]; 3 -> 1}]]")
        ret = Interpreter.interpret("fila([1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 99999999999], [4, 1, 8], \"1 -> 3;\", \"3 -> 1\")\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, desired_queue)

    def test_graphviz_linked_list(self):
        desired_linked_list=('[[DOT digraph {node [shape=none];  s0 [label=<<TABLE CELLPADDING="0" '
                            'CELLSPACING="0"><TR><TD WIDTH="42" HEIGHT="36" SIDES="R" BGCOLOR="white" '
                            'PORT="c">5</TD><TD BORDER="0" PORT="r"><TABLE CELLPADDING="0" '
                            'CELLSPACING="0" BORDER="0" ><TR><TD PORT="ru"> </TD></TR><TR><TD PORT="rd"> '
                            '</TD></TR></TABLE></TD></TR></TABLE>>]; s1 [label=<<TABLE CELLPADDING="0" '
                            'CELLSPACING="0"><TR><TD WIDTH="42" HEIGHT="36" SIDES="R" BGCOLOR="white" '
                            'PORT="c">10</TD><TD BORDER="0" PORT="r"><TABLE CELLPADDING="0" '
                            'CELLSPACING="0" BORDER="0" ><TR><TD PORT="ru"> </TD></TR><TR><TD PORT="rd"> '
                            '</TD></TR></TABLE></TD></TR></TABLE>>]; s2 [label=<<TABLE CELLPADDING="0" '
                            'CELLSPACING="0"><TR><TD WIDTH="42" HEIGHT="36" SIDES="R" BGCOLOR="white" '
                            'PORT="c">3</TD><TD BORDER="0" PORT="r"><TABLE CELLPADDING="0" '
                            'CELLSPACING="0" BORDER="0" ><TR><TD PORT="ru"> </TD></TR><TR><TD PORT="rd"> '
                            '</TD></TR></TABLE></TD></TR></TABLE>>]; s3 [label=<<TABLE CELLPADDING="0" '
                            'CELLSPACING="0"><TR><TD WIDTH="42" HEIGHT="36" SIDES="R" BGCOLOR="yellow" '
                            'PORT="c">15</TD><TD BORDER="0" PORT="r"><TABLE CELLPADDING="0" '
                            'CELLSPACING="0" BORDER="0" ><TR><TD PORT="ru"> </TD></TR><TR><TD PORT="rd"> '
                            '</TD></TR></TABLE></TD></TR></TABLE>>]; s4 [label=<<TABLE CELLPADDING="0" '
                            'CELLSPACING="0"><TR><TD WIDTH="42" HEIGHT="36" SIDES="R" BGCOLOR="white" '
                            'PORT="c">20</TD><TD BORDER="0" PORT="r"><TABLE CELLPADDING="0" '
                            'CELLSPACING="0" BORDER="0" ><TR><TD PORT="ru"> </TD></TR><TR><TD PORT="rd"> '
                            '</TD></TR></TABLE></TD></TR></TABLE>>]; s4:r -> null:w; s3:r -> s4:c; s2:r '
                            '-> s3:c; s1:r -> s2:c; s0:r -> s1:c; {rank = same; null; s0; s1; s2; s3; s4; '
                            '};  null [shape=point]; }]]')

        desired_double_linked_list=('[[DOT digraph {node [shape=none];  s0 [label=<<TABLE CELLPADDING="0" '
                                    'CELLSPACING="0"><TR><TD BORDER="0" PORT="l"><TABLE CELLPADDING="0" '
                                    'CELLSPACING="0" BORDER="0" ><TR><TD PORT="lu"> </TD></TR><TR><TD PORT="ld"> '
                                    '</TD></TR></TABLE></TD><TD WIDTH="42" HEIGHT="36" SIDES="LR" BGCOLOR="white" '
                                    'PORT="c">5</TD><TD BORDER="0" PORT="r"><TABLE CELLPADDING="0" '
                                    'CELLSPACING="0" BORDER="0" ><TR><TD PORT="ru"> </TD></TR><TR><TD PORT="rd"> '
                                    '</TD></TR></TABLE></TD></TR></TABLE>>]; s1 [label=<<TABLE CELLPADDING="0" '
                                    'CELLSPACING="0"><TR><TD BORDER="0" PORT="l"><TABLE CELLPADDING="0" '
                                    'CELLSPACING="0" BORDER="0" ><TR><TD PORT="lu"> </TD></TR><TR><TD PORT="ld"> '
                                    '</TD></TR></TABLE></TD><TD WIDTH="42" HEIGHT="36" SIDES="LR" BGCOLOR="white" '
                                    'PORT="c">10</TD><TD BORDER="0" PORT="r"><TABLE CELLPADDING="0" '
                                    'CELLSPACING="0" BORDER="0" ><TR><TD PORT="ru"> </TD></TR><TR><TD PORT="rd"> '
                                    '</TD></TR></TABLE></TD></TR></TABLE>>]; s2 [label=<<TABLE CELLPADDING="0" '
                                    'CELLSPACING="0"><TR><TD BORDER="0" PORT="l"><TABLE CELLPADDING="0" '
                                    'CELLSPACING="0" BORDER="0" ><TR><TD PORT="lu"> </TD></TR><TR><TD PORT="ld"> '
                                    '</TD></TR></TABLE></TD><TD WIDTH="42" HEIGHT="36" SIDES="LR" BGCOLOR="white" '
                                    'PORT="c">3</TD><TD BORDER="0" PORT="r"><TABLE CELLPADDING="0" '
                                    'CELLSPACING="0" BORDER="0" ><TR><TD PORT="ru"> </TD></TR><TR><TD PORT="rd"> '
                                    '</TD></TR></TABLE></TD></TR></TABLE>>]; s3 [label=<<TABLE CELLPADDING="0" '
                                    'CELLSPACING="0"><TR><TD BORDER="0" PORT="l"><TABLE CELLPADDING="0" '
                                    'CELLSPACING="0" BORDER="0" ><TR><TD PORT="lu"> </TD></TR><TR><TD PORT="ld"> '
                                    '</TD></TR></TABLE></TD><TD WIDTH="42" HEIGHT="36" SIDES="LR" '
                                    'BGCOLOR="yellow" PORT="c">15</TD><TD BORDER="0" PORT="r"><TABLE '
                                    'CELLPADDING="0" CELLSPACING="0" BORDER="0" ><TR><TD PORT="ru"> '
                                    '</TD></TR><TR><TD PORT="rd"> </TD></TR></TABLE></TD></TR></TABLE>>]; s4 '
                                    '[label=<<TABLE CELLPADDING="0" CELLSPACING="0"><TR><TD BORDER="0" '
                                    'PORT="l"><TABLE CELLPADDING="0" CELLSPACING="0" BORDER="0" ><TR><TD '
                                    'PORT="lu"> </TD></TR><TR><TD PORT="ld"> </TD></TR></TABLE></TD><TD '
                                    'WIDTH="42" HEIGHT="36" SIDES="LR" BGCOLOR="white" PORT="c">20</TD><TD '
                                    'BORDER="0" PORT="r"><TABLE CELLPADDING="0" CELLSPACING="0" BORDER="0" '
                                    '><TR><TD PORT="ru"> </TD></TR><TR><TD PORT="rd"> '
                                    '</TD></TR></TABLE></TD></TR></TABLE>>]; s4:r -> null:w; s3:ru -> s4:lu; '
                                    's4:ld -> s3:rd; s2:ru -> s3:lu; s3:ld -> s2:rd; s1:ru -> s2:lu; s2:ld -> '
                                    's1:rd; s0:ru -> s1:lu; s1:ld -> s0:rd; {rank = same; null; s0; s1; s2; s3; '
                                    's4; };  null [shape=point]; }]]')

        desired_empty_linked_list=_empty_graphviz_return

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
        self.assertEqual(ret[0].value, desired_linked_list,)
        self.assertEqual(ret[1].type, Type.STRING)
        self.assertEqual(ret[1].value, desired_double_linked_list)
        self.assertEqual(ret[2].type, Type.STRING)
        self.assertEqual(ret[2].value, desired_empty_linked_list)

    def test_graphviz_circular_linked_list(self):
        desired_linked_list=('[[DOT digraph {node [shape=none];  s0 [label=<<TABLE CELLPADDING="0" '
                            'CELLSPACING="0"><TR><TD WIDTH="42" HEIGHT="36" SIDES="R" BGCOLOR="white" '
                            'PORT="c">5</TD><TD BORDER="0" PORT="r"><TABLE CELLPADDING="0" '
                            'CELLSPACING="0" BORDER="0" ><TR><TD PORT="ru"> </TD></TR><TR><TD PORT="rd"> '
                            '</TD></TR></TABLE></TD></TR></TABLE>>]; s1 [label=<<TABLE CELLPADDING="0" '
                            'CELLSPACING="0"><TR><TD WIDTH="42" HEIGHT="36" SIDES="R" BGCOLOR="yellow" '
                            'PORT="c">10</TD><TD BORDER="0" PORT="r"><TABLE CELLPADDING="0" '
                            'CELLSPACING="0" BORDER="0" ><TR><TD PORT="ru"> </TD></TR><TR><TD PORT="rd"> '
                            '</TD></TR></TABLE></TD></TR></TABLE>>]; null [style=invis]; s1:r:s -> '
                            's0:c:s; s0:r -> s1:c; {rank = same; null; s0; s1; };  null [shape=point]; '
                            '}]]')

        desired_double_linked_list=('[[DOT digraph {node [shape=none];  s0 [label=<<TABLE CELLPADDING="0" '
                                    'CELLSPACING="0"><TR><TD BORDER="0" PORT="l"><TABLE CELLPADDING="0" '
                                    'CELLSPACING="0" BORDER="0" ><TR><TD PORT="lu"> </TD></TR><TR><TD PORT="ld"> '
                                    '</TD></TR></TABLE></TD><TD WIDTH="42" HEIGHT="36" SIDES="LR" BGCOLOR="white" '
                                    'PORT="c">5</TD><TD BORDER="0" PORT="r"><TABLE CELLPADDING="0" '
                                    'CELLSPACING="0" BORDER="0" ><TR><TD PORT="ru"> </TD></TR><TR><TD PORT="rd"> '
                                    '</TD></TR></TABLE></TD></TR></TABLE>>]; s1 [label=<<TABLE CELLPADDING="0" '
                                    'CELLSPACING="0"><TR><TD BORDER="0" PORT="l"><TABLE CELLPADDING="0" '
                                    'CELLSPACING="0" BORDER="0" ><TR><TD PORT="lu"> </TD></TR><TR><TD PORT="ld"> '
                                    '</TD></TR></TABLE></TD><TD WIDTH="42" HEIGHT="36" SIDES="LR" '
                                    'BGCOLOR="yellow" PORT="c">10</TD><TD BORDER="0" PORT="r"><TABLE '
                                    'CELLPADDING="0" CELLSPACING="0" BORDER="0" ><TR><TD PORT="ru"> '
                                    '</TD></TR><TR><TD PORT="rd"> </TD></TR></TABLE></TD></TR></TABLE>>]; null '
                                    '[style=invis]; s1:ru:e -> s0:lu:n; s0:ld:w -> s1:rd:s; s0:ru -> s1:lu; s1:ld '
                                    '-> s0:rd; {rank = same; null; s0; s1; };  null [shape=point]; }]]')

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
        self.assertEqual(ret[0].value, desired_linked_list)
        self.assertEqual(ret[1].type, Type.STRING)
        self.assertEqual(ret[1].value, desired_double_linked_list)

    def test_graphviz_linked_list_errors(self):
        typedef = "tipo Nó:\n\tinteiro c\n\tNó prox\n\tNó(inteiro chave):\n\t\tc <- chave\n"

        self.assertRaises(TupyTypeError, Interpreter.interpret, "lista_encadeada(1)") # too few args
        self.assertRaises(TupyTypeError, Interpreter.interpret, "lista_encadeada(1, 2, 3, 4, 5, 6, 7, 8)") # too many args
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
        self.assertRaises(TupyTypeError, Interpreter.interpret,
            "{0}Nó cab <- Nó(0); lista_encadeada(cab, \"c\", \"prox\", falso, [cab], \"\", 2)".format(typedef)) #not string
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

    def test_graphviz_heap(self):
        desired_heap = ('[[DOT strict graph {overlap=false; node [fontsize=16 width=0.2 '
                        'margin=0.05 shape=circle]; edge [arrowsize=0.8]; node [shape=square]; '
                        '0 [label = "10"]; 1 [label = "5"]; 0 -- 1 ; 2 [label = "20"]; 0 -- 2 '
                        '[color = red]; 3 [label = "2"]; 1 -- 3 ; 4 [label = "7"]; 1 -- 4 ; 5 '
                        '[label = "15"]; 2 -- 5 [color = red]; 6 [label = "25"]; 2 -- 6 '
                        '[color = red]; 7 [label = "1"]; 3 -- 7 ; 8 [label = "3"]; 3 -- 8 ; 9 '
                        '[label = "6"]; 4 -- 9 ; 10 [label = "8"]; 4 -- 10 ; 3 [style = filled '
                        'fillcolor = yellow]; 5 [style = filled fillcolor = yellow]; 1 [style = '
                        'filled fillcolor = yellow]; 99 -- 0 }]]')

        desired_empty_heap = _empty_graphviz_return
        ret = Interpreter.interpret(("inteiro H[*] <- [10, 5, 20, 2, 7, 15, 25, 1, 3, 6, 8]\n"
                                     "heap(H, [3, 5, 1], [2, 5, 6], \"node [shape=square];\", \"99 -- 0\"), \\\n"
                                     "heap([], [3, 5, 1], [2, 5, 6], \"node [shape=square];\", \"99 -- 0\")\n"))
        self.assertEqual(ret[0].type, Type.STRING)
        self.assertEqual(ret[0].value, desired_heap)
        self.assertEqual(ret[1].type, Type.STRING)
        self.assertEqual(ret[1].value, desired_empty_heap)

if __name__ == '__main__':
    unittest.main()
