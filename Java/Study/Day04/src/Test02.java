import java.util.Random;

//创建一个长度为6的整数数组。请编写代码，随机生成六个0（包含）-100（不包含）
// 之间的整数存放到数组中，然后计算出数组中所有元素的和并打印。
public class Test02 {
    public static void main(String[] args) {
        int[] list1 = new int[6];
        Random random = new Random();
        for (int i = 0; i < 6; i++) {
            list1[i] = random.nextInt(100);
        }
        int num = 0;
        for (int i = 0; i < list1.length; i++) {
            num+=list1[i];
        }
        System.out.print("生成的新数组是：");
        for (int j = 0; j < list1.length; j++) {
            System.out.print(list1[j]+" ");
        }
        System.out.println();
        System.out.println(num);
    }
}
