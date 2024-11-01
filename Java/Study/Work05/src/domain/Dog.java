package domain;

public class Dog extends Animal{
    private  float weight;

    public Dog(float weight) {
        this.weight = weight;
    }

    public Dog(String name, int age, float weight) {
        super(name, age);
        this.weight = weight;
    }
    public  void  watchDoor(){
        System.out.println("看门");
    }

    @Override
    public void eat() {
        System.out.println("狗吃");
    }

    public float getWeight() {
        return weight;
    }

    public void setWeight(float weight) {
        this.weight = weight;
    }
}
