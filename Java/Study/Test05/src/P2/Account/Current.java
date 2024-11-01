package P2.Account;
/*
* 活期
* */
public class Current extends Account{
    public Current(String username, String password, String card_num, float blance) {
        super(username, password, card_num, blance);
    }

    public Current() {
    }

    @Override
    public void interestSettlement() {
        while (!isLogin){
            this.login();
        }
        System.out.println("获得利息%s元".formatted(blance*0.35/100));
    }

    @Override
    public void interestPrint() {
        while (!isLogin){
            this.login();
        }
        System.out.println("利息是0.35%");
    }
}
