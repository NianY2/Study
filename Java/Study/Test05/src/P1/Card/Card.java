package P1.Card;

public abstract class Card {
    protected float blance;
    protected String name;
    abstract public void pay(float price);

    public Card(String name,float blance) {
        this.blance = blance;
        this.name = name;
    }

    public Card() {
    }

    public float getBlance() {
        return blance;
    }

    public void setBlance(float blance) {
        this.blance = blance;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
