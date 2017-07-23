#!/usr/bin/env bash

rm testrig/*.java
rm testrig/*.class
java -jar /usr/local/lib/antlr-4.7-complete.jar -visitor langJAVA.g4 -o testrig
javac testrig/*.java
echo "Welcome to TestRig, type your program and then CTRL+D:"
(cd testrig; java org.antlr.v4.gui.TestRig langJAVA r -gui)