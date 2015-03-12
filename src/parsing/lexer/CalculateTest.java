package parsing.lexer;

import java.util.LinkedList;
import java.util.Stack;

/**
 * project_name:LIP
 * package_name:lexer
 * user: youzipi
 * date: 2015/3/10
 */
public class CalculateTest {

    static LinkedList<CalculateToken> in2post(LinkedList<CalculateToken> infixList){
        Stack<CalculateToken> ostack = new Stack<CalculateToken>();
        LinkedList<CalculateToken> postfixList = new LinkedList<CalculateToken>();
        int level = 0;
        for(CalculateToken token:infixList)
            switch (token.text.charAt(0)) {
                case ('('):
                    ostack.push(token);
                    continue;
                case (')'):
                    if(ostack.empty()){
                        ostack.push(token);
                        continue;
                    }
                    CalculateToken token1 = ostack.peek();
                    while (token1.text.charAt(0) != '(') {
                        token1 = ostack.pop();
                        if (token1.text.charAt(0) == '('){
                            break;
                        }
                        postfixList.add(token1);
                        if(ostack.empty())
                            break;
                        else
                            token1 = ostack.peek();
                    }
                    continue;
                case ('+'):
                case ('-'):
                    if(ostack.empty()){
                        ostack.push(token);
                        continue;
                    }
                    CalculateToken token2 = ostack.peek();
                    while ((token2.type >= CalculateLexer.MULTIPLY) && (token2.text.charAt(0) != '(') && !ostack.empty()) {
                        token2 = ostack.pop();
                        postfixList.add(token2);
                        if(ostack.empty())
                            break;
                        else
                            token2 = ostack.peek();
                    }
                    ostack.push(token);
                    continue;
                case ('*'):
                case ('/'):
                    if(ostack.empty()){
                        ostack.push(token);
                        continue;
                    }
                    CalculateToken token3 = ostack.peek();
                    while (token3.text.charAt(0) != '(') {
                        token3 = ostack.pop();
                        postfixList.add(token3);
                    }
                    postfixList.add(token);
                    continue;
                default:
                    postfixList.add(token);
            }
        while (!ostack.empty()){
            postfixList.add(ostack.pop());
        }
        return postfixList;
    }


    /**
     * 对前缀表达式进行计算
     * @param postfixList 前缀表达式
     * @return 计算结果
     */
    public static double calculate(LinkedList<CalculateToken> postfixList){
        Stack<Double> temp = new Stack<Double>();
        Double result = 0.0;
        for(CalculateToken token : postfixList){
            switch (token.type){
                case (3):   //NUMBER
                    temp.push(Double.parseDouble(token.text));
                    continue;
                case (6):  //OPERATION
                case (7):  //OPERATION
                case (8):  //OPERATION
                case (9):  //OPERATION
                case (10):  //OPERATION
                    Double num1 = temp.pop();
                    Double num2 = temp.pop();
                    result = calculate(num1,num2,token.text);
                    temp.push(result);
                    continue;
                default:
                    throw new Error("cannot reconginzed "+token.text);
            }
        }
        return result;
    }

    /**
     * 执行简单计算
     * @param n1 参数一
     * @param n2 参数二
     * @param operation 操作符
     * @return 计算结果
     */
    public static double calculate(double n1, double n2, String operation){
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
                    throw new Error("divided by zero");
                return n1/n2;
            default:
                throw new Error("operation not recongized");
        }
    }

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
                    throw new Error("divided by zero");
                return n1/n2;
            default:
                throw new Error("operation not recongized");
        }
    }
    public static void main(String[] args) {
        String s = "15*(5+5)";
        CalculateLexer lexer = new CalculateLexer(s);
        CalculateToken t = lexer.nextToken();
        Stack<CalculateToken> nstack = new Stack<CalculateToken>();
        Stack<CalculateToken> ostack = new Stack<CalculateToken>();
        LinkedList<CalculateToken> infixList = new LinkedList<CalculateToken>();
        LinkedList<CalculateToken> postfixList = new LinkedList<>();
        Double result;

        while (t.type != Lexer.EOF_TYPE){
            infixList.add(t);
            t = lexer.nextToken();
        }
        for(CalculateToken token : infixList){
            System.out.println(token.text);
        }
        postfixList = in2post(infixList);
        System.out.println("post");
        for(CalculateToken token : postfixList){
            System.out.println(token.text);
        }
//        result = calculate(postfixList);
//        System.out.println(result);


//        while(t.type != Lexer.EOF_TYPE){
//            if (t.type == CalculateLexer.NUMBER)
//                nstack.push(t);
//            else
//                ostack.push(t);
//            t = lexer.nextToken();
//        }
//
//        Double result = null;
//        while (!ostack.empty()){
//            String operation = ostack.pop().text;
//            String num1 = nstack.pop().text;
//            String num2 = nstack.pop().text;
////            System.out.println(num1+num2+operation);
//            result = calculate(num1,num2,operation);
//        }
//        System.out.println(t);
//        System.out.println(result);

    }
}
