
grammar c;

assign_stmt:ID '=' expr;
expr:ID
    |expr (OPERATION expr)
    |'(' expr ')'
    |NUMBER
    ;
ID:[a-zA-Z]+;
NUMBER:INT* ('.')* INT*;
INT:[0-9];
OPERATION:'+'
    | '-'
    | '*'
    | '/'
    ;