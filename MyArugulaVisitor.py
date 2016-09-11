# Generated from java-escape by ANTLR 4.5
from antlr4 import *
from ArugulaVisitor import ArugulaVisitor
import copy

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class MyArugulaVisitor(ArugulaVisitor):

    def __init__(self):
        self.variableLookup = {}
        self.funcmap = {} # ([ID1, ID2, ...], startNode)

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx):
        self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#printExpr.
    def visitPrintExpr(self, ctx):
        print(self.visit(ctx.getChild(0)))


    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, ctx):
        self.variableLookup[ctx.getChild(0).getText()] = self.visit(ctx.getChild(2))

    def visitClear(self, ctx):
        self.variableLookup = {}

    # Visit a parse tree produced by ExprParser#blank.
    def visitBlank(self, ctx):
        pass

    def visitDefine(self, ctx):
        """Associates a context (series of in-scope ids) with a
        start node for function execution and saves those to the
        function map with the function's assigned id
        """
        funcname = ctx.getChild(1).getText()
        context = self.visit(ctx.getChild(3))
        self.funcmap[funcname] = (context, ctx.getChild(6))

    def visitCall(self, ctx):
        oldVariableLookup = copy.deepcopy(self.variableLookup)
        args = self.visit(ctx.getChild(2))
        context, start = self.funcmap[ctx.getChild(0).getText()]
        if len(args) != len(context):
            raise ValueError('Incorrect number of arguments.')

        for ident, val in zip(context, args):
            self.variableLookup[ident] = val

        value = self.visit(start)
        self.variableLookup = oldVariableLookup
        return value

    def visitMultparam(self, ctx):
        return [ctx.getChild(0).getText()] + self.visit(ctx.getChild(2))

    def visitSingleparam(self, ctx):
        return [ctx.getChild(0).getText()]

    def visitMultarg(self, ctx):
        return [self.visit(ctx.getChild(0))] + self.visit(ctx.getChild(2))

    def visitSinglearg(self, ctx):
        return [self.visit(ctx.getChild(0))]

    # Visit a parse tree produced by ExprParser#parens.
    def visitParens(self, ctx):
        return self.visit(ctx.getChild(1))


    # Visit a parse tree produced by ExprParser#MulDiv.
    def visitMulDiv(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        if ctx.getChild(1).getText() == '*':
            return right * left
        else:
            return left / right


    # Visit a parse tree produced by ExprParser#AddSub.
    def visitAddSub(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        if ctx.getChild(1).getText() == '+':
            return right + left
        else:
            return left - right


    # Visit a parse tree produced by ExprParser#id.
    def visitId(self, ctx):
        return self.variableLookup[ctx.getText()]


    # Visit a parse tree produced by ExprParser#int.
    def visitInt(self, ctx):
        return int(ctx.getText())


