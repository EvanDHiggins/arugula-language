from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener
from MyExprVisitor import MyExprVisitor
import sys

def pdir(a, printhidden=False):
    for s in dir(a):
        if s[0] == '_' and not printhidden:
            continue
        print(s)


def main(argv):
    ip = FileStream(argv[1])
    lexer = ExprLexer(ip)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()

    visitor = MyExprVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
