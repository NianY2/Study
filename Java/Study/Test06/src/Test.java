//在测试类Test中创建A的对象a并调用成员方法methodA()
public class Test {
    public static void main(String[] args) {
        // 在此处完成代码
        new A().methodA(new InterA() {
            @Override
            public void showA() {
                System.out.println("我是没有名字的InterA的实现类");
            }
        });
        InterA a = new InterA() {
            @Override
            public void showA() {
                System.out.println("我是有名字的InterA的实现类");
            }
        };
        new A().methodA(a);
    }
}
//定义接口
interface InterA {
    void showA();
}
class A {
    public void methodA(InterA a) {
        a.showA();
    }
}
