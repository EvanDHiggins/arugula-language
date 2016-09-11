# Generated from java-escape by ANTLR 4.5
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\21")
        buf.write("W\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\6\rA\n\r")
        buf.write("\r\r\16\rB\3\16\6\16F\n\16\r\16\16\16G\3\17\5\17K\n\17")
        buf.write("\3\17\3\17\5\17O\n\17\3\20\6\20R\n\20\r\20\16\20S\3\20")
        buf.write("\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21\3\2\5\4\2C\\c|\3\2")
        buf.write("\62;\4\2\13\13\"\"[\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2")
        buf.write("\2\2\5#\3\2\2\2\7(\3\2\2\2\t*\3\2\2\2\13,\3\2\2\2\r/\3")
        buf.write("\2\2\2\17\61\3\2\2\2\21\63\3\2\2\2\23\65\3\2\2\2\25\67")
        buf.write("\3\2\2\2\279\3\2\2\2\31@\3\2\2\2\33E\3\2\2\2\35N\3\2\2")
        buf.write("\2\37Q\3\2\2\2!\"\7?\2\2\"\4\3\2\2\2#$\7h\2\2$%\7w\2\2")
        buf.write("%&\7p\2\2&\'\7e\2\2\'\6\3\2\2\2()\7*\2\2)\b\3\2\2\2*+")
        buf.write("\7+\2\2+\n\3\2\2\2,-\7/\2\2-.\7@\2\2.\f\3\2\2\2/\60\7")
        buf.write(".\2\2\60\16\3\2\2\2\61\62\7,\2\2\62\20\3\2\2\2\63\64\7")
        buf.write("\61\2\2\64\22\3\2\2\2\65\66\7-\2\2\66\24\3\2\2\2\678\7")
        buf.write("/\2\28\26\3\2\2\29:\7e\2\2:;\7n\2\2;<\7g\2\2<=\7c\2\2")
        buf.write("=>\7t\2\2>\30\3\2\2\2?A\t\2\2\2@?\3\2\2\2AB\3\2\2\2B@")
        buf.write("\3\2\2\2BC\3\2\2\2C\32\3\2\2\2DF\t\3\2\2ED\3\2\2\2FG\3")
        buf.write("\2\2\2GE\3\2\2\2GH\3\2\2\2H\34\3\2\2\2IK\7\17\2\2JI\3")
        buf.write("\2\2\2JK\3\2\2\2KL\3\2\2\2LO\7\f\2\2MO\7=\2\2NJ\3\2\2")
        buf.write("\2NM\3\2\2\2O\36\3\2\2\2PR\t\4\2\2QP\3\2\2\2RS\3\2\2\2")
        buf.write("SQ\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\b\20\2\2V \3\2\2\2\b")
        buf.write("\2BGJNS\3\b\2\2")
        return buf.getvalue()


class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    MUL = 7
    DIV = 8
    ADD = 9
    SUB = 10
    CLEAR = 11
    ID = 12
    INT = 13
    END = 14
    WS = 15

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            "'='", "'func'", "'('", "')'", "'->'", "','", "'*'", "'/'", 
            "'+'", "'-'", "'clear'" ]

    symbolicNames = [ u"<INVALID>",
            "MUL", "DIV", "ADD", "SUB", "CLEAR", "ID", "INT", "END", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "MUL", 
                  "DIV", "ADD", "SUB", "CLEAR", "ID", "INT", "END", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


