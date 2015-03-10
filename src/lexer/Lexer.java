package lexer;

/**
 * project_name:LIP
 * package_name:lexer
 * user: youzipi
 * date: 2015/3/10
 */
public abstract class Lexer {
    public static final char EOF = (char) -1;
    public static final int EOF_TYPE = 1;

    String input;
    int p = 0;//当前输入字符下标
    char c;//当前字符

    public Lexer(String input) {
        this.input = input;
        c = input.charAt(p);//将第一个字符赋给c
    }

    /**
     * 1.向后移动一个字符
     * 2.检测结束
     */
    public void consume() {
        p++;
        if (p >= input.length())
            c = EOF;
        else
            c = input.charAt(p);
    }

    public void back() {
        p--;
        if (p == 0)
            c = EOF;
        else
            c = input.charAt(p);
    }

    public void match(char x) {
        if (c == x)
            consume();
        else
            throw new Error("expecting " + x + "; found " + c);
    }

    public abstract Token nextToken();
//    public abstract Token prevToken();
    public abstract String getTokenName(int tokenType);


    boolean isLETTER() {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
    }

    boolean isNUMBER() {
        return (c >= '0' && c <= '9');
    }

    boolean isPOINT() {
        return c == '.';
    }
}
