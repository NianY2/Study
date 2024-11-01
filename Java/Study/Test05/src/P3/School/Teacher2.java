package P3.School;

public class Teacher2 extends  Person2{
    private float salary;

    public Teacher2(String name, int age, float salary) {
        super(name, age);
        this.salary = salary;
    }

    @Override
    public void getContent() {
        System.out.println("教师信息：-->>姓名：%s;年龄：%s；工资：%s".formatted(super.name,super.age,salary));
    }

    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }
}
