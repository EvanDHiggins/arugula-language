# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#printExpr.
    def visitPrintExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#clear.
    def visitClear(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#blank.
    def visitBlank(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#define.
    def visitDefine(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#call.
    def visitCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parens.
    def visitParens(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#MulDiv.
    def visitMulDiv(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#AddSub.
    def visitAddSub(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#id.
    def visitId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#int.
    def visitInt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#multparam.
    def visitMultparam(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#singleparam.
    def visitSingleparam(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#multarg.
    def visitMultarg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#singlearg.
    def visitSinglearg(self, ctx):
        return self.visitChildren(ctx)


