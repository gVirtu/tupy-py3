import unittest
from antlr4 import InputStream
from Instance import Instance, Type
import arithmetic as a

class TestEvalVisitor(unittest.TestCase):

    '''def test_expr(self):
        self.assertEqual(a.interpret("10+10\n")), (3, 'INTEGER'))'''

    def test_integer(self):
        ret = a.interpret("123\n")
        # print(ret)
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 123)

    def test_float(self):
        ret = a.interpret("123.0\n")
        # print(ret)
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 123.0)

    def test_string(self):
        ret = a.interpret("\"123.0\"\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "123.0")
    
    def test_char(self):
        ret = a.interpret("'a'\n")
        self.assertEqual(ret.type, Type.CHAR)
        self.assertEqual(ret.value, ord("a"))

    def test_bool(self):
        ret = a.interpret("verdadeiro\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        print("DONE")
        ret = a.interpret("falso\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)

    def test_null(self):
        ret = a.interpret("nulo\n")
        self.assertEqual(ret.type, Type.NULL)

    def test_tuple(self):
        ret = a.interpret("(1, 3.14, \"ok\", [1,5])\n")
        self.assertEqual(ret.type, Type.TUPLE)
        self.assertEqual(ret.value[0].type, Type.INT)
        self.assertEqual(ret.value[0].value, 1)
        self.assertEqual(ret.value[1].type, Type.FLOAT)
        self.assertEqual(ret.value[1].value, 3.14)
        self.assertEqual(ret.value[2].type, Type.STRING)
        self.assertEqual(ret.value[2].value, "ok")
        self.assertEqual(ret.value[3].type, Type.ARRAY)
        self.assertEqual(ret.value[3].size, 2)
        ret = a.interpret("()\n")
        self.assertEqual(ret.type, Type.TUPLE)
        self.assertEqual(ret.size, 0)

    def test_array(self):
        ret = a.interpret("[1, 2, 3]\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertEqual(ret.value[0].type, Type.INT)
        self.assertEqual(ret.value[0].value, 1)
        self.assertEqual(ret.value[1].type, Type.INT)
        self.assertEqual(ret.value[1].value, 2)
        self.assertEqual(ret.value[2].type, Type.INT)
        self.assertEqual(ret.value[2].value, 3)
        self.assertRaises(TypeError, a.interpret, "[1, 2, \"not_ok\"]\n")
        ret = a.interpret("[]\n")
        self.assertEqual(ret.type, Type.ARRAY)
        self.assertEqual(ret.size, 0)

    def test_power_integer(self):
        ret = a.interpret("2^3\n")
        # print(ret)
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 8)
        ret = a.interpret("2^-1\n")
        # print(ret)
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 0.5)

    def test_factor_integer(self):
        ret = a.interpret("-2\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, -2)

    def test_factor_except(self):        
        self.assertRaises(TypeError, a.interpret, "~verdadeiro\n")

    def test_term(self):
        ret = a.interpret("2*3\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 6)
        ret = a.interpret("1/4\n")
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 0.25)
        ret = a.interpret("3 mod 2\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = a.interpret("5 div 2\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 2)
        ret = a.interpret("\"abc\"*3\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "abcabcabc")
        ret = a.interpret("'a'*5\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, ord("a")*5)
        ret = a.interpret("verdadeiro*10\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 10)
        self.assertRaises(TypeError, a.interpret, "5 div nulo\n")

    def test_arithmetic_expr(self):
        ret = a.interpret("2+3\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)
        ret = a.interpret("2-10\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, -8)
        ret = a.interpret("2+-1\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = a.interpret("2+7.5\n")
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 9.5)
        ret = a.interpret("falso+7.11\n")
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 7.11)
        ret = a.interpret("2+\"3\"\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "23")
        ret = a.interpret("'a'+\"b\"\n")
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "ab")
        self.assertRaises(TypeError, a.interpret, "nulo - 5\n")

    def test_arithmetic_compound(self):
        ret = a.interpret("1-2+3+4+5-6\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)
        ret = a.interpret("6*2-4\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 8)
    
    def test_shift_expr(self):
        ret = a.interpret("1<<4\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 16)
        ret = a.interpret("200>>3\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 25)
        self.assertRaises(TypeError, a.interpret, "1.0<<4\n")
        self.assertRaises(TypeError, a.interpret, "200<<3.0\n")

    def test_bitwise_and_expr(self):
        ret = a.interpret("3 && 5 && 9\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)

    def test_bitwise_xor_expr(self):
        ret = a.interpret("4287 xor 1200\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5135)

    def test_comparison(self):
        ret = a.interpret("3 < 4\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = a.interpret("3 < 2\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = a.interpret("45 > 4\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = a.interpret("4 > 4\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = a.interpret("4 >= 4\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = a.interpret("0 >= 0.1\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = a.interpret("1 ~= 0\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = a.interpret("1 ~= 1\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = a.interpret("1 == 1\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = a.interpret("1 == 1.01\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)

    def test_bool_logic(self):
        ret = a.interpret("não verdadeiro\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = a.interpret("nao falso\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = a.interpret("nao não 3 == 4\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = a.interpret("verdadeiro e verdadeiro\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = a.interpret("verdadeiro e nao verdadeiro\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)
        ret = a.interpret("não falso ou falso\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = a.interpret("não verdadeiro ou 1 == 2\n")
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)

    def test_cardinality(self):
        ret = a.interpret("|12|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = a.interpret("|12.0|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = a.interpret("|'a'|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = a.interpret("|verdadeiro|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = a.interpret("|nulo|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 0)
        ret = a.interpret("|\"12\"|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 2)
        ret = a.interpret("|[10,20]|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 2)
        ret = a.interpret("|[[10],[1,2,3,4]]|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)
        ret = a.interpret("|(10,[1,2,3,4],('a', verdadeiro),\"teste\")|\n")
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 8)

if __name__ == '__main__':
    unittest.main()