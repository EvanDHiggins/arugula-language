# Generated from java-escape by ANTLR 4.5
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\r")
        buf.write("?\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\6\t)")
        buf.write("\n\t\r\t\16\t*\3\n\6\n.\n\n\r\n\16\n/\3\13\5\13\63\n\13")
        buf.write("\3\13\3\13\5\13\67\n\13\3\f\6\f:\n\f\r\f\16\f;\3\f\3\f")
        buf.write("\2\2\r\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\3\2\5\4\2C\\c|\3\2\62;\4\2\13\13\"\"C\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\3\31\3\2\2\2\5\33\3\2\2\2\7\35\3\2\2")
        buf.write("\2\t\37\3\2\2\2\13!\3\2\2\2\r#\3\2\2\2\17%\3\2\2\2\21")
        buf.write("(\3\2\2\2\23-\3\2\2\2\25\66\3\2\2\2\279\3\2\2\2\31\32")
        buf.write("\7?\2\2\32\4\3\2\2\2\33\34\7*\2\2\34\6\3\2\2\2\35\36\7")
        buf.write("+\2\2\36\b\3\2\2\2\37 \7,\2\2 \n\3\2\2\2!\"\7\61\2\2\"")
        buf.write("\f\3\2\2\2#$\7-\2\2$\16\3\2\2\2%&\7/\2\2&\20\3\2\2\2\'")
        buf.write(")\t\2\2\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\22")
        buf.write("\3\2\2\2,.\t\3\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3")
        buf.write("\2\2\2\60\24\3\2\2\2\61\63\7\17\2\2\62\61\3\2\2\2\62\63")
        buf.write("\3\2\2\2\63\64\3\2\2\2\64\67\7\f\2\2\65\67\7=\2\2\66\62")
        buf.write("\3\2\2\2\66\65\3\2\2\2\67\26\3\2\2\28:\t\4\2\298\3\2\2")
        buf.write("\2:;\3\2\2\2;9\3\2\2\2;<\3\2\2\2<=\3\2\2\2=>\b\f\2\2>")
        buf.write("\30\3\2\2\2\b\2*/\62\66;\3\b\2\2")
        return buf.getvalue()


class ArugulaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    MUL = 4
    DIV = 5
    ADD = 6
    SUB = 7
    ID = 8
    INT = 9
    END = 10
    WS = 11

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            "'='", "'('", "')'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ u"<INVALID>",
            "MUL", "DIV", "ADD", "SUB", "ID", "INT", "END", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "MUL", "DIV", "ADD", "SUB", "ID", 
                  "INT", "END", "WS" ]

    grammarFileName = "Arugula.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


