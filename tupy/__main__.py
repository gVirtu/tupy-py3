import sys
import os
import tupy.Interpreter

import gettext
import argparse
import logging
import readline

gettext.bindtextdomain('argparse', '.')
gettext.textdomain('argparse')

def main(argv):
    trace = False
    parser = argparse.ArgumentParser()
    parser.add_argument("arquivo", nargs='?', help="o arquivo que contém o código-fonte")
    parser.add_argument("-t", "--trace", help="habilita a impressão JSON da execução", action="store_true")
    parser.add_argument("-q", "--quiet", help="desabilita qualquer impressão", action="store_true")
    parser.add_argument("-L", "--lines", help="habilita a impressão dos números de linha", action="store_true")
    parser.add_argument("--tokens", help="habilita a impressão dos tokens identificados pela gramática.", action="store_true")
    parser.add_argument("-d", "--debug", help="habilita a impressão de mensagens de debug, incluindo tracebacks.", action="store_true")
    args, _unknown = parser.parse_known_args(argv[1:])

    out = open(os.devnull, 'w') if args.quiet else sys.stdout

    if args.arquivo:
        try:
            with open(args.arquivo, 'r') as myfile:
                myinput = myfile.read()

        except FileNotFoundError as err:
            print("Arquivo "+args.arquivo+" não encontrado!", file=out)
            sys.exit(2)
    else:
        print("Interpretador TuPy interativo v1.0 (TCC UERJ)\n", file=out)
        print("   Digite o seu programa abaixo, e então use CTRL+D para executá-lo.│", file=out)
        if (args.lines):
            print("   ┌────────────────────────────────────────────────────────────────┘", file=out)
        else:
            print("────────────────────────────────────────────────────────────────────┘", file=out)
        commandList = []
        myinput = ''
        line = 0
        while True:
            try:
                line = line + 1
                if (args.lines):
                    commandList.append(input("{0:<3}│ ".format(line)))
                else:
                    commandList.append(input())
            except EOFError:
                myinput = '\n'.join(commandList)
                print("\n   └─────────────────────────────────────────────────────────────────" \
                      if args.lines else "\n─────────────────────────────────────────────────────────────────────", file=out)
                break
            except KeyboardInterrupt: # pragma: no cover
                print("\nExecução terminada a comando do usuário.\nDica: Para executar o programa digitado, utilize CTRL+D.", file=out)
                sys.exit(2)

    tupy.Interpreter.Interpreter.isDebug = args.debug
    if args.quiet:
        out.close()
    return tupy.Interpreter.Interpreter.interpret(myinput, trace=args.trace, printTokens=args.tokens, quiet=args.quiet)

if __name__ == '__main__': # pragma: no cover
    main(sys.argv)
