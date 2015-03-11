package integer;

/**
 * project_name:LIP
 * package_name:integer
 * user: youzipi
 * date: 2015/3/11
 */
public class ParseIntTest {
    public static void main(String[] args) {
        String s = "25";
        int num = Integer.parseInt(s);
        int num2 = Integer.valueOf(s);
        System.out.println(num);
        System.out.println(num2);
        System.out.println(256>>>8);
    }
}
