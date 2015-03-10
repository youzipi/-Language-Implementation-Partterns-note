package lexer;

import java.util.Stack;

/**
 * project_name:LIP
 * package_name:lexer
 * user: youzipi
 * date: 2015/3/10
 */
public class CalculateTest {


    public static double calculate(String num1, String num2, String operation){
        double n1 = Double.parseDouble(num1);
        double n2 = Double.parseDouble(num2);
        double result;
        char op = operation.charAt(0);
        switch (op){
            case '+':
                return n1+n2;
            case '-':
                return n1-n2;
            case '*':
                return n1*n2;
            case '/':
                if(n2 == 0)
                    throw new Error("division by zero");
                return n1/n2;
            default:
                throw new Error("operation not recongized");
        }
    }
    public static void main(String[] args) {
        String s = "15*5";
        CalculateLexer lexer = new CalculateLexer(s);
        CalculateToken t = lexer.nextToken();
        Stack<CalculateToken> nstack = new Stack<CalculateToken>();
        Stack<CalculateToken> ostack = new Stack<CalculateToken>();
//        while (t.type != Lexer.EOF_TYPE){
//            System.out.println(t);
//            t = lexer.nextToken();
//        }
        while(t.type != Lexer.EOF_TYPE){
            if (t.type == CalculateLexer.NUMBER)
                nstack.push(t);
            else
                ostack.push(t);
            t = lexer.nextToken();
        }

        Double result = null;
        while (!ostack.empty()){
            String operation = ostack.pop().text;
            String num1 = nstack.pop().text;
            String num2 = nstack.pop().text;
//            System.out.println(num1+num2+operation);
            result = calculate(num1,num2,operation);
        }
        System.out.println(t);
        System.out.println(result);
    }
}
