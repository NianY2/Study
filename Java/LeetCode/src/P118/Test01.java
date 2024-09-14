package P118;

import java.util.ArrayList;
import java.util.List;

//https://leetcode.cn/problems/pascals-triangle/?envType=problem-list-v2&envId=dynamic-programming
public class Test01 {
    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<Integer>();
            for (int j = 0; j <= i; j++) {
                if (j==0 || j==i){
                    row.add(1);
                }else {
                    row.add(res.get(i-1).get(j-1)+res.get(i-1).get(j));
                }
            }
            res.add(row);
        }
        return  res;
    }
    public static void main(String[] args) {
        System.out.println(generate(3));
    }
}
