package parsing.lexer;

/**
 * project_name:LIP
 * package_name:lexer
 * user: youzipi
 * date: 2015/3/10
 */
public class ListLexer extends Lexer {
    public static int NAME = 2;
    public static int COMMA = 3;
    public static int LBREAK = 4;
    public static int RBREAK = 5;

    public static String[] tokenNames = {"n/a", "<EOF>", "NAME", "COMMA", "LBREAK", "RBREAK"};

    public ListLexer(String input) {
        super(input);
    }

    @Override
    public String getTokenName(int x) {
        return tokenNames[x];
    }

    @Override
    public ListToken nextToken() {
        ListToken t;
        while (c != EOF) {
            switch (c) {
                case ' ':
                case '\t':
                case '\n':
                case '\r':
                    WS();
                    continue;
                case ',':
                    consume();
                    return new ListToken(COMMA, ",");
                case '[':
                case '(':
                case '{':
                    t = new ListToken(LBREAK, String.valueOf(c));
                    consume();
                    return t;
                case ']':
                case ')':
                case '}':
                    t = new ListToken(RBREAK, String.valueOf(c));
                    consume();
                    return t;
                default:        //普通字符
                    if (isWORD())
                        return NAME();
                    throw new Error("invalid character: " + c);


            }
        }
        return new ListToken(EOF_TYPE, "EOF");
    }


    boolean isWORD() {
        return isLETTER() || isNUMBER() || isPOINT();

    }


    /**
     * ignore all whitespaces
     * WS:(' '|'\t'|'\n'|'\r')*
     */
    void WS() {
        while (c == ' ' || c == '\t' || c == '\n' || c == '\r') {
            consume();
        }
    }

    /**
     * NAME:('a'..'z'|'A'..'Z'|'0'..'9'|'.'|)+
     */
    ListToken NAME() {
        StringBuilder builder = new StringBuilder();
        do {
            builder.append(c);
            consume();
        } while (isWORD());
        return new ListToken(NAME, builder.toString());
    }
}
