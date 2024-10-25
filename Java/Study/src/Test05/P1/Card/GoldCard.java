package Test05.P1.Card;

public class GoldCard extends Card {
    public GoldCard(String name,float blance) {
        super(name, blance);
    }

    public GoldCard() {
    }

    @Override
    public void pay(float price) {
        this.blance -= price*0.8;
        System.out.println("消费%s元，折后%s元，余额%s元".formatted(price,price*0.8,this.blance));
    }
}
