grammar Calculate;

expr:NUMBER
    |list
    | expr OPERATION expr
    ;
list: '(' expr ')';
NUMBER:INT* ('.')* INT*;
INT:[0-9];
OPERATION:'+'
    | '-'
    | '*'
    | '/'
    ;