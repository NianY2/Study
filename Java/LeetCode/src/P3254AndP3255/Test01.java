package P3254AndP3255;

/*
* 3254. 长度为 K 的子数组的能量值 I
*https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-i/?envType=daily-question&envId=2024-11-06
* 暴力
* */

import java.util.Arrays;

public class Test01 {
    public static int[] resultsArray(int[] nums, int k) {
        int[] resList = new  int[nums.length-k+1];

        for (int i = 0; i+k <= nums.length; i++) {

            boolean flag = true;
            for (int j = 1; j < k && flag; j++) {
                flag = (nums[j+i] == nums[i]+j);
            }

            if(flag){
                resList[i] = nums[i+k-1];
            }else {
                resList[i] = -1;
            }

        }
        return  resList;
    }
    public static void main(String[] args) {
        System.out.println(Arrays.toString(resultsArray(new int[]{1,2,3,4,3,2,5},3))); // [3,4,-1,-1,-1]
        System.out.println(Arrays.toString(resultsArray(new int[]{2,2,2,2,2},4))); // [-1,-1]
        System.out.println(Arrays.toString(resultsArray(new int[]{3,2,3,2,3,2},2))); // [-1,3,-1,3,-1]
    }
}
