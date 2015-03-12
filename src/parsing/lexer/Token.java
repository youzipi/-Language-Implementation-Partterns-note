package parsing.lexer;

/**
 * project_name:LIP
 * package_name:lexer
 * user: youzipi
 * date: 2015/3/10
 */
public class Token {
    public int type;
    public String text;

    public Token(int type, String text) {
        this.type = type;
        this.text = text;
    }
}
