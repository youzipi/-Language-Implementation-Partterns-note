grammar Plus;

ee: bb '+' bb
    | bb
    ;
bb: bb '*' bb
    |'a'
    |'(' ee ')'
    ;

