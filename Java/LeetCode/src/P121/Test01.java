package P121;

public class Test01 {
    public static int maxProfit(int[] prices) {
        int maxPrice  = 0;
        for (var i:prices){
            for (var k:prices){
                System.out.println(k-i);
                maxPrice =  Math.max(maxPrice,k-i);
            }
        }
        return maxPrice;
    }
    public static void main(String[] args) {
        int[] prices  = {7,1,5,3,6,4};
        System.out.println(maxProfit(prices));
    }
}
