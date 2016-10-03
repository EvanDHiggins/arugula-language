from antlr4 import *
from ArugulaLexer import ArugulaLexer
from ArugulaParser import ArugulaParser
from ArugulaCGenerator import ArugulaCGenerator
import sys

def pdir(a, printhidden=False):
    for s in dir(a):
        if s[0] == '_' and not printhidden:
            continue
        print(s)


def main(argv):
    ip = FileStream(argv[1])
    lexer = ArugulaLexer(ip)
    stream = CommonTokenStream(lexer)
    parser = ArugulaParser(stream)
    programRootNode = parser.prog()

    visitor = ArugulaCGenerator(argv[1].replace('.ag', '.c'))
    visitor.visit(programRootNode)

if __name__ == '__main__':
    main(sys.argv)
