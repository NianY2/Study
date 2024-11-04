package P3222;
/*
* https://leetcode.cn/problems/find-the-winning-player-in-coin-game/description/*/
public class Test01 {
    public static String losingPlayer(int x, int y) {
        boolean flag = true;
        while (x >= 1 && y >= 4){
            x-=1;
            y-=4;
            flag = !flag;
        }
        if(flag){
            return "Bob";
        }else {
            return "Alice";
        }
    }
    public static void main(String[] args) {
        System.out.println(losingPlayer(4,11));
    }
}
