package parsing.recursive_descent;

import parsing.lexer.Lexer;
import parsing.lexer.Token;

/**
 * project_name:LIP
 * package_name:parsing.recursive_descent
 * user: youzipi
 * date: 2015/3/30
 */
public class Parser {
    Lexer input;
    Token lookahead;

    public Parser(Lexer input) {
        this.input = input;
    }

    public void match(int x){
        if ( lookahead.type == x){
            consume();
        }
    }

    private void consume() {
        lookahead = input.nextToken();
    }
}
