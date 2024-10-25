package Test05.P1.Card;

public class SilverCard  extends Card {
    public SilverCard(String name,float blance) {
        super(name, blance);
    }

    public SilverCard() {
    }

    @Override
    public void pay(float price) {
        this.blance -= price*0.85;
        System.out.println("消费%s元，折后%s元，余额%s元".formatted(price,price*0.5,this.blance));
    }
}