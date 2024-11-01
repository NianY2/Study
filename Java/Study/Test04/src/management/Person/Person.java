package management.Person;

public class Person {
    private String name;
    private  int age;
    private  String collage;
    private  String major;

    public Person() {
    }

    public Person(String name, int age, String collage, String major) {
        this.name = name;
        this.age = age;
        this.collage = collage;
        this.major = major;
    }

    public  void  selfIntroduction(){
        System.out.println("我是"+this.name);
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

    public String getCollage() {
        return collage;
    }

    public void setCollage(String collage) {
        this.collage = collage;
    }

    public String getMajor() {
        return major;
    }

    public void setMajor(String major) {
        this.major = major;
    }
}
