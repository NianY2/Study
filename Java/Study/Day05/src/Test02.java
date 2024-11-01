import java.util.Scanner;

//2.通过键盘录入两个整数n和m。n代表行数，m代表列数。定义一个方法，方法的功能是打印n行m列的@符号。执行效果如下：
//        ```
//        请输入行数：
//        4
//        请输入列数：
//        5
//@@@@@
//@@@@@
//@@@@@
//@@@@@
//```
public class Test02 {
    public  static  void print(int n,int m){
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print("@");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("行数n:");
        int n = sc.nextInt();
        System.out.print("列数m:");
        int m = sc.nextInt();
        print(n,m);
    }
}
