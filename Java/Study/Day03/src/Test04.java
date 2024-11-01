import java.util.Random;
import java.util.Scanner;

//4.（选做）猜数字游戏
//        随机生成一个1-100之间的数据，提示用户猜测，
//        猜大提示过大，猜小提示过小，直到猜中结束游戏。
public class Test04 {
    public static void main(String[] args) {
        Random random = new Random();
        int num = random.nextInt(100)+1;
        System.out.println("答案是："+num);
        System.out.print("请输入你的答案：");
        Scanner sc = new Scanner(System.in);
        int res = sc.nextInt();
        while (res != num){
            if(res > num){
                System.out.println("大了");
            }else {
                System.out.println("小了");
            }
            System.out.print("请输入你的答案：");
            res = sc.nextInt();
        }
        System.out.println("猜中了，结束游戏");
    }
}
