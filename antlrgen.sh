#!/usr/bin/env bash

ANTLR=`java -jar /usr/local/lib/antlr-4.7-complete.jar -visitor -Dlanguage=Python3 lang.g4`
$ANTLR