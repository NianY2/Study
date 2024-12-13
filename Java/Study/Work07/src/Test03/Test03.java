package Test03;

import java.util.Scanner;

public class Test03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true){
            System.out.println("1. 查看商品列表");
            System.out.println("2. 查看购物车列表");
            System.out.println("3. 添加购物车");
            System.out.println("4. 退出");
            String m = sc.nextLine();
            switch (m){
                case "1":
                    System.out.println(GoodManage.goodMap);
                    break;
                case "2":
                    System.out.println(ShoppingCart.catMap);
                    break;
                case "3":
                    System.out.println(GoodManage.goodMap);
                    System.out.print("商品编号：");

                    int gid = sc.nextInt();
                    sc.nextLine();
                    while (!GoodManage.contains(gid)){
                        System.out.println("商品不存在");
                        System.out.print("商品编号：");
                        gid = sc.nextInt();
                        sc.nextLine();
                    }
                    ShoppingCart.add(gid);
                    System.out.println(ShoppingCart.catMap);
                    break;
                case "4":
                    System.exit(0);
            }
        }
    }
}
