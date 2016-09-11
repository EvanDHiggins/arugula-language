grammar Expr;

prog: stat+ ;

stat:   expr END            # printExpr
    |   ID '=' expr END     # assign
    |   CLEAR END           # clear
    |   END                 # blank
    |   'func' ID '(' params ')' '->' expr END # define
    ;

expr:   expr ('*'|'/') expr     # MulDiv
    |   expr ('+'|'-') expr     # AddSub
    |   ID '(' args ')'         # call
    |   INT                     # int
    |   ID                      # id
    |   '(' expr ')'            # parens
    ;

params: ID ',' params           # multparam
     | ID                       # singleparam
     ;

args: expr ',' args             # multarg
    | expr                      # singlearg
    ;

MUL: '*' ;
DIV: '/' ;
ADD: '+' ;
SUB: '-' ;

CLEAR: 'clear' ;
ID: [a-zA-Z]+ ;
INT: [0-9]+ ;
END: ('\r'? '\n')|';' ;
WS : [ \t]+ -> skip ;         
