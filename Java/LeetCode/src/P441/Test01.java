package P441;
/*
* 441. 排列硬币
*https://leetcode.cn/problems/arranging-coins/description/?envType=problem-list-v2&envId=binary-search
* */
public class Test01 {
    public static int arrangeCoins(int n) {
        return (int)((Math.pow((long)8*n+1,0.5)-1)/2);
    }
    public static void main(String[] args) {
        System.out.println(arrangeCoins(8));
    }
}
