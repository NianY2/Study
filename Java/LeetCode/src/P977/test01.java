package P977;

import java.util.Arrays;
//https://leetcode.cn/problems/squares-of-a-sorted-array/description/
public class test01 {
    public static int[] sortedSquares(int[] nums) {
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            res[i] = nums[i]*nums[i];
        }
        Arrays.sort(res);
        return res;
    }

    public static void main(String[] args) {
        int[] nums = {-4,-1,0,3,10};
        System.out.println(Arrays.toString(sortedSquares(nums)));
    }
}
