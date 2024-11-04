package P3222;
/*
* https://leetcode.cn/problems/find-the-winning-player-in-coin-game/description/*/
public class Test02 {
    public static String losingPlayer(int x, int y) {
        return(Math.min(x,y/4) %2)==1?"Alice" :"Bob";
    }
    public static void main(String[] args) {
        System.out.println(losingPlayer(4,11));
    }
}
