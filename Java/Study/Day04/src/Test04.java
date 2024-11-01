import java.util.Scanner;

//有一个数组，其中有十个元素从小到大依次排列
//        {12,14,23,45,66,68,70,77,90,91}。再通过键盘录入一个整数数字。
//        要求：把数字放入数组序列中，生成一个新的数组，并且数组的元素依旧是从小到大排列的。执行效果如下：
public class Test04 {
    public static void main(String[] args) {
        int[] list1 = {12,14,23,45,66,68,70,77,90,91};
        int[] list2 = new  int[list1.length+1];
        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入一个整数数字：");
        int num1 = scanner.nextInt();
        int index = list1.length;
        for (int i = 0; i < list1.length; i++) {
            if(num1<=list1[i] && index == list1.length){
                index = i;
            }
            if(num1<=list1[i]){
                list2[i+1] = list1[i];
            } else {
                list2[i] = list1[i];
            }
        }
        list2[index] = num1;
//        生成的新数组是：12 14 23 45 50 66 68 70 77 90
        System.out.print("生成的新数组是：");
        for (int j = 0; j < list2.length; j++) {
            System.out.print(list2[j]+" ");
        }
    }
}
