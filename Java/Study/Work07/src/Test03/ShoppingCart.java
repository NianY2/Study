package Test03;

import java.util.HashMap;

public class ShoppingCart {
    static HashMap<Integer,GoodCart> catMap = new HashMap<>();
    public static boolean add(int gid){
        if(!GoodManage.contains(gid)){
            System.out.println("商品不存在");
            return false;
        }
        if(catMap.containsKey(gid)){
            GoodCart goodCart = catMap.get(gid);
            goodCart.setNum(goodCart.getNum()+1);
            catMap.put(gid,goodCart);
        }else {
            GoodCart goodCart = new GoodCart(GoodManage.getGood(gid),1);
            catMap.put(gid,goodCart);
        }
        return true;
    }
}
