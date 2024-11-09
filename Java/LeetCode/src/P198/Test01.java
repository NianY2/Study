package P198;

import java.util.Arrays;

public class Test01 {
    public static int rob(int[] nums) {
        int n = nums.length;
        if(n==0)return 0;
        if(n==1)return nums[0];
        int[] ans = new  int[n];
        ans[0] = nums[0];
        ans[1] = Math.max(nums[0],nums[1]);
        for (int i = 2; i < n; i++) {
            ans[i] = Math.max(ans[i-1],ans[i-2]+nums[i]);
        }
        System.out.println(Arrays.toString(ans));
        return ans[n-1];
    }
    public static void main(String[] args) {
        System.out.println(rob(new int[]{1,2,3,1}));//4
        System.out.println(rob(new int[]{2,7,9,3,1}));//12
    }
}
