import java.util.Scanner;

/*
* 请编写程序，由键盘录入一个字符串，
* 统计字符串中英文字母和数字分别有多少个。
* 比如：Hello12345Java中字母：9个，数字：5个
* */
public class Test01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s =  sc.nextLine();
        int ans1 = 0;
        int ans2 = 0;

        for (int i = 0; i < s.length(); i++) {
            if(Character.isLetter(s.charAt(i))){
                ans1++;
            }
            if(Character.isDigit(s.charAt(i))){
                ans2++;
            }
        }
        System.out.println(ans1);
        System.out.println(ans2);
    }
}
