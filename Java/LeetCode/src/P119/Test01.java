package P119;

import java.util.ArrayList;
import java.util.List;

public class Test01 {
    public static List<Integer> getRow(int rowIndex) {
        rowIndex= rowIndex+1;
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < rowIndex; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j <= i; j++) {
                if(j==0 || j==i){
                    row.add(1);
                }else {
                    row.add(res.get(i-1).get(j)+res.get(i-1).get(j-1));
                }
            }
            res.add(row);
        }

        return  res.get(rowIndex-1);
    }

    public static void main(String[] args) {
        System.out.println(getRow(3));
    }
}
