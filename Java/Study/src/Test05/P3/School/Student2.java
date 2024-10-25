package Test05.P3.School;

public class Student2 extends  Person2{
    private float score;

    public Student2(String name, int age, float score) {
        super(name, age);
        this.score = score;
    }

    @Override
    public void getContent() {
        System.out.println("学生信息：-->>姓名：%s;年龄：%s；成绩：%s".formatted(name,age,score));
    }

    public float getScore() {
        return score;
    }

    public void setScore(float score) {
        this.score = score;
    }
}
