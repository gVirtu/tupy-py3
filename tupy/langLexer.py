# Generated from lang.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr4.Token import CommonToken
import re
import importlib
# Allow languages to extend the lexer and parser, by loading the parser dinamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2O")
        buf.write("\u0303\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00e7")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n")
        buf.write("\u0102\n\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u012d\n\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u0149\n\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0157")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u0167\n\24\3\25\3\25\3\26\3")
        buf.write("\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#")
        buf.write("\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*")
        buf.write("\3*\3+\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\61\5\61\u01b6\n\61\3\62\3\62\3\62\3\63\3")
        buf.write("\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\38\38\38\38\39\39\39\59\u01d1\n9\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\5:\u01db\n:\3;\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\3>\3>\5>\u01ff\n>\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\3?\3?\5?\u020d\n?\3@\3@\3@\3@\3A\3A\3A\3")
        buf.write("A\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\5B\u0229\nB\3C\3C\3C\5C\u022e\nC\3C\3C\5C\u0232\nC\3")
        buf.write("C\5C\u0235\nC\5C\u0237\nC\3C\3C\3D\3D\7D\u023d\nD\fD\16")
        buf.write("D\u0240\13D\3E\3E\3E\3F\3F\3F\5F\u0248\nF\3F\3F\3F\3G")
        buf.write("\3G\7G\u024f\nG\fG\16G\u0252\13G\3G\6G\u0255\nG\rG\16")
        buf.write("G\u0256\5G\u0259\nG\3H\3H\3H\6H\u025e\nH\rH\16H\u025f")
        buf.write("\3I\3I\3I\6I\u0265\nI\rI\16I\u0266\3J\3J\3J\6J\u026c\n")
        buf.write("J\rJ\16J\u026d\3K\3K\3L\3L\5L\u0274\nL\3L\3L\3M\3M\3M")
        buf.write("\5M\u027b\nM\3M\3M\3N\3N\3O\3O\3O\7O\u0284\nO\fO\16O\u0287")
        buf.write("\13O\3O\3O\3P\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3U\3U\3V\3")
        buf.write("V\3V\3W\6W\u029c\nW\rW\16W\u029d\3X\3X\6X\u02a2\nX\rX")
        buf.write("\16X\u02a3\3Y\3Y\3Y\7Y\u02a9\nY\fY\16Y\u02ac\13Y\3Y\3")
        buf.write("Y\3Y\3Y\7Y\u02b2\nY\fY\16Y\u02b5\13Y\3Y\5Y\u02b8\nY\3")
        buf.write("Z\3Z\3Z\3Z\3Z\7Z\u02bf\nZ\fZ\16Z\u02c2\13Z\3Z\3Z\3Z\3")
        buf.write("Z\3Z\3Z\3Z\3Z\7Z\u02cc\nZ\fZ\16Z\u02cf\13Z\3Z\3Z\3Z\5")
        buf.write("Z\u02d4\nZ\3[\3[\5[\u02d8\n[\3\\\5\\\u02db\n\\\3]\5]\u02de")
        buf.write("\n]\3^\5^\u02e1\n^\3_\3_\3_\3`\6`\u02e7\n`\r`\16`\u02e8")
        buf.write("\3a\3a\7a\u02ed\na\fa\16a\u02f0\13a\3b\3b\5b\u02f4\nb")
        buf.write("\3b\5b\u02f7\nb\3b\3b\5b\u02fb\nb\3c\5c\u02fe\nc\3d\3")
        buf.write("d\5d\u0302\nd\4\u02c0\u02cd\2e\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091")
        buf.write("J\u0093K\u0095L\u0097M\u0099N\u009bO\u009d\2\u009f\2\u00a1")
        buf.write("\2\u00a3\2\u00a5\2\u00a7\2\u00a9\2\u00ab\2\u00ad\2\u00af")
        buf.write("\2\u00b1\2\u00b3\2\u00b5\2\u00b7\2\u00b9\2\u00bb\2\u00bd")
        buf.write("\2\u00bf\2\u00c1\2\u00c3\2\u00c5\2\u00c7\2\3\2\24\6\2")
        buf.write("\f\f\17\17$$^^\4\2QQqq\4\2ZZzz\4\2DDdd\4\2LLll\3\2\63")
        buf.write(";\3\2\62;\3\2\629\5\2\62;CHch\3\2\62\63\7\2\2\13\r\16")
        buf.write("\20(*]_\u0081\7\2\2\13\r\16\20#%]_\u0081\4\2\2]_\u0081")
        buf.write("\3\2\2\u0081\4\2\13\13\"\"\4\2\f\f\17\17\u0129\2C\\aa")
        buf.write("c|\u00ac\u00ac\u00b7\u00b7\u00bc\u00bc\u00c2\u00d8\u00da")
        buf.write("\u00f8\u00fa\u0243\u0252\u02c3\u02c8\u02d3\u02e2\u02e6")
        buf.write("\u02f0\u02f0\u037c\u037c\u0388\u0388\u038a\u038c\u038e")
        buf.write("\u038e\u0390\u03a3\u03a5\u03d0\u03d2\u03f7\u03f9\u0483")
        buf.write("\u048c\u04d0\u04d2\u04fb\u0502\u0511\u0533\u0558\u055b")
        buf.write("\u055b\u0563\u0589\u05d2\u05ec\u05f2\u05f4\u0623\u063c")
        buf.write("\u0642\u064c\u0670\u0671\u0673\u06d5\u06d7\u06d7\u06e7")
        buf.write("\u06e8\u06f0\u06f1\u06fc\u06fe\u0701\u0701\u0712\u0712")
        buf.write("\u0714\u0731\u074f\u076f\u0782\u07a7\u07b3\u07b3\u0906")
        buf.write("\u093b\u093f\u093f\u0952\u0952\u095a\u0963\u097f\u097f")
        buf.write("\u0987\u098e\u0991\u0992\u0995\u09aa\u09ac\u09b2\u09b4")
        buf.write("\u09b4\u09b8\u09bb\u09bf\u09bf\u09d0\u09d0\u09de\u09df")
        buf.write("\u09e1\u09e3\u09f2\u09f3\u0a07\u0a0c\u0a11\u0a12\u0a15")
        buf.write("\u0a2a\u0a2c\u0a32\u0a34\u0a35\u0a37\u0a38\u0a3a\u0a3b")
        buf.write("\u0a5b\u0a5e\u0a60\u0a60\u0a74\u0a76\u0a87\u0a8f\u0a91")
        buf.write("\u0a93\u0a95\u0aaa\u0aac\u0ab2\u0ab4\u0ab5\u0ab7\u0abb")
        buf.write("\u0abf\u0abf\u0ad2\u0ad2\u0ae2\u0ae3\u0b07\u0b0e\u0b11")
        buf.write("\u0b12\u0b15\u0b2a\u0b2c\u0b32\u0b34\u0b35\u0b37\u0b3b")
        buf.write("\u0b3f\u0b3f\u0b5e\u0b5f\u0b61\u0b63\u0b73\u0b73\u0b85")
        buf.write("\u0b85\u0b87\u0b8c\u0b90\u0b92\u0b94\u0b97\u0b9b\u0b9c")
        buf.write("\u0b9e\u0b9e\u0ba0\u0ba1\u0ba5\u0ba6\u0baa\u0bac\u0bb0")
        buf.write("\u0bbb\u0c07\u0c0e\u0c10\u0c12\u0c14\u0c2a\u0c2c\u0c35")
        buf.write("\u0c37\u0c3b\u0c62\u0c63\u0c87\u0c8e\u0c90\u0c92\u0c94")
        buf.write("\u0caa\u0cac\u0cb5\u0cb7\u0cbb\u0cbf\u0cbf\u0ce0\u0ce0")
        buf.write("\u0ce2\u0ce3\u0d07\u0d0e\u0d10\u0d12\u0d14\u0d2a\u0d2c")
        buf.write("\u0d3b\u0d62\u0d63\u0d87\u0d98\u0d9c\u0db3\u0db5\u0dbd")
        buf.write("\u0dbf\u0dbf\u0dc2\u0dc8\u0e03\u0e32\u0e34\u0e35\u0e42")
        buf.write("\u0e48\u0e83\u0e84\u0e86\u0e86\u0e89\u0e8a\u0e8c\u0e8c")
        buf.write("\u0e8f\u0e8f\u0e96\u0e99\u0e9b\u0ea1\u0ea3\u0ea5\u0ea7")
        buf.write("\u0ea7\u0ea9\u0ea9\u0eac\u0ead\u0eaf\u0eb2\u0eb4\u0eb5")
        buf.write("\u0ebf\u0ebf\u0ec2\u0ec6\u0ec8\u0ec8\u0ede\u0edf\u0f02")
        buf.write("\u0f02\u0f42\u0f49\u0f4b\u0f6c\u0f8a\u0f8d\u1002\u1023")
        buf.write("\u1025\u1029\u102b\u102c\u1052\u1057\u10a2\u10c7\u10d2")
        buf.write("\u10fc\u10fe\u10fe\u1102\u115b\u1161\u11a4\u11aa\u11fb")
        buf.write("\u1202\u124a\u124c\u124f\u1252\u1258\u125a\u125a\u125c")
        buf.write("\u125f\u1262\u128a\u128c\u128f\u1292\u12b2\u12b4\u12b7")
        buf.write("\u12ba\u12c0\u12c2\u12c2\u12c4\u12c7\u12ca\u12d8\u12da")
        buf.write("\u1312\u1314\u1317\u131a\u135c\u1382\u1391\u13a2\u13f6")
        buf.write("\u1403\u166e\u1671\u1678\u1683\u169c\u16a2\u16ec\u16f0")
        buf.write("\u16f2\u1702\u170e\u1710\u1713\u1722\u1733\u1742\u1753")
        buf.write("\u1762\u176e\u1770\u1772\u1782\u17b5\u17d9\u17d9\u17de")
        buf.write("\u17de\u1822\u1879\u1882\u18aa\u1902\u191e\u1952\u196f")
        buf.write("\u1972\u1976\u1982\u19ab\u19c3\u19c9\u1a02\u1a18\u1d02")
        buf.write("\u1dc1\u1e02\u1e9d\u1ea2\u1efb\u1f02\u1f17\u1f1a\u1f1f")
        buf.write("\u1f22\u1f47\u1f4a\u1f4f\u1f52\u1f59\u1f5b\u1f5b\u1f5d")
        buf.write("\u1f5d\u1f5f\u1f5f\u1f61\u1f7f\u1f82\u1fb6\u1fb8\u1fbe")
        buf.write("\u1fc0\u1fc0\u1fc4\u1fc6\u1fc8\u1fce\u1fd2\u1fd5\u1fd8")
        buf.write("\u1fdd\u1fe2\u1fee\u1ff4\u1ff6\u1ff8\u1ffe\u2073\u2073")
        buf.write("\u2081\u2081\u2092\u2096\u2104\u2104\u2109\u2109\u210c")
        buf.write("\u2115\u2117\u2117\u211a\u211f\u2126\u2126\u2128\u2128")
        buf.write("\u212a\u212a\u212c\u2133\u2135\u213b\u213e\u2141\u2147")
        buf.write("\u214b\u2162\u2185\u2c02\u2c30\u2c32\u2c60\u2c82\u2ce6")
        buf.write("\u2d02\u2d27\u2d32\u2d67\u2d71\u2d71\u2d82\u2d98\u2da2")
        buf.write("\u2da8\u2daa\u2db0\u2db2\u2db8\u2dba\u2dc0\u2dc2\u2dc8")
        buf.write("\u2dca\u2dd0\u2dd2\u2dd8\u2dda\u2de0\u3007\u3009\u3023")
        buf.write("\u302b\u3033\u3037\u303a\u303e\u3043\u3098\u309d\u30a1")
        buf.write("\u30a3\u30fc\u30fe\u3101\u3107\u312e\u3133\u3190\u31a2")
        buf.write("\u31b9\u31f2\u3201\u3402\u4db7\u4e02\u9fbd\ua002\ua48e")
        buf.write("\ua802\ua803\ua805\ua807\ua809\ua80c\ua80e\ua824\uac02")
        buf.write("\ud7a5\uf902\ufa2f\ufa32\ufa6c\ufa72\ufadb\ufb02\ufb08")
        buf.write("\ufb15\ufb19\ufb1f\ufb1f\ufb21\ufb2a\ufb2c\ufb38\ufb3a")
        buf.write("\ufb3e\ufb40\ufb40\ufb42\ufb43\ufb45\ufb46\ufb48\ufbb3")
        buf.write("\ufbd5\ufd3f\ufd52\ufd91\ufd94\ufdc9\ufdf2\ufdfd\ufe72")
        buf.write("\ufe76\ufe78\ufefe\uff23\uff3c\uff43\uff5c\uff68\uffc0")
        buf.write("\uffc4\uffc9\uffcc\uffd1\uffd4\uffd9\uffdc\uffde\u0096")
        buf.write("\2\62;\u0302\u0371\u0485\u0488\u0593\u05bb\u05bd\u05bf")
        buf.write("\u05c1\u05c1\u05c3\u05c4\u05c6\u05c7\u05c9\u05c9\u0612")
        buf.write("\u0617\u064d\u0660\u0662\u066b\u0672\u0672\u06d8\u06de")
        buf.write("\u06e1\u06e6\u06e9\u06ea\u06ec\u06ef\u06f2\u06fb\u0713")
        buf.write("\u0713\u0732\u074c\u07a8\u07b2\u0903\u0905\u093e\u093e")
        buf.write("\u0940\u094f\u0953\u0956\u0964\u0965\u0968\u0971\u0983")
        buf.write("\u0985\u09be\u09be\u09c0\u09c6\u09c9\u09ca\u09cd\u09cf")
        buf.write("\u09d9\u09d9\u09e4\u09e5\u09e8\u09f1\u0a03\u0a05\u0a3e")
        buf.write("\u0a3e\u0a40\u0a44\u0a49\u0a4a\u0a4d\u0a4f\u0a68\u0a73")
        buf.write("\u0a83\u0a85\u0abe\u0abe\u0ac0\u0ac7\u0ac9\u0acb\u0acd")
        buf.write("\u0acf\u0ae4\u0ae5\u0ae8\u0af1\u0b03\u0b05\u0b3e\u0b3e")
        buf.write("\u0b40\u0b45\u0b49\u0b4a\u0b4d\u0b4f\u0b58\u0b59\u0b68")
        buf.write("\u0b71\u0b84\u0b84\u0bc0\u0bc4\u0bc8\u0bca\u0bcc\u0bcf")
        buf.write("\u0bd9\u0bd9\u0be8\u0bf1\u0c03\u0c05\u0c40\u0c46\u0c48")
        buf.write("\u0c4a\u0c4c\u0c4f\u0c57\u0c58\u0c68\u0c71\u0c84\u0c85")
        buf.write("\u0cbe\u0cbe\u0cc0\u0cc6\u0cc8\u0cca\u0ccc\u0ccf\u0cd7")
        buf.write("\u0cd8\u0ce8\u0cf1\u0d04\u0d05\u0d40\u0d45\u0d48\u0d4a")
        buf.write("\u0d4c\u0d4f\u0d59\u0d59\u0d68\u0d71\u0d84\u0d85\u0dcc")
        buf.write("\u0dcc\u0dd1\u0dd6\u0dd8\u0dd8\u0dda\u0de1\u0df4\u0df5")
        buf.write("\u0e33\u0e33\u0e36\u0e3c\u0e49\u0e50\u0e52\u0e5b\u0eb3")
        buf.write("\u0eb3\u0eb6\u0ebb\u0ebd\u0ebe\u0eca\u0ecf\u0ed2\u0edb")
        buf.write("\u0f1a\u0f1b\u0f22\u0f2b\u0f37\u0f37\u0f39\u0f39\u0f3b")
        buf.write("\u0f3b\u0f40\u0f41\u0f73\u0f86\u0f88\u0f89\u0f92\u0f99")
        buf.write("\u0f9b\u0fbe\u0fc8\u0fc8\u102e\u1034\u1038\u103b\u1042")
        buf.write("\u104b\u1058\u105b\u1361\u1361\u136b\u1373\u1714\u1716")
        buf.write("\u1734\u1736\u1754\u1755\u1774\u1775\u17b8\u17d5\u17df")
        buf.write("\u17df\u17e2\u17eb\u180d\u180f\u1812\u181b\u18ab\u18ab")
        buf.write("\u1922\u192d\u1932\u193d\u1948\u1951\u19b2\u19c2\u19ca")
        buf.write("\u19cb\u19d2\u19db\u1a19\u1a1d\u1dc2\u1dc5\u2041\u2042")
        buf.write("\u2056\u2056\u20d2\u20de\u20e3\u20e3\u20e7\u20ed\u302c")
        buf.write("\u3031\u309b\u309c\ua804\ua804\ua808\ua808\ua80d\ua80d")
        buf.write("\ua825\ua829\ufb20\ufb20\ufe02\ufe11\ufe22\ufe25\ufe35")
        buf.write("\ufe36\ufe4f\ufe51\uff12\uff1b\uff41\uff41\2\u031a\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\3\u00c9\3\2\2\2\5\u00d2")
        buf.write("\3\2\2\2\7\u00d9\3\2\2\2\t\u00e6\3\2\2\2\13\u00e8\3\2")
        buf.write("\2\2\r\u00f1\3\2\2\2\17\u00f6\3\2\2\2\21\u00f9\3\2\2\2")
        buf.write("\23\u0101\3\2\2\2\25\u0103\3\2\2\2\27\u0108\3\2\2\2\31")
        buf.write("\u0113\3\2\2\2\33\u0119\3\2\2\2\35\u012c\3\2\2\2\37\u012e")
        buf.write("\3\2\2\2!\u0148\3\2\2\2#\u014a\3\2\2\2%\u0156\3\2\2\2")
        buf.write("\'\u0166\3\2\2\2)\u0168\3\2\2\2+\u016a\3\2\2\2-\u016d")
        buf.write("\3\2\2\2/\u016f\3\2\2\2\61\u0172\3\2\2\2\63\u0175\3\2")
        buf.write("\2\2\65\u0177\3\2\2\2\67\u0179\3\2\2\29\u017b\3\2\2\2")
        buf.write(";\u017d\3\2\2\2=\u0180\3\2\2\2?\u0183\3\2\2\2A\u0186\3")
        buf.write("\2\2\2C\u0189\3\2\2\2E\u018d\3\2\2\2G\u0190\3\2\2\2I\u0193")
        buf.write("\3\2\2\2K\u0196\3\2\2\2M\u0198\3\2\2\2O\u019a\3\2\2\2")
        buf.write("Q\u019c\3\2\2\2S\u019e\3\2\2\2U\u01a2\3\2\2\2W\u01a6\3")
        buf.write("\2\2\2Y\u01a8\3\2\2\2[\u01ab\3\2\2\2]\u01ae\3\2\2\2_\u01b0")
        buf.write("\3\2\2\2a\u01b5\3\2\2\2c\u01b7\3\2\2\2e\u01ba\3\2\2\2")
        buf.write("g\u01bd\3\2\2\2i\u01c0\3\2\2\2k\u01c2\3\2\2\2m\u01c5\3")
        buf.write("\2\2\2o\u01c9\3\2\2\2q\u01d0\3\2\2\2s\u01da\3\2\2\2u\u01dc")
        buf.write("\3\2\2\2w\u01e4\3\2\2\2y\u01e9\3\2\2\2{\u01fe\3\2\2\2")
        buf.write("}\u020c\3\2\2\2\177\u020e\3\2\2\2\u0081\u0212\3\2\2\2")
        buf.write("\u0083\u0228\3\2\2\2\u0085\u0236\3\2\2\2\u0087\u023a\3")
        buf.write("\2\2\2\u0089\u0241\3\2\2\2\u008b\u0244\3\2\2\2\u008d\u0258")
        buf.write("\3\2\2\2\u008f\u025a\3\2\2\2\u0091\u0261\3\2\2\2\u0093")
        buf.write("\u0268\3\2\2\2\u0095\u026f\3\2\2\2\u0097\u0273\3\2\2\2")
        buf.write("\u0099\u027a\3\2\2\2\u009b\u027e\3\2\2\2\u009d\u0280\3")
        buf.write("\2\2\2\u009f\u028a\3\2\2\2\u00a1\u028d\3\2\2\2\u00a3\u028f")
        buf.write("\3\2\2\2\u00a5\u0291\3\2\2\2\u00a7\u0293\3\2\2\2\u00a9")
        buf.write("\u0295\3\2\2\2\u00ab\u0297\3\2\2\2\u00ad\u029b\3\2\2\2")
        buf.write("\u00af\u029f\3\2\2\2\u00b1\u02b7\3\2\2\2\u00b3\u02d3\3")
        buf.write("\2\2\2\u00b5\u02d7\3\2\2\2\u00b7\u02da\3\2\2\2\u00b9\u02dd")
        buf.write("\3\2\2\2\u00bb\u02e0\3\2\2\2\u00bd\u02e2\3\2\2\2\u00bf")
        buf.write("\u02e6\3\2\2\2\u00c1\u02ea\3\2\2\2\u00c3\u02f1\3\2\2\2")
        buf.write("\u00c5\u02fd\3\2\2\2\u00c7\u0301\3\2\2\2\u00c9\u00ca\7")
        buf.write("t\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd")
        buf.write("\7q\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0")
        buf.write("\7c\2\2\u00d0\u00d1\7t\2\2\u00d1\4\3\2\2\2\u00d2\u00d3")
        buf.write("\7w\2\2\u00d3\u00d4\7u\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6")
        buf.write("\7p\2\2\u00d6\u00d7\7f\2\2\u00d7\u00d8\7q\2\2\u00d8\6")
        buf.write("\3\2\2\2\u00d9\u00da\7u\2\2\u00da\u00db\7g\2\2\u00db\b")
        buf.write("\3\2\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de\7g\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df\u00e0\7\u00e5\2\2\u00e0\u00e7\7q\2\2\u00e1")
        buf.write("\u00e2\7u\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4\7p\2\2\u00e4")
        buf.write("\u00e5\7c\2\2\u00e5\u00e7\7q\2\2\u00e6\u00dc\3\2\2\2\u00e6")
        buf.write("\u00e1\3\2\2\2\u00e7\n\3\2\2\2\u00e8\u00e9\7g\2\2\u00e9")
        buf.write("\u00ea\7p\2\2\u00ea\u00eb\7s\2\2\u00eb\u00ec\7w\2\2\u00ec")
        buf.write("\u00ed\7c\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7v\2\2\u00ef")
        buf.write("\u00f0\7q\2\2\u00f0\f\3\2\2\2\u00f1\u00f2\7r\2\2\u00f2")
        buf.write("\u00f3\7c\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5\7c\2\2\u00f5")
        buf.write("\16\3\2\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7w\2\2\u00f8")
        buf.write("\20\3\2\2\2\u00f9\u00fa\7g\2\2\u00fa\22\3\2\2\2\u00fb")
        buf.write("\u00fc\7p\2\2\u00fc\u00fd\7\u00e5\2\2\u00fd\u0102\7q\2")
        buf.write("\2\u00fe\u00ff\7p\2\2\u00ff\u0100\7c\2\2\u0100\u0102\7")
        buf.write("q\2\2\u0101\u00fb\3\2\2\2\u0101\u00fe\3\2\2\2\u0102\24")
        buf.write("\3\2\2\2\u0103\u0104\7p\2\2\u0104\u0105\7w\2\2\u0105\u0106")
        buf.write("\7n\2\2\u0106\u0107\7q\2\2\u0107\26\3\2\2\2\u0108\u0109")
        buf.write("\7x\2\2\u0109\u010a\7g\2\2\u010a\u010b\7t\2\2\u010b\u010c")
        buf.write("\7f\2\2\u010c\u010d\7c\2\2\u010d\u010e\7f\2\2\u010e\u010f")
        buf.write("\7g\2\2\u010f\u0110\7k\2\2\u0110\u0111\7t\2\2\u0111\u0112")
        buf.write("\7q\2\2\u0112\30\3\2\2\2\u0113\u0114\7h\2\2\u0114\u0115")
        buf.write("\7c\2\2\u0115\u0116\7n\2\2\u0116\u0117\7u\2\2\u0117\u0118")
        buf.write("\7q\2\2\u0118\32\3\2\2\2\u0119\u011a\7v\2\2\u011a\u011b")
        buf.write("\7k\2\2\u011b\u011c\7r\2\2\u011c\u011d\7q\2\2\u011d\34")
        buf.write("\3\2\2\2\u011e\u011f\7c\2\2\u011f\u0120\7x\2\2\u0120\u0121")
        buf.write("\7c\2\2\u0121\u0122\7p\2\2\u0122\u0123\7\u00e9\2\2\u0123")
        buf.write("\u0124\7c\2\2\u0124\u012d\7t\2\2\u0125\u0126\7c\2\2\u0126")
        buf.write("\u0127\7x\2\2\u0127\u0128\7c\2\2\u0128\u0129\7p\2\2\u0129")
        buf.write("\u012a\7e\2\2\u012a\u012b\7c\2\2\u012b\u012d\7t\2\2\u012c")
        buf.write("\u011e\3\2\2\2\u012c\u0125\3\2\2\2\u012d\36\3\2\2\2\u012e")
        buf.write("\u012f\7r\2\2\u012f\u0130\7c\2\2\u0130\u0131\7t\2\2\u0131")
        buf.write("\u0132\7c\2\2\u0132\u0133\7t\2\2\u0133 \3\2\2\2\u0134")
        buf.write("\u0135\7g\2\2\u0135\u0136\7p\2\2\u0136\u0137\7w\2\2\u0137")
        buf.write("\u0138\7o\2\2\u0138\u0139\7g\2\2\u0139\u013a\7t\2\2\u013a")
        buf.write("\u013b\7c\2\2\u013b\u013c\7\u00e9\2\2\u013c\u013d\7\u00e5")
        buf.write("\2\2\u013d\u0149\7q\2\2\u013e\u013f\7g\2\2\u013f\u0140")
        buf.write("\7p\2\2\u0140\u0141\7w\2\2\u0141\u0142\7o\2\2\u0142\u0143")
        buf.write("\7g\2\2\u0143\u0144\7t\2\2\u0144\u0145\7c\2\2\u0145\u0146")
        buf.write("\7e\2\2\u0146\u0147\7c\2\2\u0147\u0149\7q\2\2\u0148\u0134")
        buf.write("\3\2\2\2\u0148\u013e\3\2\2\2\u0149\"\3\2\2\2\u014a\u014b")
        buf.write("\7r\2\2\u014b\u014c\7c\2\2\u014c\u014d\7u\2\2\u014d\u014e")
        buf.write("\7u\2\2\u014e\u014f\7q\2\2\u014f$\3\2\2\2\u0150\u0151")
        buf.write("\7c\2\2\u0151\u0152\7v\2\2\u0152\u0157\7g\2\2\u0153\u0154")
        buf.write("\7c\2\2\u0154\u0155\7v\2\2\u0155\u0157\7\u00eb\2\2\u0156")
        buf.write("\u0150\3\2\2\2\u0156\u0153\3\2\2\2\u0157&\3\2\2\2\u0158")
        buf.write("\u0159\7k\2\2\u0159\u015a\7p\2\2\u015a\u015b\7e\2\2\u015b")
        buf.write("\u015c\7n\2\2\u015c\u015d\7w\2\2\u015d\u015e\7u\2\2\u015e")
        buf.write("\u015f\7k\2\2\u015f\u0160\7x\2\2\u0160\u0167\7g\2\2\u0161")
        buf.write("\u0162\7k\2\2\u0162\u0163\7p\2\2\u0163\u0164\7e\2\2\u0164")
        buf.write("\u0165\7n\2\2\u0165\u0167\7\60\2\2\u0166\u0158\3\2\2\2")
        buf.write("\u0166\u0161\3\2\2\2\u0167(\3\2\2\2\u0168\u0169\7\60\2")
        buf.write("\2\u0169*\3\2\2\2\u016a\u016b\7\60\2\2\u016b\u016c\7\60")
        buf.write("\2\2\u016c,\3\2\2\2\u016d\u016e\7~\2\2\u016e.\3\2\2\2")
        buf.write("\u016f\u0170\7*\2\2\u0170\u0171\b\30\2\2\u0171\60\3\2")
        buf.write("\2\2\u0172\u0173\7+\2\2\u0173\u0174\b\31\3\2\u0174\62")
        buf.write("\3\2\2\2\u0175\u0176\7.\2\2\u0176\64\3\2\2\2\u0177\u0178")
        buf.write("\7<\2\2\u0178\66\3\2\2\2\u0179\u017a\7=\2\2\u017a8\3\2")
        buf.write("\2\2\u017b\u017c\7`\2\2\u017c:\3\2\2\2\u017d\u017e\7>")
        buf.write("\2\2\u017e\u017f\7/\2\2\u017f<\3\2\2\2\u0180\u0181\7]")
        buf.write("\2\2\u0181\u0182\b\37\4\2\u0182>\3\2\2\2\u0183\u0184\7")
        buf.write("_\2\2\u0184\u0185\b \5\2\u0185@\3\2\2\2\u0186\u0187\7")
        buf.write("~\2\2\u0187\u0188\7~\2\2\u0188B\3\2\2\2\u0189\u018a\7")
        buf.write("z\2\2\u018a\u018b\7q\2\2\u018b\u018c\7t\2\2\u018cD\3\2")
        buf.write("\2\2\u018d\u018e\7(\2\2\u018e\u018f\7(\2\2\u018fF\3\2")
        buf.write("\2\2\u0190\u0191\7>\2\2\u0191\u0192\7>\2\2\u0192H\3\2")
        buf.write("\2\2\u0193\u0194\7@\2\2\u0194\u0195\7@\2\2\u0195J\3\2")
        buf.write("\2\2\u0196\u0197\7-\2\2\u0197L\3\2\2\2\u0198\u0199\7/")
        buf.write("\2\2\u0199N\3\2\2\2\u019a\u019b\7,\2\2\u019bP\3\2\2\2")
        buf.write("\u019c\u019d\7\61\2\2\u019dR\3\2\2\2\u019e\u019f\7o\2")
        buf.write("\2\u019f\u01a0\7q\2\2\u01a0\u01a1\7f\2\2\u01a1T\3\2\2")
        buf.write("\2\u01a2\u01a3\7f\2\2\u01a3\u01a4\7k\2\2\u01a4\u01a5\7")
        buf.write("x\2\2\u01a5V\3\2\2\2\u01a6\u01a7\7\u0080\2\2\u01a7X\3")
        buf.write("\2\2\2\u01a8\u01a9\7}\2\2\u01a9\u01aa\b-\6\2\u01aaZ\3")
        buf.write("\2\2\2\u01ab\u01ac\7\177\2\2\u01ac\u01ad\b.\7\2\u01ad")
        buf.write("\\\3\2\2\2\u01ae\u01af\7>\2\2\u01af^\3\2\2\2\u01b0\u01b1")
        buf.write("\7@\2\2\u01b1`\3\2\2\2\u01b2\u01b6\7?\2\2\u01b3\u01b4")
        buf.write("\7?\2\2\u01b4\u01b6\7?\2\2\u01b5\u01b2\3\2\2\2\u01b5\u01b3")
        buf.write("\3\2\2\2\u01b6b\3\2\2\2\u01b7\u01b8\7@\2\2\u01b8\u01b9")
        buf.write("\7?\2\2\u01b9d\3\2\2\2\u01ba\u01bb\7>\2\2\u01bb\u01bc")
        buf.write("\7?\2\2\u01bcf\3\2\2\2\u01bd\u01be\7#\2\2\u01be\u01bf")
        buf.write("\7?\2\2\u01bfh\3\2\2\2\u01c0\u01c1\7B\2\2\u01c1j\3\2\2")
        buf.write("\2\u01c2\u01c3\7/\2\2\u01c3\u01c4\7@\2\2\u01c4l\3\2\2")
        buf.write("\2\u01c5\u01c6\7x\2\2\u01c6\u01c7\7c\2\2\u01c7\u01c8\7")
        buf.write("n\2\2\u01c8n\3\2\2\2\u01c9\u01ca\7t\2\2\u01ca\u01cb\7")
        buf.write("g\2\2\u01cb\u01cc\7h\2\2\u01ccp\3\2\2\2\u01cd\u01ce\7")
        buf.write("r\2\2\u01ce\u01d1\7k\2\2\u01cf\u01d1\7\u03c2\2\2\u01d0")
        buf.write("\u01cd\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1r\3\2\2\2\u01d2")
        buf.write("\u01d3\7g\2\2\u01d3\u01d4\7u\2\2\u01d4\u01d5\7v\2\2\u01d5")
        buf.write("\u01db\7g\2\2\u01d6\u01d7\7g\2\2\u01d7\u01d8\7u\2\2\u01d8")
        buf.write("\u01d9\7v\2\2\u01d9\u01db\7c\2\2\u01da\u01d2\3\2\2\2\u01da")
        buf.write("\u01d6\3\2\2\2\u01dbt\3\2\2\2\u01dc\u01dd\7k\2\2\u01dd")
        buf.write("\u01de\7p\2\2\u01de\u01df\7v\2\2\u01df\u01e0\7g\2\2\u01e0")
        buf.write("\u01e1\7k\2\2\u01e1\u01e2\7t\2\2\u01e2\u01e3\7q\2\2\u01e3")
        buf.write("v\3\2\2\2\u01e4\u01e5\7t\2\2\u01e5\u01e6\7g\2\2\u01e6")
        buf.write("\u01e7\7c\2\2\u01e7\u01e8\7n\2\2\u01e8x\3\2\2\2\u01e9")
        buf.write("\u01ea\7e\2\2\u01ea\u01eb\7c\2\2\u01eb\u01ec\7t\2\2\u01ec")
        buf.write("\u01ed\7c\2\2\u01ed\u01ee\7e\2\2\u01ee\u01ef\7v\2\2\u01ef")
        buf.write("\u01f0\7g\2\2\u01f0\u01f1\7t\2\2\u01f1z\3\2\2\2\u01f2")
        buf.write("\u01f3\7e\2\2\u01f3\u01f4\7c\2\2\u01f4\u01f5\7f\2\2\u01f5")
        buf.write("\u01f6\7g\2\2\u01f6\u01f7\7k\2\2\u01f7\u01ff\7c\2\2\u01f8")
        buf.write("\u01f9\7x\2\2\u01f9\u01fa\7k\2\2\u01fa\u01fb\7u\2\2\u01fb")
        buf.write("\u01fc\7w\2\2\u01fc\u01fd\7c\2\2\u01fd\u01ff\7n\2\2\u01fe")
        buf.write("\u01f2\3\2\2\2\u01fe\u01f8\3\2\2\2\u01ff|\3\2\2\2\u0200")
        buf.write("\u0201\7n\2\2\u0201\u0202\7\u00f5\2\2\u0202\u0203\7i\2")
        buf.write("\2\u0203\u0204\7k\2\2\u0204\u0205\7e\2\2\u0205\u020d\7")
        buf.write("q\2\2\u0206\u0207\7n\2\2\u0207\u0208\7q\2\2\u0208\u0209")
        buf.write("\7i\2\2\u0209\u020a\7k\2\2\u020a\u020b\7e\2\2\u020b\u020d")
        buf.write("\7q\2\2\u020c\u0200\3\2\2\2\u020c\u0206\3\2\2\2\u020d")
        buf.write("~\3\2\2\2\u020e\u020f\7\60\2\2\u020f\u0210\7\60\2\2\u0210")
        buf.write("\u0211\7\60\2\2\u0211\u0080\3\2\2\2\u0212\u0213\7e\2\2")
        buf.write("\u0213\u0214\7q\2\2\u0214\u0215\7p\2\2\u0215\u0216\7u")
        buf.write("\2\2\u0216\u0217\7v\2\2\u0217\u0218\7c\2\2\u0218\u0219")
        buf.write("\7p\2\2\u0219\u021a\7v\2\2\u021a\u021b\7g\2\2\u021b\u0082")
        buf.write("\3\2\2\2\u021c\u021d\7q\2\2\u021d\u021e\7e\2\2\u021e\u021f")
        buf.write("\7w\2\2\u021f\u0220\7n\2\2\u0220\u0221\7v\2\2\u0221\u0229")
        buf.write("\7q\2\2\u0222\u0223\7q\2\2\u0223\u0224\7e\2\2\u0224\u0225")
        buf.write("\7w\2\2\u0225\u0226\7n\2\2\u0226\u0227\7v\2\2\u0227\u0229")
        buf.write("\7c\2\2\u0228\u021c\3\2\2\2\u0228\u0222\3\2\2\2\u0229")
        buf.write("\u0084\3\2\2\2\u022a\u022b\6C\2\2\u022b\u0237\5\u00bf")
        buf.write("`\2\u022c\u022e\7\17\2\2\u022d\u022c\3\2\2\2\u022d\u022e")
        buf.write("\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0232\7\f\2\2\u0230")
        buf.write("\u0232\7\17\2\2\u0231\u022d\3\2\2\2\u0231\u0230\3\2\2")
        buf.write("\2\u0232\u0234\3\2\2\2\u0233\u0235\5\u00bf`\2\u0234\u0233")
        buf.write("\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u0237\3\2\2\2\u0236")
        buf.write("\u022a\3\2\2\2\u0236\u0231\3\2\2\2\u0237\u0238\3\2\2\2")
        buf.write("\u0238\u0239\bC\b\2\u0239\u0086\3\2\2\2\u023a\u023e\5")
        buf.write("\u00c5c\2\u023b\u023d\5\u00c7d\2\u023c\u023b\3\2\2\2\u023d")
        buf.write("\u0240\3\2\2\2\u023e\u023c\3\2\2\2\u023e\u023f\3\2\2\2")
        buf.write("\u023f\u0088\3\2\2\2\u0240\u023e\3\2\2\2\u0241\u0242\5")
        buf.write("\u009dO\2\u0242\u0243\bE\t\2\u0243\u008a\3\2\2\2\u0244")
        buf.write("\u0247\7)\2\2\u0245\u0248\5\u009fP\2\u0246\u0248\n\2\2")
        buf.write("\2\u0247\u0245\3\2\2\2\u0247\u0246\3\2\2\2\u0248\u0249")
        buf.write("\3\2\2\2\u0249\u024a\7)\2\2\u024a\u024b\bF\n\2\u024b\u008c")
        buf.write("\3\2\2\2\u024c\u0250\5\u00a1Q\2\u024d\u024f\5\u00a3R\2")
        buf.write("\u024e\u024d\3\2\2\2\u024f\u0252\3\2\2\2\u0250\u024e\3")
        buf.write("\2\2\2\u0250\u0251\3\2\2\2\u0251\u0259\3\2\2\2\u0252\u0250")
        buf.write("\3\2\2\2\u0253\u0255\7\62\2\2\u0254\u0253\3\2\2\2\u0255")
        buf.write("\u0256\3\2\2\2\u0256\u0254\3\2\2\2\u0256\u0257\3\2\2\2")
        buf.write("\u0257\u0259\3\2\2\2\u0258\u024c\3\2\2\2\u0258\u0254\3")
        buf.write("\2\2\2\u0259\u008e\3\2\2\2\u025a\u025b\7\62\2\2\u025b")
        buf.write("\u025d\t\3\2\2\u025c\u025e\5\u00a5S\2\u025d\u025c\3\2")
        buf.write("\2\2\u025e\u025f\3\2\2\2\u025f\u025d\3\2\2\2\u025f\u0260")
        buf.write("\3\2\2\2\u0260\u0090\3\2\2\2\u0261\u0262\7\62\2\2\u0262")
        buf.write("\u0264\t\4\2\2\u0263\u0265\5\u00a7T\2\u0264\u0263\3\2")
        buf.write("\2\2\u0265\u0266\3\2\2\2\u0266\u0264\3\2\2\2\u0266\u0267")
        buf.write("\3\2\2\2\u0267\u0092\3\2\2\2\u0268\u0269\7\62\2\2\u0269")
        buf.write("\u026b\t\5\2\2\u026a\u026c\5\u00a9U\2\u026b\u026a\3\2")
        buf.write("\2\2\u026c\u026d\3\2\2\2\u026d\u026b\3\2\2\2\u026d\u026e")
        buf.write("\3\2\2\2\u026e\u0094\3\2\2\2\u026f\u0270\5\u00abV\2\u0270")
        buf.write("\u0096\3\2\2\2\u0271\u0274\5\u0095K\2\u0272\u0274\5\u00ad")
        buf.write("W\2\u0273\u0271\3\2\2\2\u0273\u0272\3\2\2\2\u0274\u0275")
        buf.write("\3\2\2\2\u0275\u0276\t\6\2\2\u0276\u0098\3\2\2\2\u0277")
        buf.write("\u027b\5\u00bf`\2\u0278\u027b\5\u00c1a\2\u0279\u027b\5")
        buf.write("\u00c3b\2\u027a\u0277\3\2\2\2\u027a\u0278\3\2\2\2\u027a")
        buf.write("\u0279\3\2\2\2\u027b\u027c\3\2\2\2\u027c\u027d\bM\13\2")
        buf.write("\u027d\u009a\3\2\2\2\u027e\u027f\13\2\2\2\u027f\u009c")
        buf.write("\3\2\2\2\u0280\u0285\7$\2\2\u0281\u0284\5\u009fP\2\u0282")
        buf.write("\u0284\n\2\2\2\u0283\u0281\3\2\2\2\u0283\u0282\3\2\2\2")
        buf.write("\u0284\u0287\3\2\2\2\u0285\u0283\3\2\2\2\u0285\u0286\3")
        buf.write("\2\2\2\u0286\u0288\3\2\2\2\u0287\u0285\3\2\2\2\u0288\u0289")
        buf.write("\7$\2\2\u0289\u009e\3\2\2\2\u028a\u028b\7^\2\2\u028b\u028c")
        buf.write("\13\2\2\2\u028c\u00a0\3\2\2\2\u028d\u028e\t\7\2\2\u028e")
        buf.write("\u00a2\3\2\2\2\u028f\u0290\t\b\2\2\u0290\u00a4\3\2\2\2")
        buf.write("\u0291\u0292\t\t\2\2\u0292\u00a6\3\2\2\2\u0293\u0294\t")
        buf.write("\n\2\2\u0294\u00a8\3\2\2\2\u0295\u0296\t\13\2\2\u0296")
        buf.write("\u00aa\3\2\2\2\u0297\u0298\5\u00adW\2\u0298\u0299\5\u00af")
        buf.write("X\2\u0299\u00ac\3\2\2\2\u029a\u029c\5\u00a3R\2\u029b\u029a")
        buf.write("\3\2\2\2\u029c\u029d\3\2\2\2\u029d\u029b\3\2\2\2\u029d")
        buf.write("\u029e\3\2\2\2\u029e\u00ae\3\2\2\2\u029f\u02a1\7\60\2")
        buf.write("\2\u02a0\u02a2\5\u00a3R\2\u02a1\u02a0\3\2\2\2\u02a2\u02a3")
        buf.write("\3\2\2\2\u02a3\u02a1\3\2\2\2\u02a3\u02a4\3\2\2\2\u02a4")
        buf.write("\u00b0\3\2\2\2\u02a5\u02aa\7)\2\2\u02a6\u02a9\5\u00b7")
        buf.write("\\\2\u02a7\u02a9\5\u00bd_\2\u02a8\u02a6\3\2\2\2\u02a8")
        buf.write("\u02a7\3\2\2\2\u02a9\u02ac\3\2\2\2\u02aa\u02a8\3\2\2\2")
        buf.write("\u02aa\u02ab\3\2\2\2\u02ab\u02ad\3\2\2\2\u02ac\u02aa\3")
        buf.write("\2\2\2\u02ad\u02b8\7)\2\2\u02ae\u02b3\7$\2\2\u02af\u02b2")
        buf.write("\5\u00b9]\2\u02b0\u02b2\5\u00bd_\2\u02b1\u02af\3\2\2\2")
        buf.write("\u02b1\u02b0\3\2\2\2\u02b2\u02b5\3\2\2\2\u02b3\u02b1\3")
        buf.write("\2\2\2\u02b3\u02b4\3\2\2\2\u02b4\u02b6\3\2\2\2\u02b5\u02b3")
        buf.write("\3\2\2\2\u02b6\u02b8\7$\2\2\u02b7\u02a5\3\2\2\2\u02b7")
        buf.write("\u02ae\3\2\2\2\u02b8\u00b2\3\2\2\2\u02b9\u02ba\7)\2\2")
        buf.write("\u02ba\u02bb\7)\2\2\u02bb\u02bc\7)\2\2\u02bc\u02c0\3\2")
        buf.write("\2\2\u02bd\u02bf\5\u00b5[\2\u02be\u02bd\3\2\2\2\u02bf")
        buf.write("\u02c2\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c0\u02be\3\2\2\2")
        buf.write("\u02c1\u02c3\3\2\2\2\u02c2\u02c0\3\2\2\2\u02c3\u02c4\7")
        buf.write(")\2\2\u02c4\u02c5\7)\2\2\u02c5\u02d4\7)\2\2\u02c6\u02c7")
        buf.write("\7$\2\2\u02c7\u02c8\7$\2\2\u02c8\u02c9\7$\2\2\u02c9\u02cd")
        buf.write("\3\2\2\2\u02ca\u02cc\5\u00b5[\2\u02cb\u02ca\3\2\2\2\u02cc")
        buf.write("\u02cf\3\2\2\2\u02cd\u02ce\3\2\2\2\u02cd\u02cb\3\2\2\2")
        buf.write("\u02ce\u02d0\3\2\2\2\u02cf\u02cd\3\2\2\2\u02d0\u02d1\7")
        buf.write("$\2\2\u02d1\u02d2\7$\2\2\u02d2\u02d4\7$\2\2\u02d3\u02b9")
        buf.write("\3\2\2\2\u02d3\u02c6\3\2\2\2\u02d4\u00b4\3\2\2\2\u02d5")
        buf.write("\u02d8\5\u00bb^\2\u02d6\u02d8\5\u00bd_\2\u02d7\u02d5\3")
        buf.write("\2\2\2\u02d7\u02d6\3\2\2\2\u02d8\u00b6\3\2\2\2\u02d9\u02db")
        buf.write("\t\f\2\2\u02da\u02d9\3\2\2\2\u02db\u00b8\3\2\2\2\u02dc")
        buf.write("\u02de\t\r\2\2\u02dd\u02dc\3\2\2\2\u02de\u00ba\3\2\2\2")
        buf.write("\u02df\u02e1\t\16\2\2\u02e0\u02df\3\2\2\2\u02e1\u00bc")
        buf.write("\3\2\2\2\u02e2\u02e3\7^\2\2\u02e3\u02e4\t\17\2\2\u02e4")
        buf.write("\u00be\3\2\2\2\u02e5\u02e7\t\20\2\2\u02e6\u02e5\3\2\2")
        buf.write("\2\u02e7\u02e8\3\2\2\2\u02e8\u02e6\3\2\2\2\u02e8\u02e9")
        buf.write("\3\2\2\2\u02e9\u00c0\3\2\2\2\u02ea\u02ee\7%\2\2\u02eb")
        buf.write("\u02ed\n\21\2\2\u02ec\u02eb\3\2\2\2\u02ed\u02f0\3\2\2")
        buf.write("\2\u02ee\u02ec\3\2\2\2\u02ee\u02ef\3\2\2\2\u02ef\u00c2")
        buf.write("\3\2\2\2\u02f0\u02ee\3\2\2\2\u02f1\u02f3\7^\2\2\u02f2")
        buf.write("\u02f4\5\u00bf`\2\u02f3\u02f2\3\2\2\2\u02f3\u02f4\3\2")
        buf.write("\2\2\u02f4\u02fa\3\2\2\2\u02f5\u02f7\7\17\2\2\u02f6\u02f5")
        buf.write("\3\2\2\2\u02f6\u02f7\3\2\2\2\u02f7\u02f8\3\2\2\2\u02f8")
        buf.write("\u02fb\7\f\2\2\u02f9\u02fb\7\17\2\2\u02fa\u02f6\3\2\2")
        buf.write("\2\u02fa\u02f9\3\2\2\2\u02fb\u00c4\3\2\2\2\u02fc\u02fe")
        buf.write("\t\22\2\2\u02fd\u02fc\3\2\2\2\u02fe\u00c6\3\2\2\2\u02ff")
        buf.write("\u0302\5\u00c5c\2\u0300\u0302\t\23\2\2\u0301\u02ff\3\2")
        buf.write("\2\2\u0301\u0300\3\2\2\2\u0302\u00c8\3\2\2\2\64\2\u00e6")
        buf.write("\u0101\u012c\u0148\u0156\u0166\u01b5\u01d0\u01da\u01fe")
        buf.write("\u020c\u0228\u022d\u0231\u0234\u0236\u023e\u0247\u0250")
        buf.write("\u0256\u0258\u025f\u0266\u026d\u0273\u027a\u0283\u0285")
        buf.write("\u029d\u02a3\u02a8\u02aa\u02b1\u02b3\u02b7\u02c0\u02cd")
        buf.write("\u02d3\u02d7\u02da\u02dd\u02e0\u02e8\u02ee\u02f3\u02f6")
        buf.write("\u02fa\u02fd\u0301\f\3\30\2\3\31\3\3\37\4\3 \5\3-\6\3")
        buf.write(".\7\3C\b\3E\t\3F\n\b\2\2")
        return buf.getvalue()


class langLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    RETURN = 1
    IMPORT = 2
    IF = 3
    ELSE = 4
    WHILE = 5
    FOR = 6
    OR = 7
    AND = 8
    NOT = 9
    NULL = 10
    TRUE = 11
    FALSE = 12
    CLASS = 13
    CONTINUE = 14
    BREAK = 15
    ENUM = 16
    STEP = 17
    UNTIL = 18
    INCLUSIVE = 19
    DOT = 20
    RANGE_OP = 21
    CARDINALITY_OP = 22
    OPEN_PAREN = 23
    CLOSE_PAREN = 24
    COMMA = 25
    COLON = 26
    SEMI_COLON = 27
    POWER = 28
    ASSIGN = 29
    OPEN_BRACK = 30
    CLOSE_BRACK = 31
    OR_OP = 32
    XOR = 33
    AND_OP = 34
    LEFT_SHIFT = 35
    RIGHT_SHIFT = 36
    ADD = 37
    MINUS = 38
    STAR = 39
    DIV = 40
    MOD = 41
    IDIV = 42
    NOT_OP = 43
    OPEN_BRACE = 44
    CLOSE_BRACE = 45
    LESS_THAN = 46
    GREATER_THAN = 47
    EQUALS = 48
    GT_EQ = 49
    LT_EQ = 50
    NOT_EQ = 51
    AT = 52
    ARROW = 53
    VAL = 54
    REF = 55
    PI = 56
    THIS = 57
    INTEGER = 58
    REAL = 59
    CHAR = 60
    STRING = 61
    BOOLEAN = 62
    VARIADIC = 63
    CONSTANT = 64
    INVISIBLE = 65
    NEWLINE = 66
    NAME = 67
    STRING_LITERAL = 68
    CHAR_LITERAL = 69
    DECIMAL_INTEGER = 70
    OCT_INTEGER = 71
    HEX_INTEGER = 72
    BIN_INTEGER = 73
    FLOAT_NUMBER = 74
    IMAG_NUMBER = 75
    SKIP_ = 76
    UNKNOWN_CHAR = 77

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'retornar'", "'usando'", "'se'", "'enquanto'", "'para'", "'ou'", 
            "'e'", "'nulo'", "'verdadeiro'", "'falso'", "'tipo'", "'parar'", 
            "'passo'", "'.'", "'..'", "'|'", "'('", "')'", "','", "':'", 
            "';'", "'^'", "'<-'", "'['", "']'", "'||'", "'xor'", "'&&'", 
            "'<<'", "'>>'", "'+'", "'-'", "'*'", "'/'", "'mod'", "'div'", 
            "'~'", "'{'", "'}'", "'<'", "'>'", "'>='", "'<='", "'!='", "'@'", 
            "'->'", "'val'", "'ref'", "'inteiro'", "'real'", "'caracter'", 
            "'...'", "'constante'" ]

    symbolicNames = [ "<INVALID>",
            "RETURN", "IMPORT", "IF", "ELSE", "WHILE", "FOR", "OR", "AND", 
            "NOT", "NULL", "TRUE", "FALSE", "CLASS", "CONTINUE", "BREAK", 
            "ENUM", "STEP", "UNTIL", "INCLUSIVE", "DOT", "RANGE_OP", "CARDINALITY_OP", 
            "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", 
            "POWER", "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", "XOR", 
            "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", "STAR", 
            "DIV", "MOD", "IDIV", "NOT_OP", "OPEN_BRACE", "CLOSE_BRACE", 
            "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ", 
            "AT", "ARROW", "VAL", "REF", "PI", "THIS", "INTEGER", "REAL", 
            "CHAR", "STRING", "BOOLEAN", "VARIADIC", "CONSTANT", "INVISIBLE", 
            "NEWLINE", "NAME", "STRING_LITERAL", "CHAR_LITERAL", "DECIMAL_INTEGER", 
            "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", 
            "IMAG_NUMBER", "SKIP_", "UNKNOWN_CHAR" ]

    ruleNames = [ "RETURN", "IMPORT", "IF", "ELSE", "WHILE", "FOR", "OR", 
                  "AND", "NOT", "NULL", "TRUE", "FALSE", "CLASS", "CONTINUE", 
                  "BREAK", "ENUM", "STEP", "UNTIL", "INCLUSIVE", "DOT", 
                  "RANGE_OP", "CARDINALITY_OP", "OPEN_PAREN", "CLOSE_PAREN", 
                  "COMMA", "COLON", "SEMI_COLON", "POWER", "ASSIGN", "OPEN_BRACK", 
                  "CLOSE_BRACK", "OR_OP", "XOR", "AND_OP", "LEFT_SHIFT", 
                  "RIGHT_SHIFT", "ADD", "MINUS", "STAR", "DIV", "MOD", "IDIV", 
                  "NOT_OP", "OPEN_BRACE", "CLOSE_BRACE", "LESS_THAN", "GREATER_THAN", 
                  "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ", "AT", "ARROW", "VAL", 
                  "REF", "PI", "THIS", "INTEGER", "REAL", "CHAR", "STRING", 
                  "BOOLEAN", "VARIADIC", "CONSTANT", "INVISIBLE", "NEWLINE", 
                  "NAME", "STRING_LITERAL", "CHAR_LITERAL", "DECIMAL_INTEGER", 
                  "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", 
                  "IMAG_NUMBER", "SKIP_", "UNKNOWN_CHAR", "SHORT_STRING", 
                  "STRING_ESCAPE_SEQ", "NON_ZERO_DIGIT", "DIGIT", "OCT_DIGIT", 
                  "HEX_DIGIT", "BIN_DIGIT", "POINT_FLOAT", "INT_PART", "FRACTION", 
                  "SHORT_BYTES", "LONG_BYTES", "LONG_BYTES_ITEM", "SHORT_BYTES_CHAR_NO_SINGLE_QUOTE", 
                  "SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE", "LONG_BYTES_CHAR", 
                  "BYTES_ESCAPE_SEQ", "SPACES", "COMMENT", "LINE_JOINING", 
                  "ID_START", "ID_CONTINUE" ]

    grammarFileName = "lang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    @property
    def tokens(self):
        try:
            return self._tokens
        except AttributeError:
            self._tokens = []
            return self._tokens

    @property
    def indents(self):
        try:
            return self._indents
        except AttributeError:
            self._indents = []
            return self._indents

    @property
    def opened(self):
        try:
            return self._opened
        except AttributeError:
            self._opened = 0
            return self._opened

    @opened.setter
    def opened(self, value):
        self._opened = value

    @property
    def lastToken(self):
        try:
            return self._lastToken
        except AttributeError:
            self._lastToken = None
            return self._lastToken

    @lastToken.setter
    def lastToken(self, value):
        self._lastToken = value

    def reset(self):
        super().reset()
        self.tokens = []
        self.indents = []
        self.opened = 0
        self.lastToken = None

    def emitToken(self, t):
        super().emitToken(t)
        self.tokens.append(t)

    def nextToken(self):
        if self._input.LA(1) == Token.EOF and self.indents:
            for i in range(len(self.tokens)-1,-1,-1):
                if self.tokens[i].type == Token.EOF:
                    self.tokens.pop(i)
            self.emitToken(self.commonToken(LanguageParser.NEWLINE, '\n'))
            while self.indents:
                self.emitToken(self.createDedent())
                self.indents.pop()
            self.emitToken(self.commonToken(LanguageParser.EOF, "<EOF>"))
        next = super().nextToken()
        if next.channel == Token.DEFAULT_CHANNEL:
            self.lastToken = next
        return next if not self.tokens else self.tokens.pop(0)

    def createDedent(self):
        dedent = self.commonToken(LanguageParser.DEDENT, "")
        dedent.line = self.lastToken.line
        return dedent

    def commonToken(self, type, text, indent=0):
        stop = self.getCharIndex()-1-indent
        start = (stop - len(text) + 1) if text else stop
        return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)

    @staticmethod
    def getIndentationCount(spaces):
        count = 0
        for ch in spaces:
            if ch == '\t':
                count += 8 - (count % 8)
            else:
                count += 1
        return count

    def atStartOfInput(self):
        return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
    	if self._actions is None:
    		actions = dict()
    		actions[22] = self.OPEN_PAREN_action 
    		actions[23] = self.CLOSE_PAREN_action 
    		actions[29] = self.OPEN_BRACK_action 
    		actions[30] = self.CLOSE_BRACK_action 
    		actions[43] = self.OPEN_BRACE_action 
    		actions[44] = self.CLOSE_BRACE_action 
    		actions[65] = self.NEWLINE_action 
    		actions[67] = self.STRING_LITERAL_action 
    		actions[68] = self.CHAR_LITERAL_action 
    		self._actions = actions
    	action = self._actions.get(ruleIndex, None)
    	if action is not None:
    		action(localctx, actionIndex)
    	else:
    		raise Exception("No registered action for:" + str(ruleIndex))

    def OPEN_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.opened+=1
     

    def CLOSE_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.opened-=1
     

    def OPEN_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.opened+=1
     

    def CLOSE_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.opened-=1
     

    def OPEN_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.opened+=1
     

    def CLOSE_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.opened-=1
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            tempt = Lexer.text.fget(self)
            newLine = re.sub("[^\r\n]+", "", tempt)
            spaces = re.sub("[\r\n]+", "", tempt)
            la_char = ""
            try:
                la = self._input.LA(1)
                la_char = chr(la)       # Python does not compare char to ints directly
            except ValueError:          # End of file
                pass

            # print(la_char)

            if self.opened > 0 or la_char == '\r' or la_char == '\n' or la_char == '#':
                self.skip()
            else:
                indent = self.getIndentationCount(spaces)
                previous = self.indents[-1] if self.indents else 0
                # NEWLINE is actually the '\n' char
                self.emitToken(self.commonToken(self.NEWLINE, newLine, indent=indent))
                if indent == previous:
                    self.skip()
                elif indent > previous:
                    self.indents.append(indent)
                    self.emitToken(self.commonToken(LanguageParser.INDENT, spaces))
                else:
                    while self.indents and self.indents[-1] > indent:
                        self.emitToken(self.createDedent())
                        self.indents.pop()
                
     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            self.text = self.text[1:-1]
     

    def CHAR_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
            self.text = self.text[1:-1]
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[65] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


