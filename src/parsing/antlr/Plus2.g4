grammar Plus2;

ee: ee '+' ee
    | ee '*' ee
    | '(' ee ')'
    |'a'
    ;

