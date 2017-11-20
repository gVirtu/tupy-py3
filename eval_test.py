import unittest
import pytest
from antlr4 import InputStream
from Instance import Instance
from Type import Type
from Interpreter import Interpreter

class TestEvalVisitor(unittest.TestCase):

    '''def test_expr(self):
        self.assertEqual(self.evalExpression("10+10\n")), (3, 'INTEGER'))'''

    eex = "testOrExpression"

    def evalExpression(self, expr):
        return Interpreter.interpret(expr, type(self).eex).get()

    def assertArrayEquals(self, ret, targetType, array):
        print("assertArrayEquals({0}, {1}, {2})".format(ret, targetType, array))
        self.assertEqual(len(ret.value), len(array))
        for ind in range(len(array)):
            if (isinstance(array[ind], list)):
                self.assertEqual(ret.value[ind].get().type, Type.ARRAY)
                self.assertArrayEquals(ret.value[ind].get(), targetType, array[ind])
            else:
                self.assertEqual(ret.value[ind].get().type, targetType)
                self.assertEqual(ret.value[ind].get().value, array[ind])

    def test_integer(self):
        ret = self.evalExpression("123\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 123)

    def test_float(self):
        ret = self.evalExpression("123.0\n")
        # print(ret)
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 123.0)

    def test_string(self):
        ret = self.evalExpression("\"123.0\"\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "123.0")
    
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

    def test_tuple(self):
        ret = self.evalExpression("(1, 3.14, \"ok\", [1,5])\n")
        self.assertEqual(ret.type, Type.TUPLE)
        self.assertEqual(ret.value[0].get().type, Type.INT)
        self.assertEqual(ret.value[0].get().value, 1)
        self.assertEqual(ret.value[1].get().type, Type.FLOAT)
        self.assertEqual(ret.value[1].get().value, 3.14)
        self.assertEqual(ret.value[2].get().type, Type.STRING)
        self.assertEqual(ret.value[2].get().value, "ok")
        self.assertEqual(ret.value[3].get().type, Type.ARRAY)
        self.assertEqual(ret.value[3].get().size, 2)
        ret = self.evalExpression("()\n")
        self.assertEqual(ret.type, Type.TUPLE)
        self.assertEqual(ret.size, 0)

    def test_array(self):
        ret = self.evalExpression("[1, 2, 3]\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertEqual(ret.value[0].get().type, Type.INT)
        self.assertEqual(ret.value[0].get().value, 1)
        self.assertEqual(ret.value[1].get().type, Type.INT)
        self.assertEqual(ret.value[1].get().value, 2)
        self.assertEqual(ret.value[2].get().type, Type.INT)
        self.assertEqual(ret.value[2].get().value, 3)
        self.assertRaises(TypeError, self.evalExpression, "[1, 2, \"not_ok\"]\n")
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
        self.assertRaises(TypeError, self.evalExpression, "~verdadeiro\n")

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
        self.assertRaises(TypeError, self.evalExpression, "5 div nulo\n")

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
        self.assertRaises(TypeError, self.evalExpression, "nulo - 5\n")

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
        self.assertRaises(TypeError, self.evalExpression, "5 - [4]\n")
        

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
        self.assertRaises(TypeError, self.evalExpression, "1.0<<4\n")
        self.assertRaises(TypeError, self.evalExpression, "200>>3.0\n")

    def test_bitwise_and_expr(self):
        ret = self.evalExpression("3 && 5 && 9\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        self.assertRaises(TypeError, self.evalExpression, "3.0 && 5\n")
        self.assertRaises(TypeError, self.evalExpression, "3 && 5.0\n")

    def test_bitwise_or_expr(self):
        ret = self.evalExpression("1 || 2 || 13 || 16\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 31)
        self.assertRaises(TypeError, self.evalExpression, "1.0 || 2\n")
        self.assertRaises(TypeError, self.evalExpression, "2 || 13.0\n")

    def test_bitwise_xor_expr(self):
        ret = self.evalExpression("4287 xor 1200\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5135)
        self.assertRaises(TypeError, self.evalExpression, "4287 xor \"1200\"\n")
        self.assertRaises(TypeError, self.evalExpression, "4287.0 xor 1200\n")

    def test_bitwise_not_expr(self):
        ret = self.evalExpression("~(100+73)\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, -174)
        self.assertRaises(TypeError, self.evalExpression, "~verdadeiro\n")

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
        ret = self.evalExpression("0 >= 0.1\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = self.evalExpression("\"a\" <= \"b\"\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = self.evalExpression("\'a\' <= \'A\'\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = self.evalExpression("1 ~= 0\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = self.evalExpression("1 ~= 1\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = self.evalExpression("1 == 1\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = self.evalExpression("1 == 1.01\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)

    def test_bool_logic(self):
        ret = self.evalExpression("não verdadeiro\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = self.evalExpression("nao falso\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = self.evalExpression("nao não 3 == 4\n")
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
        ret = self.evalExpression("não verdadeiro ou 1 == 2\n")
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
        self.assertEqual(ret.value[0].get().type, Type.INT)
        self.assertEqual(ret.value[0].get().value, 10)
        self.assertEqual(ret.value[1].get().type, Type.INT)
        self.assertEqual(ret.value[1].get().value, 20)
        ret = self.evalExpression("(5,10.1,20,40)[1..2]\n")
        self.assertEqual(ret.type, Type.TUPLE)
        self.assertEqual(ret.value[0].get().type, Type.FLOAT)
        self.assertEqual(ret.value[0].get().value, 10.1)
        self.assertEqual(ret.value[1].get().type, Type.INT)
        self.assertEqual(ret.value[1].get().value, 20)
        ret_1 = self.evalExpression("[5,10,20,40]\n")
        ret_2 = self.evalExpression("[5,10,20,40][*]\n")
        self.assertEqual(ret_2.type, Type.ARRAY)
        for i in range(len(ret_1.value)):
            self.assertEqual(ret_2.value[i].get().type, ret_1.value[i].get().type)
            self.assertEqual(ret_2.value[i].get().value, ret_1.value[i].get().value)
        self.assertRaises(TypeError, Interpreter.interpret, "2[0]\n")


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
        self.assertRaises(NameError, Interpreter.interpret, "inteiro a <- b\n")
        self.assertRaises(NameError, Interpreter.interpret, "inteiro a <- b <- 3\n")
        self.assertRaises(TypeError, Interpreter.interpret, "inteiro a; real b <- 3.0; a <- b; a\n")
        self.assertRaises(TypeError, Interpreter.interpret, "inteiro a <- 3.01; a\n")
        self.assertRaises(TypeError, Interpreter.interpret, "inteiro a, b <- 3, 3.01; a, b\n")
        self.assertRaises(SyntaxError, Interpreter.interpret, "2 <- b\n")
        self.assertRaises(SyntaxError, Interpreter.interpret, "inteiro a(2) <- [1, 2]\n")
        self.assertRaises(ValueError, Interpreter.interpret, "inteiro a, b, c <- 1, 2\n")
        self.assertRaises(ValueError, Interpreter.interpret, "inteiro a, b, c <- 1, 2, 3, 4\n")

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
        self.assertRaises(TypeError, Interpreter.interpret, "inteiro a[4] <- [9,8,7,6,5]; a\n")
        self.assertRaises(SyntaxError, Interpreter.interpret, "inteiro a[10..15] <- [1,2,3]; a\n")
        self.assertRaises(SyntaxError, Interpreter.interpret, "inteiro a[-3] <- [1,2,3]; a\n")
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
        self.assertRaises(TypeError, Interpreter.interpret, "inteiro a[2,2] <- [[[2,2],[2,2]],[[2,2],[2,2]]]; a\n")

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
        self.assertRaises(SyntaxError, Interpreter.interpret, "inteiro a[5] <- [1,2,3,4,5]; a[2..1]\n")

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
        self.assertRaises(NameError, Interpreter.interpret, ("inteiro a <- 5\n"
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
        self.assertRaises(TypeError, Interpreter.interpret, ("inteiro func():\n"
                                                             "\t retornar 5\n"
                                                             "func(5)\n"
                                                            ))
        self.assertRaises(TypeError, Interpreter.interpret, ("inteiro func(inteiro a):\n"
                                                             "\t retornar a\n"
                                                             "func(\"5\")\n"
                                                            ))
        self.assertRaises(TypeError, Interpreter.interpret, ("inteiro func(inteiro a):\n"
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
        self.assertRaises(NameError, Interpreter.interpret, 
                         ("inteiro func(inteiro a, inteiro b):\n"
                          "\t retornar a+b\n"
                          "inteiro func(inteiro a, inteiro b <- 1):\n"
                          "\t retornar a*b\n"
                          "func(5,2)\n"
                         ))
        self.assertRaises(NameError, Interpreter.interpret, 
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
        ret = Interpreter.interpret(("inteiro[][] matriz(inteiro[][] a):\n"
                                     "\t a[*,1] <- 0\n"
                                     "\t retornar a\n"
                                     "matriz([[1,2,3],[4,5,6]])\n"
                                    ))
        self.assertArrayEquals(ret, Type.INT, [[1, 0, 3], [4, 0, 6]])        

    def test_function_variadic(self):
        ret = Interpreter.interpret(("inteiro teste(args...):\n"
                                     "\t se |args|>1:\n"
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
        ret = Interpreter.interpret(("inteiro escrever(inteiro n):\n"
                                     "\t retornar 100\n"
                                     "escrever(5)\n"
                                    ))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 100)


    def test_function_errors(self):
        self.assertRaises(TypeError, Interpreter.interpret, 
                         ("inteiro func():\n"
                          "\t retornar 2.3\n"
                          "func()\n"
                         ))
        self.assertRaises(TypeError, Interpreter.interpret, 
                         ("inteiro func(inteiro a):\n"
                          "\t retornar 200\n"
                          "func(\"xyz\")\n"
                         ))
        self.assertRaises(TypeError, Interpreter.interpret, 
                         ("inteiro[] func(inteiro a):\n"
                          "\t retornar a\n"
                          "func(2)\n"
                         ))
        self.assertRaises(TypeError, Interpreter.interpret, 
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
        self.assertRaises(SyntaxError, Interpreter.interpret, 
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
        self.assertRaises(RuntimeError, Interpreter.interpret, 
                         ("enquanto verdadeiro:\n"
                          "\t 1\n"
                         ))
        
if __name__ == '__main__':
    unittest.main()
