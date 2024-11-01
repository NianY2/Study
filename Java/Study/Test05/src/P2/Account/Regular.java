package P2.Account;


/*
 * 活期
 * */
public class Regular extends Account{
    public Regular(String username, String password, String card_num, float blance) {
        super(username, password, card_num, blance);
    }

    public Regular() {
    }

    @Override
    public void interestSettlement() {
        while (!isLogin){
            this.login();
        }
        if(this.blance > 100000){
            System.out.println("获得利息%s元".formatted(blance*4.75/100));
        }else {
            System.out.println("获得利息%s元".formatted(blance*1.75/100));
        }
    }

    @Override
    public void interestPrint() {
        while (!isLogin){
            this.login();
        }
        if(this.blance > 100000){
            System.out.println("利息是4,75%");
        }else {
            System.out.println("利息是1.75%");
        }

    }
}
