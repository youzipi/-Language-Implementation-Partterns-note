package lexer;

/**
 * project_name:LIP
 * package_name:lexer
 * user: youzipi
 * date: 2015/3/10
 */
public class CalculateToken extends Token{

    public CalculateToken(int type, String text) {
        super(type,text);
    }

    @Override
    public String toString() {
        String tname = CalculateLexer.tokenNames[type];
        return "<'"+text+"',"+tname+">";
    }
}
