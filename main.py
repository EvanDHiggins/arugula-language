from antlr4 import *
from ArugulaLexer import ArugulaLexer
from ArugulaParser import ArugulaParser
from PythonGenerator import MyArugulaVisitor
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
    tree = parser.prog()

    visitor = PythonGenerator()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
