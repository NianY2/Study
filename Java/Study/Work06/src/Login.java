import java.util.Scanner;

public class Login {
    public void login_yzm(){
        TestRandom testRandom = new TestRandom();
        String yzm = testRandom.getRandom(4);
        System.out.println("生成的验证码为："+yzm);
        System.out.println("请输入验证码");
        Scanner sc = new Scanner(System.in);
        String s =  sc.nextLine();
//        判断验证码时一般不区分大小写
        if(s.equalsIgnoreCase(yzm)){
            System.out.println("输入正确");
        }else {
            System.out.println("输入错误，请重新输入...");
            login_yzm();
        }
    }
    public static void main(String[] args) {
        Login login = new Login();
        login.login_yzm();
    }
}
