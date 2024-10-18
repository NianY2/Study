package Test04.management;

public class Student  extends  Person{
    private  String num;
    private  String class_room;

    public Student() { }

    public Student(String name, int age, String collage, String major, String num, String class_room) {
        super(name, age, collage, major);
        this.num = num;
        this.class_room = class_room;
    }
    public  void teaching(){
        System.out.println("教学");
    }

    public String getNum() {
        return num;
    }

    public void setNum(String num) {
        this.num = num;
    }

    public String getClass_room() {
        return class_room;
    }

    public void setClass_room(String class_room) {
        this.class_room = class_room;
    }
}
