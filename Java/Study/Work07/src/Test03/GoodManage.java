package Test03;

import java.util.HashMap;

public class GoodManage {
    static HashMap<Integer,Good> goodMap = new HashMap<>();
    static  {
        goodMap.put(1,new Good(1,"小米手机","3999"));
        goodMap.put(2,new Good(2,"鸭梨手机","9999"));
        goodMap.put(3,new Good(3,"8848手机","8848"));
    }
    public static boolean contains(int gid){
        return goodMap.containsKey(gid);
    }
    public static Good getGood(int gid){
        return goodMap.get(gid);
    }
}
