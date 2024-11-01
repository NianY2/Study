package Test05.P1;

import Test05.P1.Card.GoldCard;
import Test05.P1.Card.SilverCard;

public class Test01 {
    public static void main(String[] args) {
        GoldCard goldCard = new  GoldCard("CY",999);
        goldCard.pay(10);
        goldCard.pay(20);
        SilverCard silverCard = new SilverCard("CY",9999);
        silverCard.pay(100);
        silverCard.pay(900);
    }
}
