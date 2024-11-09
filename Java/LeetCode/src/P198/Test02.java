package P198;

import java.util.Arrays;

public class Test02 {
    public static int rob(int[] nums) {
        int n = nums.length;
        if(n==0)return 0;
        if(n==1)return nums[0];

        int first = nums[0];
        int second = Math.max(nums[0],nums[1]);
        for (int i = 2; i < n; i++) {
            int temp = second;
            second = Math.max(second,first+nums[i]);
            first = temp;
        }

        return second;
    }
    public static void main(String[] args) {
        System.out.println(rob(new int[]{1,2,3,1}));//4
        System.out.println(rob(new int[]{2,7,9,3,1}));//12
    }
}
