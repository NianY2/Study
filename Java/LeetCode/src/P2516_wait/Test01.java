package P2516_wait;

//https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/
// 暴力
public class Test01 {
    public static int takeCharacters(String s, int k) {
        int len = s.length();
        int answer = len+1;
        if (k == 0){
            return 0;
        }
        // 左边取i个
        for (int i = 0; i < len; i++) {

            int[] count_list = new  int[3];
            for (int j = 0; j <= i; j++) {
                count_list[s.charAt(j)-'a']++;
            }
            if (count_list[0] >= k && count_list[1] >= k && count_list[2] >= k){
                answer = Math.min(answer,count_list[0]+count_list[1]+count_list[2]);
                continue;
            }
            // 左边取全部到有结果
            for (int r = len-1; r != i; r--) {
                count_list[s.charAt(r)-'a']++;
                if (count_list[0] >= k && count_list[1] >= k && count_list[2] >= k){
                    answer = Math.min(answer,count_list[0]+count_list[1]+count_list[2]);
                    break;
                }
            }
        }
        //        存在全从右边开始的情况
        int[] count_list = new  int[3];
        for (int r = len-1; r != -1; r--) {
            count_list[s.charAt(r)-'a']++;
            if (count_list[0] >= k && count_list[1] >= k && count_list[2] >= k){
                answer = Math.min(answer,count_list[0]+count_list[1]+count_list[2]);
                break;
            }
        }
        if(answer>len){
            return  -1;
        }
        return answer;
    }
    public static void main(String[] args) {
        String s = "caccbbba";
        int k = 1;
        System.out.println(takeCharacters(s,k));
    }
}
