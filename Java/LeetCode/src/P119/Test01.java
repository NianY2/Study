package P119;

import java.util.ArrayList;
import java.util.List;

//https://leetcode.cn/problems/pascals-triangle-ii/?envType=problem-list-v2&envId=dynamic-programming
public class Test01 {
    public static List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<Integer>();
        for (int i = 0; i < rowIndex; i++) {
            List<Integer> old = new ArrayList<Integer>();
        }
        return  res;
    }
    public static void main(String[] args) {
        System.out.println(getRow(3));
    }
}
