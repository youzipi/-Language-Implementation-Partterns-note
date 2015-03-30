package parsing.backtrack;


import parsing.lexer.Lexer;
import parsing.lexer.Token;
import parsing.recursive_descent.ListParser;

import java.util.List;

/**
 * project_name:LIP
 * package_name:parsing.backtrack
 * user: youzipi
 * date: 2015/3/30
 */
public class Parser extends ListParser{
    Lexer input;
    List<Integer> markers;
    List<Token> lookahead;
    int p =0;

    public Parser(Lexer input) {
        super(input);
    }


    public Token LT(int i){
        sync(i);
        return lookahead.get(p+i-1);
    }

    public int LA(int i ){
        return LT(i).type;
    }

    public void match(int x) {
        if(LA(1) == x){
            consume();
        }
        else {
            throw new Error("excepting" + input.getTokenName(x) + ";found " + LT(1));
        }
    }

    private void consume() {
        p++;
        if(p==lookahead.size() && !isSpeculating()){
            p=0;
            lookahead.clear();
        }
        sync(1);
    }

    private boolean isSpeculating() {
        return markers.size() > 0;
    }

    private void sync(int i) {
        if(p+i-1>(lookahead.size()-1)){
            int n = (p+i-1)-(lookahead.size()-1);
            fill(n);
        }
    }

    private void fill(int n) {
        for (int i = 0; i < n; i++) {
            lookahead.add(input.nextToken());
        }
    }
}
