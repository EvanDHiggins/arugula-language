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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\r")
        buf.write(".\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\30\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\5\4!\n\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\7\4)\n\4\f\4\16\4,\13\4\3\4\2\3\6\5\2\4\6\2\4\3\2")
        buf.write("\6\7\3\2\b\t\61\2\t\3\2\2\2\4\27\3\2\2\2\6 \3\2\2\2\b")
        buf.write("\n\5\4\3\2\t\b\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2\13\f")
        buf.write("\3\2\2\2\f\3\3\2\2\2\r\16\5\6\4\2\16\17\7\f\2\2\17\30")
        buf.write("\3\2\2\2\20\21\7\n\2\2\21\22\7\n\2\2\22\23\7\3\2\2\23")
        buf.write("\24\5\6\4\2\24\25\7\f\2\2\25\30\3\2\2\2\26\30\7\f\2\2")
        buf.write("\27\r\3\2\2\2\27\20\3\2\2\2\27\26\3\2\2\2\30\5\3\2\2\2")
        buf.write("\31\32\b\4\1\2\32!\7\13\2\2\33!\7\n\2\2\34\35\7\4\2\2")
        buf.write("\35\36\5\6\4\2\36\37\7\5\2\2\37!\3\2\2\2 \31\3\2\2\2 ")
        buf.write("\33\3\2\2\2 \34\3\2\2\2!*\3\2\2\2\"#\f\7\2\2#$\t\2\2\2")
        buf.write("$)\5\6\4\b%&\f\6\2\2&\'\t\3\2\2\')\5\6\4\7(\"\3\2\2\2")
        buf.write("(%\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\7\3\2\2\2,*")
        buf.write("\3\2\2\2\7\13\27 (*")
        return buf.getvalue()


class ArugulaParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'='", u"'('", u"')'", u"'*'", u"'/'", 
                     u"'+'", u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"MUL", u"DIV", u"ADD", u"SUB", u"ID", u"INT", u"END", 
                      u"WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    MUL=4
    DIV=5
    ADD=6
    SUB=7
    ID=8
    INT=9
    END=10
    WS=11

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
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ArugulaParser.T__1) | (1 << ArugulaParser.ID) | (1 << ArugulaParser.INT) | (1 << ArugulaParser.END))) != 0)):
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ArugulaParser.ID)
            else:
                return self.getToken(ArugulaParser.ID, i)
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
            self.state = 21
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = ArugulaParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.expr(0)
                self.state = 12
                self.match(ArugulaParser.END)
                pass

            elif la_ == 2:
                localctx = ArugulaParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(ArugulaParser.ID)
                self.state = 15
                self.match(ArugulaParser.ID)
                self.state = 16
                self.match(ArugulaParser.T__0)
                self.state = 17
                self.expr(0)
                self.state = 18
                self.match(ArugulaParser.END)
                pass

            elif la_ == 3:
                localctx = ArugulaParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 20
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
            self.state = 30
            token = self._input.LA(1)
            if token in [ArugulaParser.INT]:
                localctx = ArugulaParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 24
                self.match(ArugulaParser.INT)

            elif token in [ArugulaParser.ID]:
                localctx = ArugulaParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(ArugulaParser.ID)

            elif token in [ArugulaParser.T__1]:
                localctx = ArugulaParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(ArugulaParser.T__1)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.match(ArugulaParser.T__2)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ArugulaParser.MulDivContext(self, ArugulaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 33
                        _la = self._input.LA(1)
                        if not(_la==ArugulaParser.MUL or _la==ArugulaParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 34
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ArugulaParser.AddSubContext(self, ArugulaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 36
                        _la = self._input.LA(1)
                        if not(_la==ArugulaParser.ADD or _la==ArugulaParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 37
                        self.expr(5)
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         



