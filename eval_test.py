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
                             TupyIndexError, TupyAssertionError

class TestEvalVisitor(unittest.TestCase):
    eex = "testOrExpression"

    def setUp(self):
        Interpreter.isDebug = False

    def evalExpression(self, expr):
        return Interpreter.interpret(expr, type(self).eex).get()

    def assertArrayEquals(self, ret, targetType, array):
        print("assertArrayEquals({0}, {1}, {2})".format(ret, targetType, array))
        self.assertEqual(len(ret.value), len(array))
        for ind in range(len(array)):
            if (isinstance(array[ind], list)):
                self.assertEqual(memRead(ret.value[ind]).type, Type.ARRAY)
                self.assertArrayEquals(memRead(ret.value[ind]), targetType, array[ind])
            else:
                self.assertEqual(memRead(ret.value[ind]).type, targetType)
                self.assertEqual(memRead(ret.value[ind]).value, array[ind])

    def test_integer(self):
        ret = self.evalExpression("123\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 123)
        ret = self.evalExpression("0XFF\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 255)
        ret = self.evalExpression("0o17\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 15)
        ret = self.evalExpression("0b11011\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 27)

    def test_float(self):
        ret = self.evalExpression("123.0\n")
        # print(ret)
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 123.0)

    def test_string(self):
        ret = self.evalExpression("\"123.0\"\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "123.0")
        ret = self.evalExpression("\"123.0\" \"00.32\" \"1.000\"\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "123.000.321.000")
        ret = self.evalExpression("\"123.0\" \\\n\"00.32\" \\\n\"1.000\"\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "123.000.321.000")
    
    def test_char(self):
        ret = self.evalExpression("'a'\n")
        self.assertEqual(ret.type, Type.CHAR)
        self.assertEqual(ret.value, ord("a"))

    def test_bool(self):
        ret = self.evalExpression("verdadeiro\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        print("DONE")
        ret = self.evalExpression("falso\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)

    def test_null(self):
        ret = self.evalExpression("nulo\n")
        self.assertEqual(ret.type, Type.NULL)

    def test_pi(self):
        ret = self.evalExpression("pi\n")
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.pi)
        ret = self.evalExpression("π\n")
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.pi)

    def test_tuple(self):
        ret = self.evalExpression("(1, 3.14, \"ok\", [1,5])\n")
        self.assertEqual(ret.type, Type.TUPLE)
        self.assertEqual(memRead(ret.value[0]).type, Type.INT)
        self.assertEqual(memRead(ret.value[0]).value, 1)
        self.assertEqual(memRead(ret.value[1]).type, Type.FLOAT)
        self.assertEqual(memRead(ret.value[1]).value, 3.14)
        self.assertEqual(memRead(ret.value[2]).type, Type.STRING)
        self.assertEqual(memRead(ret.value[2]).value, "ok")
        self.assertEqual(memRead(ret.value[3]).type, Type.ARRAY)
        self.assertEqual(memRead(ret.value[3]).size, 2)
        ret = self.evalExpression("()\n")
        self.assertEqual(ret.type, Type.TUPLE)
        self.assertEqual(ret.size, 0)

    def test_array(self):
        ret = self.evalExpression("[1, 2, 3]\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertEqual(memRead(ret.value[0]).type, Type.INT)
        self.assertEqual(memRead(ret.value[0]).value, 1)
        self.assertEqual(memRead(ret.value[1]).type, Type.INT)
        self.assertEqual(memRead(ret.value[1]).value, 2)
        self.assertEqual(memRead(ret.value[2]).type, Type.INT)
        self.assertEqual(memRead(ret.value[2]).value, 3)
        self.assertRaises(TupyTypeError, self.evalExpression, "[1, 2, \"not_ok\"]\n")
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
            ("tipo A:\n"
             "\tinteiro x\n"
             "tipo B:\n"
             "\tinteiro x\n"
             "[A(), B()]\n"))
        ret = self.evalExpression("[]\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertEqual(ret.size, 0)

    def test_power_integer(self):
        ret = self.evalExpression("2^3\n")
        # print(ret)
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 8)
        ret = self.evalExpression("2^-1\n")
        # print(ret)
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 0.5)

    def test_factor_integer(self):
        ret = self.evalExpression("-2\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, -2)

    def test_factor_except(self):        
        self.assertRaises(TupyTypeError, self.evalExpression, "~verdadeiro\n")

    def test_term(self):
        ret = self.evalExpression("2*3\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 6)
        ret = self.evalExpression("1/4\n")
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 0.25)
        ret = self.evalExpression("3 mod 2\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = self.evalExpression("5 div 2\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 2)
        ret = self.evalExpression("\"abc\"*3\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "abcabcabc")
        ret = self.evalExpression("'a'*5\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, ord("a")*5)
        ret = self.evalExpression("verdadeiro*10\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 10)
        self.assertRaises(TupyTypeError, self.evalExpression, "5 div nulo\n")

    def test_arithmetic_expr(self):
        ret = self.evalExpression("2+3\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)
        ret = self.evalExpression("2-10\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, -8)
        ret = self.evalExpression("2+-1\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = self.evalExpression("+-10\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, -10)
        ret = self.evalExpression("2+7.5\n")
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 9.5)
        ret = self.evalExpression("falso+7.11\n")
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 7.11)
        ret = self.evalExpression("2+\"3\"\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "23")
        ret = self.evalExpression("'a'+\"b\"\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "ab")
        self.assertRaises(TupyTypeError, self.evalExpression, "nulo - 5\n")

    def test_arithmetic_compound(self):
        ret = self.evalExpression("1-2+3+4+5-6\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)
        ret = self.evalExpression("6*2-4\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 8)

    def test_typed_arithmetic(self):
        ret = self.evalExpression("verdadeiro + falso\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = self.evalExpression("\'9\' - \'0\'\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 9)
        self.assertRaises(TupyTypeError, self.evalExpression, "5 - [4]\n")
        

    def test_arithmetic_parenthesis(self):
        ret = self.evalExpression("((1-2)*(3+4)-7)/-((2^3)-(10^(128 && 32)))\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 2)
    
    def test_shift_expr(self):
        ret = self.evalExpression("1<<4\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 16)
        ret = self.evalExpression("200>>3\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 25)
        self.assertRaises(TupyTypeError, self.evalExpression, "1.0<<4\n")
        self.assertRaises(TupyTypeError, self.evalExpression, "200>>3.0\n")

    def test_bitwise_and_expr(self):
        ret = self.evalExpression("3 && 5 && 9\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        self.assertRaises(TupyTypeError, self.evalExpression, "3.0 && 5\n")
        self.assertRaises(TupyTypeError, self.evalExpression, "3 && 5.0\n")

    def test_bitwise_or_expr(self):
        ret = self.evalExpression("1 || 2 || 13 || 16\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 31)
        self.assertRaises(TupyTypeError, self.evalExpression, "1.0 || 2\n")
        self.assertRaises(TupyTypeError, self.evalExpression, "2 || 13.0\n")

    def test_bitwise_xor_expr(self):
        ret = self.evalExpression("4287 xor 1200\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5135)
        self.assertRaises(TupyTypeError, self.evalExpression, "4287 xor \"1200\"\n")
        self.assertRaises(TupyTypeError, self.evalExpression, "4287.0 xor 1200\n")

    def test_bitwise_not_expr(self):
        ret = self.evalExpression("~(100+73)\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, -174)
        self.assertRaises(TupyTypeError, self.evalExpression, "~verdadeiro\n")

    def test_arithmetic_error(self):        
        self.assertRaises(TupyTypeError, Interpreter.interpret, ("inteiro func(inteiro a):\n"
                                                             "\tretornar a\n"
                                                             "func + func\n"
                                                            ))
        self.assertRaises(TupyTypeError, Interpreter.interpret, ("tipo Teste:\n"
                                                             "\tinteiro a\n"
                                                             "Teste u, v <- Teste(), Teste()\n"
                                                             "u + v\n"
                                                            ))


    def test_comparison(self):
        ret = self.evalExpression("3 < 4\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = self.evalExpression("3 < 2\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = self.evalExpression("45 > 4\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = self.evalExpression("4 > 4\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = self.evalExpression("4 >= 4\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = self.evalExpression("0.00 >= 0.01\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = self.evalExpression("\"a\" <= \"b\"\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = self.evalExpression("\'a\' <= \'A\'\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = self.evalExpression("1 != 0\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = self.evalExpression("1 != 1\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = self.evalExpression("1 = 1\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = self.evalExpression("1.00 = 1.01\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)

    def test_bool_logic(self):
        ret = self.evalExpression("não verdadeiro\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = self.evalExpression("nao falso\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = self.evalExpression("nao não 3 = 4\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = self.evalExpression("verdadeiro e verdadeiro\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = self.evalExpression("verdadeiro e nao verdadeiro\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = self.evalExpression("não falso ou falso\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = self.evalExpression("não verdadeiro ou 1 = 2\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)

    def test_cardinality(self):
        ret = self.evalExpression("|12|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = self.evalExpression("|12.0|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = self.evalExpression("|'a'|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = self.evalExpression("|verdadeiro|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = self.evalExpression("|nulo|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 0)
        ret = self.evalExpression("|\"12\"|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 2)
        ret = self.evalExpression("|[10,20]|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 2)
        ret = self.evalExpression("|[[10],[1,2,3,4]]|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)
        ret = self.evalExpression("|(10,[1,2,3,4],('a', verdadeiro),\"teste\")|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 8)


    def test_subscripts(self):
        ret = self.evalExpression("[5,10,20,40][2]\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 20)
        ret = self.evalExpression("[5,10,20,40][1..2]\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertEqual(memRead(ret.value[0]).type, Type.INT)
        self.assertEqual(memRead(ret.value[0]).value, 10)
        self.assertEqual(memRead(ret.value[1]).type, Type.INT)
        self.assertEqual(memRead(ret.value[1]).value, 20)
        ret = self.evalExpression("(5,10.1,20,40)[1..2]\n")
        self.assertEqual(ret.type, Type.TUPLE)
        self.assertEqual(memRead(ret.value[0]).type, Type.FLOAT)
        self.assertEqual(memRead(ret.value[0]).value, 10.1)
        self.assertEqual(memRead(ret.value[1]).type, Type.INT)
        self.assertEqual(memRead(ret.value[1]).value, 20)
        ret_1 = self.evalExpression("[5,10,20,40]\n")
        ret_2 = self.evalExpression("[5,10,20,40][*]\n")
        self.assertEqual(ret_2.type, Type.ARRAY)
        for i in range(len(ret_1.value)):
            self.assertEqual(memRead(ret_2.value[i]).type, memRead(ret_1.value[i]).type)
            self.assertEqual(memRead(ret_2.value[i]).value, memRead(ret_1.value[i]).value)
        self.assertRaises(TupyTypeError, Interpreter.interpret, "2[0]\n")


    def test_declaration_defaults(self):
        ret = Interpreter.interpret("inteiro a, b, c; a\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 0)
        ret = Interpreter.interpret("real a, b, c; b\n")
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 0)
        ret = Interpreter.interpret("caracter a, b, c; c\n")
        self.assertEqual(ret.type, Type.CHAR)
        self.assertEqual(ret.value, 0)
        ret = Interpreter.interpret("logico a, b, c; a\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = Interpreter.interpret("cadeia a, b, c; b\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "")
        ret = Interpreter.interpret("inteiro a[5]; a\n")
        self.assertArrayEquals(ret, Type.INT, [0, 0, 0, 0, 0])
        ret = Interpreter.interpret("inteiro a[3,3,3]; a\n")
        self.assertArrayEquals(ret, Type.INT, [[[0,0,0], [0,0,0], [0,0,0]], 
                                               [[0,0,0], [0,0,0], [0,0,0]],
                                               [[0,0,0], [0,0,0], [0,0,0]]])
        ret = Interpreter.interpret("inteiro a[*]; a\n")
        self.assertArrayEquals(ret, Type.INT, [])
        ret = Interpreter.interpret("inteiro a[*,*,3]; a\n")
        self.assertArrayEquals(ret, Type.INT, [])
        ret = Interpreter.interpret("inteiro a[3,*,*]; a\n")
        self.assertArrayEquals(ret, Type.INT, [[],[],[]])
        ret = Interpreter.interpret("inteiro a[*,3,*]; a\n")
        self.assertArrayEquals(ret, Type.INT, [])

    def test_assignment(self):
        ret = Interpreter.interpret("inteiro a <- 3; a\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 3)
        ret = Interpreter.interpret("caracter b, c <- '3', '5'; b, c\n")
        self.assertEqual(ret[0].type, Type.CHAR)
        self.assertEqual(ret[0].value, ord("3"))
        self.assertEqual(ret[1].type, Type.CHAR)
        self.assertEqual(ret[1].value, ord("5"))
        ret = Interpreter.interpret("inteiro a, b; a <- b <- 3; a, b\n")
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 3)
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 3)
        ret = Interpreter.interpret("inteiro c, d; inteiro a, b <- c, d <- 3, 30; a, b, c, d\n")
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 3)
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 30)
        self.assertEqual(ret[2].type, Type.INT)
        self.assertEqual(ret[2].value, 3)
        self.assertEqual(ret[3].type, Type.INT)
        self.assertEqual(ret[3].value, 30)
        self.assertRaises(TupyNameError, Interpreter.interpret, "inteiro a <- b\n")
        self.assertRaises(TupyNameError, Interpreter.interpret, "inteiro a <- b <- 3\n")
        self.assertRaises(TupyTypeError, Interpreter.interpret, "inteiro a; real b <- 3.0; a <- b; a\n")
        self.assertRaises(TupyTypeError, Interpreter.interpret, "inteiro a <- 3.01; a\n")
        self.assertRaises(TupyTypeError, Interpreter.interpret, "inteiro a, b <- 3, 3.01; a, b\n")
        self.assertRaises(TupySyntaxError, Interpreter.interpret, "2 <- b\n")
        self.assertRaises(TupySyntaxError, Interpreter.interpret, "inteiro a(2) <- [1, 2]\n")
        self.assertRaises(TupySyntaxError, Interpreter.interpret, "inteiro a[2][1] <- [[1], [2]]\n")
        self.assertRaises(TupyValueError, Interpreter.interpret, "inteiro a, b, c <- 1, 2\n")
        self.assertRaises(TupyValueError, Interpreter.interpret, "inteiro a, b, c <- 1, 2, 3, 4\n")

    def test_assignment_cache(self):
        ret = Interpreter.interpret("inteiro a, b, c <- 1, 2, 3\na, b, c <- b, c, a\n")
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 2)
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 3)
        self.assertEqual(ret[2].type, Type.INT)
        self.assertEqual(ret[2].value, 1)

    def test_unicode_identifier(self):
        ret = Interpreter.interpret("inteiro ímã <- 333; ímã\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 333)

    def test_array_declaration(self):
        ret = Interpreter.interpret("inteiro a[5] <- [9,8,7,6,5]; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        targetArray = [9,8,7,6,5]
        self.assertArrayEquals(ret, Type.INT, targetArray)
        ret = Interpreter.interpret("inteiro a[*] <- [9,8,7,6,5]; a\n")
        self.assertArrayEquals(ret, Type.INT, targetArray)
        self.assertRaises(TupyTypeError, Interpreter.interpret, "inteiro a[4] <- [9,8,7,6,5]; a\n")
        self.assertRaises(TupySyntaxError, Interpreter.interpret, "inteiro a[10..15] <- [1,2,3]; a\n")
        self.assertRaises(TupySyntaxError, Interpreter.interpret, "inteiro a[-3] <- [1,2,3]; a\n")
        targetArray = [[1,2,3], [4,5,6], [7,8,9]]
        ret = Interpreter.interpret("inteiro m[3,3] <- [[1,2,3], [4,5,6], [7,8,9]]; m\n")
        self.assertArrayEquals(ret, Type.INT, targetArray)
        ret = Interpreter.interpret("inteiro a[5] <- [9,8,7]; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        targetArray = [9,8,7,0,0]
        self.assertArrayEquals(ret, Type.INT, targetArray)
        ret = Interpreter.interpret("cadeia s[3,2] <- [[\"oi\"], [\"tudo\"], [\"ok\"]]; s\n")
        targetArray = [["oi", ""], ["tudo", ""], ["ok", ""]]
        self.assertArrayEquals(ret, Type.STRING, targetArray)
        ret = Interpreter.interpret("real s[3,2,2] <- [ [[1.0], [2.0, 3.0]], [[4.0], []], [[5.0, 6.0]]]; s\n")
        targetArray = [ [[1.0, 0.0], [2.0, 3.0]], [[4.0, 0.0], [0.0, 0.0]], [[5.0, 6.0], [0.0, 0.0]] ]
        self.assertArrayEquals(ret, Type.FLOAT, targetArray)
        ret = Interpreter.interpret("real s[3,2,*] <- [ [[1.0], [2.0, 3.0]], [[4.0], []], [[5.0, 6.0]]]; s\n")
        targetArray = [ [[1.0], [2.0, 3.0]], [[4.0], []], [[5.0, 6.0], []] ]
        self.assertArrayEquals(ret, Type.FLOAT, targetArray)
        ret = Interpreter.interpret("inteiro a[5], b <- [9,8,7,6,5], 69; a, b\n")
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 69)
        self.assertRaises(TupyTypeError, Interpreter.interpret, "inteiro a[2,2] <- [[[2,2],[2,2]],[[2,2],[2,2]]]; a\n")

    def test_array_get(self):
        ret = Interpreter.interpret("inteiro a[5] <- [1,2,3,4,5]; a[-1], a[-4..-1]\n")
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 5)
        self.assertEqual(ret[1].type, Type.ARRAY)
        self.assertArrayEquals(ret[1], Type.INT, [2,3,4,5])
        ret = Interpreter.interpret("inteiro a[3,3] <- [[1,2,3], [4,5,6], [7,8,9]]; a[1..2, 1..2], a[1..2][1..2]\n")
        self.assertEqual(ret[0].type, Type.ARRAY)
        self.assertEqual(ret[1].type, Type.ARRAY)
        targetArray = [[5,6], [8,9]]
        targetArray2 = [[7,8,9]]
        self.assertArrayEquals(ret[0], Type.INT, targetArray)
        self.assertArrayEquals(ret[1], Type.INT, targetArray2)
        ret = Interpreter.interpret(
            ("inteiro a[3,3,3] <- [[[1,2,3], [4,5,6], [7,8,9]],"
                                  "[[11,12,13], [14,15,16], [17,18,19]],"
                                  "[[21,22,23], [24,25,26], [27,28,29]]];"
                                  "a[1..2, *, 0]\n"))
        self.assertEqual(ret.type, Type.ARRAY)
        targetArray = [[11, 14, 17], [21, 24, 27]]
        self.assertArrayEquals(ret, Type.INT, targetArray)
        ret = Interpreter.interpret("cadeia S <- \"Hello World\"; S[1..2]\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "el")
        ret = Interpreter.interpret("cadeia S <- \"Hello World\"; S[*]\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "Hello World")
        ret = Interpreter.interpret("cadeia S <- \"Hello World\"; S[4]\n")
        self.assertEqual(ret.type, Type.CHAR)
        self.assertEqual(ret.value, ord("o"))
        ret = Interpreter.interpret("cadeia S[3] <- [\"Hello\", \"World\"]; S\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertArrayEquals(ret, Type.STRING, ["Hello", "World", ""])
        ret = Interpreter.interpret("cadeia S[3] <- [\"Hello\", \"World\"]; S[1,2..3]\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "rl")
        self.assertRaises(TupySyntaxError, Interpreter.interpret, "inteiro a[5] <- [1,2,3,4,5]; a[2..1]\n")

    def test_array_assignment(self):
        ret = Interpreter.interpret("inteiro a[5]; a <- [1]; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        targetArray = [1,0,0,0,0]
        self.assertArrayEquals(ret, Type.INT, targetArray)
        ret = Interpreter.interpret("inteiro a[3,3]; a <- [[1,1], [1, 1]]; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        targetArray = [[1,1,0],[1,1,0],[0,0,0]]
        self.assertArrayEquals(ret, Type.INT, targetArray)
        ret = Interpreter.interpret("inteiro a[5]; a[2] <- 1; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        targetArray = [0,0,1,0,0]
        self.assertArrayEquals(ret, Type.INT, targetArray)
        ret = Interpreter.interpret("inteiro a[5]; a[1..3] <- [2, 2, 2]; a[2] <- 1; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        targetArray = [0,2,1,2,0]
        self.assertArrayEquals(ret, Type.INT, targetArray)
        ret = Interpreter.interpret("inteiro a[5]; a[*] <- [1, 2, 3, 4]; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        targetArray = [1,2,3,4,0]
        self.assertArrayEquals(ret, Type.INT, targetArray)
        ret = Interpreter.interpret("inteiro a[5]; a[*] <- 4; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertArrayEquals(ret, Type.INT, [4,4,4,4,4])
        ret = Interpreter.interpret("inteiro a[2,2,2]; a[*,*,*] <- 1; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertArrayEquals(ret, Type.INT, [[[1,1], [1,1]], [[1,1], [1,1]]])
        ret = Interpreter.interpret("inteiro a[2,2,2]; a[*,1,*] <- 1; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertArrayEquals(ret, Type.INT, [[[0,0], [1,1]],
                                               [[0,0], [1,1]]])
        ret = Interpreter.interpret("inteiro a[3], b[4] <- nulo, [1, 2, 3]; a <- b[-3..-2]; a, b\n")
        self.assertEqual(ret[0].type, Type.ARRAY)
        self.assertArrayEquals(ret[0], Type.INT, [2,3,0])
        self.assertEqual(ret[1].type, Type.ARRAY)
        self.assertArrayEquals(ret[1], Type.INT, [1,2,3,0])
        ret = Interpreter.interpret("inteiro a[3,3] <- [[1,2,3], [4,5,6], [7,8,9]]; a[1..2, 1..2] <- 0; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        targetArray = [[1,2,3], [4,0,0], [7,0,0]]
        self.assertArrayEquals(ret, Type.INT, targetArray)
        ret = Interpreter.interpret("inteiro a[3,3] <- [[1,2,3], [4,5,6], [7,8,9]]; a[1][1] <- 2; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        targetArray = [[1,2,3], [4,2,6], [7,8,9]]
        self.assertArrayEquals(ret, Type.INT, targetArray)  
        ret = Interpreter.interpret(("inteiro a[2,3,3]\n"
                                     "a[1,0..1,1..2] <- [3, 4]\n"
                                     "a\n"
                                    ))
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertArrayEquals(ret, Type.INT, [ [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                                                [[0, 3, 3], [0, 4, 4], [0, 0, 0]] ])    

    def test_dynamic_arrays(self):
        ret = Interpreter.interpret("inteiro a[*]; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertArrayEquals(ret, Type.INT, [])
        ret = Interpreter.interpret("inteiro a[*]; inteiro b[2], c[2] <- [1,2], [3,4]; a[*] <- b + c; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertArrayEquals(ret, Type.INT, [1,2,3,4])
        ret = Interpreter.interpret("inteiro a[*]; a <- a + [0]; a <- a + [0]; a <- a + [5]; a, |a|\n")
        self.assertEqual(ret[0].type, Type.ARRAY)
        self.assertArrayEquals(ret[0], Type.INT, [0,0,5])
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 3)
        ret = Interpreter.interpret("inteiro a[*,*]; a <- a + [[]]; a <- a + [[]]; a[0] <- [1, 2, 3]; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertArrayEquals(ret, Type.INT, [[1, 2, 3], []])
        ret = Interpreter.interpret("inteiro a[*,2]; a <- a + [[]]; a <- a + [[]]; a[0,0] <- 8; a[0,1] <- 10; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertArrayEquals(ret, Type.INT, [[8, 10], [0, 0]])
        ret = Interpreter.interpret("inteiro a[2,*]; a[0] <- a[0] + [1, 2]; a[1] <- a[0] + [3, 4]; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertArrayEquals(ret, Type.INT, [[1, 2], [1, 2, 3, 4]])
        ret = Interpreter.interpret(("inteiro a[*,*] <- [[1, 2, 3], [4, 5], [6]]\n"
                                     "a[1..2] <- [[4, 5, 6], [7, 8, 9, 0]]\n"
                                     "a, |a|\n"))
        self.assertEqual(ret[0].type, Type.ARRAY)
        self.assertArrayEquals(ret[0], Type.INT, [[1, 2, 3], [4, 5, 6], [7, 8, 9, 0]])
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 10)
        ret = Interpreter.interpret(("inteiro X[*,*], Y[*,*]\n"
                                     "X <- [[1, 2], [3, 4, 5]]\n"
                                     "Y <- [[5, 4, 3], [2, 1]]\n"
                                     "X[0,*] <- Y[0,*]\n"
                                     "X, Y\n"
                                    ))
        self.assertArrayEquals(ret[0], Type.INT, [[5, 4, 3], [3, 4, 5]])
        self.assertArrayEquals(ret[1], Type.INT, [[5, 4, 3], [2, 1]])

    def test_if(self):
        ret = Interpreter.interpret("se 2 > 1: \"ok\"\nsenão: \"not ok\"\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "ok")
        ret = Interpreter.interpret("se 1 > 2: \"not ok\"\nsenão: \"ok\"\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "ok")
        ret = Interpreter.interpret("se falso: \"not ok\"\nsenao se verdadeiro: \"ok\"\nsenão: \"not ok\"\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "ok")


    def test_nested_if(self):
        ret = Interpreter.interpret(("se verdadeiro:\n"
                                     "\t se 2 > 3:\n"
                                     "\t\t\"not ok\"\n"
                                     "\t senao se verdadeiro:\n"
                                     "\t\t\"ok\"\n"
                                     "\t senão: \"not ok\"\n"))
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "ok")

    def test_block(self):
        ret = Interpreter.interpret(("inteiro a <- 5\n"
                                     "se verdadeiro:\n"
                                     "\t inteiro b <- 6\n"
                                     "a\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)
        self.assertRaises(TupyNameError, Interpreter.interpret, ("inteiro a <- 5\n"
                                                             "se verdadeiro:\n"
                                                             "\t inteiro b <- 6\n"
                                                             "b\n"
                                                            ))
        ret = Interpreter.interpret(("inteiro a <- 5\n"
                                     "se verdadeiro:\n"
                                     "\t inteiro a <- 6\n"
                                     "a\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)

    def test_return(self):
        ret = Interpreter.interpret(("inteiro a <- 5\n"
                                     "retornar a\n"
                                     "a <- 6\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)

    def test_function(self):
        ret = Interpreter.interpret(("inteiro func():\n"
                                     "\t retornar 5\n"
                                     "func()\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)
        ret = Interpreter.interpret(("inteiro func(inteiro a, inteiro b):\n"
                                     "\t retornar a+b\n"
                                     "func(10,-5)\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)
        ret = Interpreter.interpret(("inteiro func(inteiro a, inteiro b <- 5):\n"
                                     "\t retornar a+b\n"
                                     "func(-4, 10), func(10)\n"
                                    ))
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 6)
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 15)
        self.assertRaises(TupyTypeError, Interpreter.interpret, ("inteiro func():\n"
                                                             "\t retornar 5\n"
                                                             "func(5)\n"
                                                            ))
        self.assertRaises(TupyTypeError, Interpreter.interpret, ("inteiro func(inteiro a):\n"
                                                             "\t retornar a\n"
                                                             "func(\"5\")\n"
                                                            ))
        self.assertRaises(TupyTypeError, Interpreter.interpret, ("inteiro func(inteiro a):\n"
                                                             "\t retornar a\n"
                                                             "func()\n"
                                                            ))

    def test_function_no_return(self):
        ret = Interpreter.interpret(("inteiro a <- 1\n"
                                     "func(inteiro b):\n"
                                     "\t a <- a + b\n"
                                     "func(5)\n"
                                     "a\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 6)
        ret = Interpreter.interpret(("inteiro a <- 1\n"
                                     "func(inteiro b):\n"
                                     "\t a <- a + b\n"
                                     "\t retornar\n"
                                     "\t a <- 0\n"
                                     "func(10)\n"
                                     "a\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 11)

    def test_function_character(self):
        ret = Interpreter.interpret(("cadeia s <- \"Teste\"\n"
                                     "caracter func(caracter x):\n"
                                     "\tretornar caracter(x + 1)\n"
                                     "func(s[1])\n"
                                    ))
        self.assertEqual(ret.type, Type.CHAR)
        self.assertEqual(ret.value, ord("f"))

    def test_function_overload(self):
        ret = Interpreter.interpret(("inteiro func(inteiro a, inteiro b):\n"
                                     "\t retornar a+b\n"
                                     "cadeia func(cadeia a, inteiro b):\n"
                                     "\t retornar a*b\n"
                                     "func(10,-5), func(\"a\",5)\n"
                                    ))
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 5)
        self.assertEqual(ret[1].type, Type.STRING)
        self.assertEqual(ret[1].value, "aaaaa")
        self.assertRaises(TupyNameError, Interpreter.interpret, 
                         ("inteiro func(inteiro a, inteiro b):\n"
                          "\t retornar a+b\n"
                          "inteiro func(inteiro a, inteiro b <- 1):\n"
                          "\t retornar a*b\n"
                          "func(5,2)\n"
                         ))
        self.assertRaises(TupyNameError, Interpreter.interpret, 
                         ("inteiro func(inteiro a):\n"
                          "\t retornar a*a\n"
                          "inteiro func(inteiro a, inteiro b <- 1):\n"
                          "\t retornar a*b\n"
                          "func(5)\n"
                         ))

    def test_function_array(self):
        ret = Interpreter.interpret(("inteiro tamanho(inteiro[] a):\n"
                                     "\t retornar |a|\n"
                                     "tamanho([1,3,5,7,9])\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)
        ret = Interpreter.interpret(("inteiro[][] altera_matriz(inteiro[][] a):\n"
                                     "\t a[*,1] <- 0\n"
                                     "\t retornar a\n"
                                     "altera_matriz([[1,2,3],[4,5,6]])\n"
                                    ))
        self.assertArrayEquals(ret, Type.INT, [[1, 0, 3], [4, 0, 6]])        

    def test_function_variadic(self):
        ret = Interpreter.interpret(("inteiro teste(args...):\n"
                                     "\t se |args| > 1:\n"
                                     "\t\t retornar args[0] + args[1]\n"
                                     "\t senão:\n"
                                     "\t\t retornar 0\n"
                                     "teste(2,2), teste(2), teste()\n"
                                    ))
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 4)
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 0)
        self.assertEqual(ret[2].type, Type.INT)
        self.assertEqual(ret[2].value, 0)
        ret = Interpreter.interpret(("inteiro teste(inteiro a, args...):\n"
                                     "\t retornar a+|args|\n"
                                     "teste(10,4,5,6,7)\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 14)
        ret = Interpreter.interpret(("inteiro teste(inteiro a, args...):\n"
                                     "\t retornar a+|args|\n"
                                     "cadeia teste(inteiro a, cadeia b):\n"
                                     "\t retornar b*a\n"
                                     "teste(5,\"c\")\n"
                                    ))
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "ccccc")
        ret = Interpreter.interpret(("cadeia teste(ref args...):\n"
                                     "\t retornar escrever(args[0])\n"
                                     "inteiro V[5]\n"
                                     "teste(V[2])\n"
                                    ))
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "referência a 'V'")

        self.assertRaises(TupyTypeError, Interpreter.interpret, 
                         ("teste(ref args...):\n"
                          "\t retornar args[0] > args[1]\n"
                          "inteiro a, b\n"
                          "teste(a, b)\n"
                         ))

        self.assertRaises(TupyTypeError, Interpreter.interpret, 
                         ("teste(ref args...):\n"
                          "\t retornar args[0] + args[1]\n"
                          "inteiro a, b\n"
                          "teste(a, b)\n"
                         ))

    def test_recursion(self):
        ret = Interpreter.interpret(("inteiro fat(inteiro n):\n"
                                     "\t se n = 1:\n"
                                     "\t\t retornar n\n"
                                     "\t senão:\n"
                                     "\t\t retornar n * fat(n-1)\n"
                                     "fat(5)\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 120)

    def test_builtin_function(self):
        ret = Interpreter.interpret("escrever(5)\n")
        self.assertEqual(Interpreter.outStream.getvalue(), "5\n")
        ret = Interpreter.interpret("escrever(5,\"cinco\",\'a\')\n")
        self.assertEqual(Interpreter.outStream.getvalue(), "5 cinco a\n")
        ret = Interpreter.interpret("escrever([1, 2, 3])\n")
        self.assertEqual(Interpreter.outStream.getvalue(), "[1, 2, 3]\n")
        ret = Interpreter.interpret("escrever((4, 5, 6))\n")
        self.assertEqual(Interpreter.outStream.getvalue(), "(4, 5, 6)\n")
        ret = Interpreter.interpret("inteiro func():\n\tretornar 5\nescrever(func)\n")
        self.assertEqual(Interpreter.outStream.getvalue(), "função\n")
        ret = Interpreter.interpret("tipo Aluno:\n\tinteiro nota\nAluno a <- Aluno()\nescrever(a)\n")
        self.assertEqual(Interpreter.outStream.getvalue(), "Aluno\n")
        ret = Interpreter.interpret(("inteiro escrever(inteiro n):\n"
                                     "\t retornar 100\n"
                                     "escrever(5)\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 100)


    def test_function_errors(self):
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
                         ("inteiro func():\n"
                          "\t retornar 2.3\n"
                          "func()\n"
                         ))
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
                         ("inteiro func():\n"
                          "\t2.3\n"
                          "func()\n"
                         ))
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
                         ("inteiro func(inteiro a):\n"
                          "\t retornar 200\n"
                          "func(\"xyz\")\n"
                         ))
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
                         ("inteiro[] func(inteiro a):\n"
                          "\t retornar a\n"
                          "func(2)\n"
                         ))
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
                         ("inteiro func(inteiro a):\n"
                          "\t retornar a\n"
                          "func([1, 2, 3])\n"
                         ))
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
                         ("inteiro func(inteiro[][] a):\n"
                          "\t retornar |a|\n"
                          "func([1,2,3])\n"
                         ))

    def test_function_param_passage(self):
        ret = Interpreter.interpret(("inteiro x <- 1\n"
                                     "func(inteiro a, inteiro b):\n"
                                     "\t a <- a + b\n"
                                     "func(x, 10)\n"
                                     "x\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = Interpreter.interpret(("inteiro x <- 1\n"
                                     "func(val inteiro a, val inteiro b):\n"
                                     "\t a <- a + b\n"
                                     "func(x, 10)\n"
                                     "x\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = Interpreter.interpret(("inteiro x <- 1\n"
                                     "func(ref inteiro a, val inteiro b):\n"
                                     "\t a <- a + b\n"
                                     "func(x, 10)\n"
                                     "x\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 11)
        ret = Interpreter.interpret(("inteiro x <- 1\n"
                                     "func(ref inteiro a):\n"
                                     "\t a <- a + 1\n"
                                     "\t a <- a + x\n"
                                     "func(x)\n"
                                     "x\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 4)
        self.assertRaises(TupySyntaxError, Interpreter.interpret, 
                         ("inteiro x, y <- 1, 2\n"
                          "func(ref inteiro a, val inteiro b):\n"
                          "\t a <- a + b\n"
                          "func(x+y, 10)\n"
                          "x\n"
                        ))
        ret = Interpreter.interpret(("real x[3] <- 5.0\n"
                                     "func(ref real[] a, val inteiro b):\n"
                                     "\t a[1] <- a[1] * b\n"
                                     "func(x, 5)\n"
                                     "x\n"
                                    ))
        self.assertArrayEquals(ret, Type.FLOAT, [5.0, 25.0, 5.0])  


    def test_while(self):
        ret = Interpreter.interpret(("inteiro i, x <- 0, 1\n"
                                     "enquanto i < 10:\n"
                                     "\t x <- x * 2\n"
                                     "\t i <- i + 1\n"
                                     "x\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1024)

    # SLOW!! : https://github.com/antlr/antlr4/issues/1219
    def test_infinite_loop(self):
        self.assertRaises(TupyRuntimeError, Interpreter.interpret, 
                         ("enquanto verdadeiro:\n"
                          "\t 1\n"
                         ))
        self.assertRaises(TupyRuntimeError, Interpreter.interpret, 
                         ("inteiro i\n"
                          "para i <- 1..0 passo 1:\n"
                          "\t1\n"
                         ))

    def test_simple_class(self):
        ret = Interpreter.interpret(("tipo Aluno:\n"
                                     "\tcadeia nome\n"
                                     "\n"
                                     "Aluno a <- Aluno()\n"
                                     "a.nome <- \"Paulo\"\n"
                                     "a.nome\n"
                                    ))
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "Paulo")
        self.assertRaises(TupyRuntimeError, Interpreter.interpret, 
                         ("tipo Aluno:\n"
                          "\tcadeia nome\n"
                          "Aluno a\n"
                          "a.nome\n"
                         ))

    def test_class_method(self):
        ret = Interpreter.interpret(("tipo Teste:\n"
                                     "\tinteiro func(inteiro a, inteiro b):\n"
                                     "\t\tretornar a*a+b*b\n"
                                     "Teste t <- Teste()\n"
                                     "t.func(5,2)\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 29)

    def test_class_method_attribute(self):
        ret = Interpreter.interpret(("tipo Teste:\n"
                                     "\tinteiro contador\n"
                                     "\tincrementa():\n"
                                     "\t\tcontador <- contador+1\n"
                                     "Teste t <- Teste()\n"
                                     "t.incrementa(); t.incrementa();\n"
                                     "t.contador\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 2)

    def test_class_inheritance(self):
        ret = Interpreter.interpret(("tipo Teste:\n"
                                     "\tinteiro func(inteiro a, inteiro b):\n"
                                     "\t\tretornar a*a+b*b\n"
                                     "\n"
                                     "tipo Teste2(Teste):\n"
                                     "\tinteiro func2(inteiro a):\n"
                                     "\t\tretornar a*a*a\n"
                                     "\n"
                                     "Teste2 t <- Teste2()\n"
                                     "t.func(5,2), t.func2(10)\n"
                                    ))
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 29)
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 1000)

    def test_class_constructor(self):
        ret = Interpreter.interpret(("tipo Teste:\n"
                                     "\tinteiro x, y\n"
                                     "\tTeste(inteiro a, inteiro b):\n"
                                     "\t\tx <- a\n"
                                     "\t\ty <- b\n"
                                     "\n"
                                     "\tinteiro soma():\n"
                                     "\t\tretornar x+y\n"
                                     "Teste t <- Teste(10, 50)\n"
                                     "t.soma()\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 60)

    def test_class_multiple_constructors(self):
        ret = Interpreter.interpret(("tipo Teste:\n"
                                     "\tinteiro x <- 10\n"
                                     "\tTeste(inteiro a, inteiro b):\n"
                                     "\t\tx <- a*b\n"
                                     "\n"
                                     "\tTeste(inteiro a):\n"
                                     "\t\tx <- a*a\n"
                                     "Teste t, u, v <- Teste(5, 4), Teste(), Teste(6)\n"
                                     "t.x, u.x, v.x\n"
                                    ))
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 20)
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 10)
        self.assertEqual(ret[2].type, Type.INT)
        self.assertEqual(ret[2].value, 36)

    def test_function_class_parameters(self):
        ret = Interpreter.interpret(("tipo Ponto:\n"
                                     "\tinteiro x, y\n"
                                     "\tPonto(inteiro a, inteiro b):\n"
                                     "\t\tx, y <- a, b\n"
                                     "\n"
                                     "inteiro distancia(Ponto P, Ponto Q):\n"
                                     "\tretornar (P.x - Q.x)^2 + (P.y - Q.y)^2\n"
                                     "Ponto A, B <- Ponto(0, 0), Ponto(30, 40)\n"
                                     "distancia(A, B)\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 2500)

    def test_class_errors(self):
        self.assertRaises(TupyTypeError, Interpreter.interpret, "Aluno a\n")
        self.assertRaises(TupyTypeError, Interpreter.interpret, "tipo Aluno(Pessoa):\n\tinteiro a\n")
        self.assertRaises(TupyNameError, Interpreter.interpret, 
                         ("tipo Teste:\n"
                          "\tinteiro a\n"
                          "Teste t <- Teste()\n"
                          "t.b <- 10\n"
                          ))
        self.assertRaises(TupyNameError, Interpreter.interpret, 
                         ("tipo Teste:\n"
                          "\tinteiro func(inteiro a, inteiro b):\n"
                          "\t\tretornar a*a+b*b\n"
                          "Teste t <- Teste()\n"
                          "func(5,2)\n"
                          ))
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
                         ("tipo Quadrado:\n"
                          "\tinteiro a <- 5\n"
                          "tipo Círculo:\n"
                          "\tinteiro b <- 6\n"
                          "Quadrado Q <- Quadrado()\n"
                          "Círculo C <- Círculo()\n"
                          "Q <- C\n"
                          ))
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
                         ("tipo Teste:\n"
                          "\tinteiro v\n"
                          "tipo Outro:\n"
                          "\tinteiro v\n"
                          "inteiro func(Teste t):\n"
                          "\tretornar t.v\n"
                          "func(Outro())\n"
                          ))
        self.assertRaises(NameError, Interpreter.newClassInstance, "classeInexistente")

    def test_for_loop(self):
        ret = Interpreter.interpret(("inteiro i\n"
                                     "inteiro soma <- 0\n"
                                     "para i <- 0..9 inclusive:\n"
                                     "\tsoma <- soma + i\n"
                                     "soma\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 45)
        ret = Interpreter.interpret(("inteiro i\n"
                                     "inteiro fat <- 362880\n"
                                     "para i <- 9..1 inclusive passo -1:\n"
                                     "\tfat <- fat / i\n"
                                     "fat\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = Interpreter.interpret(("inteiro i\n"
                                     "inteiro A[*]\n"
                                     "para i <- 9..1 inclusive:\n"
                                     "\tA <- inserir(A, i)\n"
                                     "A\n"
                                    ))
        self.assertArrayEquals(ret, Type.INT, [9, 8, 7, 6, 5, 4, 3, 2, 1])
        ret = Interpreter.interpret(("inteiro i, j\n"
                                     "inteiro tot <- 0\n"
                                     "para i, j <- 1..4, 1..3 inclusive:\n"
                                     "\ttot <- tot + i + j\n"
                                     "tot\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 36)
        ret = Interpreter.interpret(("inteiro i, j\n"
                                     "inteiro tot <- 0\n"
                                     "para i <- 1..3 inclusive:\n"
                                     "\tpara j <- 1..i inclusive:\n"
                                     "\t\ttot <- tot + j\n"
                                     "tot\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 10)
        ret = Interpreter.interpret(("inteiro i\n"
                                     "inteiro tot <- 0\n"
                                     "para i <- 1..10 incl. passo i:\n"
                                     "\ttot <- tot + i\n"
                                     "tot\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 15)
        ret = Interpreter.interpret(("inteiro i, j, k\n"
                                     "inteiro tot <- 0\n"
                                     "para i, j, k <- 1..4, 1..4, 1..4:\n"
                                     "\tse i = j e j = k:\n"
                                     "\t\ttot <- tot - (i+j+k)\n"
                                     "\tsenao:\n"
                                     "\t\ttot <- tot + (i+j+k)\n"
                                     "tot\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 126)

    def test_for_loop_errors(self):
        self.assertRaises(TupySyntaxError, Interpreter.interpret, 
                         ("inteiro i, j\n"
                          "inteiro soma <- 0\n"
                          "para i, j <- 0..9:\n"
                          "\tsoma <- soma + i\n"
                          "soma\n"
                         ))
 
    def test_break(self) :
        ret = Interpreter.interpret(("inteiro tot, i <- 0, 0\n"
                                     "enquanto verdadeiro:\n"
                                     "\ti <- i + 1\n"
                                     "\ttot <- tot + i\n"
                                     "\tse tot > 10:\n"
                                     "\t\tparar\n"
                                     "\ttot <- tot - 1\n"
                                     "tot\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 11)

    def test_break_nested_for(self):
        ret = Interpreter.interpret(("inteiro tot, i, j <- 0, 0, 0\n"
                                     "para i, j <- 3..1 incl., 1..3 incl. passo -1, 1:\n"
                                     "\tse j>i :\n"
                                     "\t\tparar\n"
                                     "\ttot <- tot + i*j\n"
                                     "tot\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 24)

    def test_continue(self):
        ret = Interpreter.interpret(("inteiro tot, i <- 0, 0\n"
                                     "para i <- 1..10 inclusive:\n"
                                     "\ttot <- tot + 1\n"
                                     "\tse i mod 2 > 0:\n"
                                     "\t\tavançar\n"
                                     "\ttot <- tot + i\n"
                                     "tot\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 40)

    def test_function_refparam_with_trailers(self):
        ret = Interpreter.interpret(("inteiro x[5] <- [1, 2, 3, 4, 5]\n"
                                     "func(ref inteiro a, inteiro b):\n"
                                     "\t a <- a + b\n"
                                     "func(x[2], 7)\n"
                                     "x\n"
                                    ))
        self.assertArrayEquals(ret, Type.INT, [1, 2, 10, 4, 5])  
        ret = Interpreter.interpret(("tipo Teste:\n"
                                     "\tinteiro chave\n"
                                     "func(ref inteiro a, inteiro b):\n"
                                     "\t a <- a + b\n"
                                     "Teste T <- Teste()\n"
                                     "T.chave <- 5\n"
                                     "func(T.chave, 15)\n"
                                     "T.chave\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 20)

    def test_function_refparam_errors(self):
        self.assertRaises(TupySyntaxError, Interpreter.interpret, 
                         ("inteiro func(inteiro a):\n"
                          "\tretornar a\n"
                          "teste(ref inteiro a):\n"
                          "\ta <- a + 1\n"
                          "teste(func(5))\n"
                          ))
        self.assertRaises(TupySyntaxError, Interpreter.interpret, 
                         ("teste(ref caracter c):\n"
                          "\tc <- c + 1\n"
                          "cadeia s <- \"Ola\"\n"
                          "teste(s[2])\n"
                          ))

    def test_reference_errors(self):
        self.assertRaises(TupySyntaxError, Interpreter.interpret, 
                         ("inteiro V[5] <- [2, 4, 8, 16, 32]\n"
                          "inteiro X[3] <- ref V[1..3]\n"
                          ))
        self.assertRaises(TupySyntaxError, Interpreter.interpret, 
                         ("inteiro V[2] <- [2, 4]\n"
                          "inteiro X[3] <- [1, 2, 3]\n"
                          "X[1..2] <- ref V\n"
                          ))
        self.assertRaises(TupySyntaxError, Interpreter.interpret, 
                         ("inteiro func(inteiro a):\n"
                          "\tretornar a\n"
                          "inteiro teste(inteiro a):\n"
                          "\tretornar a + 1\n"
                          "func(1) <- ref teste\n"
                          ))
        self.assertRaises(TupySyntaxError, Interpreter.interpret, 
                         ("cadeia s <- \"Ola\"\n"
                          "caracter a <- \'A\'\n"
                          "s[1] <- ref a\n"
                          ))
        self.assertRaises(TupySyntaxError, Interpreter.interpret, 
                         ("inteiro a <- ref 25\n"))

    def test_reference_assign(self):
        ret = Interpreter.interpret(("inteiro a, b\n"
                                     "b <- ref a\n"
                                     "a <- 5\n"
                                     "b\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)

    def test_reference_assign_array_element(self):
        ret = Interpreter.interpret(("inteiro A[3] <- [10, 50, 200]\n"
                                     "inteiro x\n"
                                     "A[1] <- ref x\n"
                                     "x <- 100\n"
                                     "A\n"
                                    ))
        self.assertArrayEquals(ret, Type.INT, [10, 100, 200])  

    def test_reference_reassign(self):
        ret = Interpreter.interpret(("inteiro a, b, c, d\n"
                                     "a <- ref b\n"
                                     "b <- 5\n"
                                     "d <- a\n"
                                     "a <- ref c\n"
                                     "a <- 7\n"
                                     "a, b, c, d\n"
                                    ))
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 7)
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 5)
        self.assertEqual(ret[2].type, Type.INT)
        self.assertEqual(ret[2].value, 7)
        self.assertEqual(ret[3].type, Type.INT)
        self.assertEqual(ret[3].value, 5)

    def test_reference_assign_2(self):
        ret = Interpreter.interpret(("inteiro a <- 100\n"
                                     "inteiro func(inteiro x):\n"
                                     "\tinteiro y <- ref a\n"
                                     "\tinteiro a <- 10\n"
                                     "\tretornar x+y\n"
                                     "func(a)\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 200)

    def test_reference_assign_field(self):
        ret = Interpreter.interpret(("tipo Teste:\n"
                                     "\tinteiro x\n"
                                     "Teste t <- Teste()\n"
                                     "inteiro a\n"
                                     "t.x <- ref a\n"
                                     "a <- 10\n"
                                     "t.x\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 10)

    def test_reference_assign_bridge(self):
        ret = Interpreter.interpret(("func(ref inteiro a):\n"
                                     "\tinteiro x <- ref a\n"
                                     "\tx <- 55\n"
                                     "inteiro y <- 100\n"
                                     "func(y)\n"
                                     "y\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 55)

    def test_reference_assign_bridge_2(self):
        ret = Interpreter.interpret(("tipo Teste:\n"
                                     "\tcadeia s\n"
                                     "\tTeste x\n"
                                     "Teste t, u <- Teste(), Teste()\n"
                                     "t.x <- ref u\n"
                                     "u.s <- \"OK!\"\n"
                                     "t.x.s\n"
                                    ))
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "OK!")

    def test_linked_list(self):
        ret = Interpreter.interpret(("tipo Lista:\n"
                                     "\tinteiro chave\n"
                                     "\tLista prox\n"
                                     "\tLista(inteiro c):\n"
                                     "\t\tchave <- c\n"
                                     "\t\tprox <- nulo\n"
                                     "Lista cab <- Lista(10)\n"
                                     "inteiro i\n"
                                     "Lista atual <- cab\n"
                                     "para i <- 1..5:\n"
                                     "\tLista p <- Lista(10-(i*2))\n"
                                     "\tatual.prox <- p\n"
                                     "\tatual <- p\n"
                                     "enquanto cab != nulo:\n"
                                     "\tescrever(cab.chave)\n"
                                     "\tcab <- cab.prox\n"
                                    ))
        self.assertEqual(Interpreter.outStream.getvalue(), "10\n8\n6\n4\n2\n")

    def test_logarithm(self):
        ret = Interpreter.interpret("log(32.0, 2.0)\n")
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 5.0)
        ret = Interpreter.interpret("log(real(32), real(2))\n")
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 5.0)

    def test_no_function_call_assign(self):
        self.assertRaises(TupySyntaxError, Interpreter.interpret, 
                         ("inteiro func(inteiro x):\n"
                          "\tretornar x*x\n"
                          "inteiro func2(inteiro x):\n"
                          "\tretornar x+x\n"
                          "func(1) <- func2(1)\n"
                         ))

    def test_math_builtins(self):
        x = random.uniform(2.0, 100.0)
        y = random.uniform(2.0, 100.0)
        a = random.uniform(-1.0, 1.0)
        ix = random.randint(2, 100)
        ret = Interpreter.interpret("ln({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.log(x))
        ret = Interpreter.interpret("raiz({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.sqrt(x))
        ret = Interpreter.interpret("exp({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.exp(x))
        ret = Interpreter.interpret("abs({0})\n".format(-x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, builtins.abs(-x))
        ret = Interpreter.interpret("abs({0})\n".format(-ix))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, builtins.abs(-ix))
        ret = Interpreter.interpret("sinal({0})\n".format(-x))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, math.copysign(1,-x))
        ret = Interpreter.interpret("piso({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.floor(x))
        ret = Interpreter.interpret("teto({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.ceil(x))
        ret = Interpreter.interpret("arredondar({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, builtins.round(x))
        ret = Interpreter.interpret("graus({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.degrees(x))
        ret = Interpreter.interpret("radianos({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.radians(x))
        ret = Interpreter.interpret("sen({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.sin(x))
        ret = Interpreter.interpret("arcsen({0})\n".format(a))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.asin(a))
        ret = Interpreter.interpret("senh({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.sinh(x))
        ret = Interpreter.interpret("arsenh({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.asinh(x))
        ret = Interpreter.interpret("cos({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.cos(x))
        ret = Interpreter.interpret("arccos({0})\n".format(a))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.acos(a))
        ret = Interpreter.interpret("cosh({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.cosh(x))
        ret = Interpreter.interpret("arcosh({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.acosh(x))
        ret = Interpreter.interpret("tg({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.tan(x))
        ret = Interpreter.interpret("arctg({0})\n".format(a))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.atan(a))
        ret = Interpreter.interpret("arctg2({0}, {1})\n".format(y, -x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.atan2(y, -x))
        ret = Interpreter.interpret("tgh({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.tanh(x))
        ret = Interpreter.interpret("artgh({0})\n".format(a))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, math.atanh(a))
        ret = Interpreter.interpret("aleatorio()\n")
        self.assertEqual(ret.type, Type.FLOAT)
        ret = Interpreter.interpret("aleatorio({0})\n".format(x))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertTrue(ret.value <= x)
        ret = Interpreter.interpret("aleatorio({0}, {1})\n".format(x, y))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertTrue(min(x, y) <= ret.value and ret.value <= max(x, y))
        ret = Interpreter.interpret("inteiro_aleatorio({0})\n".format(int(x)))
        self.assertEqual(ret.type, Type.INT)
        self.assertTrue(ret.value <= x)
        ret = Interpreter.interpret("inteiro_aleatorio({0}, {1})\n".format(int(x), int(y)))
        self.assertEqual(ret.type, Type.INT)
        self.assertTrue(int(min(x, y)) <= ret.value and ret.value <= int(max(x, y)))

    def test_string_split_join(self):
        ret = Interpreter.interpret("lista(\"a b c d efg\")\n")
        self.assertArrayEquals(ret, Type.STRING, ["a", "b", "c", "d", "efg"])
        ret = Interpreter.interpret("lista(\"a, b, c, d, efg\", \", \")\n")
        self.assertArrayEquals(ret, Type.STRING, ["a", "b", "c", "d", "efg"])
        ret = Interpreter.interpret("juntar([1, 2, 3, 4])\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "1234")
        ret = Interpreter.interpret("juntar([1, 2, 3, 4], \"abc\")\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "1abc2abc3abc4")
        ret = Interpreter.interpret("juntar((1, verdadeiro, 'O', \"uFalso\"))\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "1verdadeiroOuFalso")

        self.assertRaises(TupyTypeError, Interpreter.interpret, "juntar(\"abcd\")")
        self.assertRaises(TupyTypeError, Interpreter.interpret, "juntar([1, 2, 3], 4)")

    def test_list_shuffle(self):
        ret = Interpreter.interpret("embaralhar([1, 3, 5, 7, 9])\n")
        self.assertEqual(ret.type, Type.ARRAY)
        retValues = [memRead(val).value for val in ret.value]
        self.assertTrue( set([1, 3, 5, 7, 9]) == set(retValues) )

        self.assertRaises(TupyTypeError, Interpreter.interpret, "embaralhar([1, 2], [3, 4])")
        self.assertRaises(TupyTypeError, Interpreter.interpret, "embaralhar(\"abcd\")")

    def test_print_base(self):
        ret = Interpreter.interpret("binário(5461)\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "1010101010101")
        ret = Interpreter.interpret("binario(455)\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "111000111")
        ret = Interpreter.interpret("octal(342391)\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "1234567")
        ret = Interpreter.interpret("hexadecimal(11259375)\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "ABCDEF")

    def test_string_modify(self):
        ret = Interpreter.interpret(("inteiro i\n"
                                     "cadeia S <- \"Uma string\"\n"
                                     "para i <- 0..|S|:\n"
                                     "  S[i] <- 'A'\n"
                                     "S\n"))
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "AAAAAAAAAA")
        ret = Interpreter.interpret(("cadeia S <- \"Uma string\"\n"
                                     "S[2..6] <- \"AAAAA\"\n"
                                     "S\n"))
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "UmAAAAAing")
        ret = Interpreter.interpret(("cadeia S <- \"Uma string\"\n"
                                     "S[4..9] <- \'z\'\n"
                                     "S\n"))
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "Uma zzzzzz")
        ret = Interpreter.interpret(("cadeia S <- \"Uma string\"\n"
                                     "S[*] <- \'k\'\n"
                                     "S\n"))
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "kkkkkkkkkk")
    
    def test_string_modify_errors(self):
        self.assertRaises(TupyTypeError, Interpreter.interpret, 
                            ("cadeia S <- \"Uma string\"\n"
                             "S <- \'k\'\n"
                             "S\n"))

        self.assertRaises(TupyTypeError, Interpreter.interpret, 
                            ("cadeia S <- \"Uma string\"\n"
                             "S[2..6] <- \"AA\"\n"
                             "S\n"))

        self.assertRaises(TupyTypeError, Interpreter.interpret, 
                            ("cadeia S <- \"Uma string\"\n"
                             "S[2] <- \"AA\"\n"
                             "S\n"))

    def test_type_cast(self):
        ret = Interpreter.interpret("caracter(71), caracter(\"*\")\n")
        self.assertEqual(ret[0].type, Type.CHAR); self.assertEqual(ret[0].value, 71)
        self.assertEqual(ret[1].type, Type.CHAR); self.assertEqual(ret[1].value, ord('*'))

        ret = Interpreter.interpret("real(35), real(\"36\"), real('a'), real(verdadeiro)\n")
        self.assertEqual(ret[0].type, Type.FLOAT); self.assertEqual(ret[0].value, 35)
        self.assertEqual(ret[1].type, Type.FLOAT); self.assertEqual(ret[1].value, 36)
        self.assertEqual(ret[2].type, Type.FLOAT); self.assertEqual(ret[2].value, ord('a'))
        self.assertEqual(ret[3].type, Type.FLOAT); self.assertEqual(ret[3].value, 1)

        ret = Interpreter.interpret("inteiro(35.4), inteiro(\"FF\", 16), inteiro('a'), inteiro(falso)\n")
        self.assertEqual(ret[0].type, Type.INT); self.assertEqual(ret[0].value, 35)
        self.assertEqual(ret[1].type, Type.INT); self.assertEqual(ret[1].value, 255)
        self.assertEqual(ret[2].type, Type.INT); self.assertEqual(ret[2].value, ord('a'))
        self.assertEqual(ret[3].type, Type.INT); self.assertEqual(ret[3].value, 0)

        ret = Interpreter.interpret("cadeia(35.4), cadeia(36), cadeia('a'), cadeia(verdadeiro), cadeia([1, 2, 3]), cadeia(nulo)\n")
        self.assertEqual(ret[0].type, Type.STRING); self.assertEqual(ret[0].value, "35.4")
        self.assertEqual(ret[1].type, Type.STRING); self.assertEqual(ret[1].value, "36")
        self.assertEqual(ret[2].type, Type.STRING); self.assertEqual(ret[2].value, "a")
        self.assertEqual(ret[3].type, Type.STRING); self.assertEqual(ret[3].value, "verdadeiro")
        self.assertEqual(ret[4].type, Type.STRING); self.assertEqual(ret[4].value, "[1, 2, 3]")
        self.assertEqual(ret[5].type, Type.STRING); self.assertEqual(ret[5].value, "nulo")

        ret = Interpreter.interpret("logico(35.4), logico(\"\"), logico('a'), logico(0)\n")
        self.assertEqual(ret[0].type, Type.BOOL); self.assertEqual(ret[0].value, True)
        self.assertEqual(ret[1].type, Type.BOOL); self.assertEqual(ret[1].value, False)
        self.assertEqual(ret[2].type, Type.BOOL); self.assertEqual(ret[2].value, True)
        self.assertEqual(ret[3].type, Type.BOOL); self.assertEqual(ret[3].value, False)

    def test_type_cast_errors(self):
        self.assertRaises(TupyValueError, Interpreter.interpret, "inteiro(\"a\")\n")
        self.assertRaises(TupyValueError, Interpreter.interpret, "real(\"ff\")\n")
        self.assertRaises(TupyValueError, Interpreter.interpret, "caracter(-1)\n")
        self.assertRaises(TupyValueError, Interpreter.interpret, "caracter(\"abc\")\n")
        self.assertRaises(TupyValueError, Interpreter.interpret, "cadeia(1, 2, 3, 4)\n")

    def test_parse_error(self):
        self.assertRaises(TupyParseError, Interpreter.interpret, "a({=\n")
        # Falha inesperada de sintaxe:
        self.assertRaises(TupyParseError, Interpreter.interpret, "tipo Aluno():\n\tinteiro a\n")

    def test_function_depth_priority(self):
        ret = Interpreter.interpret(("inteiro func(inteiro a):\n"
                                     "\tretornar a\n"
                                     "\n"
                                     "se verdadeiro:\n"
                                     "\tinteiro func(inteiro a):\n"
                                     "\t\tretornar 2*a\n"
                                     "\n"
                                     "\tfunc(2)"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 4)

    def test_polymorphism(self):
        ret = Interpreter.interpret(("tipo Pessoa:\n"
                                     "\tinteiro func(inteiro a):\n"
                                     "\t\tretornar a*2\n"
                                     "\n"
                                     "tipo Aluno(Pessoa):\n"
                                     "\tinteiro func(inteiro a):\n"
                                     "\t\tretornar a\n"
                                     "\n"
                                     "Aluno a <- Aluno()\n"
                                     "Pessoa p <- Pessoa()\n"
                                     "a.func(2), p.func(2)\n"))
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 2)
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 4)

    def test_list_insert(self):
        ret = Interpreter.interpret("inserir([1, 2, 3], 4)\n")
        self.assertArrayEquals(ret, Type.INT, [1, 2, 3, 4]) 
        ret = Interpreter.interpret("inserir([1, 2, 3], 4, 0)\n")
        self.assertArrayEquals(ret, Type.INT, [4, 1, 2, 3]) 
        ret = Interpreter.interpret("inserir([], \"olá\")\n")
        self.assertArrayEquals(ret, Type.STRING, ["olá"]) 
        ret = Interpreter.interpret("inserir([], [])\n")
        self.assertArrayEquals(ret, Type.ARRAY, [[]]) 
        ret = Interpreter.interpret("inserir([1, 2, 3], 4, 25)\n")
        self.assertArrayEquals(ret, Type.INT, [1, 2, 3, 4])
        self.assertRaises(TupyTypeError, Interpreter.interpret, "inserir([1, 2], 3.0)\n") 
        self.assertRaises(TupyTypeError, Interpreter.interpret, "inserir([1, 2])\n") 
        self.assertRaises(TupyTypeError, Interpreter.interpret, "inserir([1, 2], 3, 4, 5)\n") 
        self.assertRaises(TupyTypeError, Interpreter.interpret, "inserir(1, 2, 3)\n") 
        self.assertRaises(TupyTypeError, Interpreter.interpret, "inserir([1, 2], 2, \"hein\")\n") 
        self.assertRaises(TupyTypeError, Interpreter.interpret, "inserir([1, 2], [3, 4])\n") 
        self.assertRaises(TupyTypeError, Interpreter.interpret, "inserir([[1, 2]], 3)\n") 
        self.assertRaises(TupyTypeError, Interpreter.interpret, ("tipo A:\n"
                                                                 "\tinteiro v\n"
                                                                 "tipo B:\n"
                                                                 "\tinteiro v\n"
                                                                 "A x <- A()\n"
                                                                 "B V[*]\n"
                                                                 "inserir(V, x)\n")) 
        ret = Interpreter.interpret(("inteiro M[3] <- [1, 2, 3]\n"
                                     "inserir(M, 4)\n"
                                     "M\n"))
        self.assertArrayEquals(ret, Type.INT, [1, 2, 3])

    def test_list_remove(self):
        ret = Interpreter.interpret("remover([1, 2, 3, 4], 1)\n")
        self.assertArrayEquals(ret, Type.INT, [1, 3, 4]) 
        ret = Interpreter.interpret("remover([1, 2, 3, 4], -1)\n")
        self.assertArrayEquals(ret, Type.INT, [1, 2, 3]) 
        self.assertRaises(TupyTypeError, Interpreter.interpret, "remover([1, 2, 3], 2, 4)\n") 
        self.assertRaises(TupyTypeError, Interpreter.interpret, "remover([1, 2, 3], 3.0)\n") 
        self.assertRaises(TupyTypeError, Interpreter.interpret, "remover(1, 2)\n") 

    def test_trace_offset(self):
        ret = Interpreter.interpret("-----\ninteiro a <- 1\n---")
        self.assertEqual(Interpreter.traceBars, [1,3])

    def test_minmax(self):
        ret = Interpreter.interpret("mín(50, -4), máx(50, -4)\n")
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, -4)
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 50)
        ret = Interpreter.interpret("mín(-4.01, 50.35), máx(-4.01, 50.35)\n")
        self.assertEqual(ret[0].type, Type.FLOAT)
        self.assertEqual(ret[0].value, -4.01)
        self.assertEqual(ret[1].type, Type.FLOAT)
        self.assertEqual(ret[1].value, 50.35)
        ret = Interpreter.interpret("mín('d', 'z'), máx('d', 'z')\n")
        self.assertEqual(ret[0].type, Type.CHAR)
        self.assertEqual(ret[0].value, ord('d'))
        self.assertEqual(ret[1].type, Type.CHAR)
        self.assertEqual(ret[1].value, ord('z'))
        ret = Interpreter.interpret("mín(\"adf\", \"abc\"), máx(\"adf\", \"abc\")\n")
        self.assertEqual(ret[0].type, Type.STRING)
        self.assertEqual(ret[0].value, "abc")
        self.assertEqual(ret[1].type, Type.STRING)
        self.assertEqual(ret[1].value, "adf")

    def test_access_out_of_range(self):
        self.assertRaises(TupyIndexError, Interpreter.interpret, "inteiro M[2] <- [1, 5]\nescrever(M[3])")

    def test_intertype_comparison(self):
        ret = Interpreter.interpret("132 = nulo, nulo = nulo\n")
        self.assertEqual(ret[0].type, Type.BOOL)
        self.assertEqual(ret[0].value, False)
        self.assertEqual(ret[1].type, Type.BOOL)
        self.assertEqual(ret[1].value, True)

        self.assertRaises(TupyTypeError, Interpreter.interpret, "1 >= 1.0")
        self.assertRaises(TupyTypeError, Interpreter.interpret, "[1, 2, 3] = (1, 2, 3)")
        self.assertRaises(TupyTypeError, Interpreter.interpret, "(1, 2) = 1")
        self.assertRaises(TupyTypeError, Interpreter.interpret, "123 = \"123\"")
        self.assertRaises(TupyTypeError, Interpreter.interpret, "func():\n\tretornar 1\nfunc2():\n\tretornar 2\nfunc = func2")

    def test_recursion_error(self):
        self.assertRaises(TupyRuntimeError, Interpreter.interpret, "inteiro func(inteiro a):\n\tretornar func(a+1)\nfunc(1)\n")

    def test_short_circuit(self):
        ret = Interpreter.interpret("verdadeiro ou a\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = Interpreter.interpret("falso e b\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        # Precedence: NOT > AND > OR
        ret = Interpreter.interpret("não verdadeiro e a ou verdadeiro\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = Interpreter.interpret(("inteiro j, fim <- 1, 0\n"
                                     "se (j > fim) ou (i <= limite e B[i] <= B[j]):\n"
                                     "\tverdadeiro\n"))
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)

    def test_array_dimension_anomaly(self):
        ret = Interpreter.interpret("inteiro A[*,*]\ninteiro[][] func(ref inteiro[][] V):\n\tretornar inserir(V, [1, 2, 3])\nfunc(A)\n")
        self.assertArrayEquals(ret, Type.INT, [[1, 2, 3]])
        ret = Interpreter.interpret(("inteiro A[*,*,*] <- [ [ [1, 2], [3], [] ], [[5], [7], [6, 4]] ]\n"
                                     "A[*,1] <- [[], []]\nA\n"))
        self.assertArrayEquals(ret, Type.INT, [[[1,2], [], []], [[5], [], [6, 4]]])

    def test_input_single(self):
        ret = Interpreter.interpret(("inteiro a\n"
                                     "real b\n"
                                     "lógico c\n"
                                     "caracter d\n"
                                     "cadeia f\n"
                                     "ler(a, b, c, d, f)\n"
                                     "a, b, c, d, f\n"), stdin="1 2    3\t65\n70")
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 1)
        self.assertEqual(ret[1].type, Type.FLOAT)
        self.assertEqual(ret[1].value, 2.0)
        self.assertEqual(ret[2].type, Type.BOOL)
        self.assertEqual(ret[2].value, True)
        self.assertEqual(ret[3].type, Type.CHAR)
        self.assertEqual(ret[3].value, ord('A'))
        self.assertEqual(ret[4].type, Type.STRING)
        self.assertEqual(ret[4].value, "70")

        ret = Interpreter.interpret(("inteiro a\n"
                                     "real b\n"
                                     "ler(a, b)\n"), stdin="-55")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)

        ret = Interpreter.interpret(("inteiro a[5] <- [1, 2, 3, 4, 5]\n"
                                     "ler(a[3])\n"
                                     "a\n"), stdin="10")
        self.assertArrayEquals(ret, Type.INT, [1, 2, 3, 10, 5])

        ret = Interpreter.interpret(("inteiro a, b, c\n"
                                     "ler(a, b, c)\n"
                                     "a, b, c\n"), stdin="0xF 0o21 0b111")
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 15)
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 17)
        self.assertEqual(ret[2].type, Type.INT)
        self.assertEqual(ret[2].value, 7)

    def test_input_single_errors(self):
        self.assertRaises(TupySyntaxError, Interpreter.interpret, "ler([1, 2, 3])", stdin="1, 2, 3")
        self.assertRaises(TupyValueError, Interpreter.interpret, "inteiro a[3]; ler(a)", stdin="1, 2, 3")

    def test_input_line(self):
        ret = Interpreter.interpret(("cadeia linha, linha2\n"
                                     "ler_linha(linha)\n"
                                     "ler_linha(linha2)\n"
                                     "linha, linha2\n"), stdin="1 2    3\t65\n70")
        self.assertEqual(ret[0].type, Type.STRING)
        self.assertEqual(ret[0].value, "1 2    3\t65\n")
        self.assertEqual(ret[1].type, Type.STRING)
        self.assertEqual(ret[1].value, "70")

        ret = Interpreter.interpret(("cadeia linha <- \"abcde\"\n"
                                     "ler_linha(linha[1..3])\n"
                                     "linha\n"), stdin="dcb")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "adcbe")

        self.assertRaises(TupySyntaxError, Interpreter.interpret, "ler_linha(\"abc\")")

    def test_input_mixed(self):
        ret = Interpreter.interpret(("inteiro a\n"
                                     "ler(a)\n"
                                     "cadeia linha\n"
                                     "ler_linha(linha)\n"
                                     "a, linha"), stdin="1234 abc  defg")
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 1234)
        self.assertEqual(ret[1].type, Type.STRING)
        self.assertEqual(ret[1].value, "abc  defg")

        ret = Interpreter.interpret(("inteiro a\n"
                                     "ler(a)\n"
                                     "cadeia linha\n"
                                     "ler_linha(linha)\n"
                                     "a, linha"), stdin="1234")
        self.assertEqual(ret[0].type, Type.INT)
        self.assertEqual(ret[0].value, 1234)
        self.assertEqual(ret[1].type, Type.STRING)
        self.assertEqual(ret[1].value, "")

    def test_function_int_type_inference(self):
        ret = Interpreter.interpret(("inteiro tam(inteiro[] V):\n"
                                     "\tretornar |V|\n"
                                     "tam([])\n"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 0)
        ret = Interpreter.interpret(("real cubo(real n):\n"
                                     "\tretornar n^3\n"
                                     "cubo(3)\n"))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 27)

    def test_negative_array_indices(self):
        ret = Interpreter.interpret("inteiro V[5] <- [1, 2, 3, 4, 5]; V[-3..-1]")
        self.assertArrayEquals(ret, Type.INT, [3, 4, 5])
        ret = Interpreter.interpret("inteiro V[*] <- [1, 2, 3, 4]; V[-3..-1]")
        self.assertArrayEquals(ret, Type.INT, [2, 3, 4])
        ret = Interpreter.interpret("inteiro V[5] <- [1, 2, 3, 4]; V[-3..-1] <- 3; V")
        self.assertArrayEquals(ret, Type.INT, [1, 2, 3, 3, 3])
        ret = Interpreter.interpret("inteiro V[*] <- [1, 2, 3, 4]; V[-3..-1] <- 3; V")
        self.assertArrayEquals(ret, Type.INT, [1, 3, 3, 3])

    def test_assertion(self):
        ret = Interpreter.interpret("asserção(2 > 1); verdadeiro")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        self.assertRaises(TupyAssertionError, Interpreter.interpret, "assercao(falso); verdadeiro")

    def test_struct_copy(self):
        ret = Interpreter.interpret(("tipo Teste:\n"
                                     "\tTeste prox\n"
                                     "\tinteiro a[5]\n"
                                     "Teste t <- Teste()\n"
                                     "t.a <- [5, 4, 3, 2, 1]\n"
                                     "Teste u <- Teste()\n"
                                     "u.a <- [1, 2, 3, 4, 5]\n"
                                     "t.prox <- u\n"
                                     "u.prox <- t\n"
                                     "Teste v <- copiar(t)\n"
                                     "Teste w <- v\n"
                                     "v.a[2] <- 30\n"
                                     "t.a, v.a, w.a, v.prox.a\n"))
        self.assertArrayEquals(ret[0], Type.INT, [5, 4, 3, 2, 1])
        self.assertArrayEquals(ret[1], Type.INT, [5, 4, 30, 2, 1])
        self.assertArrayEquals(ret[2], Type.INT, [5, 4, 30, 2, 1])
        self.assertArrayEquals(ret[3], Type.INT, [1, 2, 3, 4, 5])
        self.assertRaises(TupyValueError, Interpreter.interpret, "copiar(2, 3)")
        self.assertRaises(TupyTypeError, Interpreter.interpret, "copiar(2)")

    def test_array_with_nulls(self):
        ret = Interpreter.interpret("[nulo, 123]\n")
        self.assertEqual(ret.heldtype, Type.INT)
        self.assertRaises(TupyTypeError, Interpreter.interpret, ("inteiro L[*] <- [nulo, 123]\n"
                                                                 "L[0] <- \"abc\"\n"))

    def test_builtin_length(self):
        ret = Interpreter.interpret("comprimento([ [1, 2, 3], [4, 5, 6], [7, 8, 9], [10] ])\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 4)
        self.assertRaises(TupyTypeError, Interpreter.interpret, "comprimento(2, 3)")
        self.assertRaises(TupyTypeError, Interpreter.interpret, "comprimento(2)")

    def test_lower_depth_variable_access_from_instance(self):
        ret = Interpreter.interpret(("tipo Teste:\n"
                                     "\tcadeia func():\n"
                                     "\t\tretornar out_func(S)\n"
                                     "cadeia out_func(cadeia S):\n"
                                     "\tretornar S + \"K\"\n"
                                     "cadeia S <- \"O\"\n"
                                     "Teste T <- Teste()\n"
                                     "T.func()\n"))
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "OK")

    def test_class_function_override(self):
        ret = Interpreter.interpret(("tipo Teste:\n"
                                     "\tinteiro func(inteiro a, inteiro b):\n"
                                     "\t\tretornar func(a)+func(b)\n"
                                     "inteiro func(inteiro a):\n"
                                     "\tretornar a*a\n"
                                     "Teste T <- Teste()\n"
                                     "T.func(2,3)\n"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 13)

if __name__ == '__main__':
    unittest.main()
