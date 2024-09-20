package P119;

import java.util.ArrayList;
import java.util.List;

public class Test02 {
    public static List<Integer> getRow(int rowIndex) {

       List<Integer> res = new ArrayList<>();
        for (int i = 0; i <= rowIndex; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j <= i; j++) {
                if(j==0 || j==i){
                    row.add(1);
                }else {
                    row.add(res.get(j)+res.get(j-1));
                }
            }
            res = row;
        }

        return res;
    }

    public static void main(String[] args) {
        System.out.println(getRow(3));
    }
}
