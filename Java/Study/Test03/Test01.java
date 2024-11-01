package Test03;
/*需求：定义一个经理类Manager，定义程序员类Coder，定义一个测试类，在测试类中通过对象完成成员变量和成员方法的使用。
        要求：
        （1）按照以上要求定义Manager类和Coder类,属性要私有,生成空参、有参构造，set和get方法
        （2）定义测试类,在main方法中创建该类的对象并给属性赋值(set方法或有参构造方法)
        （3）调用成员方法,打印格式如下:
        ```
        工号为123基本工资为15000奖金为6000的项目经理正在努力的做着管理工作,分配任务,检查员工提交上来的代码.....
        工号为135基本工资为10000的程序员正在努力的写着代码......
        ```*/

class  Manager{
    private String name;
    private String id;
    private double salary;
    private  double bonus;

    public Manager(String name, String id, double salary, double bonus) {
        this.name = name;
        this.id = id;
        this.salary = salary;
        this.bonus = bonus;
    }

    public Manager() { }
    public String getName() {return name; }
    public void setName(String name) { this.name = name; }
    public String getId() {return id; }
    public void setId(String id) { this.id = id; }
    public double getSalary() { return salary; }
    public void setSalary(double salary) { this.salary = salary; }
    public double getBonus() { return bonus; }
    public void setBonus(double bonus) { this.bonus = bonus; }

    public void work() {
        System.out.println("工号为"+ this.id
                +"基本工资为"  + this.salary
                + "奖金为"+ this.bonus +"的项目经理正在努力的做着管理工作,分配任务,检查员工提交上来的代码....");
    }
}
class  Coder{
    private String name;
    private String id;
    private double salary;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public double getSalary() { return salary; }
    public void setSalary(double salary) { this.salary = salary; }
    public Coder() { }
    public Coder(String name, String id, double salary) {
        this.name = name;
        this.id = id;
        this.salary = salary;
    }

    public void work() {
        System.out.println("工号为"+ this.id +"基本工资为"+ this.salary +"的程序员正在努力的写着代码......");
    }
}
public class Test01 {
    public static void main(String[] args) {
        Manager manager = new Manager("小明","123",15000,6000);
        Coder coder = new Coder("小红","135",10000);
        manager.work();
        coder.work();
    }
}
