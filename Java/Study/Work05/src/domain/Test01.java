package domain;

public class Test01 {
    public static void main(String[] args) {
        Cat cat = new Cat("小白",1,99);
        Dog dog = new Dog("小黑",1,99999);
        cat.eat();
        cat.catchMice();
        dog.eat();
        dog.watchDoor();

        Animal animal1 = new Cat("小白",1,99);
        Animal animal2 = new Dog("小黑",1,99999);
        animal1.eat();
        animal2.eat();
    }
}
