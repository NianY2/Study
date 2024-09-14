package P03;

import java.util.HashSet;
import java.util.Set;

public class test01 {
    public static int lengthOfLongestSubstring(String s) {
        Set<Character> occ = new HashSet<Character>();
        int n = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
//                s.charAt(j);
                if (occ.contains(s.charAt(j))) {
                    break;
                } else {
                    occ.add(s.charAt(j));
                }
            }
            if(occ.size() > n){
                n = occ.size();
            }
            occ.clear();
        }
        return n;
    }

    public static void main(String[] args) {

        System.out.println(lengthOfLongestSubstring("pwwkew"));
    }
}
