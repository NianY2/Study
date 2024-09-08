package app03;

import java.util.HashSet;
import java.util.Set;

public class test02 {
    public static int lengthOfLongestSubstring(String s) {
        Set<Character> occ = new HashSet<Character>();
        int rk = -1, ans = 0;
        for (int i = 0; i < s.length(); i++) {
            if(i != 0){
                occ.remove(s.charAt(i-1));
            }
            while (rk+1 < s.length() && !occ.contains(s.charAt(rk+1))){
                occ.add(s.charAt(rk+1));
                rk++;
            }

            ans = Math.max(ans,occ.size());
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("astdytjhsdg"));
    }
}
