package Test04.management;

public class Test {
    public static void main(String[] args) {
        Student student  = new Student("陈煜",22,"现代信息产业学院","软件工程","202212390606","06");
        student.selfIntroduction();
        student.teaching();
        System.out.println("==============");
        Teacher teacher = new Teacher("陈煜",22,"现代信息产业学院","软件工程","123","软件工程教研室");
        teacher.selfIntroduction();
        teacher.study();
    }
}
