import sys
import tupy.Interpreter

import gettext
import argparse
import logging

gettext.bindtextdomain('argparse', '.')
gettext.textdomain('argparse')

def main(argv):
    trace = False
    parser = argparse.ArgumentParser()
    parser.add_argument("arquivo", nargs='?', help="o arquivo que contém o código-fonte")
    parser.add_argument("-t", "--trace", help="habilita a impressão JSON da execução", action="store_true")
    parser.add_argument("--tokens", help="habilita a impressão dos tokens identificados pela gramática.", action="store_true")
    parser.add_argument("-d", "--debug", help="habilita a impressão de mensagens de debug, incluindo tracebacks.", action="store_true")
    args, _unknown = parser.parse_known_args(argv[1:])

    if args.arquivo:
        try:
            with open(args.arquivo, 'r') as myfile:
                input = myfile.read()

        except FileNotFoundError as err:
            print("Arquivo "+args.arquivo+" não encontrado!")
            sys.exit(2)
    else:
        input = sys.stdin.read()

    tupy.Interpreter.Interpreter.isDebug = args.debug
    return tupy.Interpreter.Interpreter.interpret(input, trace=args.trace, printTokens=args.tokens)

if __name__ == '__main__': # pragma: no cover
    main(sys.argv)
