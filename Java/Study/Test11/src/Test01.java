import java.util.ArrayList;
import java.util.List;

/*
* 1.	现有如下字符串元素：["aaa", "bbb", "aaa", "aaa", "ccc", "bbb"]，
*       请将所有的元素按顺序存入ArrayList集合中，并遍历集合查看存储结果。
* */
public class Test01 {
    public static void main(String[] args) {
        String[] sl =  {"aaa", "bbb", "aaa", "aaa", "ccc", "bbb"};
        List<String> sl2 = new ArrayList<>();
        for (int i = 0; i < sl.length; i++) {
            sl2.add(sl[i]);
        }

        System.out.println(sl2);
    }
}
