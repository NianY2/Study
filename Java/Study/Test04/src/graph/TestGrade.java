package graph;

public class TestGrade {
    public static void main(String[] args) {
        Rectangle rectangle = new Rectangle(3,4);
        System.out.println("面积："+rectangle.area());
        System.out.println("周长："+rectangle.perimeter());
        System.out.println("======================================");
        Cuboid cuboid = new Cuboid(3,4,5);
        System.out.println("面积："+cuboid.area());
        System.out.println("周长："+cuboid.perimeter());
        System.out.println("体积："+cuboid.volume());
    }
}
