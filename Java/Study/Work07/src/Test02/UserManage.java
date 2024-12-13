package Test02;

import java.util.HashMap;



public class  UserManage{
    static HashMap<String,User> userMap = new HashMap<>();
    public static boolean containsEmail(String email){
        if(userMap.containsKey(email)){
            return true;
        }
        return false;
    }
    public static  boolean  register(User user){
        if(containsEmail(user.getEmail())){
            System.out.println("账号已存在");
            return false;
        }
        userMap.put(user.getEmail(),user);
        System.out.println("注册成功");
        return true;
    }
}