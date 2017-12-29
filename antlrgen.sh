#!/usr/bin/env bash

ANTLR=`java -jar /usr/local/lib/antlr-4.7-complete.jar -visitor -Dlanguage=Python3 lang.g4`
$ANTLR
mv langLexer.py tupy/langLexer.py
mv langParser.py tupy/langParser.py
