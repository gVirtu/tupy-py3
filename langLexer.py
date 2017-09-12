# Generated from lang.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


import re
from Stack import Stack
from langParser import langParser
from antlr4.Token import CommonToken


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2K")
        buf.write("\u02be\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("^\t^\4_\t_\4`\t`\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00df\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00fa\n\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u013b\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0149\n\23")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3,\3,\3,\3-\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3")
        buf.write("\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\3")
        buf.write("8\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3")
        buf.write(";\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\5<\u01d6")
        buf.write("\n<\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3?\3?\3")
        buf.write("?\5?\u01e9\n?\3?\3?\5?\u01ed\n?\3?\5?\u01f0\n?\5?\u01f2")
        buf.write("\n?\3?\3?\3@\3@\7@\u01f8\n@\f@\16@\u01fb\13@\3A\3A\3A")
        buf.write("\3B\3B\3B\5B\u0203\nB\3B\3B\3B\3C\3C\7C\u020a\nC\fC\16")
        buf.write("C\u020d\13C\3C\6C\u0210\nC\rC\16C\u0211\5C\u0214\nC\3")
        buf.write("D\3D\3D\6D\u0219\nD\rD\16D\u021a\3E\3E\3E\6E\u0220\nE")
        buf.write("\rE\16E\u0221\3F\3F\3F\6F\u0227\nF\rF\16F\u0228\3G\3G")
        buf.write("\3H\3H\5H\u022f\nH\3H\3H\3I\3I\3I\5I\u0236\nI\3I\3I\3")
        buf.write("J\3J\3K\3K\3K\7K\u023f\nK\fK\16K\u0242\13K\3K\3K\3L\3")
        buf.write("L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3R\3S\6S\u0257")
        buf.write("\nS\rS\16S\u0258\3T\3T\6T\u025d\nT\rT\16T\u025e\3U\3U")
        buf.write("\3U\7U\u0264\nU\fU\16U\u0267\13U\3U\3U\3U\3U\7U\u026d")
        buf.write("\nU\fU\16U\u0270\13U\3U\5U\u0273\nU\3V\3V\3V\3V\3V\7V")
        buf.write("\u027a\nV\fV\16V\u027d\13V\3V\3V\3V\3V\3V\3V\3V\3V\7V")
        buf.write("\u0287\nV\fV\16V\u028a\13V\3V\3V\3V\5V\u028f\nV\3W\3W")
        buf.write("\5W\u0293\nW\3X\5X\u0296\nX\3Y\5Y\u0299\nY\3Z\5Z\u029c")
        buf.write("\nZ\3[\3[\3[\3\\\6\\\u02a2\n\\\r\\\16\\\u02a3\3]\3]\7")
        buf.write("]\u02a8\n]\f]\16]\u02ab\13]\3^\3^\5^\u02af\n^\3^\5^\u02b2")
        buf.write("\n^\3^\3^\5^\u02b6\n^\3_\5_\u02b9\n_\3`\3`\5`\u02bd\n")
        buf.write("`\4\u027b\u0288\2a\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g")
        buf.write("\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085")
        buf.write("D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091J\u0093K\u0095")
        buf.write("\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3")
        buf.write("\2\u00a5\2\u00a7\2\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1")
        buf.write("\2\u00b3\2\u00b5\2\u00b7\2\u00b9\2\u00bb\2\u00bd\2\u00bf")
        buf.write("\2\3\2\24\6\2\f\f\17\17$$^^\4\2QQqq\4\2ZZzz\4\2DDdd\4")
        buf.write("\2LLll\3\2\63;\3\2\62;\3\2\629\5\2\62;CHch\3\2\62\63\7")
        buf.write("\2\2\13\r\16\20(*]_\u0081\7\2\2\13\r\16\20#%]_\u0081\4")
        buf.write("\2\2]_\u0081\3\2\2\u0081\4\2\13\13\"\"\4\2\f\f\17\17\u0129")
        buf.write("\2C\\aac|\u00ac\u00ac\u00b7\u00b7\u00bc\u00bc\u00c2\u00d8")
        buf.write("\u00da\u00f8\u00fa\u0243\u0252\u02c3\u02c8\u02d3\u02e2")
        buf.write("\u02e6\u02f0\u02f0\u037c\u037c\u0388\u0388\u038a\u038c")
        buf.write("\u038e\u038e\u0390\u03a3\u03a5\u03d0\u03d2\u03f7\u03f9")
        buf.write("\u0483\u048c\u04d0\u04d2\u04fb\u0502\u0511\u0533\u0558")
        buf.write("\u055b\u055b\u0563\u0589\u05d2\u05ec\u05f2\u05f4\u0623")
        buf.write("\u063c\u0642\u064c\u0670\u0671\u0673\u06d5\u06d7\u06d7")
        buf.write("\u06e7\u06e8\u06f0\u06f1\u06fc\u06fe\u0701\u0701\u0712")
        buf.write("\u0712\u0714\u0731\u074f\u076f\u0782\u07a7\u07b3\u07b3")
        buf.write("\u0906\u093b\u093f\u093f\u0952\u0952\u095a\u0963\u097f")
        buf.write("\u097f\u0987\u098e\u0991\u0992\u0995\u09aa\u09ac\u09b2")
        buf.write("\u09b4\u09b4\u09b8\u09bb\u09bf\u09bf\u09d0\u09d0\u09de")
        buf.write("\u09df\u09e1\u09e3\u09f2\u09f3\u0a07\u0a0c\u0a11\u0a12")
        buf.write("\u0a15\u0a2a\u0a2c\u0a32\u0a34\u0a35\u0a37\u0a38\u0a3a")
        buf.write("\u0a3b\u0a5b\u0a5e\u0a60\u0a60\u0a74\u0a76\u0a87\u0a8f")
        buf.write("\u0a91\u0a93\u0a95\u0aaa\u0aac\u0ab2\u0ab4\u0ab5\u0ab7")
        buf.write("\u0abb\u0abf\u0abf\u0ad2\u0ad2\u0ae2\u0ae3\u0b07\u0b0e")
        buf.write("\u0b11\u0b12\u0b15\u0b2a\u0b2c\u0b32\u0b34\u0b35\u0b37")
        buf.write("\u0b3b\u0b3f\u0b3f\u0b5e\u0b5f\u0b61\u0b63\u0b73\u0b73")
        buf.write("\u0b85\u0b85\u0b87\u0b8c\u0b90\u0b92\u0b94\u0b97\u0b9b")
        buf.write("\u0b9c\u0b9e\u0b9e\u0ba0\u0ba1\u0ba5\u0ba6\u0baa\u0bac")
        buf.write("\u0bb0\u0bbb\u0c07\u0c0e\u0c10\u0c12\u0c14\u0c2a\u0c2c")
        buf.write("\u0c35\u0c37\u0c3b\u0c62\u0c63\u0c87\u0c8e\u0c90\u0c92")
        buf.write("\u0c94\u0caa\u0cac\u0cb5\u0cb7\u0cbb\u0cbf\u0cbf\u0ce0")
        buf.write("\u0ce0\u0ce2\u0ce3\u0d07\u0d0e\u0d10\u0d12\u0d14\u0d2a")
        buf.write("\u0d2c\u0d3b\u0d62\u0d63\u0d87\u0d98\u0d9c\u0db3\u0db5")
        buf.write("\u0dbd\u0dbf\u0dbf\u0dc2\u0dc8\u0e03\u0e32\u0e34\u0e35")
        buf.write("\u0e42\u0e48\u0e83\u0e84\u0e86\u0e86\u0e89\u0e8a\u0e8c")
        buf.write("\u0e8c\u0e8f\u0e8f\u0e96\u0e99\u0e9b\u0ea1\u0ea3\u0ea5")
        buf.write("\u0ea7\u0ea7\u0ea9\u0ea9\u0eac\u0ead\u0eaf\u0eb2\u0eb4")
        buf.write("\u0eb5\u0ebf\u0ebf\u0ec2\u0ec6\u0ec8\u0ec8\u0ede\u0edf")
        buf.write("\u0f02\u0f02\u0f42\u0f49\u0f4b\u0f6c\u0f8a\u0f8d\u1002")
        buf.write("\u1023\u1025\u1029\u102b\u102c\u1052\u1057\u10a2\u10c7")
        buf.write("\u10d2\u10fc\u10fe\u10fe\u1102\u115b\u1161\u11a4\u11aa")
        buf.write("\u11fb\u1202\u124a\u124c\u124f\u1252\u1258\u125a\u125a")
        buf.write("\u125c\u125f\u1262\u128a\u128c\u128f\u1292\u12b2\u12b4")
        buf.write("\u12b7\u12ba\u12c0\u12c2\u12c2\u12c4\u12c7\u12ca\u12d8")
        buf.write("\u12da\u1312\u1314\u1317\u131a\u135c\u1382\u1391\u13a2")
        buf.write("\u13f6\u1403\u166e\u1671\u1678\u1683\u169c\u16a2\u16ec")
        buf.write("\u16f0\u16f2\u1702\u170e\u1710\u1713\u1722\u1733\u1742")
        buf.write("\u1753\u1762\u176e\u1770\u1772\u1782\u17b5\u17d9\u17d9")
        buf.write("\u17de\u17de\u1822\u1879\u1882\u18aa\u1902\u191e\u1952")
        buf.write("\u196f\u1972\u1976\u1982\u19ab\u19c3\u19c9\u1a02\u1a18")
        buf.write("\u1d02\u1dc1\u1e02\u1e9d\u1ea2\u1efb\u1f02\u1f17\u1f1a")
        buf.write("\u1f1f\u1f22\u1f47\u1f4a\u1f4f\u1f52\u1f59\u1f5b\u1f5b")
        buf.write("\u1f5d\u1f5d\u1f5f\u1f5f\u1f61\u1f7f\u1f82\u1fb6\u1fb8")
        buf.write("\u1fbe\u1fc0\u1fc0\u1fc4\u1fc6\u1fc8\u1fce\u1fd2\u1fd5")
        buf.write("\u1fd8\u1fdd\u1fe2\u1fee\u1ff4\u1ff6\u1ff8\u1ffe\u2073")
        buf.write("\u2073\u2081\u2081\u2092\u2096\u2104\u2104\u2109\u2109")
        buf.write("\u210c\u2115\u2117\u2117\u211a\u211f\u2126\u2126\u2128")
        buf.write("\u2128\u212a\u212a\u212c\u2133\u2135\u213b\u213e\u2141")
        buf.write("\u2147\u214b\u2162\u2185\u2c02\u2c30\u2c32\u2c60\u2c82")
        buf.write("\u2ce6\u2d02\u2d27\u2d32\u2d67\u2d71\u2d71\u2d82\u2d98")
        buf.write("\u2da2\u2da8\u2daa\u2db0\u2db2\u2db8\u2dba\u2dc0\u2dc2")
        buf.write("\u2dc8\u2dca\u2dd0\u2dd2\u2dd8\u2dda\u2de0\u3007\u3009")
        buf.write("\u3023\u302b\u3033\u3037\u303a\u303e\u3043\u3098\u309d")
        buf.write("\u30a1\u30a3\u30fc\u30fe\u3101\u3107\u312e\u3133\u3190")
        buf.write("\u31a2\u31b9\u31f2\u3201\u3402\u4db7\u4e02\u9fbd\ua002")
        buf.write("\ua48e\ua802\ua803\ua805\ua807\ua809\ua80c\ua80e\ua824")
        buf.write("\uac02\ud7a5\uf902\ufa2f\ufa32\ufa6c\ufa72\ufadb\ufb02")
        buf.write("\ufb08\ufb15\ufb19\ufb1f\ufb1f\ufb21\ufb2a\ufb2c\ufb38")
        buf.write("\ufb3a\ufb3e\ufb40\ufb40\ufb42\ufb43\ufb45\ufb46\ufb48")
        buf.write("\ufbb3\ufbd5\ufd3f\ufd52\ufd91\ufd94\ufdc9\ufdf2\ufdfd")
        buf.write("\ufe72\ufe76\ufe78\ufefe\uff23\uff3c\uff43\uff5c\uff68")
        buf.write("\uffc0\uffc4\uffc9\uffcc\uffd1\uffd4\uffd9\uffdc\uffde")
        buf.write("\u0096\2\62;\u0302\u0371\u0485\u0488\u0593\u05bb\u05bd")
        buf.write("\u05bf\u05c1\u05c1\u05c3\u05c4\u05c6\u05c7\u05c9\u05c9")
        buf.write("\u0612\u0617\u064d\u0660\u0662\u066b\u0672\u0672\u06d8")
        buf.write("\u06de\u06e1\u06e6\u06e9\u06ea\u06ec\u06ef\u06f2\u06fb")
        buf.write("\u0713\u0713\u0732\u074c\u07a8\u07b2\u0903\u0905\u093e")
        buf.write("\u093e\u0940\u094f\u0953\u0956\u0964\u0965\u0968\u0971")
        buf.write("\u0983\u0985\u09be\u09be\u09c0\u09c6\u09c9\u09ca\u09cd")
        buf.write("\u09cf\u09d9\u09d9\u09e4\u09e5\u09e8\u09f1\u0a03\u0a05")
        buf.write("\u0a3e\u0a3e\u0a40\u0a44\u0a49\u0a4a\u0a4d\u0a4f\u0a68")
        buf.write("\u0a73\u0a83\u0a85\u0abe\u0abe\u0ac0\u0ac7\u0ac9\u0acb")
        buf.write("\u0acd\u0acf\u0ae4\u0ae5\u0ae8\u0af1\u0b03\u0b05\u0b3e")
        buf.write("\u0b3e\u0b40\u0b45\u0b49\u0b4a\u0b4d\u0b4f\u0b58\u0b59")
        buf.write("\u0b68\u0b71\u0b84\u0b84\u0bc0\u0bc4\u0bc8\u0bca\u0bcc")
        buf.write("\u0bcf\u0bd9\u0bd9\u0be8\u0bf1\u0c03\u0c05\u0c40\u0c46")
        buf.write("\u0c48\u0c4a\u0c4c\u0c4f\u0c57\u0c58\u0c68\u0c71\u0c84")
        buf.write("\u0c85\u0cbe\u0cbe\u0cc0\u0cc6\u0cc8\u0cca\u0ccc\u0ccf")
        buf.write("\u0cd7\u0cd8\u0ce8\u0cf1\u0d04\u0d05\u0d40\u0d45\u0d48")
        buf.write("\u0d4a\u0d4c\u0d4f\u0d59\u0d59\u0d68\u0d71\u0d84\u0d85")
        buf.write("\u0dcc\u0dcc\u0dd1\u0dd6\u0dd8\u0dd8\u0dda\u0de1\u0df4")
        buf.write("\u0df5\u0e33\u0e33\u0e36\u0e3c\u0e49\u0e50\u0e52\u0e5b")
        buf.write("\u0eb3\u0eb3\u0eb6\u0ebb\u0ebd\u0ebe\u0eca\u0ecf\u0ed2")
        buf.write("\u0edb\u0f1a\u0f1b\u0f22\u0f2b\u0f37\u0f37\u0f39\u0f39")
        buf.write("\u0f3b\u0f3b\u0f40\u0f41\u0f73\u0f86\u0f88\u0f89\u0f92")
        buf.write("\u0f99\u0f9b\u0fbe\u0fc8\u0fc8\u102e\u1034\u1038\u103b")
        buf.write("\u1042\u104b\u1058\u105b\u1361\u1361\u136b\u1373\u1714")
        buf.write("\u1716\u1734\u1736\u1754\u1755\u1774\u1775\u17b8\u17d5")
        buf.write("\u17df\u17df\u17e2\u17eb\u180d\u180f\u1812\u181b\u18ab")
        buf.write("\u18ab\u1922\u192d\u1932\u193d\u1948\u1951\u19b2\u19c2")
        buf.write("\u19ca\u19cb\u19d2\u19db\u1a19\u1a1d\u1dc2\u1dc5\u2041")
        buf.write("\u2042\u2056\u2056\u20d2\u20de\u20e3\u20e3\u20e7\u20ed")
        buf.write("\u302c\u3031\u309b\u309c\ua804\ua804\ua808\ua808\ua80d")
        buf.write("\ua80d\ua825\ua829\ufb20\ufb20\ufe02\ufe11\ufe22\ufe25")
        buf.write("\ufe35\ufe36\ufe4f\ufe51\uff12\uff1b\uff41\uff41\2\u02ce")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
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
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\3\u00c1\3\2\2\2\5\u00ca\3\2\2")
        buf.write("\2\7\u00d1\3\2\2\2\t\u00de\3\2\2\2\13\u00e0\3\2\2\2\r")
        buf.write("\u00e9\3\2\2\2\17\u00ee\3\2\2\2\21\u00f1\3\2\2\2\23\u00f9")
        buf.write("\3\2\2\2\25\u00fb\3\2\2\2\27\u0100\3\2\2\2\31\u010b\3")
        buf.write("\2\2\2\33\u0111\3\2\2\2\35\u0116\3\2\2\2\37\u0120\3\2")
        buf.write("\2\2!\u013a\3\2\2\2#\u013c\3\2\2\2%\u0148\3\2\2\2\'\u014a")
        buf.write("\3\2\2\2)\u014c\3\2\2\2+\u014f\3\2\2\2-\u0151\3\2\2\2")
        buf.write("/\u0154\3\2\2\2\61\u0157\3\2\2\2\63\u0159\3\2\2\2\65\u015b")
        buf.write("\3\2\2\2\67\u015d\3\2\2\29\u015f\3\2\2\2;\u0162\3\2\2")
        buf.write("\2=\u0165\3\2\2\2?\u0168\3\2\2\2A\u016b\3\2\2\2C\u016f")
        buf.write("\3\2\2\2E\u0172\3\2\2\2G\u0175\3\2\2\2I\u0178\3\2\2\2")
        buf.write("K\u017a\3\2\2\2M\u017c\3\2\2\2O\u017e\3\2\2\2Q\u0180\3")
        buf.write("\2\2\2S\u0184\3\2\2\2U\u0188\3\2\2\2W\u018a\3\2\2\2Y\u018d")
        buf.write("\3\2\2\2[\u0190\3\2\2\2]\u0192\3\2\2\2_\u0194\3\2\2\2")
        buf.write("a\u0196\3\2\2\2c\u0199\3\2\2\2e\u019c\3\2\2\2g\u019f\3")
        buf.write("\2\2\2i\u01a1\3\2\2\2k\u01a4\3\2\2\2m\u01a8\3\2\2\2o\u01ac")
        buf.write("\3\2\2\2q\u01b4\3\2\2\2s\u01b9\3\2\2\2u\u01c2\3\2\2\2")
        buf.write("w\u01d5\3\2\2\2y\u01d7\3\2\2\2{\u01db\3\2\2\2}\u01f1\3")
        buf.write("\2\2\2\177\u01f5\3\2\2\2\u0081\u01fc\3\2\2\2\u0083\u01ff")
        buf.write("\3\2\2\2\u0085\u0213\3\2\2\2\u0087\u0215\3\2\2\2\u0089")
        buf.write("\u021c\3\2\2\2\u008b\u0223\3\2\2\2\u008d\u022a\3\2\2\2")
        buf.write("\u008f\u022e\3\2\2\2\u0091\u0235\3\2\2\2\u0093\u0239\3")
        buf.write("\2\2\2\u0095\u023b\3\2\2\2\u0097\u0245\3\2\2\2\u0099\u0248")
        buf.write("\3\2\2\2\u009b\u024a\3\2\2\2\u009d\u024c\3\2\2\2\u009f")
        buf.write("\u024e\3\2\2\2\u00a1\u0250\3\2\2\2\u00a3\u0252\3\2\2\2")
        buf.write("\u00a5\u0256\3\2\2\2\u00a7\u025a\3\2\2\2\u00a9\u0272\3")
        buf.write("\2\2\2\u00ab\u028e\3\2\2\2\u00ad\u0292\3\2\2\2\u00af\u0295")
        buf.write("\3\2\2\2\u00b1\u0298\3\2\2\2\u00b3\u029b\3\2\2\2\u00b5")
        buf.write("\u029d\3\2\2\2\u00b7\u02a1\3\2\2\2\u00b9\u02a5\3\2\2\2")
        buf.write("\u00bb\u02ac\3\2\2\2\u00bd\u02b8\3\2\2\2\u00bf\u02bc\3")
        buf.write("\2\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4")
        buf.write("\7v\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7t\2\2\u00c9\4")
        buf.write("\3\2\2\2\u00ca\u00cb\7w\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd")
        buf.write("\7c\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7f\2\2\u00cf\u00d0")
        buf.write("\7q\2\2\u00d0\6\3\2\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3")
        buf.write("\7g\2\2\u00d3\b\3\2\2\2\u00d4\u00d5\7u\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7\u00e5\2\2\u00d8")
        buf.write("\u00df\7q\2\2\u00d9\u00da\7u\2\2\u00da\u00db\7g\2\2\u00db")
        buf.write("\u00dc\7p\2\2\u00dc\u00dd\7c\2\2\u00dd\u00df\7q\2\2\u00de")
        buf.write("\u00d4\3\2\2\2\u00de\u00d9\3\2\2\2\u00df\n\3\2\2\2\u00e0")
        buf.write("\u00e1\7g\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7s\2\2\u00e3")
        buf.write("\u00e4\7w\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7p\2\2\u00e6")
        buf.write("\u00e7\7v\2\2\u00e7\u00e8\7q\2\2\u00e8\f\3\2\2\2\u00e9")
        buf.write("\u00ea\7r\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7t\2\2\u00ec")
        buf.write("\u00ed\7c\2\2\u00ed\16\3\2\2\2\u00ee\u00ef\7q\2\2\u00ef")
        buf.write("\u00f0\7w\2\2\u00f0\20\3\2\2\2\u00f1\u00f2\7g\2\2\u00f2")
        buf.write("\22\3\2\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7\u00e5\2\2")
        buf.write("\u00f5\u00fa\7q\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8\7c")
        buf.write("\2\2\u00f8\u00fa\7q\2\2\u00f9\u00f3\3\2\2\2\u00f9\u00f6")
        buf.write("\3\2\2\2\u00fa\24\3\2\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd")
        buf.write("\7w\2\2\u00fd\u00fe\7n\2\2\u00fe\u00ff\7q\2\2\u00ff\26")
        buf.write("\3\2\2\2\u0100\u0101\7x\2\2\u0101\u0102\7g\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7f\2\2\u0104\u0105\7c\2\2\u0105\u0106")
        buf.write("\7f\2\2\u0106\u0107\7g\2\2\u0107\u0108\7k\2\2\u0108\u0109")
        buf.write("\7t\2\2\u0109\u010a\7q\2\2\u010a\30\3\2\2\2\u010b\u010c")
        buf.write("\7h\2\2\u010c\u010d\7c\2\2\u010d\u010e\7n\2\2\u010e\u010f")
        buf.write("\7u\2\2\u010f\u0110\7q\2\2\u0110\32\3\2\2\2\u0111\u0112")
        buf.write("\7v\2\2\u0112\u0113\7k\2\2\u0113\u0114\7r\2\2\u0114\u0115")
        buf.write("\7q\2\2\u0115\34\3\2\2\2\u0116\u0117\7e\2\2\u0117\u0118")
        buf.write("\7q\2\2\u0118\u0119\7p\2\2\u0119\u011a\7v\2\2\u011a\u011b")
        buf.write("\7k\2\2\u011b\u011c\7p\2\2\u011c\u011d\7w\2\2\u011d\u011e")
        buf.write("\7c\2\2\u011e\u011f\7t\2\2\u011f\36\3\2\2\2\u0120\u0121")
        buf.write("\7r\2\2\u0121\u0122\7c\2\2\u0122\u0123\7t\2\2\u0123\u0124")
        buf.write("\7c\2\2\u0124\u0125\7t\2\2\u0125 \3\2\2\2\u0126\u0127")
        buf.write("\7g\2\2\u0127\u0128\7p\2\2\u0128\u0129\7w\2\2\u0129\u012a")
        buf.write("\7o\2\2\u012a\u012b\7g\2\2\u012b\u012c\7t\2\2\u012c\u012d")
        buf.write("\7c\2\2\u012d\u012e\7\u00e9\2\2\u012e\u012f\7\u00e5\2")
        buf.write("\2\u012f\u013b\7q\2\2\u0130\u0131\7g\2\2\u0131\u0132\7")
        buf.write("p\2\2\u0132\u0133\7w\2\2\u0133\u0134\7o\2\2\u0134\u0135")
        buf.write("\7g\2\2\u0135\u0136\7t\2\2\u0136\u0137\7c\2\2\u0137\u0138")
        buf.write("\7e\2\2\u0138\u0139\7c\2\2\u0139\u013b\7q\2\2\u013a\u0126")
        buf.write("\3\2\2\2\u013a\u0130\3\2\2\2\u013b\"\3\2\2\2\u013c\u013d")
        buf.write("\7r\2\2\u013d\u013e\7c\2\2\u013e\u013f\7u\2\2\u013f\u0140")
        buf.write("\7u\2\2\u0140\u0141\7q\2\2\u0141$\3\2\2\2\u0142\u0143")
        buf.write("\7c\2\2\u0143\u0144\7v\2\2\u0144\u0149\7g\2\2\u0145\u0146")
        buf.write("\7c\2\2\u0146\u0147\7v\2\2\u0147\u0149\7\u00eb\2\2\u0148")
        buf.write("\u0142\3\2\2\2\u0148\u0145\3\2\2\2\u0149&\3\2\2\2\u014a")
        buf.write("\u014b\7\60\2\2\u014b(\3\2\2\2\u014c\u014d\7\60\2\2\u014d")
        buf.write("\u014e\7\60\2\2\u014e*\3\2\2\2\u014f\u0150\7~\2\2\u0150")
        buf.write(",\3\2\2\2\u0151\u0152\7*\2\2\u0152\u0153\b\27\2\2\u0153")
        buf.write(".\3\2\2\2\u0154\u0155\7+\2\2\u0155\u0156\b\30\3\2\u0156")
        buf.write("\60\3\2\2\2\u0157\u0158\7.\2\2\u0158\62\3\2\2\2\u0159")
        buf.write("\u015a\7<\2\2\u015a\64\3\2\2\2\u015b\u015c\7=\2\2\u015c")
        buf.write("\66\3\2\2\2\u015d\u015e\7`\2\2\u015e8\3\2\2\2\u015f\u0160")
        buf.write("\7>\2\2\u0160\u0161\7/\2\2\u0161:\3\2\2\2\u0162\u0163")
        buf.write("\7]\2\2\u0163\u0164\b\36\4\2\u0164<\3\2\2\2\u0165\u0166")
        buf.write("\7_\2\2\u0166\u0167\b\37\5\2\u0167>\3\2\2\2\u0168\u0169")
        buf.write("\7~\2\2\u0169\u016a\7~\2\2\u016a@\3\2\2\2\u016b\u016c")
        buf.write("\7z\2\2\u016c\u016d\7q\2\2\u016d\u016e\7t\2\2\u016eB\3")
        buf.write("\2\2\2\u016f\u0170\7(\2\2\u0170\u0171\7(\2\2\u0171D\3")
        buf.write("\2\2\2\u0172\u0173\7>\2\2\u0173\u0174\7>\2\2\u0174F\3")
        buf.write("\2\2\2\u0175\u0176\7@\2\2\u0176\u0177\7@\2\2\u0177H\3")
        buf.write("\2\2\2\u0178\u0179\7-\2\2\u0179J\3\2\2\2\u017a\u017b\7")
        buf.write("/\2\2\u017bL\3\2\2\2\u017c\u017d\7,\2\2\u017dN\3\2\2\2")
        buf.write("\u017e\u017f\7\61\2\2\u017fP\3\2\2\2\u0180\u0181\7o\2")
        buf.write("\2\u0181\u0182\7q\2\2\u0182\u0183\7f\2\2\u0183R\3\2\2")
        buf.write("\2\u0184\u0185\7f\2\2\u0185\u0186\7k\2\2\u0186\u0187\7")
        buf.write("x\2\2\u0187T\3\2\2\2\u0188\u0189\7\u0080\2\2\u0189V\3")
        buf.write("\2\2\2\u018a\u018b\7}\2\2\u018b\u018c\b,\6\2\u018cX\3")
        buf.write("\2\2\2\u018d\u018e\7\177\2\2\u018e\u018f\b-\7\2\u018f")
        buf.write("Z\3\2\2\2\u0190\u0191\7>\2\2\u0191\\\3\2\2\2\u0192\u0193")
        buf.write("\7@\2\2\u0193^\3\2\2\2\u0194\u0195\7?\2\2\u0195`\3\2\2")
        buf.write("\2\u0196\u0197\7@\2\2\u0197\u0198\7?\2\2\u0198b\3\2\2")
        buf.write("\2\u0199\u019a\7>\2\2\u019a\u019b\7?\2\2\u019bd\3\2\2")
        buf.write("\2\u019c\u019d\7\u0080\2\2\u019d\u019e\7?\2\2\u019ef\3")
        buf.write("\2\2\2\u019f\u01a0\7B\2\2\u01a0h\3\2\2\2\u01a1\u01a2\7")
        buf.write("/\2\2\u01a2\u01a3\7@\2\2\u01a3j\3\2\2\2\u01a4\u01a5\7")
        buf.write("x\2\2\u01a5\u01a6\7c\2\2\u01a6\u01a7\7n\2\2\u01a7l\3\2")
        buf.write("\2\2\u01a8\u01a9\7t\2\2\u01a9\u01aa\7g\2\2\u01aa\u01ab")
        buf.write("\7h\2\2\u01abn\3\2\2\2\u01ac\u01ad\7k\2\2\u01ad\u01ae")
        buf.write("\7p\2\2\u01ae\u01af\7v\2\2\u01af\u01b0\7g\2\2\u01b0\u01b1")
        buf.write("\7k\2\2\u01b1\u01b2\7t\2\2\u01b2\u01b3\7q\2\2\u01b3p\3")
        buf.write("\2\2\2\u01b4\u01b5\7t\2\2\u01b5\u01b6\7g\2\2\u01b6\u01b7")
        buf.write("\7c\2\2\u01b7\u01b8\7n\2\2\u01b8r\3\2\2\2\u01b9\u01ba")
        buf.write("\7e\2\2\u01ba\u01bb\7c\2\2\u01bb\u01bc\7t\2\2\u01bc\u01bd")
        buf.write("\7c\2\2\u01bd\u01be\7e\2\2\u01be\u01bf\7v\2\2\u01bf\u01c0")
        buf.write("\7g\2\2\u01c0\u01c1\7t\2\2\u01c1t\3\2\2\2\u01c2\u01c3")
        buf.write("\7e\2\2\u01c3\u01c4\7c\2\2\u01c4\u01c5\7f\2\2\u01c5\u01c6")
        buf.write("\7g\2\2\u01c6\u01c7\7k\2\2\u01c7\u01c8\7c\2\2\u01c8v\3")
        buf.write("\2\2\2\u01c9\u01ca\7n\2\2\u01ca\u01cb\7\u00f5\2\2\u01cb")
        buf.write("\u01cc\7i\2\2\u01cc\u01cd\7k\2\2\u01cd\u01ce\7e\2\2\u01ce")
        buf.write("\u01d6\7q\2\2\u01cf\u01d0\7n\2\2\u01d0\u01d1\7q\2\2\u01d1")
        buf.write("\u01d2\7i\2\2\u01d2\u01d3\7k\2\2\u01d3\u01d4\7e\2\2\u01d4")
        buf.write("\u01d6\7q\2\2\u01d5\u01c9\3\2\2\2\u01d5\u01cf\3\2\2\2")
        buf.write("\u01d6x\3\2\2\2\u01d7\u01d8\7\60\2\2\u01d8\u01d9\7\60")
        buf.write("\2\2\u01d9\u01da\7\60\2\2\u01daz\3\2\2\2\u01db\u01dc\7")
        buf.write("e\2\2\u01dc\u01dd\7q\2\2\u01dd\u01de\7p\2\2\u01de\u01df")
        buf.write("\7u\2\2\u01df\u01e0\7v\2\2\u01e0\u01e1\7c\2\2\u01e1\u01e2")
        buf.write("\7p\2\2\u01e2\u01e3\7v\2\2\u01e3\u01e4\7g\2\2\u01e4|\3")
        buf.write("\2\2\2\u01e5\u01e6\6?\2\2\u01e6\u01f2\5\u00b7\\\2\u01e7")
        buf.write("\u01e9\7\17\2\2\u01e8\u01e7\3\2\2\2\u01e8\u01e9\3\2\2")
        buf.write("\2\u01e9\u01ea\3\2\2\2\u01ea\u01ed\7\f\2\2\u01eb\u01ed")
        buf.write("\7\17\2\2\u01ec\u01e8\3\2\2\2\u01ec\u01eb\3\2\2\2\u01ed")
        buf.write("\u01ef\3\2\2\2\u01ee\u01f0\5\u00b7\\\2\u01ef\u01ee\3\2")
        buf.write("\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f2\3\2\2\2\u01f1\u01e5")
        buf.write("\3\2\2\2\u01f1\u01ec\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3")
        buf.write("\u01f4\b?\b\2\u01f4~\3\2\2\2\u01f5\u01f9\5\u00bd_\2\u01f6")
        buf.write("\u01f8\5\u00bf`\2\u01f7\u01f6\3\2\2\2\u01f8\u01fb\3\2")
        buf.write("\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u0080")
        buf.write("\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc\u01fd\5\u0095K\2\u01fd")
        buf.write("\u01fe\bA\t\2\u01fe\u0082\3\2\2\2\u01ff\u0202\7)\2\2\u0200")
        buf.write("\u0203\5\u0097L\2\u0201\u0203\n\2\2\2\u0202\u0200\3\2")
        buf.write("\2\2\u0202\u0201\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205")
        buf.write("\7)\2\2\u0205\u0206\bB\n\2\u0206\u0084\3\2\2\2\u0207\u020b")
        buf.write("\5\u0099M\2\u0208\u020a\5\u009bN\2\u0209\u0208\3\2\2\2")
        buf.write("\u020a\u020d\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020c\3")
        buf.write("\2\2\2\u020c\u0214\3\2\2\2\u020d\u020b\3\2\2\2\u020e\u0210")
        buf.write("\7\62\2\2\u020f\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0214\3\2\2\2")
        buf.write("\u0213\u0207\3\2\2\2\u0213\u020f\3\2\2\2\u0214\u0086\3")
        buf.write("\2\2\2\u0215\u0216\7\62\2\2\u0216\u0218\t\3\2\2\u0217")
        buf.write("\u0219\5\u009dO\2\u0218\u0217\3\2\2\2\u0219\u021a\3\2")
        buf.write("\2\2\u021a\u0218\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u0088")
        buf.write("\3\2\2\2\u021c\u021d\7\62\2\2\u021d\u021f\t\4\2\2\u021e")
        buf.write("\u0220\5\u009fP\2\u021f\u021e\3\2\2\2\u0220\u0221\3\2")
        buf.write("\2\2\u0221\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u008a")
        buf.write("\3\2\2\2\u0223\u0224\7\62\2\2\u0224\u0226\t\5\2\2\u0225")
        buf.write("\u0227\5\u00a1Q\2\u0226\u0225\3\2\2\2\u0227\u0228\3\2")
        buf.write("\2\2\u0228\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u008c")
        buf.write("\3\2\2\2\u022a\u022b\5\u00a3R\2\u022b\u008e\3\2\2\2\u022c")
        buf.write("\u022f\5\u008dG\2\u022d\u022f\5\u00a5S\2\u022e\u022c\3")
        buf.write("\2\2\2\u022e\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0231")
        buf.write("\t\6\2\2\u0231\u0090\3\2\2\2\u0232\u0236\5\u00b7\\\2\u0233")
        buf.write("\u0236\5\u00b9]\2\u0234\u0236\5\u00bb^\2\u0235\u0232\3")
        buf.write("\2\2\2\u0235\u0233\3\2\2\2\u0235\u0234\3\2\2\2\u0236\u0237")
        buf.write("\3\2\2\2\u0237\u0238\bI\13\2\u0238\u0092\3\2\2\2\u0239")
        buf.write("\u023a\13\2\2\2\u023a\u0094\3\2\2\2\u023b\u0240\7$\2\2")
        buf.write("\u023c\u023f\5\u0097L\2\u023d\u023f\n\2\2\2\u023e\u023c")
        buf.write("\3\2\2\2\u023e\u023d\3\2\2\2\u023f\u0242\3\2\2\2\u0240")
        buf.write("\u023e\3\2\2\2\u0240\u0241\3\2\2\2\u0241\u0243\3\2\2\2")
        buf.write("\u0242\u0240\3\2\2\2\u0243\u0244\7$\2\2\u0244\u0096\3")
        buf.write("\2\2\2\u0245\u0246\7^\2\2\u0246\u0247\13\2\2\2\u0247\u0098")
        buf.write("\3\2\2\2\u0248\u0249\t\7\2\2\u0249\u009a\3\2\2\2\u024a")
        buf.write("\u024b\t\b\2\2\u024b\u009c\3\2\2\2\u024c\u024d\t\t\2\2")
        buf.write("\u024d\u009e\3\2\2\2\u024e\u024f\t\n\2\2\u024f\u00a0\3")
        buf.write("\2\2\2\u0250\u0251\t\13\2\2\u0251\u00a2\3\2\2\2\u0252")
        buf.write("\u0253\5\u00a5S\2\u0253\u0254\5\u00a7T\2\u0254\u00a4\3")
        buf.write("\2\2\2\u0255\u0257\5\u009bN\2\u0256\u0255\3\2\2\2\u0257")
        buf.write("\u0258\3\2\2\2\u0258\u0256\3\2\2\2\u0258\u0259\3\2\2\2")
        buf.write("\u0259\u00a6\3\2\2\2\u025a\u025c\7\60\2\2\u025b\u025d")
        buf.write("\5\u009bN\2\u025c\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e")
        buf.write("\u025c\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u00a8\3\2\2\2")
        buf.write("\u0260\u0265\7)\2\2\u0261\u0264\5\u00afX\2\u0262\u0264")
        buf.write("\5\u00b5[\2\u0263\u0261\3\2\2\2\u0263\u0262\3\2\2\2\u0264")
        buf.write("\u0267\3\2\2\2\u0265\u0263\3\2\2\2\u0265\u0266\3\2\2\2")
        buf.write("\u0266\u0268\3\2\2\2\u0267\u0265\3\2\2\2\u0268\u0273\7")
        buf.write(")\2\2\u0269\u026e\7$\2\2\u026a\u026d\5\u00b1Y\2\u026b")
        buf.write("\u026d\5\u00b5[\2\u026c\u026a\3\2\2\2\u026c\u026b\3\2")
        buf.write("\2\2\u026d\u0270\3\2\2\2\u026e\u026c\3\2\2\2\u026e\u026f")
        buf.write("\3\2\2\2\u026f\u0271\3\2\2\2\u0270\u026e\3\2\2\2\u0271")
        buf.write("\u0273\7$\2\2\u0272\u0260\3\2\2\2\u0272\u0269\3\2\2\2")
        buf.write("\u0273\u00aa\3\2\2\2\u0274\u0275\7)\2\2\u0275\u0276\7")
        buf.write(")\2\2\u0276\u0277\7)\2\2\u0277\u027b\3\2\2\2\u0278\u027a")
        buf.write("\5\u00adW\2\u0279\u0278\3\2\2\2\u027a\u027d\3\2\2\2\u027b")
        buf.write("\u027c\3\2\2\2\u027b\u0279\3\2\2\2\u027c\u027e\3\2\2\2")
        buf.write("\u027d\u027b\3\2\2\2\u027e\u027f\7)\2\2\u027f\u0280\7")
        buf.write(")\2\2\u0280\u028f\7)\2\2\u0281\u0282\7$\2\2\u0282\u0283")
        buf.write("\7$\2\2\u0283\u0284\7$\2\2\u0284\u0288\3\2\2\2\u0285\u0287")
        buf.write("\5\u00adW\2\u0286\u0285\3\2\2\2\u0287\u028a\3\2\2\2\u0288")
        buf.write("\u0289\3\2\2\2\u0288\u0286\3\2\2\2\u0289\u028b\3\2\2\2")
        buf.write("\u028a\u0288\3\2\2\2\u028b\u028c\7$\2\2\u028c\u028d\7")
        buf.write("$\2\2\u028d\u028f\7$\2\2\u028e\u0274\3\2\2\2\u028e\u0281")
        buf.write("\3\2\2\2\u028f\u00ac\3\2\2\2\u0290\u0293\5\u00b3Z\2\u0291")
        buf.write("\u0293\5\u00b5[\2\u0292\u0290\3\2\2\2\u0292\u0291\3\2")
        buf.write("\2\2\u0293\u00ae\3\2\2\2\u0294\u0296\t\f\2\2\u0295\u0294")
        buf.write("\3\2\2\2\u0296\u00b0\3\2\2\2\u0297\u0299\t\r\2\2\u0298")
        buf.write("\u0297\3\2\2\2\u0299\u00b2\3\2\2\2\u029a\u029c\t\16\2")
        buf.write("\2\u029b\u029a\3\2\2\2\u029c\u00b4\3\2\2\2\u029d\u029e")
        buf.write("\7^\2\2\u029e\u029f\t\17\2\2\u029f\u00b6\3\2\2\2\u02a0")
        buf.write("\u02a2\t\20\2\2\u02a1\u02a0\3\2\2\2\u02a2\u02a3\3\2\2")
        buf.write("\2\u02a3\u02a1\3\2\2\2\u02a3\u02a4\3\2\2\2\u02a4\u00b8")
        buf.write("\3\2\2\2\u02a5\u02a9\7%\2\2\u02a6\u02a8\n\21\2\2\u02a7")
        buf.write("\u02a6\3\2\2\2\u02a8\u02ab\3\2\2\2\u02a9\u02a7\3\2\2\2")
        buf.write("\u02a9\u02aa\3\2\2\2\u02aa\u00ba\3\2\2\2\u02ab\u02a9\3")
        buf.write("\2\2\2\u02ac\u02ae\7^\2\2\u02ad\u02af\5\u00b7\\\2\u02ae")
        buf.write("\u02ad\3\2\2\2\u02ae\u02af\3\2\2\2\u02af\u02b5\3\2\2\2")
        buf.write("\u02b0\u02b2\7\17\2\2\u02b1\u02b0\3\2\2\2\u02b1\u02b2")
        buf.write("\3\2\2\2\u02b2\u02b3\3\2\2\2\u02b3\u02b6\7\f\2\2\u02b4")
        buf.write("\u02b6\7\17\2\2\u02b5\u02b1\3\2\2\2\u02b5\u02b4\3\2\2")
        buf.write("\2\u02b6\u00bc\3\2\2\2\u02b7\u02b9\t\22\2\2\u02b8\u02b7")
        buf.write("\3\2\2\2\u02b9\u00be\3\2\2\2\u02ba\u02bd\5\u00bd_\2\u02bb")
        buf.write("\u02bd\t\23\2\2\u02bc\u02ba\3\2\2\2\u02bc\u02bb\3\2\2")
        buf.write("\2\u02bd\u00c0\3\2\2\2-\2\u00de\u00f9\u013a\u0148\u01d5")
        buf.write("\u01e8\u01ec\u01ef\u01f1\u01f9\u0202\u020b\u0211\u0213")
        buf.write("\u021a\u0221\u0228\u022e\u0235\u023e\u0240\u0258\u025e")
        buf.write("\u0263\u0265\u026c\u026e\u0272\u027b\u0288\u028e\u0292")
        buf.write("\u0295\u0298\u029b\u02a3\u02a9\u02ae\u02b1\u02b5\u02b8")
        buf.write("\u02bc\f\3\27\2\3\30\3\3\36\4\3\37\5\3,\6\3-\7\3?\b\3")
        buf.write("A\t\3B\n\b\2\2")
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
    RANGE_OP = 20
    CARDINALITY_OP = 21
    OPEN_PAREN = 22
    CLOSE_PAREN = 23
    COMMA = 24
    COLON = 25
    SEMI_COLON = 26
    POWER = 27
    ASSIGN = 28
    OPEN_BRACK = 29
    CLOSE_BRACK = 30
    OR_OP = 31
    XOR = 32
    AND_OP = 33
    LEFT_SHIFT = 34
    RIGHT_SHIFT = 35
    ADD = 36
    MINUS = 37
    STAR = 38
    DIV = 39
    MOD = 40
    IDIV = 41
    NOT_OP = 42
    OPEN_BRACE = 43
    CLOSE_BRACE = 44
    LESS_THAN = 45
    GREATER_THAN = 46
    EQUALS = 47
    GT_EQ = 48
    LT_EQ = 49
    NOT_EQ = 50
    AT = 51
    ARROW = 52
    VAL = 53
    REF = 54
    INTEGER = 55
    REAL = 56
    CHAR = 57
    STRING = 58
    BOOLEAN = 59
    VARIADIC = 60
    CONSTANT = 61
    NEWLINE = 62
    NAME = 63
    STRING_LITERAL = 64
    CHAR_LITERAL = 65
    DECIMAL_INTEGER = 66
    OCT_INTEGER = 67
    HEX_INTEGER = 68
    BIN_INTEGER = 69
    FLOAT_NUMBER = 70
    IMAG_NUMBER = 71
    SKIP_ = 72
    UNKNOWN_CHAR = 73

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'retornar'", "'usando'", "'se'", "'enquanto'", "'para'", "'ou'", 
            "'e'", "'nulo'", "'verdadeiro'", "'falso'", "'tipo'", "'continuar'", 
            "'parar'", "'passo'", "'.'", "'..'", "'|'", "'('", "')'", "','", 
            "':'", "';'", "'^'", "'<-'", "'['", "']'", "'||'", "'xor'", 
            "'&&'", "'<<'", "'>>'", "'+'", "'-'", "'*'", "'/'", "'mod'", 
            "'div'", "'~'", "'{'", "'}'", "'<'", "'>'", "'='", "'>='", "'<='", 
            "'~='", "'@'", "'->'", "'val'", "'ref'", "'inteiro'", "'real'", 
            "'caracter'", "'cadeia'", "'...'", "'constante'" ]

    symbolicNames = [ "<INVALID>",
            "RETURN", "IMPORT", "IF", "ELSE", "WHILE", "FOR", "OR", "AND", 
            "NOT", "NULL", "TRUE", "FALSE", "CLASS", "CONTINUE", "BREAK", 
            "ENUM", "STEP", "UNTIL", "DOT", "RANGE_OP", "CARDINALITY_OP", 
            "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", 
            "POWER", "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", "XOR", 
            "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", "STAR", 
            "DIV", "MOD", "IDIV", "NOT_OP", "OPEN_BRACE", "CLOSE_BRACE", 
            "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ", 
            "AT", "ARROW", "VAL", "REF", "INTEGER", "REAL", "CHAR", "STRING", 
            "BOOLEAN", "VARIADIC", "CONSTANT", "NEWLINE", "NAME", "STRING_LITERAL", 
            "CHAR_LITERAL", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", 
            "BIN_INTEGER", "FLOAT_NUMBER", "IMAG_NUMBER", "SKIP_", "UNKNOWN_CHAR" ]

    ruleNames = [ "RETURN", "IMPORT", "IF", "ELSE", "WHILE", "FOR", "OR", 
                  "AND", "NOT", "NULL", "TRUE", "FALSE", "CLASS", "CONTINUE", 
                  "BREAK", "ENUM", "STEP", "UNTIL", "DOT", "RANGE_OP", "CARDINALITY_OP", 
                  "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", 
                  "POWER", "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", 
                  "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", 
                  "STAR", "DIV", "MOD", "IDIV", "NOT_OP", "OPEN_BRACE", 
                  "CLOSE_BRACE", "LESS_THAN", "GREATER_THAN", "EQUALS", 
                  "GT_EQ", "LT_EQ", "NOT_EQ", "AT", "ARROW", "VAL", "REF", 
                  "INTEGER", "REAL", "CHAR", "STRING", "BOOLEAN", "VARIADIC", 
                  "CONSTANT", "NEWLINE", "NAME", "STRING_LITERAL", "CHAR_LITERAL", 
                  "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", 
                  "FLOAT_NUMBER", "IMAG_NUMBER", "SKIP_", "UNKNOWN_CHAR", 
                  "SHORT_STRING", "STRING_ESCAPE_SEQ", "NON_ZERO_DIGIT", 
                  "DIGIT", "OCT_DIGIT", "HEX_DIGIT", "BIN_DIGIT", "POINT_FLOAT", 
                  "INT_PART", "FRACTION", "SHORT_BYTES", "LONG_BYTES", "LONG_BYTES_ITEM", 
                  "SHORT_BYTES_CHAR_NO_SINGLE_QUOTE", "SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE", 
                  "LONG_BYTES_CHAR", "BYTES_ESCAPE_SEQ", "SPACES", "COMMENT", 
                  "LINE_JOINING", "ID_START", "ID_CONTINUE" ]

    grammarFileName = "lang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



        #Uma fila para tokens adicionais (ver a regra NEWLINE do lexer)
        self.tokens = []

        #A pilha para controlar o nível de indentação
        self.indents = Stack()

        #O número de colchetes e parênteses abertos
        self.opened = 0

        #A token produzida mais recente.
        self.lastToken = None

    def emitToken(self, t):
        self._token = t
        self.tokens.append(t)

    def nextToken(self):
        # Checar se atingimos o final do arquivo e faltam DEDENTS a serem emitidos
        if self._input.LA(1) == Token.EOF and len(self.indents)>0:

          # Remove tokens EOF por enquanto
          for i in range(tokens.size() - 1, 0, -1):
            if (self.tokens.get(i).getType() == EOF):
              self.tokens.remove(i)

          # Emite uma token de quebra de linha, que termina a declaração atual
          self.emitToken(commonToken(langParser.NEWLINE, "\n"))

          # Emite quantos DEDENTS necessários 
          while (not self.indents.isEmpty()):
            self.emitToken(createDedent())
            self.indents.pop()

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
      dedent = self.commonToken(langParser.DEDENT, "")
      dedent.line = self.lastToken.line
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
    		actions[21] = self.OPEN_PAREN_action 
    		actions[22] = self.CLOSE_PAREN_action 
    		actions[28] = self.OPEN_BRACK_action 
    		actions[29] = self.CLOSE_BRACK_action 
    		actions[42] = self.OPEN_BRACE_action 
    		actions[43] = self.CLOSE_BRACE_action 
    		actions[61] = self.NEWLINE_action 
    		actions[63] = self.STRING_LITERAL_action 
    		actions[64] = self.CHAR_LITERAL_action 
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

                newLine = re.sub(r"[^\r\n]+", "", self.text)
                spaces = re.sub(r"[\r\n]+", "", self.text)
                nextTok = self._input.LA(1)

                if (self.opened > 0 or nextTok == '\r' or nextTok == '\n' or nextTok == '#'):
                  # If we are inside a list or on a blank line, ignore all indents
                  # dedents and line breaks.
                  self.skip()
                else:
                  self.emitToken(self.commonToken(langParser.NEWLINE, newLine))

                  indent = self.getIndentationCount(spaces)
                  previous = 0 if len(self.indents)==0 else self.indents.top()

                  if (indent == previous):
                    # skip indents of the same size as the present indent-size
                    self.skip()
                  elif (indent > previous):
                    self.indents.push(indent)
                    self.emitToken(self.commonToken(langParser.INDENT, spaces))
                  else:
                    # Possibly emit more than 1 DEDENT token.
                    while(len(self.indents)>0 and self.indents.top() > indent):
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
            preds[61] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


