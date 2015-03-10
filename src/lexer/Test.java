package lexer;

/**
 * project_name:LIP
 * user: youzipi
 * date: 2015/3/10
 */
public class Test {
    public static void main(String[] args) {
        String s = "[1,sss,{5},4.5]";
//        ListLexer lexer = new ListLexer(args[0]);
        ListLexer lexer = new ListLexer(s);
        ListToken t = lexer.nextToken();
        while (t.type != Lexer.EOF_TYPE){
            System.out.println(t);
            t = lexer.nextToken();
        }
        System.out.println(t);
    }
}
