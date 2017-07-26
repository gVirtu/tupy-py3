import unittest
from antlr4 import InputStream
from Instance import Instance, Type
import arithmetic as a

class TestEvalVisitor(unittest.TestCase):

    '''def test_expr(self):
        self.assertEqual(a.interpret(InputStream("10+10")), (3, 'INTEGER'))'''

    def test_integer(self):
        ret = a.interpret(InputStream("123"))
        # print(ret)
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 123)

    def test_float(self):
        ret = a.interpret(InputStream("123.0"))
        # print(ret)
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 123.0)

    def test_string(self):
        ret = a.interpret(InputStream("\"123.0\""))
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "123.0")
    
    def test_char(self):
        ret = a.interpret(InputStream("'a'"))
        self.assertEqual(ret.type, Type.CHAR)
        self.assertEqual(ret.value, ord("a"))

    def test_bool(self):
        ret = a.interpret(InputStream("verdadeiro"))
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, True)
        ret = a.interpret(InputStream("falso"))
        self.assertEqual(ret.type, Type.BOOL)
        self.assertEqual(ret.value, False)

    def test_null(self):
        ret = a.interpret(InputStream("nulo"))
        self.assertEqual(ret.type, Type.NULL)

    def test_power_integer(self):
        ret = a.interpret(InputStream("2^3"))
        # print(ret)
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 8)
        ret = a.interpret(InputStream("2^-1"))
        # print(ret)
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 0.5)

    def test_factor_integer(self):
        ret = a.interpret(InputStream("-2"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, -2)

    def test_factor_except(self):        
        self.assertRaises(TypeError, a.interpret, InputStream("~verdadeiro"))

    def test_term(self):
        ret = a.interpret(InputStream("2*3"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 6)
        ret = a.interpret(InputStream("1/4"))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 0.25)
        ret = a.interpret(InputStream("3 mod 2"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = a.interpret(InputStream("5 div 2"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 2)
        ret = a.interpret(InputStream("\"abc\"*3"))
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "abcabcabc")
        ret = a.interpret(InputStream("'a'*5"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, ord("a")*5)
        ret = a.interpret(InputStream("verdadeiro*10"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 10)
        self.assertRaises(TypeError, a.interpret, InputStream("5 div nulo"))

    def test_arithmetic_expr(self):
        ret = a.interpret(InputStream("2+3"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)
        ret = a.interpret(InputStream("2-10"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, -8)
        ret = a.interpret(InputStream("2+-1"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)
        ret = a.interpret(InputStream("2+7.5"))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 9.5)
        ret = a.interpret(InputStream("falso+7.11"))
        self.assertEqual(ret.type, Type.FLOAT)
        self.assertEqual(ret.value, 7.11)
        ret = a.interpret(InputStream("2+\"3\""))
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "23")
        ret = a.interpret(InputStream("'a'+\"b\""))
        self.assertEqual(ret.type, Type.STRING)
        self.assertEqual(ret.value, "ab")
        self.assertRaises(TypeError, a.interpret, InputStream("nulo - 5"))

    def test_arithmetic_compound(self):
        ret = a.interpret(InputStream("1-2+3+4+5-6"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5)
        ret = a.interpret(InputStream("6*2-4"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 8)
    
    def test_shift_expr(self):
        ret = a.interpret(InputStream("1<<4"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 16)
        ret = a.interpret(InputStream("200>>3"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 25)
        self.assertRaises(TypeError, a.interpret, InputStream("1.0<<4"))
        self.assertRaises(TypeError, a.interpret, InputStream("200<<3.0"))

    def test_bitwise_and_expr(self):
        ret = a.interpret(InputStream("3 && 5 && 9"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 1)

    def test_bitwise_xor_expr(self):
        ret = a.interpret(InputStream("4287 xor 1200"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 5135)

    def test_bitwise_or_expr(self):
        ret = a.interpret(InputStream("3 || 4 || 8 || 16"))
        self.assertEqual(ret.type, Type.INT)
        self.assertEqual(ret.value, 31)

if __name__ == '__main__':
    unittest.main()