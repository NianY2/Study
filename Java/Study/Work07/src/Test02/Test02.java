package Test02;

import java.util.Scanner;

public class Test02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true){
            System.out.println("1. 注册");
            System.out.println("2. 查看");
            System.out.println("3. 退出");
            String m = sc.nextLine();
            switch (m){
                case "1":
                    System.out.print("账号(邮箱)：");
                    String email = sc.nextLine();
                    while (UserManage.containsEmail(email)){
                        System.out.println("账号已存在");
                        System.out.print("账号(邮箱)：");
                        email = sc.nextLine();
                    }
                    System.out.print("密码：");
                    String pwd = sc.nextLine();
                    User user = new User(email,pwd);
                    UserManage.register(user);
                    break;
                case "2":
                    System.out.println(UserManage.userMap);
                    break;
                case "3":
                    System.exit(0);
            }
        }

    }
}
