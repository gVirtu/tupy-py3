# Generated from lang.g4 by ANTLR 4.7
from antlr4 import *
from antlr4.Token import CommonToken
from langParser import langParser
from io import StringIO
from typing.io import TextIO
import sys
import re


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2I")
        buf.write("\u0307\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00e5\n")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0100")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0141\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\5\23\u014f\n\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3")
        buf.write("\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$")
        buf.write("\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3+")
        buf.write("\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\38\38\39\39\39\39\39\39")
        buf.write("\39\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\3;\3;\5;\u01d9\n;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3")
        buf.write("<\3=\3=\3=\5=\u01e8\n=\3=\3=\5=\u01ec\n=\3=\5=\u01ef\n")
        buf.write("=\5=\u01f1\n=\3=\3=\3>\3>\7>\u01f7\n>\f>\16>\u01fa\13")
        buf.write(">\3?\5?\u01fd\n?\3?\5?\u0200\n?\3?\3?\5?\u0204\n?\3@\3")
        buf.write("@\5@\u0208\n@\3@\3@\5@\u020c\n@\3A\3A\7A\u0210\nA\fA\16")
        buf.write("A\u0213\13A\3A\6A\u0216\nA\rA\16A\u0217\5A\u021a\nA\3")
        buf.write("B\3B\3B\6B\u021f\nB\rB\16B\u0220\3C\3C\3C\6C\u0226\nC")
        buf.write("\rC\16C\u0227\3D\3D\3D\6D\u022d\nD\rD\16D\u022e\3E\3E")
        buf.write("\5E\u0233\nE\3F\3F\5F\u0237\nF\3F\3F\3G\3G\3G\5G\u023e")
        buf.write("\nG\3G\3G\3H\3H\3I\3I\3I\7I\u0247\nI\fI\16I\u024a\13I")
        buf.write("\3I\3I\3I\3I\7I\u0250\nI\fI\16I\u0253\13I\3I\5I\u0256")
        buf.write("\nI\3J\3J\3J\3J\3J\7J\u025d\nJ\fJ\16J\u0260\13J\3J\3J")
        buf.write("\3J\3J\3J\3J\3J\3J\7J\u026a\nJ\fJ\16J\u026d\13J\3J\3J")
        buf.write("\3J\5J\u0272\nJ\3K\3K\5K\u0276\nK\3L\3L\3M\3M\3M\3N\3")
        buf.write("N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\5S\u0288\nS\3S\3S\3S\3S\5")
        buf.write("S\u028e\nS\3T\3T\5T\u0292\nT\3T\3T\3U\6U\u0297\nU\rU\16")
        buf.write("U\u0298\3V\3V\6V\u029d\nV\rV\16V\u029e\3W\3W\5W\u02a3")
        buf.write("\nW\3W\6W\u02a6\nW\rW\16W\u02a7\3X\3X\3X\7X\u02ad\nX\f")
        buf.write("X\16X\u02b0\13X\3X\3X\3X\3X\7X\u02b6\nX\fX\16X\u02b9\13")
        buf.write("X\3X\5X\u02bc\nX\3Y\3Y\3Y\3Y\3Y\7Y\u02c3\nY\fY\16Y\u02c6")
        buf.write("\13Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\7Y\u02d0\nY\fY\16Y\u02d3")
        buf.write("\13Y\3Y\3Y\3Y\5Y\u02d8\nY\3Z\3Z\5Z\u02dc\nZ\3[\5[\u02df")
        buf.write("\n[\3\\\5\\\u02e2\n\\\3]\5]\u02e5\n]\3^\3^\3^\3_\6_\u02eb")
        buf.write("\n_\r_\16_\u02ec\3`\3`\7`\u02f1\n`\f`\16`\u02f4\13`\3")
        buf.write("a\3a\5a\u02f8\na\3a\5a\u02fb\na\3a\3a\5a\u02ff\na\3b\5")
        buf.write("b\u0302\nb\3c\3c\5c\u0306\nc\6\u025e\u026b\u02c4\u02d1")
        buf.write("\2d\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F")
        buf.write("\u008bG\u008dH\u008fI\u0091\2\u0093\2\u0095\2\u0097\2")
        buf.write("\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5")
        buf.write("\2\u00a7\2\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1\2\u00b3")
        buf.write("\2\u00b5\2\u00b7\2\u00b9\2\u00bb\2\u00bd\2\u00bf\2\u00c1")
        buf.write("\2\u00c3\2\u00c5\2\3\2\32\4\2WWww\4\2TTtt\4\2DDdd\4\2")
        buf.write("QQqq\4\2ZZzz\4\2LLll\6\2\f\f\17\17))^^\6\2\f\f\17\17$")
        buf.write("$^^\3\2^^\3\2\63;\3\2\62;\3\2\629\5\2\62;CHch\3\2\62\63")
        buf.write("\4\2GGgg\4\2--//\7\2\2\13\r\16\20(*]_\u0081\7\2\2\13\r")
        buf.write("\16\20#%]_\u0081\4\2\2]_\u0081\3\2\2\u0081\4\2\13\13\"")
        buf.write("\"\4\2\f\f\17\17\u0129\2C\\aac|\u00ac\u00ac\u00b7\u00b7")
        buf.write("\u00bc\u00bc\u00c2\u00d8\u00da\u00f8\u00fa\u0243\u0252")
        buf.write("\u02c3\u02c8\u02d3\u02e2\u02e6\u02f0\u02f0\u037c\u037c")
        buf.write("\u0388\u0388\u038a\u038c\u038e\u038e\u0390\u03a3\u03a5")
        buf.write("\u03d0\u03d2\u03f7\u03f9\u0483\u048c\u04d0\u04d2\u04fb")
        buf.write("\u0502\u0511\u0533\u0558\u055b\u055b\u0563\u0589\u05d2")
        buf.write("\u05ec\u05f2\u05f4\u0623\u063c\u0642\u064c\u0670\u0671")
        buf.write("\u0673\u06d5\u06d7\u06d7\u06e7\u06e8\u06f0\u06f1\u06fc")
        buf.write("\u06fe\u0701\u0701\u0712\u0712\u0714\u0731\u074f\u076f")
        buf.write("\u0782\u07a7\u07b3\u07b3\u0906\u093b\u093f\u093f\u0952")
        buf.write("\u0952\u095a\u0963\u097f\u097f\u0987\u098e\u0991\u0992")
        buf.write("\u0995\u09aa\u09ac\u09b2\u09b4\u09b4\u09b8\u09bb\u09bf")
        buf.write("\u09bf\u09d0\u09d0\u09de\u09df\u09e1\u09e3\u09f2\u09f3")
        buf.write("\u0a07\u0a0c\u0a11\u0a12\u0a15\u0a2a\u0a2c\u0a32\u0a34")
        buf.write("\u0a35\u0a37\u0a38\u0a3a\u0a3b\u0a5b\u0a5e\u0a60\u0a60")
        buf.write("\u0a74\u0a76\u0a87\u0a8f\u0a91\u0a93\u0a95\u0aaa\u0aac")
        buf.write("\u0ab2\u0ab4\u0ab5\u0ab7\u0abb\u0abf\u0abf\u0ad2\u0ad2")
        buf.write("\u0ae2\u0ae3\u0b07\u0b0e\u0b11\u0b12\u0b15\u0b2a\u0b2c")
        buf.write("\u0b32\u0b34\u0b35\u0b37\u0b3b\u0b3f\u0b3f\u0b5e\u0b5f")
        buf.write("\u0b61\u0b63\u0b73\u0b73\u0b85\u0b85\u0b87\u0b8c\u0b90")
        buf.write("\u0b92\u0b94\u0b97\u0b9b\u0b9c\u0b9e\u0b9e\u0ba0\u0ba1")
        buf.write("\u0ba5\u0ba6\u0baa\u0bac\u0bb0\u0bbb\u0c07\u0c0e\u0c10")
        buf.write("\u0c12\u0c14\u0c2a\u0c2c\u0c35\u0c37\u0c3b\u0c62\u0c63")
        buf.write("\u0c87\u0c8e\u0c90\u0c92\u0c94\u0caa\u0cac\u0cb5\u0cb7")
        buf.write("\u0cbb\u0cbf\u0cbf\u0ce0\u0ce0\u0ce2\u0ce3\u0d07\u0d0e")
        buf.write("\u0d10\u0d12\u0d14\u0d2a\u0d2c\u0d3b\u0d62\u0d63\u0d87")
        buf.write("\u0d98\u0d9c\u0db3\u0db5\u0dbd\u0dbf\u0dbf\u0dc2\u0dc8")
        buf.write("\u0e03\u0e32\u0e34\u0e35\u0e42\u0e48\u0e83\u0e84\u0e86")
        buf.write("\u0e86\u0e89\u0e8a\u0e8c\u0e8c\u0e8f\u0e8f\u0e96\u0e99")
        buf.write("\u0e9b\u0ea1\u0ea3\u0ea5\u0ea7\u0ea7\u0ea9\u0ea9\u0eac")
        buf.write("\u0ead\u0eaf\u0eb2\u0eb4\u0eb5\u0ebf\u0ebf\u0ec2\u0ec6")
        buf.write("\u0ec8\u0ec8\u0ede\u0edf\u0f02\u0f02\u0f42\u0f49\u0f4b")
        buf.write("\u0f6c\u0f8a\u0f8d\u1002\u1023\u1025\u1029\u102b\u102c")
        buf.write("\u1052\u1057\u10a2\u10c7\u10d2\u10fc\u10fe\u10fe\u1102")
        buf.write("\u115b\u1161\u11a4\u11aa\u11fb\u1202\u124a\u124c\u124f")
        buf.write("\u1252\u1258\u125a\u125a\u125c\u125f\u1262\u128a\u128c")
        buf.write("\u128f\u1292\u12b2\u12b4\u12b7\u12ba\u12c0\u12c2\u12c2")
        buf.write("\u12c4\u12c7\u12ca\u12d8\u12da\u1312\u1314\u1317\u131a")
        buf.write("\u135c\u1382\u1391\u13a2\u13f6\u1403\u166e\u1671\u1678")
        buf.write("\u1683\u169c\u16a2\u16ec\u16f0\u16f2\u1702\u170e\u1710")
        buf.write("\u1713\u1722\u1733\u1742\u1753\u1762\u176e\u1770\u1772")
        buf.write("\u1782\u17b5\u17d9\u17d9\u17de\u17de\u1822\u1879\u1882")
        buf.write("\u18aa\u1902\u191e\u1952\u196f\u1972\u1976\u1982\u19ab")
        buf.write("\u19c3\u19c9\u1a02\u1a18\u1d02\u1dc1\u1e02\u1e9d\u1ea2")
        buf.write("\u1efb\u1f02\u1f17\u1f1a\u1f1f\u1f22\u1f47\u1f4a\u1f4f")
        buf.write("\u1f52\u1f59\u1f5b\u1f5b\u1f5d\u1f5d\u1f5f\u1f5f\u1f61")
        buf.write("\u1f7f\u1f82\u1fb6\u1fb8\u1fbe\u1fc0\u1fc0\u1fc4\u1fc6")
        buf.write("\u1fc8\u1fce\u1fd2\u1fd5\u1fd8\u1fdd\u1fe2\u1fee\u1ff4")
        buf.write("\u1ff6\u1ff8\u1ffe\u2073\u2073\u2081\u2081\u2092\u2096")
        buf.write("\u2104\u2104\u2109\u2109\u210c\u2115\u2117\u2117\u211a")
        buf.write("\u211f\u2126\u2126\u2128\u2128\u212a\u212a\u212c\u2133")
        buf.write("\u2135\u213b\u213e\u2141\u2147\u214b\u2162\u2185\u2c02")
        buf.write("\u2c30\u2c32\u2c60\u2c82\u2ce6\u2d02\u2d27\u2d32\u2d67")
        buf.write("\u2d71\u2d71\u2d82\u2d98\u2da2\u2da8\u2daa\u2db0\u2db2")
        buf.write("\u2db8\u2dba\u2dc0\u2dc2\u2dc8\u2dca\u2dd0\u2dd2\u2dd8")
        buf.write("\u2dda\u2de0\u3007\u3009\u3023\u302b\u3033\u3037\u303a")
        buf.write("\u303e\u3043\u3098\u309d\u30a1\u30a3\u30fc\u30fe\u3101")
        buf.write("\u3107\u312e\u3133\u3190\u31a2\u31b9\u31f2\u3201\u3402")
        buf.write("\u4db7\u4e02\u9fbd\ua002\ua48e\ua802\ua803\ua805\ua807")
        buf.write("\ua809\ua80c\ua80e\ua824\uac02\ud7a5\uf902\ufa2f\ufa32")
        buf.write("\ufa6c\ufa72\ufadb\ufb02\ufb08\ufb15\ufb19\ufb1f\ufb1f")
        buf.write("\ufb21\ufb2a\ufb2c\ufb38\ufb3a\ufb3e\ufb40\ufb40\ufb42")
        buf.write("\ufb43\ufb45\ufb46\ufb48\ufbb3\ufbd5\ufd3f\ufd52\ufd91")
        buf.write("\ufd94\ufdc9\ufdf2\ufdfd\ufe72\ufe76\ufe78\ufefe\uff23")
        buf.write("\uff3c\uff43\uff5c\uff68\uffc0\uffc4\uffc9\uffcc\uffd1")
        buf.write("\uffd4\uffd9\uffdc\uffde\u0096\2\62;\u0302\u0371\u0485")
        buf.write("\u0488\u0593\u05bb\u05bd\u05bf\u05c1\u05c1\u05c3\u05c4")
        buf.write("\u05c6\u05c7\u05c9\u05c9\u0612\u0617\u064d\u0660\u0662")
        buf.write("\u066b\u0672\u0672\u06d8\u06de\u06e1\u06e6\u06e9\u06ea")
        buf.write("\u06ec\u06ef\u06f2\u06fb\u0713\u0713\u0732\u074c\u07a8")
        buf.write("\u07b2\u0903\u0905\u093e\u093e\u0940\u094f\u0953\u0956")
        buf.write("\u0964\u0965\u0968\u0971\u0983\u0985\u09be\u09be\u09c0")
        buf.write("\u09c6\u09c9\u09ca\u09cd\u09cf\u09d9\u09d9\u09e4\u09e5")
        buf.write("\u09e8\u09f1\u0a03\u0a05\u0a3e\u0a3e\u0a40\u0a44\u0a49")
        buf.write("\u0a4a\u0a4d\u0a4f\u0a68\u0a73\u0a83\u0a85\u0abe\u0abe")
        buf.write("\u0ac0\u0ac7\u0ac9\u0acb\u0acd\u0acf\u0ae4\u0ae5\u0ae8")
        buf.write("\u0af1\u0b03\u0b05\u0b3e\u0b3e\u0b40\u0b45\u0b49\u0b4a")
        buf.write("\u0b4d\u0b4f\u0b58\u0b59\u0b68\u0b71\u0b84\u0b84\u0bc0")
        buf.write("\u0bc4\u0bc8\u0bca\u0bcc\u0bcf\u0bd9\u0bd9\u0be8\u0bf1")
        buf.write("\u0c03\u0c05\u0c40\u0c46\u0c48\u0c4a\u0c4c\u0c4f\u0c57")
        buf.write("\u0c58\u0c68\u0c71\u0c84\u0c85\u0cbe\u0cbe\u0cc0\u0cc6")
        buf.write("\u0cc8\u0cca\u0ccc\u0ccf\u0cd7\u0cd8\u0ce8\u0cf1\u0d04")
        buf.write("\u0d05\u0d40\u0d45\u0d48\u0d4a\u0d4c\u0d4f\u0d59\u0d59")
        buf.write("\u0d68\u0d71\u0d84\u0d85\u0dcc\u0dcc\u0dd1\u0dd6\u0dd8")
        buf.write("\u0dd8\u0dda\u0de1\u0df4\u0df5\u0e33\u0e33\u0e36\u0e3c")
        buf.write("\u0e49\u0e50\u0e52\u0e5b\u0eb3\u0eb3\u0eb6\u0ebb\u0ebd")
        buf.write("\u0ebe\u0eca\u0ecf\u0ed2\u0edb\u0f1a\u0f1b\u0f22\u0f2b")
        buf.write("\u0f37\u0f37\u0f39\u0f39\u0f3b\u0f3b\u0f40\u0f41\u0f73")
        buf.write("\u0f86\u0f88\u0f89\u0f92\u0f99\u0f9b\u0fbe\u0fc8\u0fc8")
        buf.write("\u102e\u1034\u1038\u103b\u1042\u104b\u1058\u105b\u1361")
        buf.write("\u1361\u136b\u1373\u1714\u1716\u1734\u1736\u1754\u1755")
        buf.write("\u1774\u1775\u17b8\u17d5\u17df\u17df\u17e2\u17eb\u180d")
        buf.write("\u180f\u1812\u181b\u18ab\u18ab\u1922\u192d\u1932\u193d")
        buf.write("\u1948\u1951\u19b2\u19c2\u19ca\u19cb\u19d2\u19db\u1a19")
        buf.write("\u1a1d\u1dc2\u1dc5\u2041\u2042\u2056\u2056\u20d2\u20de")
        buf.write("\u20e3\u20e3\u20e7\u20ed\u302c\u3031\u309b\u309c\ua804")
        buf.write("\ua804\ua808\ua808\ua80d\ua80d\ua825\ua829\ufb20\ufb20")
        buf.write("\ufe02\ufe11\ufe22\ufe25\ufe35\ufe36\ufe4f\ufe51\uff12")
        buf.write("\uff1b\uff41\uff41\2\u0323\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\3\u00c7\3\2\2\2\5\u00d0\3\2\2")
        buf.write("\2\7\u00d7\3\2\2\2\t\u00e4\3\2\2\2\13\u00e6\3\2\2\2\r")
        buf.write("\u00ef\3\2\2\2\17\u00f4\3\2\2\2\21\u00f7\3\2\2\2\23\u00ff")
        buf.write("\3\2\2\2\25\u0101\3\2\2\2\27\u0106\3\2\2\2\31\u0111\3")
        buf.write("\2\2\2\33\u0117\3\2\2\2\35\u011c\3\2\2\2\37\u0126\3\2")
        buf.write("\2\2!\u0140\3\2\2\2#\u0142\3\2\2\2%\u014e\3\2\2\2\'\u0150")
        buf.write("\3\2\2\2)\u0152\3\2\2\2+\u0154\3\2\2\2-\u0157\3\2\2\2")
        buf.write("/\u015a\3\2\2\2\61\u015c\3\2\2\2\63\u015e\3\2\2\2\65\u0160")
        buf.write("\3\2\2\2\67\u0162\3\2\2\29\u0165\3\2\2\2;\u0168\3\2\2")
        buf.write("\2=\u016b\3\2\2\2?\u016e\3\2\2\2A\u0172\3\2\2\2C\u0175")
        buf.write("\3\2\2\2E\u0178\3\2\2\2G\u017b\3\2\2\2I\u017d\3\2\2\2")
        buf.write("K\u017f\3\2\2\2M\u0181\3\2\2\2O\u0183\3\2\2\2Q\u0187\3")
        buf.write("\2\2\2S\u018b\3\2\2\2U\u018d\3\2\2\2W\u0190\3\2\2\2Y\u0193")
        buf.write("\3\2\2\2[\u0195\3\2\2\2]\u0197\3\2\2\2_\u0199\3\2\2\2")
        buf.write("a\u019c\3\2\2\2c\u019f\3\2\2\2e\u01a2\3\2\2\2g\u01a4\3")
        buf.write("\2\2\2i\u01a7\3\2\2\2k\u01ab\3\2\2\2m\u01af\3\2\2\2o\u01b7")
        buf.write("\3\2\2\2q\u01bc\3\2\2\2s\u01c5\3\2\2\2u\u01d8\3\2\2\2")
        buf.write("w\u01da\3\2\2\2y\u01f0\3\2\2\2{\u01f4\3\2\2\2}\u01fc\3")
        buf.write("\2\2\2\177\u0205\3\2\2\2\u0081\u0219\3\2\2\2\u0083\u021b")
        buf.write("\3\2\2\2\u0085\u0222\3\2\2\2\u0087\u0229\3\2\2\2\u0089")
        buf.write("\u0232\3\2\2\2\u008b\u0236\3\2\2\2\u008d\u023d\3\2\2\2")
        buf.write("\u008f\u0241\3\2\2\2\u0091\u0255\3\2\2\2\u0093\u0271\3")
        buf.write("\2\2\2\u0095\u0275\3\2\2\2\u0097\u0277\3\2\2\2\u0099\u0279")
        buf.write("\3\2\2\2\u009b\u027c\3\2\2\2\u009d\u027e\3\2\2\2\u009f")
        buf.write("\u0280\3\2\2\2\u00a1\u0282\3\2\2\2\u00a3\u0284\3\2\2\2")
        buf.write("\u00a5\u028d\3\2\2\2\u00a7\u0291\3\2\2\2\u00a9\u0296\3")
        buf.write("\2\2\2\u00ab\u029a\3\2\2\2\u00ad\u02a0\3\2\2\2\u00af\u02bb")
        buf.write("\3\2\2\2\u00b1\u02d7\3\2\2\2\u00b3\u02db\3\2\2\2\u00b5")
        buf.write("\u02de\3\2\2\2\u00b7\u02e1\3\2\2\2\u00b9\u02e4\3\2\2\2")
        buf.write("\u00bb\u02e6\3\2\2\2\u00bd\u02ea\3\2\2\2\u00bf\u02ee\3")
        buf.write("\2\2\2\u00c1\u02f5\3\2\2\2\u00c3\u0301\3\2\2\2\u00c5\u0305")
        buf.write("\3\2\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf\7t\2\2\u00cf\4")
        buf.write("\3\2\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3")
        buf.write("\7c\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7f\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\6\3\2\2\2\u00d7\u00d8\7u\2\2\u00d8\u00d9")
        buf.write("\7g\2\2\u00d9\b\3\2\2\2\u00da\u00db\7u\2\2\u00db\u00dc")
        buf.write("\7g\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7\u00e5\2\2\u00de")
        buf.write("\u00e5\7q\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1\7g\2\2\u00e1")
        buf.write("\u00e2\7p\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e5\7q\2\2\u00e4")
        buf.write("\u00da\3\2\2\2\u00e4\u00df\3\2\2\2\u00e5\n\3\2\2\2\u00e6")
        buf.write("\u00e7\7g\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7s\2\2\u00e9")
        buf.write("\u00ea\7w\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7p\2\2\u00ec")
        buf.write("\u00ed\7v\2\2\u00ed\u00ee\7q\2\2\u00ee\f\3\2\2\2\u00ef")
        buf.write("\u00f0\7r\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7t\2\2\u00f2")
        buf.write("\u00f3\7c\2\2\u00f3\16\3\2\2\2\u00f4\u00f5\7q\2\2\u00f5")
        buf.write("\u00f6\7w\2\2\u00f6\20\3\2\2\2\u00f7\u00f8\7g\2\2\u00f8")
        buf.write("\22\3\2\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb\7\u00e5\2\2")
        buf.write("\u00fb\u0100\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7c")
        buf.write("\2\2\u00fe\u0100\7q\2\2\u00ff\u00f9\3\2\2\2\u00ff\u00fc")
        buf.write("\3\2\2\2\u0100\24\3\2\2\2\u0101\u0102\7p\2\2\u0102\u0103")
        buf.write("\7w\2\2\u0103\u0104\7n\2\2\u0104\u0105\7q\2\2\u0105\26")
        buf.write("\3\2\2\2\u0106\u0107\7x\2\2\u0107\u0108\7g\2\2\u0108\u0109")
        buf.write("\7t\2\2\u0109\u010a\7f\2\2\u010a\u010b\7c\2\2\u010b\u010c")
        buf.write("\7f\2\2\u010c\u010d\7g\2\2\u010d\u010e\7k\2\2\u010e\u010f")
        buf.write("\7t\2\2\u010f\u0110\7q\2\2\u0110\30\3\2\2\2\u0111\u0112")
        buf.write("\7h\2\2\u0112\u0113\7c\2\2\u0113\u0114\7n\2\2\u0114\u0115")
        buf.write("\7u\2\2\u0115\u0116\7q\2\2\u0116\32\3\2\2\2\u0117\u0118")
        buf.write("\7v\2\2\u0118\u0119\7k\2\2\u0119\u011a\7r\2\2\u011a\u011b")
        buf.write("\7q\2\2\u011b\34\3\2\2\2\u011c\u011d\7e\2\2\u011d\u011e")
        buf.write("\7q\2\2\u011e\u011f\7p\2\2\u011f\u0120\7v\2\2\u0120\u0121")
        buf.write("\7k\2\2\u0121\u0122\7p\2\2\u0122\u0123\7w\2\2\u0123\u0124")
        buf.write("\7c\2\2\u0124\u0125\7t\2\2\u0125\36\3\2\2\2\u0126\u0127")
        buf.write("\7r\2\2\u0127\u0128\7c\2\2\u0128\u0129\7t\2\2\u0129\u012a")
        buf.write("\7c\2\2\u012a\u012b\7t\2\2\u012b \3\2\2\2\u012c\u012d")
        buf.write("\7g\2\2\u012d\u012e\7p\2\2\u012e\u012f\7w\2\2\u012f\u0130")
        buf.write("\7o\2\2\u0130\u0131\7g\2\2\u0131\u0132\7t\2\2\u0132\u0133")
        buf.write("\7c\2\2\u0133\u0134\7\u00e9\2\2\u0134\u0135\7\u00e5\2")
        buf.write("\2\u0135\u0141\7q\2\2\u0136\u0137\7g\2\2\u0137\u0138\7")
        buf.write("p\2\2\u0138\u0139\7w\2\2\u0139\u013a\7o\2\2\u013a\u013b")
        buf.write("\7g\2\2\u013b\u013c\7t\2\2\u013c\u013d\7c\2\2\u013d\u013e")
        buf.write("\7e\2\2\u013e\u013f\7c\2\2\u013f\u0141\7q\2\2\u0140\u012c")
        buf.write("\3\2\2\2\u0140\u0136\3\2\2\2\u0141\"\3\2\2\2\u0142\u0143")
        buf.write("\7r\2\2\u0143\u0144\7c\2\2\u0144\u0145\7u\2\2\u0145\u0146")
        buf.write("\7u\2\2\u0146\u0147\7q\2\2\u0147$\3\2\2\2\u0148\u0149")
        buf.write("\7c\2\2\u0149\u014a\7v\2\2\u014a\u014f\7g\2\2\u014b\u014c")
        buf.write("\7c\2\2\u014c\u014d\7v\2\2\u014d\u014f\7\u00eb\2\2\u014e")
        buf.write("\u0148\3\2\2\2\u014e\u014b\3\2\2\2\u014f&\3\2\2\2\u0150")
        buf.write("\u0151\7\60\2\2\u0151(\3\2\2\2\u0152\u0153\7~\2\2\u0153")
        buf.write("*\3\2\2\2\u0154\u0155\7*\2\2\u0155\u0156\b\26\2\2\u0156")
        buf.write(",\3\2\2\2\u0157\u0158\7+\2\2\u0158\u0159\b\27\3\2\u0159")
        buf.write(".\3\2\2\2\u015a\u015b\7.\2\2\u015b\60\3\2\2\2\u015c\u015d")
        buf.write("\7<\2\2\u015d\62\3\2\2\2\u015e\u015f\7=\2\2\u015f\64\3")
        buf.write("\2\2\2\u0160\u0161\7`\2\2\u0161\66\3\2\2\2\u0162\u0163")
        buf.write("\7>\2\2\u0163\u0164\7/\2\2\u01648\3\2\2\2\u0165\u0166")
        buf.write("\7]\2\2\u0166\u0167\b\35\4\2\u0167:\3\2\2\2\u0168\u0169")
        buf.write("\7_\2\2\u0169\u016a\b\36\5\2\u016a<\3\2\2\2\u016b\u016c")
        buf.write("\7~\2\2\u016c\u016d\7~\2\2\u016d>\3\2\2\2\u016e\u016f")
        buf.write("\7z\2\2\u016f\u0170\7q\2\2\u0170\u0171\7t\2\2\u0171@\3")
        buf.write("\2\2\2\u0172\u0173\7(\2\2\u0173\u0174\7(\2\2\u0174B\3")
        buf.write("\2\2\2\u0175\u0176\7>\2\2\u0176\u0177\7>\2\2\u0177D\3")
        buf.write("\2\2\2\u0178\u0179\7@\2\2\u0179\u017a\7@\2\2\u017aF\3")
        buf.write("\2\2\2\u017b\u017c\7-\2\2\u017cH\3\2\2\2\u017d\u017e\7")
        buf.write("/\2\2\u017eJ\3\2\2\2\u017f\u0180\7,\2\2\u0180L\3\2\2\2")
        buf.write("\u0181\u0182\7\61\2\2\u0182N\3\2\2\2\u0183\u0184\7o\2")
        buf.write("\2\u0184\u0185\7q\2\2\u0185\u0186\7f\2\2\u0186P\3\2\2")
        buf.write("\2\u0187\u0188\7f\2\2\u0188\u0189\7k\2\2\u0189\u018a\7")
        buf.write("x\2\2\u018aR\3\2\2\2\u018b\u018c\7\u0080\2\2\u018cT\3")
        buf.write("\2\2\2\u018d\u018e\7}\2\2\u018e\u018f\b+\6\2\u018fV\3")
        buf.write("\2\2\2\u0190\u0191\7\177\2\2\u0191\u0192\b,\7\2\u0192")
        buf.write("X\3\2\2\2\u0193\u0194\7>\2\2\u0194Z\3\2\2\2\u0195\u0196")
        buf.write("\7@\2\2\u0196\\\3\2\2\2\u0197\u0198\7?\2\2\u0198^\3\2")
        buf.write("\2\2\u0199\u019a\7@\2\2\u019a\u019b\7?\2\2\u019b`\3\2")
        buf.write("\2\2\u019c\u019d\7>\2\2\u019d\u019e\7?\2\2\u019eb\3\2")
        buf.write("\2\2\u019f\u01a0\7\u0080\2\2\u01a0\u01a1\7?\2\2\u01a1")
        buf.write("d\3\2\2\2\u01a2\u01a3\7B\2\2\u01a3f\3\2\2\2\u01a4\u01a5")
        buf.write("\7/\2\2\u01a5\u01a6\7@\2\2\u01a6h\3\2\2\2\u01a7\u01a8")
        buf.write("\7x\2\2\u01a8\u01a9\7c\2\2\u01a9\u01aa\7n\2\2\u01aaj\3")
        buf.write("\2\2\2\u01ab\u01ac\7t\2\2\u01ac\u01ad\7g\2\2\u01ad\u01ae")
        buf.write("\7h\2\2\u01ael\3\2\2\2\u01af\u01b0\7k\2\2\u01b0\u01b1")
        buf.write("\7p\2\2\u01b1\u01b2\7v\2\2\u01b2\u01b3\7g\2\2\u01b3\u01b4")
        buf.write("\7k\2\2\u01b4\u01b5\7t\2\2\u01b5\u01b6\7q\2\2\u01b6n\3")
        buf.write("\2\2\2\u01b7\u01b8\7t\2\2\u01b8\u01b9\7g\2\2\u01b9\u01ba")
        buf.write("\7c\2\2\u01ba\u01bb\7n\2\2\u01bbp\3\2\2\2\u01bc\u01bd")
        buf.write("\7e\2\2\u01bd\u01be\7c\2\2\u01be\u01bf\7t\2\2\u01bf\u01c0")
        buf.write("\7c\2\2\u01c0\u01c1\7e\2\2\u01c1\u01c2\7v\2\2\u01c2\u01c3")
        buf.write("\7g\2\2\u01c3\u01c4\7t\2\2\u01c4r\3\2\2\2\u01c5\u01c6")
        buf.write("\7e\2\2\u01c6\u01c7\7c\2\2\u01c7\u01c8\7f\2\2\u01c8\u01c9")
        buf.write("\7g\2\2\u01c9\u01ca\7k\2\2\u01ca\u01cb\7c\2\2\u01cbt\3")
        buf.write("\2\2\2\u01cc\u01cd\7n\2\2\u01cd\u01ce\7\u00f5\2\2\u01ce")
        buf.write("\u01cf\7i\2\2\u01cf\u01d0\7k\2\2\u01d0\u01d1\7e\2\2\u01d1")
        buf.write("\u01d9\7q\2\2\u01d2\u01d3\7n\2\2\u01d3\u01d4\7q\2\2\u01d4")
        buf.write("\u01d5\7i\2\2\u01d5\u01d6\7k\2\2\u01d6\u01d7\7e\2\2\u01d7")
        buf.write("\u01d9\7q\2\2\u01d8\u01cc\3\2\2\2\u01d8\u01d2\3\2\2\2")
        buf.write("\u01d9v\3\2\2\2\u01da\u01db\7e\2\2\u01db\u01dc\7q\2\2")
        buf.write("\u01dc\u01dd\7p\2\2\u01dd\u01de\7u\2\2\u01de\u01df\7v")
        buf.write("\2\2\u01df\u01e0\7c\2\2\u01e0\u01e1\7p\2\2\u01e1\u01e2")
        buf.write("\7v\2\2\u01e2\u01e3\7g\2\2\u01e3x\3\2\2\2\u01e4\u01e5")
        buf.write("\6=\2\2\u01e5\u01f1\5\u00bd_\2\u01e6\u01e8\7\17\2\2\u01e7")
        buf.write("\u01e6\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e9\3\2\2\2")
        buf.write("\u01e9\u01ec\7\f\2\2\u01ea\u01ec\7\17\2\2\u01eb\u01e7")
        buf.write("\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec\u01ee\3\2\2\2\u01ed")
        buf.write("\u01ef\5\u00bd_\2\u01ee\u01ed\3\2\2\2\u01ee\u01ef\3\2")
        buf.write("\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01e4\3\2\2\2\u01f0\u01eb")
        buf.write("\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\b=\b\2\u01f3")
        buf.write("z\3\2\2\2\u01f4\u01f8\5\u00c3b\2\u01f5\u01f7\5\u00c5c")
        buf.write("\2\u01f6\u01f5\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8\u01f6")
        buf.write("\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9|\3\2\2\2\u01fa\u01f8")
        buf.write("\3\2\2\2\u01fb\u01fd\t\2\2\2\u01fc\u01fb\3\2\2\2\u01fc")
        buf.write("\u01fd\3\2\2\2\u01fd\u01ff\3\2\2\2\u01fe\u0200\t\3\2\2")
        buf.write("\u01ff\u01fe\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0203\3")
        buf.write("\2\2\2\u0201\u0204\5\u0091I\2\u0202\u0204\5\u0093J\2\u0203")
        buf.write("\u0201\3\2\2\2\u0203\u0202\3\2\2\2\u0204~\3\2\2\2\u0205")
        buf.write("\u0207\t\4\2\2\u0206\u0208\t\3\2\2\u0207\u0206\3\2\2\2")
        buf.write("\u0207\u0208\3\2\2\2\u0208\u020b\3\2\2\2\u0209\u020c\5")
        buf.write("\u00afX\2\u020a\u020c\5\u00b1Y\2\u020b\u0209\3\2\2\2\u020b")
        buf.write("\u020a\3\2\2\2\u020c\u0080\3\2\2\2\u020d\u0211\5\u009b")
        buf.write("N\2\u020e\u0210\5\u009dO\2\u020f\u020e\3\2\2\2\u0210\u0213")
        buf.write("\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212")
        buf.write("\u021a\3\2\2\2\u0213\u0211\3\2\2\2\u0214\u0216\7\62\2")
        buf.write("\2\u0215\u0214\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u0215")
        buf.write("\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u021a\3\2\2\2\u0219")
        buf.write("\u020d\3\2\2\2\u0219\u0215\3\2\2\2\u021a\u0082\3\2\2\2")
        buf.write("\u021b\u021c\7\62\2\2\u021c\u021e\t\5\2\2\u021d\u021f")
        buf.write("\5\u009fP\2\u021e\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220")
        buf.write("\u021e\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u0084\3\2\2\2")
        buf.write("\u0222\u0223\7\62\2\2\u0223\u0225\t\6\2\2\u0224\u0226")
        buf.write("\5\u00a1Q\2\u0225\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227")
        buf.write("\u0225\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u0086\3\2\2\2")
        buf.write("\u0229\u022a\7\62\2\2\u022a\u022c\t\4\2\2\u022b\u022d")
        buf.write("\5\u00a3R\2\u022c\u022b\3\2\2\2\u022d\u022e\3\2\2\2\u022e")
        buf.write("\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0088\3\2\2\2")
        buf.write("\u0230\u0233\5\u00a5S\2\u0231\u0233\5\u00a7T\2\u0232\u0230")
        buf.write("\3\2\2\2\u0232\u0231\3\2\2\2\u0233\u008a\3\2\2\2\u0234")
        buf.write("\u0237\5\u0089E\2\u0235\u0237\5\u00a9U\2\u0236\u0234\3")
        buf.write("\2\2\2\u0236\u0235\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u0239")
        buf.write("\t\7\2\2\u0239\u008c\3\2\2\2\u023a\u023e\5\u00bd_\2\u023b")
        buf.write("\u023e\5\u00bf`\2\u023c\u023e\5\u00c1a\2\u023d\u023a\3")
        buf.write("\2\2\2\u023d\u023b\3\2\2\2\u023d\u023c\3\2\2\2\u023e\u023f")
        buf.write("\3\2\2\2\u023f\u0240\bG\t\2\u0240\u008e\3\2\2\2\u0241")
        buf.write("\u0242\13\2\2\2\u0242\u0090\3\2\2\2\u0243\u0248\7)\2\2")
        buf.write("\u0244\u0247\5\u0099M\2\u0245\u0247\n\b\2\2\u0246\u0244")
        buf.write("\3\2\2\2\u0246\u0245\3\2\2\2\u0247\u024a\3\2\2\2\u0248")
        buf.write("\u0246\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u024b\3\2\2\2")
        buf.write("\u024a\u0248\3\2\2\2\u024b\u0256\7)\2\2\u024c\u0251\7")
        buf.write("$\2\2\u024d\u0250\5\u0099M\2\u024e\u0250\n\t\2\2\u024f")
        buf.write("\u024d\3\2\2\2\u024f\u024e\3\2\2\2\u0250\u0253\3\2\2\2")
        buf.write("\u0251\u024f\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u0254\3")
        buf.write("\2\2\2\u0253\u0251\3\2\2\2\u0254\u0256\7$\2\2\u0255\u0243")
        buf.write("\3\2\2\2\u0255\u024c\3\2\2\2\u0256\u0092\3\2\2\2\u0257")
        buf.write("\u0258\7)\2\2\u0258\u0259\7)\2\2\u0259\u025a\7)\2\2\u025a")
        buf.write("\u025e\3\2\2\2\u025b\u025d\5\u0095K\2\u025c\u025b\3\2")
        buf.write("\2\2\u025d\u0260\3\2\2\2\u025e\u025f\3\2\2\2\u025e\u025c")
        buf.write("\3\2\2\2\u025f\u0261\3\2\2\2\u0260\u025e\3\2\2\2\u0261")
        buf.write("\u0262\7)\2\2\u0262\u0263\7)\2\2\u0263\u0272\7)\2\2\u0264")
        buf.write("\u0265\7$\2\2\u0265\u0266\7$\2\2\u0266\u0267\7$\2\2\u0267")
        buf.write("\u026b\3\2\2\2\u0268\u026a\5\u0095K\2\u0269\u0268\3\2")
        buf.write("\2\2\u026a\u026d\3\2\2\2\u026b\u026c\3\2\2\2\u026b\u0269")
        buf.write("\3\2\2\2\u026c\u026e\3\2\2\2\u026d\u026b\3\2\2\2\u026e")
        buf.write("\u026f\7$\2\2\u026f\u0270\7$\2\2\u0270\u0272\7$\2\2\u0271")
        buf.write("\u0257\3\2\2\2\u0271\u0264\3\2\2\2\u0272\u0094\3\2\2\2")
        buf.write("\u0273\u0276\5\u0097L\2\u0274\u0276\5\u0099M\2\u0275\u0273")
        buf.write("\3\2\2\2\u0275\u0274\3\2\2\2\u0276\u0096\3\2\2\2\u0277")
        buf.write("\u0278\n\n\2\2\u0278\u0098\3\2\2\2\u0279\u027a\7^\2\2")
        buf.write("\u027a\u027b\13\2\2\2\u027b\u009a\3\2\2\2\u027c\u027d")
        buf.write("\t\13\2\2\u027d\u009c\3\2\2\2\u027e\u027f\t\f\2\2\u027f")
        buf.write("\u009e\3\2\2\2\u0280\u0281\t\r\2\2\u0281\u00a0\3\2\2\2")
        buf.write("\u0282\u0283\t\16\2\2\u0283\u00a2\3\2\2\2\u0284\u0285")
        buf.write("\t\17\2\2\u0285\u00a4\3\2\2\2\u0286\u0288\5\u00a9U\2\u0287")
        buf.write("\u0286\3\2\2\2\u0287\u0288\3\2\2\2\u0288\u0289\3\2\2\2")
        buf.write("\u0289\u028e\5\u00abV\2\u028a\u028b\5\u00a9U\2\u028b\u028c")
        buf.write("\7\60\2\2\u028c\u028e\3\2\2\2\u028d\u0287\3\2\2\2\u028d")
        buf.write("\u028a\3\2\2\2\u028e\u00a6\3\2\2\2\u028f\u0292\5\u00a9")
        buf.write("U\2\u0290\u0292\5\u00a5S\2\u0291\u028f\3\2\2\2\u0291\u0290")
        buf.write("\3\2\2\2\u0292\u0293\3\2\2\2\u0293\u0294\5\u00adW\2\u0294")
        buf.write("\u00a8\3\2\2\2\u0295\u0297\5\u009dO\2\u0296\u0295\3\2")
        buf.write("\2\2\u0297\u0298\3\2\2\2\u0298\u0296\3\2\2\2\u0298\u0299")
        buf.write("\3\2\2\2\u0299\u00aa\3\2\2\2\u029a\u029c\7\60\2\2\u029b")
        buf.write("\u029d\5\u009dO\2\u029c\u029b\3\2\2\2\u029d\u029e\3\2")
        buf.write("\2\2\u029e\u029c\3\2\2\2\u029e\u029f\3\2\2\2\u029f\u00ac")
        buf.write("\3\2\2\2\u02a0\u02a2\t\20\2\2\u02a1\u02a3\t\21\2\2\u02a2")
        buf.write("\u02a1\3\2\2\2\u02a2\u02a3\3\2\2\2\u02a3\u02a5\3\2\2\2")
        buf.write("\u02a4\u02a6\5\u009dO\2\u02a5\u02a4\3\2\2\2\u02a6\u02a7")
        buf.write("\3\2\2\2\u02a7\u02a5\3\2\2\2\u02a7\u02a8\3\2\2\2\u02a8")
        buf.write("\u00ae\3\2\2\2\u02a9\u02ae\7)\2\2\u02aa\u02ad\5\u00b5")
        buf.write("[\2\u02ab\u02ad\5\u00bb^\2\u02ac\u02aa\3\2\2\2\u02ac\u02ab")
        buf.write("\3\2\2\2\u02ad\u02b0\3\2\2\2\u02ae\u02ac\3\2\2\2\u02ae")
        buf.write("\u02af\3\2\2\2\u02af\u02b1\3\2\2\2\u02b0\u02ae\3\2\2\2")
        buf.write("\u02b1\u02bc\7)\2\2\u02b2\u02b7\7$\2\2\u02b3\u02b6\5\u00b7")
        buf.write("\\\2\u02b4\u02b6\5\u00bb^\2\u02b5\u02b3\3\2\2\2\u02b5")
        buf.write("\u02b4\3\2\2\2\u02b6\u02b9\3\2\2\2\u02b7\u02b5\3\2\2\2")
        buf.write("\u02b7\u02b8\3\2\2\2\u02b8\u02ba\3\2\2\2\u02b9\u02b7\3")
        buf.write("\2\2\2\u02ba\u02bc\7$\2\2\u02bb\u02a9\3\2\2\2\u02bb\u02b2")
        buf.write("\3\2\2\2\u02bc\u00b0\3\2\2\2\u02bd\u02be\7)\2\2\u02be")
        buf.write("\u02bf\7)\2\2\u02bf\u02c0\7)\2\2\u02c0\u02c4\3\2\2\2\u02c1")
        buf.write("\u02c3\5\u00b3Z\2\u02c2\u02c1\3\2\2\2\u02c3\u02c6\3\2")
        buf.write("\2\2\u02c4\u02c5\3\2\2\2\u02c4\u02c2\3\2\2\2\u02c5\u02c7")
        buf.write("\3\2\2\2\u02c6\u02c4\3\2\2\2\u02c7\u02c8\7)\2\2\u02c8")
        buf.write("\u02c9\7)\2\2\u02c9\u02d8\7)\2\2\u02ca\u02cb\7$\2\2\u02cb")
        buf.write("\u02cc\7$\2\2\u02cc\u02cd\7$\2\2\u02cd\u02d1\3\2\2\2\u02ce")
        buf.write("\u02d0\5\u00b3Z\2\u02cf\u02ce\3\2\2\2\u02d0\u02d3\3\2")
        buf.write("\2\2\u02d1\u02d2\3\2\2\2\u02d1\u02cf\3\2\2\2\u02d2\u02d4")
        buf.write("\3\2\2\2\u02d3\u02d1\3\2\2\2\u02d4\u02d5\7$\2\2\u02d5")
        buf.write("\u02d6\7$\2\2\u02d6\u02d8\7$\2\2\u02d7\u02bd\3\2\2\2\u02d7")
        buf.write("\u02ca\3\2\2\2\u02d8\u00b2\3\2\2\2\u02d9\u02dc\5\u00b9")
        buf.write("]\2\u02da\u02dc\5\u00bb^\2\u02db\u02d9\3\2\2\2\u02db\u02da")
        buf.write("\3\2\2\2\u02dc\u00b4\3\2\2\2\u02dd\u02df\t\22\2\2\u02de")
        buf.write("\u02dd\3\2\2\2\u02df\u00b6\3\2\2\2\u02e0\u02e2\t\23\2")
        buf.write("\2\u02e1\u02e0\3\2\2\2\u02e2\u00b8\3\2\2\2\u02e3\u02e5")
        buf.write("\t\24\2\2\u02e4\u02e3\3\2\2\2\u02e5\u00ba\3\2\2\2\u02e6")
        buf.write("\u02e7\7^\2\2\u02e7\u02e8\t\25\2\2\u02e8\u00bc\3\2\2\2")
        buf.write("\u02e9\u02eb\t\26\2\2\u02ea\u02e9\3\2\2\2\u02eb\u02ec")
        buf.write("\3\2\2\2\u02ec\u02ea\3\2\2\2\u02ec\u02ed\3\2\2\2\u02ed")
        buf.write("\u00be\3\2\2\2\u02ee\u02f2\7%\2\2\u02ef\u02f1\n\27\2\2")
        buf.write("\u02f0\u02ef\3\2\2\2\u02f1\u02f4\3\2\2\2\u02f2\u02f0\3")
        buf.write("\2\2\2\u02f2\u02f3\3\2\2\2\u02f3\u00c0\3\2\2\2\u02f4\u02f2")
        buf.write("\3\2\2\2\u02f5\u02f7\7^\2\2\u02f6\u02f8\5\u00bd_\2\u02f7")
        buf.write("\u02f6\3\2\2\2\u02f7\u02f8\3\2\2\2\u02f8\u02fe\3\2\2\2")
        buf.write("\u02f9\u02fb\7\17\2\2\u02fa\u02f9\3\2\2\2\u02fa\u02fb")
        buf.write("\3\2\2\2\u02fb\u02fc\3\2\2\2\u02fc\u02ff\7\f\2\2\u02fd")
        buf.write("\u02ff\7\17\2\2\u02fe\u02fa\3\2\2\2\u02fe\u02fd\3\2\2")
        buf.write("\2\u02ff\u00c2\3\2\2\2\u0300\u0302\t\30\2\2\u0301\u0300")
        buf.write("\3\2\2\2\u0302\u00c4\3\2\2\2\u0303\u0306\5\u00c3b\2\u0304")
        buf.write("\u0306\t\31\2\2\u0305\u0303\3\2\2\2\u0305\u0304\3\2\2")
        buf.write("\2\u0306\u00c6\3\2\2\2>\2\u00e4\u00ff\u0140\u014e\u01d8")
        buf.write("\u01e7\u01eb\u01ee\u01f0\u01f8\u01fc\u01ff\u0203\u0207")
        buf.write("\u020b\u0211\u0217\u0219\u0220\u0227\u022e\u0232\u0236")
        buf.write("\u023d\u0246\u0248\u024f\u0251\u0255\u025e\u026b\u0271")
        buf.write("\u0275\u0287\u028d\u0291\u0298\u029e\u02a2\u02a7\u02ac")
        buf.write("\u02ae\u02b5\u02b7\u02bb\u02c4\u02d1\u02d7\u02db\u02de")
        buf.write("\u02e1\u02e4\u02ec\u02f2\u02f7\u02fa\u02fe\u0301\u0305")
        buf.write("\n\3\26\2\3\27\3\3\35\4\3\36\5\3+\6\3,\7\3=\b\b\2\2")
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
    DOT = 19
    CARDINALITY_OP = 20
    OPEN_PAREN = 21
    CLOSE_PAREN = 22
    COMMA = 23
    COLON = 24
    SEMI_COLON = 25
    POWER = 26
    ASSIGN = 27
    OPEN_BRACK = 28
    CLOSE_BRACK = 29
    OR_OP = 30
    XOR = 31
    AND_OP = 32
    LEFT_SHIFT = 33
    RIGHT_SHIFT = 34
    ADD = 35
    MINUS = 36
    STAR = 37
    DIV = 38
    MOD = 39
    IDIV = 40
    NOT_OP = 41
    OPEN_BRACE = 42
    CLOSE_BRACE = 43
    LESS_THAN = 44
    GREATER_THAN = 45
    EQUALS = 46
    GT_EQ = 47
    LT_EQ = 48
    NOT_EQ = 49
    AT = 50
    ARROW = 51
    VAL = 52
    REF = 53
    INTEGER = 54
    REAL = 55
    CHAR = 56
    STRING = 57
    BOOLEAN = 58
    CONSTANT = 59
    NEWLINE = 60
    NAME = 61
    STRING_LITERAL = 62
    BYTES_LITERAL = 63
    DECIMAL_INTEGER = 64
    OCT_INTEGER = 65
    HEX_INTEGER = 66
    BIN_INTEGER = 67
    FLOAT_NUMBER = 68
    IMAG_NUMBER = 69
    SKIP_ = 70
    UNKNOWN_CHAR = 71

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'retornar'", "'usando'", "'se'", "'enquanto'", "'para'", "'ou'", 
            "'e'", "'nulo'", "'verdadeiro'", "'falso'", "'tipo'", "'continuar'", 
            "'parar'", "'passo'", "'.'", "'|'", "'('", "')'", "','", "':'", 
            "';'", "'^'", "'<-'", "'['", "']'", "'||'", "'xor'", "'&&'", 
            "'<<'", "'>>'", "'+'", "'-'", "'*'", "'/'", "'mod'", "'div'", 
            "'~'", "'{'", "'}'", "'<'", "'>'", "'='", "'>='", "'<='", "'~='", 
            "'@'", "'->'", "'val'", "'ref'", "'inteiro'", "'real'", "'caracter'", 
            "'cadeia'", "'constante'" ]

    symbolicNames = [ "<INVALID>",
            "RETURN", "IMPORT", "IF", "ELSE", "WHILE", "FOR", "OR", "AND", 
            "NOT", "NULL", "TRUE", "FALSE", "CLASS", "CONTINUE", "BREAK", 
            "ENUM", "STEP", "UNTIL", "DOT", "CARDINALITY_OP", "OPEN_PAREN", 
            "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", "POWER", "ASSIGN", 
            "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", "XOR", "AND_OP", "LEFT_SHIFT", 
            "RIGHT_SHIFT", "ADD", "MINUS", "STAR", "DIV", "MOD", "IDIV", 
            "NOT_OP", "OPEN_BRACE", "CLOSE_BRACE", "LESS_THAN", "GREATER_THAN", 
            "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ", "AT", "ARROW", "VAL", 
            "REF", "INTEGER", "REAL", "CHAR", "STRING", "BOOLEAN", "CONSTANT", 
            "NEWLINE", "NAME", "STRING_LITERAL", "BYTES_LITERAL", "DECIMAL_INTEGER", 
            "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", 
            "IMAG_NUMBER", "SKIP_", "UNKNOWN_CHAR" ]

    ruleNames = [ "RETURN", "IMPORT", "IF", "ELSE", "WHILE", "FOR", "OR", 
                  "AND", "NOT", "NULL", "TRUE", "FALSE", "CLASS", "CONTINUE", 
                  "BREAK", "ENUM", "STEP", "UNTIL", "DOT", "CARDINALITY_OP", 
                  "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", 
                  "POWER", "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", 
                  "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", 
                  "STAR", "DIV", "MOD", "IDIV", "NOT_OP", "OPEN_BRACE", 
                  "CLOSE_BRACE", "LESS_THAN", "GREATER_THAN", "EQUALS", 
                  "GT_EQ", "LT_EQ", "NOT_EQ", "AT", "ARROW", "VAL", "REF", 
                  "INTEGER", "REAL", "CHAR", "STRING", "BOOLEAN", "CONSTANT", 
                  "NEWLINE", "NAME", "STRING_LITERAL", "BYTES_LITERAL", 
                  "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", 
                  "FLOAT_NUMBER", "IMAG_NUMBER", "SKIP_", "UNKNOWN_CHAR", 
                  "SHORT_STRING", "LONG_STRING", "LONG_STRING_ITEM", "LONG_STRING_CHAR", 
                  "STRING_ESCAPE_SEQ", "NON_ZERO_DIGIT", "DIGIT", "OCT_DIGIT", 
                  "HEX_DIGIT", "BIN_DIGIT", "POINT_FLOAT", "EXPONENT_FLOAT", 
                  "INT_PART", "FRACTION", "EXPONENT", "SHORT_BYTES", "LONG_BYTES", 
                  "LONG_BYTES_ITEM", "SHORT_BYTES_CHAR_NO_SINGLE_QUOTE", 
                  "SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE", "LONG_BYTES_CHAR", 
                  "BYTES_ESCAPE_SEQ", "SPACES", "COMMENT", "LINE_JOINING", 
                  "ID_START", "ID_CONTINUE" ]

    grammarFileName = "lang.g4"

    def __init__(self, myInput=None, output:TextIO = sys.stdout):
        super().__init__(myInput, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self._input = myInput



    #Uma fila para tokens adicionais (ver a regra NEWLINE do lexer)
    tokens = []

    #A pilha para controlar o nível de indentação
    indents = []

    #O número de colchetes e parênteses abertos
    opened = 0

    #A token produzida mais recente.
    lastToken = None

    def emitToken(self, t):
        self._token = t
        self.tokens.append(t)

    def nextToken(self):
        # Checar se atingimos o final do arquivo e faltam DEDENTS a serem emitidos
        if self._input.LA(1) == Token.EOF and len(self.indents)>0:

          # Remove tokens EOF por enquanto
          for i in range(tokens.size() - 1, 0, -1):
            if (tokens.get(i).getType() == EOF):
              tokens.remove(i)

          # Emite uma token de quebra de linha, que termina a declaração atual
          self.emitToken(commonToken(langParser.NEWLINE, "\n"))

          # Emite quantos DEDENTS necessários 
          while (not indents.isEmpty()):
            self.emitToken(createDedent())
            indents.pop()

          # Coloca o EOF de volta
          self.emitToken(commonToken(langParser.EOF, "<EOF>"));

        nextTok = super().nextToken()

        if (nextTok.channel == Token.DEFAULT_CHANNEL):
          # Atualizar a última token produzida caso tenha sido emitida para o canal padrão
          self.lastToken = nextTok;

        if len(self.tokens) == 0:
          return nextTok
        return self.tokens.pop(0)

    def createDedent(self):
      dedent = commonToken(langParser.DEDENT, "")
      dedent.setLine(self.lastToken.getLine())
      return dedent

    def commonToken(self, mytype, text):
      stop = self.getCharIndex() - 1
      start = stop if len(text)==0 else (stop - len(text) + 1)
      return CommonToken(self._tokenFactorySourcePair, mytype, super().DEFAULT_TOKEN_CHANNEL, start, stop)

    '''
    // Calcula a indentação correspondente aos espaços dados, levando as
    // seguintes regras em consideração:
    //
    // "Tabs are replaced (from left to right) by one to eight spaces
    //  such that the total number of characters up to and including
    //  the replacement is a multiple of eight [...]"
    //
    //  -- https://docs.python.org/3.1/reference/lexical_analysis.html#indentation
    '''

    def getIndentationCount(self, spaces):
      count = 0

      for ch in spaces:
        if (ch == '\t'): #Tab
          count += 8 - (count % 8)
        else:             #Um espaço comum.
          count += 1

      return count

    def atStartOfInput(self):
      return super().column == 0 and super().line == 1

    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
    	if self._actions is None:
    		actions = dict()
    		actions[20] = self.OPEN_PAREN_action 
    		actions[21] = self.CLOSE_PAREN_action 
    		actions[27] = self.OPEN_BRACK_action 
    		actions[28] = self.CLOSE_BRACK_action 
    		actions[41] = self.OPEN_BRACE_action 
    		actions[42] = self.CLOSE_BRACE_action 
    		actions[59] = self.NEWLINE_action 
    		self._actions = actions
    	action = self._actions.get(ruleIndex, None)
    	if action is not None:
    		action(localctx, actionIndex)
    	else:
    		raise Exception("No registered action for:" + str(ruleIndex))

    def OPEN_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            opened+=1
     

    def CLOSE_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            opened-=1
     

    def OPEN_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            opened+=1
     

    def CLOSE_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            opened-=1
     

    def OPEN_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            opened+=1
     

    def CLOSE_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            opened-=1
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
          newLine = re.sub(r"[^\r\n]+", "", self.text)
          spaces = re.sub(r"[\r\n]+", "", self.text)
          nextTok = self._input.LA(1)

          if (self.opened > 0 or nextTok == '\r' or nextTok == '\n' or nextTok == '#'):
            # If we're inside a list or on a blank line, ignore all indents, 
            # dedents and line breaks.
            self.skip();
          else:
            self.emitToken(self.commonToken(langParser.NEWLINE, newLine))

            indent = self.getIndentationCount(spaces)
            previous = 0 if len(self.indents)==0 else self.indents[0]

            if (indent == previous):
              # skip indents of the same size as the present indent-size
              self.skip()
            elif (indent > previous):
              indents.push(indent)
              emitToken(commonToken(langParser.INDENT, spaces))
            else:
              # Possibly emit more than 1 DEDENT token.
              while(len(indents)>0 and indents[0] > indent):
                emitToken(createDedent())
                indents.pop()

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[59] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


