import sys
import Interpreter

import gettext
import argparse

gettext.bindtextdomain('argparse', '.')
gettext.textdomain('argparse')

def main(argv):
    trace = False
    parser = argparse.ArgumentParser()
    parser.add_argument("arquivo", nargs='?', help="o arquivo que contém o código-fonte")
    parser.add_argument("-t", "--trace", help="habilitar a impressão JSON da execução", action="store_true")
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

    return Interpreter.Interpreter.interpret(input, trace=args.trace)

if __name__ == '__main__': # pragma: no cover
    main(sys.argv)
