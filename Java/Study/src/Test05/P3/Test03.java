package Test05.P3;

import Test05.P3.School.Person2;
import Test05.P3.School.Student2;
import Test05.P3.School.Teacher2;

public class Test03 {
    public static void main(String[] args) {
        Person2 per1 = new Student2("name1",99,750);
        Person2 per2 = new Teacher2("name2",99,7500);
        per1.say();
        per2.say();
    }
}
