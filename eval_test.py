import unittest
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
    
    def test_shift_expr(self):
        ret = self.evalExpression("1<<4\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 16)
        ret = self.evalExpression("200>>3\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 25)
        self.assertRaises(TypeError, self.evalExpression, "1.0<<4\n")
        self.assertRaises(TypeError, self.evalExpression, "200<<3.0\n")

    def test_bitwise_and_expr(self):
        ret = self.evalExpression("3 && 5 && 9\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)

    def test_bitwise_xor_expr(self):
        ret = self.evalExpression("4287 xor 1200\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5135)

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

    def test_array_declaration(self):
        ret = Interpreter.interpret("inteiro a[5] <- [9,8,7,6,5]; a\n")
        self.assertEqual(ret.type, Type.ARRAY)
        targetArray = [9,8,7,6,5]
        self.assertArrayEquals(ret, Type.INT, targetArray)
        ret = Interpreter.interpret("inteiro a[*] <- [9,8,7,6,5]; a\n")
        self.assertArrayEquals(ret, Type.INT, targetArray)
        self.assertRaises(TypeError, Interpreter.interpret, "inteiro a[4] <- [9,8,7,6,5]; a\n")
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
        ret = Interpreter.interpret("real s[3,2,*] <- [ [[1.0], [2.0, 3.0]], [[4.0], []], [[5.0, 6.0]]]; s\n")
        targetArray = [ [[1.0], [2.0, 3.0]], [[4.0], []], [[5.0, 6.0], []] ]
        self.assertArrayEquals(ret, Type.FLOAT, targetArray)
        ret = Interpreter.interpret("inteiro a[5], b <- [9,8,7,6,5], 69; a, b\n")
        self.assertEqual(ret[1].type, Type.INT)
        self.assertEqual(ret[1].value, 69)

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
        
if __name__ == '__main__':
    unittest.main()