package P2516_wait;

//https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/
// 滑动窗口
public class Test02 {
    public static int takeCharacters(String s, int k) {
        char[] sCharArray = s.toCharArray();
        int[] tar = {-k, -k, -k};
        for (char c : sCharArray) tar[c - 'a']++;
        if(tar[0] < 0 || tar[1] < 0 || tar[2] < 0)return -1;
        if(tar[0] == 0 || tar[1] == 0 || tar[2] == 0)return s.length();
        int l = 0, r = 0, res = 0;
        int[] count = new int[3];
        while (r < s.length()){
            count[sCharArray[r] - 'a']++;
            r++;
            // 当count的结果比tar大，说明有多余的
            if (count[0] > tar[0] || count[1] > tar[1] || count[2] > tar[2]) {
                count[sCharArray[l] - 'a']--;
                l++;
            } else {
                //
                res = Math.max(res, r - l);
            }
        }
        return sCharArray.length - res;
    }
    public static void main(String[] args) {
        String s = "caccbba";
        int k = 1;
        System.out.println(takeCharacters(s,k));
    }
}
