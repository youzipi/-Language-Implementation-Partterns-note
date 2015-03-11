package lexer;

/**
 * project_name:LIP
 * package_name:lexer
 * user: youzipi
 * date: 2015/3/10
 */
public class CalculateLexer extends Lexer {
    public static int NUMBER = 3;
    public static int LBREAK = 4;
    public static int RBREAK = 5;
    public static int ADD = 6;
    public static int SUBTRACT = 7;
    public static int MULTIPLY = 8;
    public static int DIVIDE = 9;
    public static int OPERATION = 10;

//    public static String[] tokenNames = {"n/a", "<EOF>", "NAME", "NUMBER", "LBREAK", "RBREAK","ADD","SUBTRACT","MULTIPLY","DIVIDE"};
    public static String[] tokenNames = {"n/a", "<EOF>", "NAME", "NUMBER", "LBREAK", "RBREAK","ADD","SUBTRACT","MULTIPLY","DIVIDE","OPERATION"};

    public CalculateLexer(String input) {
        super(input);
    }

    @Override
    public CalculateToken nextToken() {
        while (c != EOF){
            CalculateToken t;
            switch (c){
                case ' ':
                    WS();
                    continue;
                case '(':
                    consume();
                    return new CalculateToken(LBREAK, "(");
                case ')':
                    consume();
                    return new CalculateToken(RBREAK, ")");
                case '+':
                    consume();
                    return new CalculateToken(ADD, "+");
                case '-':
                    consume();
                    return new CalculateToken(SUBTRACT, "-");
                case '*':
                    consume();
                    return new CalculateToken(MULTIPLY, "*");
                case '/':
                    consume();
                    return new CalculateToken(DIVIDE, "/");
                default:
                    if(isNUMBER() || isPOINT())
                        return NUMBER();
                    throw new Error("invalid character: " + c);
            }
        }
        return new CalculateToken(EOF_TYPE, "EOF");
    }

//    @Override
//    public Token prevToken() {
//        while (c != EOF){
//            CalculateToken t;
//            switch (c){
//                case ' ':
//                    WS();
//                    continue;
//                case '(':
//                    consume();
//                    return new CalculateToken(LBREAK, "(");
//                case ')':
//                    consume();
//                    return new CalculateToken(RBREAK, ")");
//                case '+':
//                case '-':
//                case '*':
//                case '/':
//                    t = new CalculateToken(DIVIDE, String.valueOf(c));
//                    consume();
//                    return t;
//                default:
//                    if(isNUMBER() || isPOINT())
//                        return NUMBER();
//                    throw new Error("invalid character: " + c);
//            }
//        }
//        return new CalculateToken(EOF_TYPE, "EOF");
//    }

    @Override
    public String getTokenName(int tokenType) {
        return null;
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
     * NUMBER:('0'..'9'|'.'|)+
     */
    CalculateToken NUMBER() {
        StringBuilder builder = new StringBuilder();
        do {
            builder.append(c);
            consume();
        } while (isNUMBER() || isPOINT());
        return new CalculateToken(NUMBER, builder.toString());
    }
}
