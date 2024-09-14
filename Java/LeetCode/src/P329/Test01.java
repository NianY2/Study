package P329;

public class Test01 {
/*
https://leetcode.cn/problems/is-subsequence/?envType=problem-list-v2&envId=dynamic-programming
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
字符串的一个子序列是原始字符串删除一些（也可以不删除）
字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
*/
//    abcde
    public static boolean isSubsequence(String s, String t) {
        int n = 0;
        if(s.length() == 0){
            return  true;
        }
        for (int i = 0; i < t.length(); i++) {
            for (int j = i; j < t.length(); j++) {
                if(s.charAt(n) == t.charAt(j)){
                    System.out.println(s.charAt(n)+" "+t.charAt(j));
                    n++;
                    if(n == s.length()){
                        return  true;
                    }
                }
            }
            n = 0;
        }
        return  false;
    }
    public static void main(String[] args) {
        System.out.println(isSubsequence("","ahbgdc"));
    }
}
