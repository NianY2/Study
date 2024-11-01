//定义一个数组其中包含多个数字。用自己的方式最终实现，
// 奇数放在数组的左边，偶数放在数组的右边。（可以创建其他数组，不必须在原数组中改变）
public class Test05 {
    public static void main(String[] args) {
        int[] list1 = {12,14,23,45,66,68,70,77,90,91};
        int[] list2 = new int[list1.length];
        int right = list1.length-1,left = 0;
        for (int i = 0; i < list1.length; i++) {
            if(list1[i] % 2 == 0){
                list2[right] = list1[i];
                right--;
            }else {
                list2[left] = list1[i];
                left++;
            }
        }
        System.out.print("生成的新数组是：");
        for (int j = 0; j < list2.length; j++) {
            System.out.print(list2[j]+" ");
        }
    }
}
