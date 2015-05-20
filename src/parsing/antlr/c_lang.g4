grammar c_lang;

program:keywords 'main' '{' expr '}';
expr:id
    |num;
id : letter+;
letter:('a'..'z')
    | ('A'..'Z')
    | '_';
num:'1'..'9' ('0'..'9'|'.')*;
keywords:'int'