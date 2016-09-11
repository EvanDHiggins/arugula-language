# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .ArugulaVisitor import ArugulaVisitor
else:
    from ArugulaVisitor import ArugulaVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\21")
        buf.write("N\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3&\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\64\n")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4<\n\4\f\4\16\4?\13\4\3\5")
        buf.write("\3\5\3\5\3\5\5\5E\n\5\3\6\3\6\3\6\3\6\3\6\5\6L\n\6\3\6")
        buf.write("\2\3\6\7\2\4\6\b\n\2\4\3\2\t\n\3\2\13\fT\2\r\3\2\2\2\4")
        buf.write("%\3\2\2\2\6\63\3\2\2\2\bD\3\2\2\2\nK\3\2\2\2\f\16\5\4")
        buf.write("\3\2\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17\20\3\2")
        buf.write("\2\2\20\3\3\2\2\2\21\22\5\6\4\2\22\23\7\20\2\2\23&\3\2")
        buf.write("\2\2\24\25\7\16\2\2\25\26\7\3\2\2\26\27\5\6\4\2\27\30")
        buf.write("\7\20\2\2\30&\3\2\2\2\31\32\7\r\2\2\32&\7\20\2\2\33&\7")
        buf.write("\20\2\2\34\35\7\4\2\2\35\36\7\16\2\2\36\37\7\5\2\2\37")
        buf.write(" \5\b\5\2 !\7\6\2\2!\"\7\7\2\2\"#\5\6\4\2#$\7\20\2\2$")
        buf.write("&\3\2\2\2%\21\3\2\2\2%\24\3\2\2\2%\31\3\2\2\2%\33\3\2")
        buf.write("\2\2%\34\3\2\2\2&\5\3\2\2\2\'(\b\4\1\2()\7\16\2\2)*\7")
        buf.write("\5\2\2*+\5\n\6\2+,\7\6\2\2,\64\3\2\2\2-\64\7\17\2\2.\64")
        buf.write("\7\16\2\2/\60\7\5\2\2\60\61\5\6\4\2\61\62\7\6\2\2\62\64")
        buf.write("\3\2\2\2\63\'\3\2\2\2\63-\3\2\2\2\63.\3\2\2\2\63/\3\2")
        buf.write("\2\2\64=\3\2\2\2\65\66\f\b\2\2\66\67\t\2\2\2\67<\5\6\4")
        buf.write("\t89\f\7\2\29:\t\3\2\2:<\5\6\4\b;\65\3\2\2\2;8\3\2\2\2")
        buf.write("<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2>\7\3\2\2\2?=\3\2\2\2@A")
        buf.write("\7\16\2\2AB\7\b\2\2BE\5\b\5\2CE\7\16\2\2D@\3\2\2\2DC\3")
        buf.write("\2\2\2E\t\3\2\2\2FG\5\6\4\2GH\7\b\2\2HI\5\n\6\2IL\3\2")
        buf.write("\2\2JL\5\6\4\2KF\3\2\2\2KJ\3\2\2\2L\13\3\2\2\2\t\17%\63")
        buf.write(";=DK")
        return buf.getvalue()


class ArugulaParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'='", u"'func'", u"'('", u"')'", u"'->'", 
                     u"','", u"'*'", u"'/'", u"'+'", u"'-'", u"'clear'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"MUL", 
                      u"DIV", u"ADD", u"SUB", u"CLEAR", u"ID", u"INT", u"END", 
                      u"WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_params = 3
    RULE_args = 4

    ruleNames =  [ "prog", "stat", "expr", "params", "args" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    MUL=7
    DIV=8
    ADD=9
    SUB=10
    CLEAR=11
    ID=12
    INT=13
    END=14
    WS=15

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArugulaParser.StatContext)
            else:
                return self.getTypedRuleContext(ArugulaParser.StatContext,i)


        def getRuleIndex(self):
            return ArugulaParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ArugulaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stat()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ArugulaParser.T__1) | (1 << ArugulaParser.T__2) | (1 << ArugulaParser.CLEAR) | (1 << ArugulaParser.ID) | (1 << ArugulaParser.INT) | (1 << ArugulaParser.END))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArugulaParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.StatContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def END(self):
            return self.getToken(ArugulaParser.END, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class ClearContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.StatContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def CLEAR(self):
            return self.getToken(ArugulaParser.CLEAR, 0)
        def END(self):
            return self.getToken(ArugulaParser.END, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitClear(self)
            else:
                return visitor.visitChildren(self)


    class DefineContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.StatContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ArugulaParser.ID, 0)
        def params(self):
            return self.getTypedRuleContext(ArugulaParser.ParamsContext,0)

        def expr(self):
            return self.getTypedRuleContext(ArugulaParser.ExprContext,0)

        def END(self):
            return self.getToken(ArugulaParser.END, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitDefine(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.StatContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArugulaParser.ExprContext,0)

        def END(self):
            return self.getToken(ArugulaParser.END, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.StatContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ArugulaParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(ArugulaParser.ExprContext,0)

        def END(self):
            return self.getToken(ArugulaParser.END, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = ArugulaParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 35
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = ArugulaParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(ArugulaParser.END)
                pass

            elif la_ == 2:
                localctx = ArugulaParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(ArugulaParser.ID)
                self.state = 19
                self.match(ArugulaParser.T__0)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(ArugulaParser.END)
                pass

            elif la_ == 3:
                localctx = ArugulaParser.ClearContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(ArugulaParser.CLEAR)
                self.state = 24
                self.match(ArugulaParser.END)
                pass

            elif la_ == 4:
                localctx = ArugulaParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 25
                self.match(ArugulaParser.END)
                pass

            elif la_ == 5:
                localctx = ArugulaParser.DefineContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.match(ArugulaParser.T__1)
                self.state = 27
                self.match(ArugulaParser.ID)
                self.state = 28
                self.match(ArugulaParser.T__2)
                self.state = 29
                self.params()
                self.state = 30
                self.match(ArugulaParser.T__3)
                self.state = 31
                self.match(ArugulaParser.T__4)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(ArugulaParser.END)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArugulaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.ExprContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ArugulaParser.ID, 0)
        def args(self):
            return self.getTypedRuleContext(ArugulaParser.ArgsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.ExprContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArugulaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.ExprContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArugulaParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArugulaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.ExprContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArugulaParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArugulaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.ExprContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ArugulaParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.ExprContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ArugulaParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArugulaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ArugulaParser.CallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 38
                self.match(ArugulaParser.ID)
                self.state = 39
                self.match(ArugulaParser.T__2)
                self.state = 40
                self.args()
                self.state = 41
                self.match(ArugulaParser.T__3)
                pass

            elif la_ == 2:
                localctx = ArugulaParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(ArugulaParser.INT)
                pass

            elif la_ == 3:
                localctx = ArugulaParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(ArugulaParser.ID)
                pass

            elif la_ == 4:
                localctx = ArugulaParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(ArugulaParser.T__2)
                self.state = 46
                self.expr(0)
                self.state = 47
                self.match(ArugulaParser.T__3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 57
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ArugulaParser.MulDivContext(self, ArugulaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 52
                        _la = self._input.LA(1)
                        if not(_la==ArugulaParser.MUL or _la==ArugulaParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 53
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = ArugulaParser.AddSubContext(self, ArugulaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 55
                        _la = self._input.LA(1)
                        if not(_la==ArugulaParser.ADD or _la==ArugulaParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 56
                        self.expr(6)
                        pass

             
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArugulaParser.RULE_params

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MultparamContext(ParamsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.ParamsContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ArugulaParser.ID, 0)
        def params(self):
            return self.getTypedRuleContext(ArugulaParser.ParamsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitMultparam(self)
            else:
                return visitor.visitChildren(self)


    class SingleparamContext(ParamsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.ParamsContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ArugulaParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitSingleparam(self)
            else:
                return visitor.visitChildren(self)



    def params(self):

        localctx = ArugulaParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_params)
        try:
            self.state = 66
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = ArugulaParser.MultparamContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(ArugulaParser.ID)
                self.state = 63
                self.match(ArugulaParser.T__5)
                self.state = 64
                self.params()
                pass

            elif la_ == 2:
                localctx = ArugulaParser.SingleparamContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(ArugulaParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArugulaParser.RULE_args

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MultargContext(ArgsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.ArgsContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArugulaParser.ExprContext,0)

        def args(self):
            return self.getTypedRuleContext(ArugulaParser.ArgsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitMultarg(self)
            else:
                return visitor.visitChildren(self)


    class SingleargContext(ArgsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArugulaParser.ArgsContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArugulaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ArugulaVisitor ):
                return visitor.visitSinglearg(self)
            else:
                return visitor.visitChildren(self)



    def args(self):

        localctx = ArugulaParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_args)
        try:
            self.state = 73
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = ArugulaParser.MultargContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.expr(0)
                self.state = 69
                self.match(ArugulaParser.T__5)
                self.state = 70
                self.args()
                pass

            elif la_ == 2:
                localctx = ArugulaParser.SingleargContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         



