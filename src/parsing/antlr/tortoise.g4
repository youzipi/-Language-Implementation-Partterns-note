grammar tortoise;

program:command+;
command: walk
    |left
    |right
    ;
walk:'walk ' INT la;
left:'left ' INT la;
right:'right ' INT la;
la:('\n')?;
INT:[0-9]+;
