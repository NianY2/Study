package Test05.P2.Account;

import java.util.Scanner;

public abstract class Account {
    protected String card_num;
    protected float blance;
    protected String username;
    protected  String password;
    protected boolean isLogin = false;

    public boolean  login(){
        Scanner sc = new Scanner(System.in);
        System.out.print("账号：");
        String username = sc.next();
        System.out.print("密码：");
        String password = sc.next();
        if(!username.equals(this.username) || !password.equals(this.password)){
            System.out.println("账号或密码错误");
            return false;
        }
        this.isLogin = true;
        return true;
    }
    public  void loginOut(){
        this.isLogin = false;
    }

    abstract public void interestSettlement();
    abstract public void interestPrint();

    public Account(String username,String password,String card_num, float blance) {
        this.card_num = card_num;
        this.blance = blance;
        this.username = username;
        this.password = password;
    }

    public Account() {
    }

    public String getCard_num() {
        return card_num;
    }

    public void setCard_num(String card_num) {
        this.card_num = card_num;
    }

    public float getBlance() {
        return blance;
    }

    public void setBlance(float blance) {
        this.blance = blance;
    }
}
