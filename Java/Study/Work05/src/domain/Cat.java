package domain;

public class Cat extends Animal {
    private  float  lovely;
    public Cat() {
    }

    public Cat(String name, int age, float lovely) {
        super(name, age);
        this.lovely = lovely;
    }

    public  void catchMice(){
        System.out.println("猫抓老鼠");
    }

    @Override
    public void eat() {
        System.out.println("猫吃");
    }

    public float getLovely() {
        return lovely;
    }

    public void setLovely(float lovely) {
        this.lovely = lovely;
    }
}
