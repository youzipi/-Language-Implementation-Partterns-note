package parsing.recursive_descent;

import parsing.lexer.Lexer;
import parsing.lexer.ListLexer;

/**
 * project_name:LIP
 * package_name:parsing.recursive_descent
 * user: youzipi
 * date: 2015/3/30
 */
public class ListParser extends Parser {
    public ListParser(Lexer input) {
        super(input);
    }

    public void list(){
        match(ListLexer.LBREAK);
        elements();
        match(ListLexer.RBREAK);
    }

    private void elements() {
        element();
        while (lookahead.type == ListLexer.COMMA){
            match(ListLexer.COMMA);
            element();
        }
    }

    private void element() {
        if(lookahead.type == ListLexer.NAME){
            match(ListLexer.NAME);
        }
        else if (lookahead.type == ListLexer.LBREAK){
            list();
        }
        else {
            throw new Error("Excepting name or list; found "+lookahead);
        }
    }
}
