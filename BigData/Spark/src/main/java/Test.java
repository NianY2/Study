class A{
    public void run(String a){
        System.out.println("1");
    }
}
class  B extends A{
    public void run(double a){
        System.out.println("2");
    }
}
public class Test {
    public static void main(String[] args) {
        B a = new B();
        a.run("1");
        a.run(3.13);
        A b = new B();

    }
}
