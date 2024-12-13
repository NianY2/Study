package Test03;

public class GoodCart {
    private Good good;
    private int num;

    public GoodCart(Good good, int num) {
        this.good = good;
        this.num = num;
    }

    public Good getGood() {
        return good;
    }

    public void setGood(Good good) {
        this.good = good;
    }

    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    @Override
    public String toString() {
        return "GoodCart{" +
                "good=" + good +
                ", num=" + num +
                '}';
    }
}
