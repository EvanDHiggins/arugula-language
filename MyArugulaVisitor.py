# Generated from java-escape by ANTLR 4.5
from antlr4 import *
from ArugulaVisitor import ArugulaVisitor
import copy

class ArugulaEvaluator(ArugulaVisitor):

    def __init__(self):
        # The current context is a mapping of variable identifiers to
        # their associated values
        self.currentContext = {}

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, node):
        self.visitChildren(node)


    # Visit a parse tree produced by ExprParser#printExpr.
    def visitPrintExpr(self, node):
        print(self.visit(node.getChild(0)))


    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, node):
        self.variableLookup[node.getChild(0).getText()] = self.visit(node.getChild(2))

    # Visit a parse tree produced by ExprParser#blank.
    def visitBlank(self, node):
        pass

    # Visit a parse tree produced by ExprParser#parens.
    def visitParens(self, node):
        return self.visit(node.getChild(1))


    # Visit a parse tree produced by ExprParser#MulDiv.
    def visitMulDiv(self, node):
        left = self.visit(node.getChild(0))
        right = self.visit(node.getChild(2))
        if node.getChild(1).getText() == '*':
            return left * right
        else:
            return left / right


    # Visit a parse tree produced by ExprParser#AddSub.
    def visitAddSub(self, node):
        left = self.visit(node.getChild(0))
        right = self.visit(node.getChild(2))
        if node.getChild(1).getText() == '+':
            return left + right
        else:
            return left - right


    # Visit a parse tree produced by ExprParser#id.
    def visitId(self, node):
        return self.variableLookup[node.getText()]


    # Visit a parse tree produced by ExprParser#int.
    def visitInt(self, node):
        return int(node.getText())
