package parsing.backtrack;


import org.antlr.v4.runtime.RecognitionException;
import parsing.lexer.Lexer;
import parsing.lexer.ListLexer;

/**
 * project_name:LIP
 * package_name:parsing.backtrack
 * user: youzipi
 * date: 2015/3/30
 */
public class BacktrackParser extends Parser{


    public BacktrackParser(Lexer input) {
        super(input);
    }

    public void stat(){
        if (speculate_stst_alt1()){
            list();
            match(Lexer.EOF_TYPE);
        }
        else if(speculate_stst_alt2()){
            assign();
            match(Lexer.EOF_TYPE);
        }
        else throw new Error("expecting stst;found"+LT(1));
    }

    public boolean speculate_stst_alt1(){
        boolean result = true;
        mark();
        try {
            list();
            match(Lexer.EOF_TYPE);
        }
        catch (RecognitionException e){
            result =false;
        }
        release();
        return result;
    }

    public boolean speculate_stst_alt2(){
        boolean result = true;
        mark();
        try {
            assign();
            match(Lexer.EOF_TYPE);
        }
        catch (RecognitionException e){
            result =false;
        }
        release();
        return result;
    }

    private void release() {
        int marker = markers.get(markers.size()-1);
        markers.remove(markers.size()-1);
        seek(marker);
    }

    private void seek(int index) {
        p = index;
    }

    private int mark() {
        markers.add(p);
        return p;
    }

    private void assign() {
        list();
        match(ListLexer.EQUAL);
        list();
    }


}
