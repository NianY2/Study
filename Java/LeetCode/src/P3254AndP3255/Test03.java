package P3254AndP3255;

/*
* 3255. 长度为 K 的子数组的能量值 II
*https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-ii/?envType=daily-question&envId=2024-11-07
* 滑动窗口
* */

import java.util.Arrays;

public class Test03 {
    public static int[] resultsArray(int[] nums, int k) {
        if (k ==1)return   nums;
        int[] ans = new  int[nums.length-k+1];
        Arrays.fill(ans,-1);
        int l=0,r=1;
        for (;r < nums.length; r++) {
            if(nums[r] - nums[l] != r-l){
                l = r;
                continue;
            }
            if (r-l != k-1)
                continue;
            ans[l] = nums[r];
            l++;
        }
        return  ans;
    }
    public static void main(String[] args) {
        System.out.println(Arrays.toString(resultsArray(new int[]{1,2,3,4,3,2,5},3))); // [3,4,-1,-1,-1]
        System.out.println(Arrays.toString(resultsArray(new int[]{2,2,2,2,2},4))); // [-1,-1]
        System.out.println(Arrays.toString(resultsArray(new int[]{3,2,3,2,3,2},2))); // [-1,3,-1,3,-1]
    }
}
