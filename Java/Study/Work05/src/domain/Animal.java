package domain;

public class Animal {
//    姓名，年龄、无参、全参、get/set方法。吃饭（）
    private  String name;
    private  int age;

    public void  eat(){
        System.out.println("吃");
    }

    public Animal() {
    }

    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
