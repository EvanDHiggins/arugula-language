# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by ArugulaParser.

class ArugulaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArugulaParser#prog.
    def visitProg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArugulaParser#printExpr.
    def visitPrintExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArugulaParser#assign.
    def visitAssign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArugulaParser#blank.
    def visitBlank(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArugulaParser#parens.
    def visitParens(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArugulaParser#MulDiv.
    def visitMulDiv(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArugulaParser#AddSub.
    def visitAddSub(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArugulaParser#id.
    def visitId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArugulaParser#int.
    def visitInt(self, ctx):
        return self.visitChildren(ctx)


