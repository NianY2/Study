package P2;

import P2.Account.Current;
import P2.Account.Regular;

public class Test02 {
    public static void main(String[] args) {
        Current current = new Current("root","123456","001",10000);
        current.interestPrint();
        current.interestSettlement();
        Regular regular = new Regular("root2","123456","002",10000);
        regular.interestPrint();
        regular.interestSettlement();
        Regular regular2 = new Regular("root3","123456","003",100000);
        regular2.interestPrint();
        regular2.interestSettlement();;

    }
}
