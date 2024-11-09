package P740;

import java.util.Arrays;

/*
* 40. 删除并获得点数
* https://leetcode.cn/problems/delete-and-earn/?envType=study-plan-v2&envId=dynamic-programming
* */
public class Test01 {
    public static int deleteAndEarn(int[] nums) {
        int maxVal = 0;
        for (int val:nums){
            maxVal = Math.max(maxVal,val);
        }
        int[] sum = new int[maxVal+1];
        for (int val:nums){
            sum[val]++;
        }
        return rob(sum);
    }
    /*
    P198 打家劫舍
    */
    public static int rob(int[] sum){
        int n = sum.length;
        if(n==1)return 0;
        int first = 0;
        int second = sum[1];
        for (int i = 2; i < n; i++) {
            int temp = second;
            second = Math.max(second,first+sum[i]*i);
            first = temp;
        }
        return second;
    }



    public static void main(String[] args) {
        System.out.println(deleteAndEarn(new int[]{3,4,2}));//6
        System.out.println(deleteAndEarn(new int[]{2,2,3,3,3,4}));//9
    }
}
