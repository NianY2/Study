//定义一个数组其中包含多个数字。用自己的方式最终实现，
// 奇数放在数组的左边，偶数放在数组的右边。（可以创建其他数组，不必须在原数组中改变）
public class Test05_2 {
    public static void main(String[] args) {
        int[] list1 = {12,14,23,45,66,68,70,77,90,91,1};
        int right = list1.length-1,left = 0;

        while (right!=left){
            if(list1[left] % 2 != 0){
                left++;
            }else {
                while (left!=right){
                    if(list1[right] % 2 == 0){
                        right--;
                    } else {
                        int num = list1[left];
                        list1[left] = list1[right];
                        list1[right] = num;
                        right--;
                        left++;
                        break;
                    }
                }
            }
//            if (list1[right] % 2 == 0){
//                right--;
//            }else {
//                while (left!=right){
//                    if(list1[left] % 2 != 0){
//                        left++;
//                    } else {
//                        int num = list1[left];
//                        list1[left] = list1[right];
//                        list1[right] = num;
//                        right--;
//                        left++;
//                        break;
//                    }
//                }
//            }
        }
        System.out.print("生成的新数组是：");
        for (int j = 0; j < list1.length; j++) {
            System.out.print(list1[j]+" ");
        }
    }
}
