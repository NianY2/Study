package P3.School;

public abstract class Person2 {
    protected String name;
    protected  int age;

    public Person2(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public abstract void  getContent();
    public void say(){
        this.getContent();
    };

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
