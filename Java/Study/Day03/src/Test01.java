import java.util.Scanner;

//1.  编写程序实现等级奖励制度划分,输入考试成绩,
//  程序会相应输出相应的奖励信息。
public class Test01 {
    public static void main(String[] args) {
        System.out.print("请输入分数：");
        Scanner sc = new Scanner(System.in);
        int sum = sc.nextInt();
        if (sum>100 || sum < 0){
            System.out.println("输入的数字应在0-100之间");
        }else if(sum>=95){
            System.out.println("自行车");
        }else if(sum>=90){
            System.out.println("去公园");
        }else if(sum>=80){
            System.out.println("机器人");
        }else if(sum>=0){
            System.out.println("乱棍打死");
        }
    }
}
