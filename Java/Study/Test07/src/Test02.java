import java.util.Scanner;
import java.util.regex.Pattern;

/*
* 我国的居民身份证号码，由由十七位数字本体码和一位数字校验码组成。请定义方法判断用户输入的身份证号码是否合法，
* 并在主方法中调用方法测试结果。
* 规则为：号码为18位，不能以数字0开头，前17位只可以是数字，最后一位可以是数字或者大写字母X。
* */
public class Test02 {
    public  static  boolean isIDCcrd(String s){
        return Pattern.matches("[1-9]\\d{16}[0-9|X]",s);
    }
    public static void main(String[] args) {
//        500225199707256876
//        50022519970725687X
//        00022519970725687X
        Scanner sc =new Scanner(System.in);
        System.out.println(isIDCcrd(sc.nextLine()));
    }
}
