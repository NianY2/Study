package Day04;
//定义一个数组来存储10个学生的成绩，例如：{72, 89, 65, 87, 91, 82, 71, 93, 76, 68}。计算并输出学生的平均成绩。
public class Test03 {
    public static void main(String[] args) {
        double[] list1 = {72, 89, 65, 87, 91, 82, 71, 93, 76, 68};
        double num = 0;
        for (int i = 0; i < list1.length; i++) {
            num+=list1[i];
        }
        System.out.println(num/list1.length);
    }
}
