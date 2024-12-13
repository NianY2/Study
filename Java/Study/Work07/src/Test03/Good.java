package Test03;

public class Good {
    private int gid;
    private String name;
    private String price;

    public Good(int gid, String name, String price) {
        this.gid = gid;
        this.name = name;
        this.price = price;
    }

    public Good() {
    }

    public int getGid() {
        return gid;
    }

    public void setGid(int gid) {
        this.gid = gid;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "Good{" +
                "gid=" + gid +
                ", name='" + name + '\'' +
                ", price='" + price + '\'' +
                '}';
    }
}
