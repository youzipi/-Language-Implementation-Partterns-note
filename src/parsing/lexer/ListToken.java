package parsing.lexer;

/**
 * project_name:LIP
 * package_name:lexer
 * user: youzipi
 * date: 2015/3/10
 */
public class ListToken extends Token{


    public ListToken(int type, String text) {
        super(type, text);
    }

    @Override
    public String toString() {
        String tname = ListLexer.tokenNames[type];
        return "<'"+text+"',"+tname+">";
    }
}
