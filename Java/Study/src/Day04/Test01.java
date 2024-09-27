package Day04;
//现有一个小数数组{12.9, 53.54, 75.0, 99.1, 3.14}。请编写代码，找出数组中的最小值并打印。
public class Test01 {
    public static void main(String[] args) {
        double[] list1 = {12.9, 53.54, 75.0, 99.1, 3.14};
        double min_num = list1[0];
        for (int i = 1; i < list1.length; i++) {
            if(min_num > list1[i]){
                min_num = list1[i];
            }
        }
        System.out.println(min_num);
    }
}
