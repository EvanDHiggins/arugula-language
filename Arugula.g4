grammar Arugula;

prog: stat+ ;

stat:   expr END            # printExpr
    |   ID '=' expr END     # assign
    |   END                 # blank
    ;

expr:   expr ('*'|'/') expr     # MulDiv
    |   expr ('+'|'-') expr     # AddSub
    |   INT                     # int
    |   ID                      # id
    |   '(' expr ')'            # parens
    ;

MUL: '*' ;
DIV: '/' ;
ADD: '+' ;
SUB: '-' ;

ID: [a-zA-Z]+ ;
INT: [0-9]+ ;
END: ('\r'? '\n')|';' ;
WS : [ \t]+ -> skip ;         
